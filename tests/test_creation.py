import json
import os
import sys
from pathlib import Path
from subprocess import PIPE, CompletedProcess, run
from typing import Any

from conftest import bake_project

BASH_EXECUTABLE = os.getenv("BASH_EXECUTABLE", "bash")


# GATLEN'S ADDED BITS #
CCDS_ORIGINAL_DIR = Path(".ccds-original")
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

    print("\n======================= STDOUT ======================")
    stdout = result.stdout.decode(encoding)
    print(stdout)

    print("\n======================= STDERR ======================")
    stderr = result.stderr.decode(encoding)
    print(stderr)

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


def test_baking_configs(config: dict[str, Any], fast: int) -> None:
    """For every generated config in the config_generator, run all
    of the tests.

    Args:
        config: Configuration dictionary
        fast: Integer controlling test speed/depth
    """
    print("using config", json.dumps(config, indent=2))
    with bake_project(config) as project_directory:
        verify_folders(project_directory, config)
        verify_files(project_directory, config)
        # install_requirements(project_directory)
        # lint(project_directory)

        if fast < 2:
            verify_makefile_commands(project_directory, config)


def verify_folders(root: Path, config: dict[str, Any]) -> None:
    """Tests that expected folders and only expected folders exist.

    Args:
        root: Root directory path
        config: Configuration dictionary
    """
    expected_dirs = {
        str(CCDS_ORIGINAL_DIR),
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

    if config["include_code_scaffold"] != "No":
        expected_dirs.add(f"{config['module_name']}/_ai")
        expected_dirs.add(f"{config['module_name']}/_ai/modeling")
        expected_dirs.add(f"{config['module_name']}/_frontend")
        expected_dirs.add(f"{config['module_name']}/_backend")
        expected_dirs.add(f"{config['module_name']}/_course")
        ignored_dirs.update({
            d.relative_to(root)
            for subdir in ["_frontend", "_backend", "_course"]
            for d in root.glob(f"{config['module_name']}/{subdir}/**/*")
            if d.is_dir()
        })

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
                ".git/hooks",
                ".git/info",
                ".git/objects",
                ".git/refs",
                ".git/refs/heads",
                ".git/refs/tags",
            }
        )
        # Expected after initial git commit
        expected_dirs.update(
            {
                ".git/logs",
                ".git/logs/refs",
                ".git/logs/refs/heads",
            }
        )
        ignored_dirs.update(
            {d.relative_to(root) for d in root.glob(".git/objects/**/*") if d.is_dir()}
        )

    expected_dirs = {Path(d) for d in expected_dirs}

    existing_dirs = {
        d.resolve().relative_to(root) for d in root.glob("**") if d.is_dir()
    }
    
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
        str(CCDS_ORIGINAL_DIR / "README.md"),
        "README.md",
        "pyproject.toml",
        ".env",
        ".gitignore",
        ".devcontainer/devcontainer.json",
        ".devcontainer/postCreateCommand.sh",
        ".github/pull_request_template.md",
        ".github/actions/setup-python-env/action.yml",
        ".github/ISSUE_TEMPLATE/bug_report.md",
        ".github/ISSUE_TEMPLATE/feature_request.md",
        ".github/ISSUE_TEMPLATE/general_question.md",
        ".github/workflows/main.yml",
        ".github/workflows/on-release-main.yml",
        ".gitattributes",
        "logs/.gitkeep",
        "data/external/.gitkeep",
        "data/interim/.gitkeep",
        "data/processed/.gitkeep",
        f"docker/{config['repo_name']}.Dockerfile",
        "data/raw/.gitkeep",
        "docs/.gitkeep",
        "tests/conftest.py",
        "tests/test_main.py",
        "notebooks/0.01_gatlen_example.ipynb",
        "notebooks/README.md",
        "secrets/schema/example.env",
        "secrets/schema/ssh/example.config.ssh",
        "secrets/schema/ssh/example.something.key",
        "secrets/schema/ssh/example.something.pub",
        str(VSCODE_CONFIG_DIR / f"{config['repo_name']}.code-workspace"),
        str(VSCODE_CONFIG_DIR / f"{config['repo_name']}.team.code-workspace"),
        str(OUT_DIR / "reports" / ".gitkeep"),
        str(OUT_DIR / "features" / ".gitkeep"),
        str(OUT_DIR / "reports" / "figures" / ".gitkeep"),
        str(OUT_DIR / "models" / ".gitkeep"),
        "Taskfile.yml",
        ".cursorrules",
        f"{config['module_name']}/__init__.py",
    }

    ignored_files = set()

    # conditional files
    if not config["open_source_license"].startswith("No license"):
        expected_files.add("LICENSE")

    if config["include_code_scaffold"] != "No":    
        expected_files.update({
            f"{config['module_name']}/_ai/dataset.py",
            f"{config['module_name']}/_ai/plots.py",
            f"{config['module_name']}/_ai/features.py",
            f"{config['module_name']}/_ai/modeling/__init__.py",
            f"{config['module_name']}/_ai/modeling/predict.py",
            f"{config['module_name']}/_ai/modeling/train.py",
            f"{config['module_name']}/config.py"
        })
        # Create a set of all files to ignore using set union
        ignored_files.update({
            f.relative_to(root)
            for subdir in ["_frontend", "_backend", "_course"]
            for f in root.glob(f"{config['module_name']}/{subdir}/**/*")
            if f.is_file()
        })
    
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

    if config["version_control"] in (
        "git (local)",
        "git (github public)",
        "git (github private)",
    ):
        # Expected after `git init`
        expected_files.update(
            {
                ".git/config",
                ".git/description",
                ".git/HEAD",
                ".git/hooks/applypatch-msg.sample",
                ".git/hooks/commit-msg.sample",
                ".git/hooks/fsmonitor-watchman.sample",
                ".git/hooks/post-update.sample",
                ".git/hooks/pre-applypatch.sample",
                ".git/hooks/pre-commit.sample",
                ".git/hooks/pre-merge-commit.sample",
                ".git/hooks/pre-push.sample",
                ".git/hooks/pre-rebase.sample",
                ".git/hooks/pre-receive.sample",
                ".git/hooks/prepare-commit-msg.sample",
                ".git/hooks/push-to-checkout.sample",
                ".git/hooks/sendemail-validate.sample",
                ".git/hooks/update.sample",
                ".git/info/exclude",
            }
        )
        # Expected after initial git commit
        expected_files.update(
            {
                ".git/COMMIT_EDITMSG",
                ".git/index",
                ".git/logs/HEAD",
                ".git/logs/refs/heads/main",
                ".git/refs/heads/main",
            }
        )
        ignored_files.update(
            {f.relative_to(root) for f in root.glob(".git/objects/**/*") if f.is_file()}
        )

    expected_files = {Path(f) for f in expected_files}

    existing_files = {f.relative_to(root) for f in root.glob("**/*") if f.is_file()}

    checked_files = existing_files - ignored_files

    assert sorted(checked_files) == sorted(expected_files)

    # Ignore files where curlies may exist but aren't unrendered jinja tags
    ignore_curly_files = {
        Path(".git/hooks/fsmonitor-watchman.sample"),
        Path(".git/index"),
        Path(".cursorrules"),
    }

    assert all(no_curlies(root / f) for f in checked_files - ignore_curly_files)


def verify_makefile_commands(root: Path, config: dict[str, Any]) -> bool:
    """Actually shell out to bash and run the make commands for:
    - blank command listing commands
    - create_environment
    - requirements
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
    elif config["environment_manager"] == "uv":
        harness_path = test_path / "uv_harness.sh"
    elif config["environment_manager"] == "none":
        return True
    else:
        raise ValueError(
            f"Environment manager '{config['environment_manager']}' not found in test harnesses."
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
    )

    stdout_output, _ = _decode_print_stdout_stderr(result)

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
