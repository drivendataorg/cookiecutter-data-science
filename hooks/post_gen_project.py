"""File to be run after template initialization by cookiecutter."""  # noqa: INP001

import os
import shutil
import subprocess
from copy import copy
from pathlib import Path

# https://github.com/cookiecutter/cookiecutter/issues/824
#   our workaround is to include these utility functions in the CCDS package
from ccds.hook_utils.configure_ssh import generate_personal_ssh_keys
from ccds.hook_utils.configure_vcs import configure_github_repo, init_local_git_repo
from ccds.hook_utils.custom_config import write_custom_config
from ccds.hook_utils.dependencies import basic, packages, scaffold, write_dependencies
from ccds.hook_utils.scaffold_cleaner import ScaffoldCleaner

MODULE_NAME = "{{ cookiecutter.module_name }}"
PROJECT_SHORT_DESCRIPTION = "{{ cookiecutter.project_short_description }}"
CODE_SCAFFOLD = "{{ cookiecutter.include_code_scaffold }}"

PROJ_ROOT = Path.cwd().resolve()
SECRETS_DIR = PROJ_ROOT / "secrets"

# ---------------------------------------------------------------------------- #
#                EMPLATIZED VARIABLES FILLED IN BY COOKIECUTTER                #
# ---------------------------------------------------------------------------- #
packages_to_install = copy(packages)

# {% if cookiecutter.dataset_storage.s3 %}
packages_to_install += ["awscli"]
# {% endif %} #

# {% if cookiecutter.include_code_scaffold != "No" %}
packages_to_install += scaffold
# {% endif %}

# {% if cookiecutter.pydata_packages == "basic" %}
packages_to_install += basic
# {% endif %}

# track packages that are not available through conda
pip_only_packages = [
    "awscli",
    "python-dotenv",
]

# Use the selected documentation package specified in the config,
# or none if none selected
docs_path = Path("docs")
# {% if cookiecutter.docs != "none" %}
packages_to_install += ["{{ cookiecutter.docs }}"]
pip_only_packages += ["{{ cookiecutter.docs }}"]
docs_subpath = docs_path / "{{ cookiecutter.docs }}"
for obj in docs_subpath.iterdir():
    shutil.move(str(obj), str(docs_path))
# {% endif %}

# Remove all remaining docs templates
for docs_template in docs_path.iterdir():
    if docs_template.is_dir() and docs_template.name != "docs":
        shutil.rmtree(docs_template)

# ---------------------------------------------------------------------------- #
#                           POST-GENERATION FUNCTIONS                          #
# ---------------------------------------------------------------------------- #
write_dependencies(
    "{{ cookiecutter.dependency_file }}",
    packages_to_install,
    pip_only_packages,
    repo_name="{{ cookiecutter.repo_name }}",
    module_name="{{ cookiecutter.module_name }}",
    python_version="{{ cookiecutter.python_version_number }}",
)

write_custom_config("{{ cookiecutter.custom_config }}")

# Remove LICENSE if "No license file"
if "{{ cookiecutter.open_source_license }}" == "No license file":  # noqa: PLR0133
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
# {% if cookiecutter.environment_manager == "uv" %}
os.chdir(Path.cwd())
subprocess.run(["make", "create_environment"], check=False)  # noqa: S603, S607
subprocess.run(["make", "requirements"], check=False)  # noqa: S603, S607
# {% endif %}

# ---------------------------------------------------------------------------- #
#                                Version Control                               #
# ---------------------------------------------------------------------------- #

# {% if cookiecutter.version_control == "git (local)" %}
init_local_git_repo(directory=Path.cwd())
# {% elif cookiecutter.version_control == "git (github private)" %}
configure_github_repo(
    directory=Path.cwd(),
    repo_name="{{ cookiecutter.repo_name }}",
    visibility="private",
    description="{{ cookiecutter.description }}",
)
# {% elif cookiecutter.version_control == "git (github public)" %}
configure_github_repo(
    directory=Path.cwd(),
    repo_name="{{ cookiecutter.repo_name }}",
    visibility="public",
    description="{{ cookiecutter.description }}",
)
# {% endif %}

# ---------------------------------------------------------------------------- #
#                              Install Pre-Commit                              #
# ---------------------------------------------------------------------------- #

# {% if cookiecutter.environment_manager == "uv" %}
os.chdir(Path.cwd())
subprocess.run(["pre-commit", "install"], check=False)  # noqa: S603, S607
# {% endif %}

# ---------------------------------------------------------------------------- #
#                                   SSH Keys                                   #
# ---------------------------------------------------------------------------- #

# --------------------------------- Personal --------------------------------- #

# {% if cookiecutter._generate_personal_ssh_keys == "y" %}
# TODO(GatlenCulp): Implement generating personal ssh keys
# ssh-keygen -t ed25519 -C "GatlenCulp" -f PROJ_ROOT/secrets/GatlenCulp
# rename (GatlenCulp, GatlenCulp.pub) -> (GatlenCulp.key, GatlenCulp.pub)
# or just do make sure it is named with .key normally.
generate_personal_ssh_keys(
    SECRETS_DIR,
    "{{ cookiecutter.author_name }}",
    comment="{{ cookiecutter.author_name }}",
)
# {% endif %}

# ------------------------------ Deployment Keys ----------------------------- #

# {% if cookiecutter._generate_and_upload_gh_deploy_keys == "y" %}
# ssh-keygen -t ed25519 -C "project-deploy" -f PROJ_ROOT/secrets/project-deploy
# rename (project-deploy, project-deploy.pub)  # noqa: ERA001
#   -> (project-deploy.key, project-deploy.pub)
# or just do make sure it is named with .key normally.
generate_personal_ssh_keys(
    SECRETS_DIR,
    "{{ cookiecutter.repo_name }}-deploy",
    comment="{{ cookiecutter.repo_name }}-deploy",
)

# TODO(GatlenCulp): Upload generated ssh key to github as deploy key
# gh repo deploy-key add project-deploy.pub
# Optional: --allow-write, --title <string>


# TODO(GatlenCulp): Test connection to github
# ssh -T git@github.com -i project-deploy.key

# TODO(GatlenCulp): Test connection to github using config file
# ssh GitHub -F config.ssh

# {% endif %}
