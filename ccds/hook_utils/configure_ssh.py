# type: ignore
# ruff: noqa
import os
import subprocess
from pathlib import Path
from typing import Literal, Union, Optional


def _ssh_keygen(command: str, **kwargs) -> subprocess.CompletedProcess:
    """Run ssh-keygen command and return the result."""
    return subprocess.run(f"ssh-keygen {command}", shell=True, check=True, **kwargs)


def generate_personal_ssh_keys(
    directory: str | Path, key_name: str, comment: Optional[str]
) -> bool:
    """Generate personal and private ssh keys in specified directory.

    These keys are meant to access project-specific remote resources
    such as databases or webservers without having to save them into
    ~/.ssh
    """
    raise NotImplementedError
    # TODO: Implement
    try:
        directory = Path(directory)
        if not directory.is_dir():
            raise ValueError(f"Directory '{directory}' does not exist.")

        os.chdir(directory)

        return True
    except Exception as e:
        print(f"Error generating ssh keys: {e}")
        return False
    # Note: Perhaps return the two generated files?


def generate_ssh_config_file(directory: str | Path) -> bool:
    """Generate the config.ssh file."""
    # TODO: Implement
    raise NotImplementedError
