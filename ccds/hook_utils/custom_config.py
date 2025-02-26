from pathlib import Path
from shutil import copytree
from tempfile import TemporaryDirectory
from urllib.request import urlretrieve
from zipfile import ZipFile

from cookiecutter.vcs import clone


def write_custom_config(user_input_config):
    if not user_input_config:
        return

    tmp = TemporaryDirectory()
    tmp_zip = None

    print(user_input_config)

    # if not absolute, test if local path relative to parent of created directory
    if not user_input_config.startswith("/"):
        test_path = Path("..") / user_input_config
    else:
        test_path = Path(user_input_config)

    # check if user passed a local path
    if test_path.exists() and test_path.is_dir():
        local_path = test_path

    elif test_path.exists() and test_path.endswith(".zip"):
        tmp_zip = test_path

    # check if user passed a url to a zip
    elif user_input_config.startswith("http") and (
        user_input_config.split(".")[-1] in ["zip"]
    ):
        tmp_zip, _ = urlretrieve(user_input_config)

    # assume it is a VCS uri and try to clone
    else:
        clone(user_input_config, clone_to_dir=tmp)
        local_path = tmp

    if tmp_zip:
        with ZipFile(tmp_zip, "r") as zipf:
            zipf.extractall(tmp)
            local_path = tmp

    # write whatever the user supplied into the project
    copytree(local_path, ".")

    tmp.cleanup()


def validate_dependency_file(config):
    """Validate that the dependency file choice is compatible with the environment manager"""
    env_manager = config["environment_manager"]
    dep_file = config["dependency_file"]

    # Validate pipenv + Pipfile combo
    if (env_manager == "pipenv") != (dep_file == "Pipfile"):
        raise ValueError(
            "Pipenv must be used with Pipfile and vice versa. "
            f"Got environment_manager={env_manager}, dependency_file={dep_file}"
        )

    # Validate conda + environment.yml
    if dep_file == "environment.yml" and env_manager != "conda":
        raise ValueError(
            "environment.yml can only be used with conda. "
            f"Got environment_manager={env_manager}"
        )

    # Validate uv dependency files
    if env_manager == "uv" and dep_file not in ["requirements.in", "pyproject.toml"]:
        raise ValueError(
            "uv can only be used with requirements.in or pyproject.toml. "
            f"Got dependency_file={dep_file}"
        )

    # Validate pyproject.toml and requirements.in with uv
    if dep_file in ["pyproject.toml", "requirements.in"] and env_manager != "uv":
        raise ValueError(
            f"{dep_file} can only be used with uv. "
            f"Got environment_manager={env_manager}"
        )

def validate_config(config):
    """Run all config validations"""
    validate_dependency_file(config)
    # ... any other existing validations ...
