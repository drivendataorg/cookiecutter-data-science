# mypy: ignore-errors
# ruff: noqa
import json
import os
import sys
import logging
from pathlib import Path
from subprocess import PIPE, CompletedProcess, run
from typing import Any

import pytest
from conftest import bake_project

logger = logging.getLogger("test_creation")

BASH_EXECUTABLE = os.getenv("BASH_EXECUTABLE", "bash")


# GATLEN'S ADDED BITS #
VSCODE_CONFIG_DIR = Path(".vscode")
OUT_DIR = Path("out")


def _decode_print_stdout_stderr(result: CompletedProcess) -> tuple[str, str]:
    """Print command stdout and stderr to console to use when debugging failing tests.
    Normally hidden by pytest except in failure we want this displayed

    Args:
        result: CompletedProcess object from subprocess.run

    Returns:
        Tuple of (stdout_string, stderr_string)
    """
    encoding = sys.stdout.encoding

    if encoding is None:
        encoding = "utf-8"

    logger.debug("\n======================= STDOUT ======================")
    stdout = result.stdout.decode(encoding)
    logger.debug(stdout)

    logger.debug("\n======================= STDERR ======================")
    stderr = result.stderr.decode(encoding)
    logger.debug(stderr)

    return stdout, stderr


def no_curlies(filepath: Path) -> bool:
    """Utility to make sure no curly braces appear in a file.
    That is, was Jinja able to render everything?

    Args:
        filepath: Path to file to check

    Returns:
        True if no template strings found, False otherwise
    """
    data = filepath.open("r", encoding="utf-8").read()

    template_strings = {
        "{{ ",
        " }}",
        "{%",
        "%}",
    }

    return not any(s in data for s in template_strings)


@pytest.mark.detailed
def test_baking_configs(config: dict[str, Any], fast: int) -> None:
    """For every generated config in the config_generator, run all
    of the tests.

    Args:
        config: Configuration dictionary
        fast: Integer controlling test speed/depth
    """
    logger.info("Testing detailed verification with config: %s", json.dumps(config, indent=2))

    with bake_project(config) as project_directory:
        logger.info("Verifying folders...")
        verify_folders(project_directory, config)

        logger.info("Verifying files...")
        verify_files(project_directory, config)
        lint(project_directory)

        if fast < 2:
            logger.info("Verifying Makefile commands...")
            verify_makefile_commands(project_directory, config)


def verify_folders(root: Path, config: dict[str, Any]) -> None:
    """Tests that expected folders and only expected folders exist.

    Args:
        root: Root directory path
        config: Configuration dictionary
    """
    expected_dirs = {
        str(VSCODE_CONFIG_DIR),
        ".",
        ".devcontainer",
        ".github",
        ".github/actions",
        ".github/actions/setup-python-env",
        ".github/ISSUE_TEMPLATE",
        ".github/workflows",
        "data",
        "data/external",
        "data/interim",
        "data/processed",
        "data/raw",
        "docs",
        "logs",
        "secrets",
        "secrets/schema",
        "secrets/schema/ssh",
        "docker",
        "tests",
        str(OUT_DIR),
        str(OUT_DIR / "models"),
        str(OUT_DIR / "features"),
        str(OUT_DIR / "reports"),
        str(OUT_DIR / "reports" / "figures"),
        "notebooks",
        config["module_name"],
    }

    ignored_dirs = set()

    if config["environment_manager"] == "uv":
        expected_dirs.add(".venv")
        ignored_dirs.update({d.relative_to(root) for d in root.glob(".venv/**/*") if d.is_dir()})

    if config["include_code_scaffold"] != "No":
        expected_dirs.add(f"{config['module_name']}/_ai")
        expected_dirs.add(f"{config['module_name']}/_ai/modeling")
        expected_dirs.add(f"{config['module_name']}/_frontend")
        expected_dirs.add(f"{config['module_name']}/_backend")
        expected_dirs.add(f"{config['module_name']}/_course")
        ignored_dirs.update(
            {
                d.relative_to(root)
                for subdir in ["_frontend", "_backend", "_course"]
                for d in root.glob(f"{config['module_name']}/{subdir}/**/*")
                if d.is_dir()
            }
        )

    if config["docs"] == "mkdocs":
        expected_dirs.add("docs/docs")

    if config["version_control"] in (
        "git (local)",
        "git (github public)",
        "git (github private)",
    ):
        # Expected after `git init`
        expected_dirs.update(
            {
                ".git",
                # ".git/hooks",
                # ".git/info",
                # ".git/objects",
                # ".git/refs",
            }
        )
        # Expected after initial git commit
        # expected_dirs.update({".git/logs", ".git/logs/refs"})
        ignored_patterns = [
            ".git/**/*",
            "",
        ]  # [".git/objects/**/*", ".git/refs/**/*", ".git/logs/refs/**/*", ".git/branches/**/*"]
        ignored_dirs.update(
            {
                d.relative_to(root)
                for pattern in ignored_patterns
                for d in root.glob(pattern)
                if d.is_dir()
            }
        )

    expected_dirs = {Path(d) for d in expected_dirs}

    existing_dirs = {d.resolve().relative_to(root) for d in root.glob("**") if d.is_dir()}

    checked_dirs = existing_dirs - ignored_dirs

    assert sorted(checked_dirs) == sorted(expected_dirs)


def verify_files(root: Path, config: dict[str, Any]) -> None:
    """Test that expected files and only expected files exist.

    Args:
        root: Root directory path
        config: Configuration dictionary
    """
    expected_files = {
        "Makefile",
        "README.md",
        "pyproject.toml",
        "setup.cfg",
        ".env",
        ".gitignore",
        ".devcontainer/devcontainer.json",
        ".devcontainer/postCreateCommand.sh",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/actions/setup-python-env/action.yml",
        ".github/ISSUE_TEMPLATE/01_BUG_REPORT.md",
        ".github/ISSUE_TEMPLATE/02_FEATURE_REQUEST.md",
        ".github/ISSUE_TEMPLATE/03_CODEBASE_IMPROVEMENT.md",
        ".github/ISSUE_TEMPLATE/04_SUPPORT_QUESTION.md",
        ".github/ISSUE_TEMPLATE/config.yml",
        ".github/CODEOWNERS",
        ".github/labels.yml",
        ".github/workflows/main.yml",
        ".github/workflows/on-release-main.yml",
        ".gitattributes",
        ".pre-commit-config.yaml",
        "logs/.gitkeep",
        "data/external/.gitkeep",
        "data/interim/.gitkeep",
        "data/processed/.gitkeep",
        f"docker/{config['repo_name']}.Dockerfile",
        "data/raw/.gitkeep",
        "docs/.gitkeep",
        "docs/CODE_OF_CONDUCT.md",
        "docs/CONTRIBUTING.md",
        "docs/SECURITY.md",
        "tests/conftest.py",
        "tests/test_main.py",
        f"notebooks/0.01_{config['author_name']}_example.ipynb",
        "notebooks/README.md",
        "secrets/schema/example.env",
        "secrets/schema/ssh/example.config.ssh",
        "secrets/schema/ssh/example.something.key",
        "secrets/schema/ssh/example.something.pub",
        str(VSCODE_CONFIG_DIR / f"{config['repo_name']}.code-workspace"),
        str(VSCODE_CONFIG_DIR / "extensions.json"),
        str(VSCODE_CONFIG_DIR / "launch.json"),
        str(VSCODE_CONFIG_DIR / "settings.json"),
        str(VSCODE_CONFIG_DIR / "tasks.json"),
        str(VSCODE_CONFIG_DIR / f"{config['repo_name']}.code-workspace"),
        str(VSCODE_CONFIG_DIR / f"{config['repo_name']}.code-workspace"),
        str(OUT_DIR / "reports" / ".gitkeep"),
        str(OUT_DIR / "features" / ".gitkeep"),
        str(OUT_DIR / "reports" / "figures" / ".gitkeep"),
        str(OUT_DIR / "models" / ".gitkeep"),
        "Taskfile.yml",
        f"{config['module_name']}/__init__.py",
    }

    ignored_files = set()

    # conditional files
    if not config["open_source_license"].startswith("No license"):
        expected_files.add("LICENSE")

    if config["include_code_scaffold"] == "Yes":
        expected_files += [
            f"{config['module_name']}/config.py",
            f"{config['module_name']}/dataset.py",
            f"{config['module_name']}/features.py",
            f"{config['module_name']}/modeling/__init__.py",
            f"{config['module_name']}/modeling/train.py",
            f"{config['module_name']}/modeling/predict.py",
            f"{config['module_name']}/plots.py",
        ]

    if config["docs"] == "mkdocs":
        expected_files.update(
            {
                "docs/mkdocs.yml",
                "docs/README.md",
                "docs/docs/index.md",
                "docs/docs/getting-started.md",
            }
        )

    expected_files.add(config["dependency_file"])

    if config["dependency_file"] != "none":
        expected_files.add(config["dependency_file"])

    if config["environment_manager"] == "uv":
        expected_files.add("uv.lock")
        ignored_files.update({f.relative_to(root) for f in root.glob(f".venv/**/*") if f.is_file()})

    if config["version_control"] in (
        "git (local)",
        "git (github public)",
        "git (github private)",
    ):
        # # Expected after `git init`
        # expected_files.update(
        #     {
        #         ".git/config",
        #         ".git/description",
        #         ".git/HEAD",
        #         ".git/hooks/applypatch-msg.sample",
        #         ".git/hooks/commit-msg.sample",
        #         ".git/hooks/fsmonitor-watchman.sample",
        #         ".git/hooks/post-update.sample",
        #         ".git/hooks/pre-applypatch.sample",
        #         ".git/hooks/pre-commit.sample",
        #         ".git/hooks/pre-merge-commit.sample",
        #         ".git/hooks/pre-push.sample",
        #         ".git/hooks/pre-rebase.sample",
        #         ".git/hooks/pre-receive.sample",
        #         ".git/hooks/prepare-commit-msg.sample",
        #         ".git/hooks/push-to-checkout.sample",
        #         ".git/hooks/sendemail-validate.sample",
        #         ".git/hooks/update.sample",
        #         ".git/info/exclude",
        #     }
        # )
        # # Expected after initial git commit
        # expected_files.update(
        #     {
        #         ".git/COMMIT_EDITMSG",
        #         ".git/index",
        #         ".git/logs/HEAD",
        #     }
        # )
        ignored_file_patterns = [".git/**/*"]
        ignored_files.update(
            {
                f.relative_to(root)
                for pattern in ignored_file_patterns
                for f in root.glob(pattern)
                if f.is_file()
            }
        )

    expected_files = {Path(f) for f in expected_files}

    existing_files = {f.relative_to(root) for f in root.glob("**/*") if f.is_file()}

    checked_files = existing_files - ignored_files

    assert sorted(existing_files) == sorted(expected_files)

    # Ignore files where curlies may exist but aren't unrendered jinja tags
    ignore_curly_files = {
        Path(".git/hooks/fsmonitor-watchman.sample"),
        Path(".git/index"),
    }

    assert all(no_curlies(root / f) for f in checked_files - ignore_curly_files)


def verify_makefile_commands(root: Path, config: dict[str, Any]) -> bool:
    """Actually shell out to bash and run the make commands for:
    - blank command listing commands
    - create_environment
    - requirements
    - linting
    - formatting
    Ensure that these use the proper environment.

    Args:
        root: Root directory path
        config: Configuration dictionary

    Returns:
        True if verification succeeds

    Raises:
        ValueError: If environment manager not found in test harnesses
    """
    test_path = Path(__file__).parent

    if config["environment_manager"] == "conda":
        harness_path = test_path / "conda_harness.sh"
    elif config["environment_manager"] == "virtualenv":
        harness_path = test_path / "virtualenv_harness.sh"
    elif config["environment_manager"] == "pipenv":
        harness_path = test_path / "pipenv_harness.sh"
    elif config["environment_manager"] == "none":
        return True
    else:
        raise ValueError(
            f"Environment manager '{config['environment_manager']}' not found in test harnesses.",
        )

    result = run(
        [
            BASH_EXECUTABLE,
            str(harness_path),
            str(root.resolve()),
            str(config["module_name"]),
        ],
        stderr=PIPE,
        stdout=PIPE,
        check=False,
    )

    stdout_output, stderr_output = _decode_print_stdout_stderr(result)

    # Check that makefile help ran successfully
    assert "Available rules:" in stdout_output
    assert "clean" in stdout_output
    assert "Delete all compiled Python files" in stdout_output

    assert result.returncode == 0


def lint(root):
    """Run the linters on the project."""
    result = run(
        ["make", "lint"],
        cwd=root,
        stderr=PIPE,
        stdout=PIPE,
    )
    _, _ = _decode_print_stdout_stderr(result)

    assert result.returncode == 0
