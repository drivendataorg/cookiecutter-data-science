import os
import subprocess
from pathlib import Path
from typing import Literal

# TODO: Refactor this entirely, maybe use github module or something.

# ---------------------------------------------------------------------------- #
#                                      Git                                     #
# ---------------------------------------------------------------------------- #


def init_local_git_repo(
    directory: str | Path, _make_initial_commit: bool = True
) -> bool:
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
    directory: str | Path,
    repo_name: str,
    protection_type: Literal["none", "main", "main_and_dev"],
    no_github: bool = False,
) -> bool:
    """
    Configure a Git repository locally and optionally on GitHub with specified branch protections.

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
                "Invalid repository name. Use only letters, numbers, underscores, and hyphens."
            )

        # Check for gh CLI if needed
        if not no_github:
            if not _check_gh_cli_installed():
                raise RuntimeError(
                    "gh CLI is required but not installed or not authenticated. "
                    "Use no_github=True to skip GitHub operations."
                )

        # Initialize local repository
        if not init_local_git_repo(directory):
            return False

        # Create dev branch if needed
        if protection_type == "main_and_dev":
            if not _branch_exists("dev"):
                _git("branch dev")

        # Add semantic versioning tag if it doesn't exist
        if not _tag_exists("v0.1.0"):
            _git("tag -a v0.1.0 -m 'Initial version'")

        # Create dev branch if needed
        if protection_type == "main_and_dev":
            if not _branch_exists("dev"):
                _git("branch dev")

        # GitHub operations
        if not no_github:
            github_username = _get_github_username()

            # Create or update GitHub repository
            if not _github_repo_exists(github_username, repo_name):
                _gh(
                    f"repo create {repo_name} --private --source=. --remote=origin --push"
                )
            else:
                remote_url = f"git@github.com:{github_username}/{repo_name}.git"
                try:
                    _git(f"remote set-url origin {remote_url}")
                except subprocess.CalledProcessError:
                    _git(f"remote add origin {remote_url}")

            # Push branches and tags
            _git("push -u origin main")
            _git("push --tags")

            if _branch_exists("dev"):
                _git("push -u origin dev")

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
                    "or with a GitHub Pro account."
                )

            print("Repository configuration complete on GitHub!")
        else:
            print("Local repository configuration complete!")

        return True

    except Exception as e:
        print(f"Error during repository configuration: {e}")
        return False


def _gh(command: str, **kwargs) -> subprocess.CompletedProcess:
    """Run a GitHub CLI command and return the result."""
    return subprocess.run(f"gh {command}", shell=True, check=True, **kwargs)


def _check_gh_cli_installed() -> bool:
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
        _git(f"rev-parse {tag}", capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def _branch_exists(branch: str) -> bool:
    """Check if a git branch exists."""
    try:
        _git(f"rev-parse --verify {branch}", capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def _get_github_username() -> str:
    """Get the authenticated GitHub username."""
    result = _gh("api user -q .login", capture_output=True, text=True)
    return result.stdout.strip()


def _github_repo_exists(username: str, repo_name: str) -> bool:
    """Check if a GitHub repository exists."""
    try:
        _gh(f"repo view {username}/{repo_name}", capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def _is_repo_public(username: str, repo_name: str) -> bool:
    """Check if a GitHub repository is public."""
    result = _gh(
        f"api repos/{username}/{repo_name} -q .private", capture_output=True, text=True
    )
    return result.stdout.strip() == "false"


def _set_branch_protection(username: str, repo_name: str, branch: str) -> None:
    """Set branch protection rules. Only works with enterprise(?)."""
    protection_data = {
        "required_status_checks": {"strict": True, "contexts": []},
        "enforce_admins": True,
        "required_pull_request_reviews": {"required_approving_review_count": 1},
        "restrictions": None,
    }

    _gh(
        f"api repos/{username}/{repo_name}/branches/{branch}/protection "
        "-X PUT -H 'Accept: application/vnd.github.v3+json' "
        f"-f required_status_checks='{protection_data['required_status_checks']}' "
        f"-f enforce_admins={protection_data['enforce_admins']} "
        f"-f required_pull_request_reviews='{protection_data['required_pull_request_reviews']}' "
        f"-f restrictions={protection_data['restrictions']}"
    )
