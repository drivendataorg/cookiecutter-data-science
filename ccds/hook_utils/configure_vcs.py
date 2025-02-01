# type: ignore
# ruff: noqa
import os
import subprocess
from pathlib import Path
from typing import Literal, Union

# ---------------------------------------------------------------------------- #
#                                      Git                                     #
# ---------------------------------------------------------------------------- #


def init_local_git_repo(directory: str | Path, _make_initial_commit: bool = True) -> bool:
    """
    Initialize a local git repository without any GitHub integration.

    Args:
        directory: Directory where the repository will be created
        _make_initial_commit: Whether to make initial commit (for testing)

    Returns:
        bool: True if initialization was successful, False otherwise
    """
    try:
        if not _check_git_cli_installed():
            raise RuntimeError("git CLI is required but not installed")

        directory = Path(directory)
        if not directory.is_dir():
            raise ValueError(f"Directory '{directory}' does not exist.")

        os.chdir(directory)

        if not (directory / ".git").is_dir():
            _git("init")
            if _make_initial_commit:
                _git("add .")
                _git("commit -m 'Initial commit'")

        return True
    except Exception as e:
        print(f"Error during repository initialization: {e}")
        return False


def _git(command: str, **kwargs) -> subprocess.CompletedProcess:
    """Run a git command and return the result."""
    return subprocess.run(f"git {command}", shell=True, check=True, **kwargs)


def _check_git_cli_installed() -> bool:
    """Check whether git cli is installed"""
    try:
        subprocess.run("git --version", shell=True, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


# ---------------------------------------------------------------------------- #
#                                 Git + Github                                 #
# ---------------------------------------------------------------------------- #


def configure_github_repo(
    directory: Union[str, Path],
    repo_name: str,
    visibility: Literal["private", "public"] = "private",
    description: str = "",
) -> bool:
    """
    Configure a Git repository locally and optionally on GitHub with specified branch protections.

    Args:
        directory: Directory where the repository will be created or updated
        repo_name: Name of the repository
        visibility: Whether to upload to github as a public or private repo

    Returns:
        bool: True if configuration was successful, False otherwise
    """
    try:
        subprocess.run("gh --version", shell=True, check=True, capture_output=True)
    except subprocess.CalledProcessError:
        raise RuntimeError("GitHub CLI is not installed. Please install and try again.")
    try:
        subprocess.run("gh auth status", shell=True, check=True, capture_output=True)
    except subprocess.CalledProcessError:
        raise RuntimeError(
            "GitHub CLI not authenticated. Please run `gh auth login` and try again."
        )

    try:
        # GitHub operations
        github_username = _gh("api user -q .login", capture_output=True, text=True).stdout.strip()

        # Create or update GitHub repository
        if not _github_repo_exists(github_username, repo_name):
            # Initialize local repository
            if not init_local_git_repo(directory):
                return False
            _gh(
                f"repo create {repo_name} "
                f"--{visibility} "
                f"--source=. "
                f"--remote=origin "
                f"--push " + (f"--description '{description}'" if description else "")
            )
        else:
            remote_url = _get_gh_remote_url(github_username, repo_name)
            raise RuntimeError(f"GitHub repo already exists at {remote_url}")
            # TODO: Prompt user if they would like to set existing repo as origin.
            # remote_url = _get_gh_remote_url(github_username, repo_name)
            # try:
            #     _git(f"remote set-url origin {remote_url}")
            # except subprocess.CalledProcessError:
            #     _git(f"remote add origin {remote_url}")

        # Push to newly created origin
        _git("push -u origin main")

        print("Repository configuration complete on GitHub!")

        return True

    except Exception as e:
        print(f"Error during repository configuration: {e}")
        return False


def _gh(command: str, **kwargs) -> subprocess.CompletedProcess:
    """Run a GitHub CLI command and return the result."""
    return subprocess.run(f"gh {command}", shell=True, check=True, **kwargs)


def _get_gh_remote_url(github_username: str, repo_name: str) -> Literal["https", "ssh"]:
    """Returns whether the github protocol is https or ssh from user's config"""
    try:
        protocol = _gh("config get git_protocol", capture_output=True, text=True).stdout.strip()
        if protocol == "ssh":
            return f"git@github.com:{github_username}/{repo_name}.git"
        elif protocol == "https":
            return f"https://github.com/{github_username}/{repo_name}"
        else:
            raise ValueError(f"Unexepected GitHub protocol {protocol}")
    except subprocess.CalledProcessError:
        # Default to https if not set
        return "https"


def _github_repo_exists(username: str, repo_name: str) -> bool:
    """Check if a GitHub repository exists."""
    try:
        _gh(f"repo view {username}/{repo_name}", capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


# ---------------------------------------------------------------------------- #
#                            GitHub SSH Deploy Keys                            #
# ---------------------------------------------------------------------------- #

# TODO(GatlenCulp): Implement this
