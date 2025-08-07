"""File to be run after template initialization by cookiecutter."""  # noqa: INP001

import json
import os
import shutil
import subprocess
from copy import copy
from pathlib import Path

from loguru import logger

# https://github.com/cookiecutter/cookiecutter/issues/824
#   our workaround is to include these utility functions in the CCDS package
from ccds.hook_utils.configure_ssh import generate_personal_ssh_keys
from ccds.hook_utils.configure_vcs import configure_github_repo, init_local_git_repo
from ccds.hook_utils.cookiecutter_args import GotemArgs
from ccds.hook_utils.custom_config import write_custom_config
from ccds.hook_utils.dependencies import (
    basic,
    flake8_black_isort,
    packages,
    ruff,
    scaffold,
    write_dependencies,
    write_python_version,
)
from ccds.hook_utils.scaffold_cleaner import ScaffoldCleaner

cookiecutter_json = """{{ cookiecutter | tojson }}"""

gotem_args = GotemArgs.model_validate_json(cookiecutter_json)
# Also create a dictionary version for easy access
cookiecutter_dict = json.loads(gotem_args.model_dump_json(by_alias=True))
logger.info(cookiecutter_dict)

# Set up constants from cookiecutter args
MODULE_NAME = gotem_args.module_name
# For project description, try to get "project_short_description" from the JSON dict
# since it may not be in our model but is needed by scaffold_cleaner
PROJECT_SHORT_DESCRIPTION = cookiecutter_dict.get(
    "project_short_description",
    gotem_args.description,
)
CODE_SCAFFOLD = gotem_args.include_code_scaffold

PROJ_ROOT = Path.cwd().resolve()
SECRETS_DIR = PROJ_ROOT / "secrets"

# ---------------------------------------------------------------------------- #
#                EMPLATIZED VARIABLES FILLED IN BY COOKIECUTTER                #
# ---------------------------------------------------------------------------- #
packages_to_install = copy(packages)

if "s3" in gotem_args.dataset_storage:
    packages_to_install += ["awscli"]

if gotem_args.include_code_scaffold != "No":
    packages_to_install += scaffold

if gotem_args.pydata_packages == "basic":
    packages_to_install += basic

# {% if cookiecutter.linting_and_formatting == "ruff" %}
packages_to_install += ruff
# Remove setup.cfg
Path("setup.cfg").unlink()
# {% elif cookiecutter.linting_and_formatting == "flake8+black+isort" %}
packages_to_install += flake8_black_isort
# {% endif %}
# track packages that are not available through conda
pip_only_packages = [
    "awscli",
    "python-dotenv",
]

# Select testing framework
tests_path = Path("tests")

# {% if cookiecutter.testing_framework == "pytest" %}
packages_to_install += ["pytest"]
# {% endif %}

# {% if cookiecutter.testing_framework == "none" %}
shutil.rmtree(tests_path)

# {% else %}
tests_subpath = tests_path / "{{ cookiecutter.testing_framework }}"
for obj in tests_subpath.iterdir():
    shutil.move(str(obj), str(tests_path))

# Remove all remaining tests templates
for tests_template in tests_path.iterdir():
    if tests_template.is_dir() and not tests_template.name == "tests":
        shutil.rmtree(tests_template)
# {% endif %}

# Use the selected documentation package specified in the config,
# or none if none selected
docs_path = Path("docs")
if gotem_args.docs != "none":
    packages_to_install += [gotem_args.docs]
    pip_only_packages += [gotem_args.docs]
    docs_subpath = docs_path / gotem_args.docs
    for obj in docs_subpath.iterdir():
        shutil.move(str(obj), str(docs_path))

# Remove all remaining docs templates
for docs_template in docs_path.iterdir():
    if docs_template.is_dir() and docs_template.name != "docs":
        shutil.rmtree(docs_template)

# ---------------------------------------------------------------------------- #
#                           POST-GENERATION FUNCTIONS                          #
# ---------------------------------------------------------------------------- #
write_dependencies(
    gotem_args.dependency_file,
    packages_to_install,
    pip_only_packages,
    repo_name=gotem_args.repo_name,
    module_name=MODULE_NAME,
    python_version=gotem_args.python_version_number,
    environment_manager=gotem_args.environment_manager,
    description=gotem_args.description,
)

write_python_version(gotem_args.python_version_number)

write_custom_config(cookiecutter_dict.get("custom_config", ""))

# Remove LICENSE if "No license file"
if gotem_args.open_source_license == "No license file":
    Path("LICENSE").unlink()

# Make single quotes prettier
# Jinja tojson escapes single-quotes with \u0027 since it's meant for HTML/JS
pyproject_text = Path("pyproject.toml").read_text()
Path("pyproject.toml").write_text(pyproject_text.replace(r"\u0027", "'"))

scaffold_cleaner = ScaffoldCleaner(PROJ_ROOT, MODULE_NAME, PROJECT_SHORT_DESCRIPTION)

if CODE_SCAFFOLD == "No":
    scaffold_cleaner()
else:
    scaffold_cleaner([CODE_SCAFFOLD])


# ---------------------------------------------------------------------------- #
#                          Install Virtual Envrionment                         #
# ---------------------------------------------------------------------------- #

# Install the virtual environment (uv only for now)
if gotem_args.environment_manager == "uv":
    os.chdir(Path.cwd())
    subprocess.run(["make", "create_environment"], check=False)  # noqa: S603, S607
    subprocess.run(["make", "requirements"], check=False)  # noqa: S603, S607

# ---------------------------------------------------------------------------- #
#                                Version Control                               #
# ---------------------------------------------------------------------------- #

if gotem_args.version_control == "git (local)":
    init_local_git_repo(directory=Path.cwd())
elif gotem_args.version_control == "git (github private)":
    configure_github_repo(
        directory=Path.cwd(),
        repo_name=gotem_args.repo_name,
        visibility="private",
        description=gotem_args.description,
    )
elif gotem_args.version_control == "git (github public)":
    configure_github_repo(
        directory=Path.cwd(),
        repo_name=gotem_args.repo_name,
        visibility="public",
        description=gotem_args.description,
    )

# ---------------------------------------------------------------------------- #
#                              Install Pre-Commit                              #
# ---------------------------------------------------------------------------- #

# if gotem_args.environment_manager == "uv":
#     os.chdir(Path.cwd())
#     subprocess.run(["pre-commit", "install"], check=False)

# ---------------------------------------------------------------------------- #
#                                   SSH Keys                                   #
# ---------------------------------------------------------------------------- #

# --------------------------------- Personal --------------------------------- #

if gotem_args.generate_personal_ssh_keys == "y":
    generate_personal_ssh_keys(
        SECRETS_DIR,
        gotem_args.author_name,
        comment=gotem_args.author_name,
    )

# ------------------------------ Deployment Keys ----------------------------- #

if gotem_args.generate_and_upload_gh_deploy_keys == "y":
    generate_personal_ssh_keys(
        SECRETS_DIR,
        f"{gotem_args.repo_name}-deploy",
        comment=f"{gotem_args.repo_name}-deploy",
    )

    # TODO(GatlenCulp): Upload generated ssh key to github as deploy key
    # gh repo deploy-key add project-deploy.pub
    # Optional: --allow-write, --title <string>

    # TODO(GatlenCulp): Test connection to github
    # ssh -T git@github.com -i project-deploy.key

    # TODO(GatlenCulp): Test connection to github using config file
    # ssh GitHub -F config.ssh
