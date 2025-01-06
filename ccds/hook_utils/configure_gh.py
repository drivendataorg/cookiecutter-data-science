# ruff: noqa
"""Configures git or vcs repositories."""

import os
import subprocess
from pathlib import Path
from typing import Literal


def configure_github_repo(
    directory: str | Path,
    repo_name: str,
    protection_type: Literal["none", "main", "main_and_dev"],
    no_github: bool = False,
) -> bool:
    """Configure a Git repository locally and optionally on GitHub with specified branch protections.

    Args:
        directory: Directory where the repository will be created or updated
        repo_name: Name of the repository
        protection_type: Type of branch protection to apply:
            - "none": No branch protection
            - "main": Protected main branch
            - "main_and_dev": Protected main and dev branches
        no_github: If True, skips GitHub operations and only sets up local repository

    Returns:
        bool: True if configuration was successful, False otherwise
    """
    try:
        directory = Path(directory)

        # Validate inputs
        if not directory.is_dir():
            raise ValueError(f"Directory '{directory}' does not exist.")

        if not repo_name.replace("-", "").replace("_", "").isalnum():
            raise ValueError(
                "Invalid repository name. Use only letters, numbers, underscores, and hyphens.",
            )

        # Check for gh CLI if needed
        if not no_github:
            if not _check_gh_cli():
                raise RuntimeError(
                    "gh CLI is required but not installed or not authenticated. "
                    "Use no_github=True to skip GitHub operations.",
                )

        # Change to specified directory
        os.chdir(directory)

        # Initialize repository if needed
        if not (directory / ".git").is_dir():
            _run_git_command("init")

        # Add and commit changes if needed
        if _run_git_command("status --porcelain", capture_output=True).stdout:
            _run_git_command("add .")
            _run_git_command("commit -m 'Initial commit'")

        # Add semantic versioning tag if it doesn't exist
        if not _tag_exists("v0.1.0"):
            _run_git_command("tag -a v0.1.0 -m 'Initial version'")

        # Create dev branch if needed
        if protection_type == "main_and_dev":
            if not _branch_exists("dev"):
                _run_git_command("branch dev")

        # GitHub operations
        if not no_github:
            github_username = _get_github_username()

            # Create or update GitHub repository
            if not _github_repo_exists(github_username, repo_name):
                _run_gh_command(
                    f"repo create {repo_name} --private --source=. --remote=origin --push",
                )
            else:
                remote_url = f"git@github.com:{github_username}/{repo_name}.git"
                try:
                    _run_git_command(f"remote set-url origin {remote_url}")
                except subprocess.CalledProcessError:
                    _run_git_command(f"remote add origin {remote_url}")

            # Push branches and tags
            _run_git_command("push -u origin main")
            _run_git_command("push --tags")

            if _branch_exists("dev"):
                _run_git_command("push -u origin dev")

            # Set branch protections if repository is public
            is_public = _is_repo_public(github_username, repo_name)
            if is_public:
                if protection_type in ["main", "main_and_dev"]:
                    _set_branch_protection(github_username, repo_name, "main")
                if protection_type == "main_and_dev":
                    _set_branch_protection(github_username, repo_name, "dev")
                print("Branch protections set successfully.")
            else:
                print(
                    "Warning: Branch protections can only be set for public repositories "
                    "or with a GitHub Pro account.",
                )

            print("Repository configuration complete on GitHub!")
        else:
            print("Local repository configuration complete!")

        return True

    except Exception as e:
        print(f"Error during repository configuration: {e}")
        return False


def _run_git_command(command: str, **kwargs) -> subprocess.CompletedProcess:
    """Run a git command and return the result."""
    return subprocess.run(f"git {command}", shell=True, check=True, **kwargs)


def _run_gh_command(command: str, **kwargs) -> subprocess.CompletedProcess:
    """Run a GitHub CLI command and return the result."""
    return subprocess.run(f"gh {command}", shell=True, check=True, **kwargs)


def _check_gh_cli() -> bool:
    """Check if gh CLI is installed and authenticated."""
    try:
        subprocess.run("gh --version", shell=True, check=True, capture_output=True)
        subprocess.run("gh auth status", shell=True, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def _tag_exists(tag: str) -> bool:
    """Check if a git tag exists."""
    try:
        _run_git_command(f"rev-parse {tag}", capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def _branch_exists(branch: str) -> bool:
    """Check if a git branch exists."""
    try:
        _run_git_command(f"rev-parse --verify {branch}", capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def _get_github_username() -> str:
    """Get the authenticated GitHub username."""
    result = _run_gh_command("api user -q .login", capture_output=True, text=True)
    return result.stdout.strip()


def _github_repo_exists(username: str, repo_name: str) -> bool:
    """Check if a GitHub repository exists."""
    try:
        _run_gh_command(f"repo view {username}/{repo_name}", capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def _is_repo_public(username: str, repo_name: str) -> bool:
    """Check if a GitHub repository is public."""
    result = _run_gh_command(
        f"api repos/{username}/{repo_name} -q .private",
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() == "false"


def _set_branch_protection(username: str, repo_name: str, branch: str) -> None:
    """Set branch protection rules."""
    protection_data = {
        "required_status_checks": {"strict": True, "contexts": []},
        "enforce_admins": True,
        "required_pull_request_reviews": {"required_approving_review_count": 1},
        "restrictions": None,
    }

    _run_gh_command(
        f"api repos/{username}/{repo_name}/branches/{branch}/protection "
        "-X PUT -H 'Accept: application/vnd.github.v3+json' "
        f"-f required_status_checks='{protection_data['required_status_checks']}' "
        f"-f enforce_admins={protection_data['enforce_admins']} "
        f"-f required_pull_request_reviews='{protection_data['required_pull_request_reviews']}' "
        f"-f restrictions={protection_data['restrictions']}",
    )
