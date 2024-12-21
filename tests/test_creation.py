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
    """Print command stdout and stderr to console to use when debugging failing tests
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
    data = filepath.open("r").read()

    template_strings = [
        "{{ ",
        " }}",  # Exclude due to Go string templates in Taskfile
        "{%",
        "%}",
    ]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


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
        lint(project_directory)

        if fast < 2:
            verify_makefile_commands(project_directory, config)


def verify_folders(root: Path, config: dict[str, Any]) -> None:
    """Tests that expected folders and only expected folders exist.

    Args:
        root: Root directory path
        config: Configuration dictionary
    """
    expected_dirs = [
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
        str(OUT_DIR),
        str(OUT_DIR / "models"),
        str(OUT_DIR / "features"),
        str(OUT_DIR / "reports" / "figures"),
        "notebooks",
        # "references",
        str(OUT_DIR / "reports"),
        config["module_name"],
    ]

    ignore_dirs = [".git", ".venv"]

    if config["include_code_scaffold"] == "Yes":
        expected_dirs += [
            f"{config['module_name']}/modeling",
        ]

    if config["docs"] == "mkdocs":
        expected_dirs += ["docs/docs"]

    expected_dirs = [
        #  (root / d).resolve().relative_to(root) for d in expected_dirs
        Path(d)
        for d in expected_dirs
    ]

    existing_dirs = [
        d.resolve().relative_to(root)
        for d in root.glob("**")
        if d.is_dir()
        and not any(
            ignore_dir in d.relative_to(root).parts for ignore_dir in ignore_dirs
        )
    ]

    assert sorted(existing_dirs) == sorted(expected_dirs)


def verify_files(root: Path, config: dict[str, Any]) -> None:
    """Test that expected files and only expected files exist.

    Args:
        root: Root directory path
        config: Configuration dictionary
    """
    expected_files = [
        "Makefile",
        str(CCDS_ORIGINAL_DIR / "README.md"),
        "README.md",
        "pyproject.toml",
        # "setup.cfg",
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
        "notebooks/01_name_example.ipynb",
        "notebooks/README.md",
        "secrets/schema/example.env",
        "secrets/schema/ssh/example.config.ssh",
        "secrets/schema/ssh/example.something.key",
        "secrets/schema/ssh/example.something.pub",
        # "references/.gitkeep",
        str(VSCODE_CONFIG_DIR / f"{config['repo_name']}.code-workspace"),
        str(VSCODE_CONFIG_DIR / "launch.json"),
        str(VSCODE_CONFIG_DIR / "settings.json"),
        str(VSCODE_CONFIG_DIR / "tasks.json"),
        str(OUT_DIR / "reports" / ".gitkeep"),
        str(OUT_DIR / "features" / ".gitkeep"),
        str(OUT_DIR / "reports" / "figures" / ".gitkeep"),
        str(OUT_DIR / "models" / ".gitkeep"),
        "Taskfile.yml",
        ".cursorrules",
        f"{config['module_name']}/__init__.py",
    ]

    ignore_dirs = [".git", ".venv"]

    # conditional files
    if not config["open_source_license"].startswith("No license"):
        expected_files.append("LICENSE")

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
        expected_files += [
            "docs/mkdocs.yml",
            "docs/README.md",
            "docs/docs/index.md",
            "docs/docs/getting-started.md",
        ]

    expected_files.append(config["dependency_file"])

    expected_files = [Path(f) for f in expected_files]

    existing_files = [
        f.relative_to(root)
        for f in root.glob("**/*")
        if f.is_file()
        and not any(
            ignore_dir in f.relative_to(root).parts for ignore_dir in ignore_dirs
        )
    ]

    assert sorted(existing_files) == sorted(expected_files)

    for f in existing_files:
        assert no_curlies(root / f)


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
    assert "clean                    Delete all compiled Python files" in stdout_output

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
