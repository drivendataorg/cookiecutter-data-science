# type: ignore
# ruff: noqa
from collections.abc import Generator
from contextlib import contextmanager
from itertools import cycle, product
import json
from pathlib import Path
import shutil
import sys
import tempfile
import logging
import re

import pytest
import colorama
from colorama import Fore, Back, Style

# Initialize colorama
colorama.init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    """Custom formatter with colored output."""

    # Define color patterns for different parts of the log message
    COLORS = {
        "DEBUG": Fore.CYAN,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.RED + Style.BRIGHT,
    }

    # Pattern to match context (e.g., "cookiecutter.hooks:hooks.py")
    CONTEXT_PATTERN = re.compile(r"([a-zA-Z0-9_\.]+):([a-zA-Z0-9_\.]+)")

    def format(self, record):
        """Format the log record with colors."""
        # Get the original formatted message
        log_message = super().format(record)

        # Color the level name
        levelname_color = self.COLORS.get(record.levelname, "")
        log_message = log_message.replace(
            record.levelname, f"{levelname_color}{record.levelname}{Style.RESET_ALL}"
        )

        # Color the context (module:file)
        def color_context(match):
            module, file = match.groups()
            return f"{Fore.MAGENTA}{module}{Style.RESET_ALL}:{Fore.BLUE}{file}{Style.RESET_ALL}"

        log_message = self.CONTEXT_PATTERN.sub(color_context, log_message)

        return log_message


# Simple logging setup for tests
@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Configure basic logging for tests with colored output."""
    # Create a colored formatter
    formatter = ColoredFormatter(
        "%(asctime)s - %(levelname)s - %(name)s:%(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Configure the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Remove any existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Create a console handler with the colored formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # Also set up a file handler for the log file
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler("logs/pytest.log")
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s:%(filename)s:%(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    root_logger.addHandler(file_handler)

    # Log that we've set up logging
    root_logger.info("Logging configured with colored output")


from ccds.__main__ import api_main


CCDS_ROOT = Path(__file__).parents[1].resolve()

default_args: dict[str, str] = {
    "project_name": "my_test_project",
    "repo_name": "my-test-repo",
    "module_name": "project_module",
    "author_name": "DrivenData",
    "description": "A test project",
}

### GATLEN'S TEST ###


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Filter test items based on their timeout marker value and test type.

    This pytest hook modifies the test collection by removing tests whose timeout
    value exceeds the maximum specified timeout, as well as tests without any
    timeout marker. The maximum timeout can be set using the --max-timeout command
    line option. If --max-timeout is not provided, all tests will run regardless
    of their timeout value.

    Additionally, it filters tests based on the --test-type option.

    Args:
        config: The pytest configuration object containing test session information
        items: List of collected test items to be filtered

    Note:
        Tests are marked with @pytest.mark.timeout(value) decorator. If a test's
        timeout value is greater than max_timeout or if it has no timeout marker,
        it will be deselected.
    """
    max_timeout = config.getoption("--max-timeout")
    test_type = config.getoption("--test-type")

    all_items = set(items)
    deselected_tests = set()

    # Filter by timeout
    if max_timeout is not None:
        deselected_tests.update(
            {
                item
                for item in items
                if not item.get_closest_marker("timeout")  # Remove tests without timeout marker
                or item.get_closest_marker("timeout").args[0]
                > max_timeout  # Remove tests exceeding max_timeout
            }
        )

    # Filter by test type
    if test_type == "basic":
        deselected_tests.update({item for item in items if not item.get_closest_marker("basic")})
    elif test_type == "detailed":
        deselected_tests.update({item for item in items if not item.get_closest_marker("detailed")})
    # If test_type is "all" or None, don't filter by test type

    if deselected_tests:
        config.hook.pytest_deselected(items=list(deselected_tests))
        items[:] = list(all_items - deselected_tests)


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add custom command line options to pytest.

    This function registers custom command line options:
    - --max-timeout: Set maximum allowed timeout for tests (default: None, run all tests)
    - --fast (-F): Control test execution speed by skipping certain validations
    - --test-type: Select which type of tests to run (basic, detailed, or all)

    Args:
        parser: The pytest command line parser to which options will be added

    Example:
        Run tests with a maximum timeout of 10 seconds:
        pytest --max-timeout=10

        Run all tests regardless of timeout:
        pytest  # without --max-timeout option

        Run tests in fast mode:
        pytest --fast or pytest -F

        Run only basic instantiation tests:
        pytest --test-type=basic

        Run only detailed verification tests:
        pytest --test-type=detailed

        Run all tests:
        pytest --test-type=all
    """
    parser.addoption(
        "--max-timeout",
        action="store",
        default=None,
        type=int,
        help="Only run tests with timeout less than this value. If not provided, run all tests.",
    )
    parser.addoption(
        "--fast",
        "-F",
        action="count",
        default=0,
        help="Speed up tests by skipping configs and/or Makefile validation",
    )
    parser.addoption(
        "--test-type",
        action="store",
        default="all",
        choices=["basic", "detailed", "all"],
        help="Select which type of tests to run: basic instantiation, detailed verification, or all",
    )


### GATLEN'S TEST ###


def config_generator(fast: int | bool = False) -> Generator[dict[str, str], None, None]:
    """Generate test configurations based on cookiecutter.json options.

    Args:
        fast: Speed control flag for test execution

    Yields:
        Dictionary of configuration options for each test case
    """
    cookiecutter_json: dict[str, list[str]] = json.load(
        (CCDS_ROOT / "ccds.json").open("r"),
    )

    running_py_version: str = f"{sys.version_info.major}.{sys.version_info.minor}"
    py_version: list[tuple[str, str]] = [("python_version_number", v) for v in [running_py_version]]

    filtered_configs = list(
        product(
            py_version,
            [("environment_manager", opt) for opt in cookiecutter_json["environment_manager"]],
            [("dependency_file", opt) for opt in cookiecutter_json["dependency_file"]],
            [("pydata_packages", opt) for opt in cookiecutter_json["pydata_packages"]],
            [("version_control", opt) for opt in ("none", "git (local)")],
            # TODO: Tests for "version_control": "git (github)"
        ),
    )

    def _is_valid(config) -> bool:
        config_dict: dict[str, str] = dict(config)
        if (config_dict["dependency_file"] == "none") and (
            config_dict["environment_manager"] != "uv"
        ):
            return False
        if (config_dict["environment_manager"] == "pipenv") ^ (
            config_dict["dependency_file"] == "Pipfile"
        ):
            return False
        # conda is the only valid env manager for environment.yml
        if (config_dict["dependency_file"] == "environment.yml") and (
            config_dict["environment_manager"] != "conda"
        ):
            return False
        # pixi is the only valid env manager for pixi.toml
        if (config_dict["dependency_file"] == "pixi.toml") and (
            config_dict["environment_manager"] != "pixi"
        ):
            return False
        # pixi supports both pixi.toml and pyproject.toml
        if (config_dict["environment_manager"] == "pixi") and (
            config_dict["dependency_file"] not in ["pixi.toml", "pyproject.toml"]
        ):
            return False
        # poetry only supports pyproject.toml
        if (config_dict["environment_manager"] == "poetry") and (
            config_dict["dependency_file"] != "pyproject.toml"
        ):
            return False
        return True

    # remove invalid configs
    filtered_configs = [c for c in filtered_configs if _is_valid(c)]

    # ensure linting and formatting options are run on code scaffold
    # otherwise, linting "passes" because one linter never runs on any code during tests
    code_format_cycler = cycle(
        product(
            [
                ("include_code_scaffold", opt)
                for opt in cookiecutter_json["include_code_scaffold"]
            ],
            [
                ("linting_and_formatting", opt)
                for opt in cookiecutter_json["linting_and_formatting"]
            ],
        )
    )

    # cycle over values for multi-select fields that should be inter-operable
    # and that we don't need to handle with combinatorics
    cycle_fields: list[str] = [
        "dataset_storage",
        "open_source_license",
        "docs",
    ]
    multi_select_cyclers = {k: cycle(cookiecutter_json[k]) for k in cycle_fields}

    for ind, c in enumerate(filtered_configs):
        config = dict(c)
        config.update(default_args)

        code_format_settings = dict(next(code_format_cycler))
        config.update(code_format_settings)

        for field, cycler in multi_select_cyclers.items():
            config[field] = next(cycler)

        config["repo_name"] += f"-{ind}"
        yield config

        # just do a single config if fast passed once or three times
        if fast == 1 or fast >= 3:
            break


@pytest.fixture
def fast(request):
    return request.config.getoption("--fast")


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:  # type: ignore[misc]
    """Generate test configurations."""

    def make_test_id(config: dict[str, str]) -> str:
        # Map full names to shorter versions
        abbreviations = {
            "environment_manager": {
                "none": "no-env",
                "virtualenv": "venv",
                "conda": "con",
                "pipenv": "penv",
                "uv": "uv",
                "pixi": "pixi",
                "poetry": "poet",
            },
            "dependency_file": {
                "requirements.txt": "req.txt",
                "environment.yml": "env.yml",
                "Pipfile": "pfile",
                "pyproject.toml": "pyproj",
                "pixi.toml": "pixi",
            },
            "docs": {"mkdocs": "mkdocs", "none": "no-doc"},
            "version_control": {
                "none": "no-vc",
                "git (local)": "git",
                "git (github private)": "gh-prv",
                "git (github public)": "gh-pub",
            },
            "pydata_packages": {"none": "no-pkg", "basic": "pkg"},
        }

        # Define column widths
        cols = [
            ("env", 6),  # environment_manager
            ("dep", 6),  # dependency_file
            ("doc", 6),  # docs
            ("vc", 6),  # version_control
            ("pkg", 6),  # pydata_packages
        ]

        # Format each component with fixed width
        components = []
        for (prefix, width), key in zip(
            cols,
            [
                "environment_manager",
                "dependency_file",
                "docs",
                "version_control",
                "pydata_packages",
            ],
            strict=False,
        ):
            value = abbreviations[key][config[key]]
            # Ensure exact width by padding or truncating
            formatted = f"{value:<{width}}"[:width]
            components.append(formatted)

        return " ".join(components)

    if "config" in metafunc.fixturenames:
        configs = list(config_generator(metafunc.config.getoption("fast")))
        parametrize_args = [
            (
                pytest.param(config, marks=pytest.mark.xfail)
                if config["environment_manager"] == "conda"
                else config
            )
            for config in configs
        ]
        metafunc.parametrize(
            "config",
            parametrize_args,
            ids=make_test_id,
        )


@contextmanager
def bake_project(config: dict[str, str]) -> Generator[Path, None, None]:
    """Creates a temporary cookiecutter project for testing purposes.

    This context manager creates a temporary directory, bakes a cookiecutter project
    using the provided configuration, and cleans up afterwards.

    Args:
        config: Dictionary containing cookiecutter template configuration values.
            Must include a 'repo_name' key.

    Yields:
        Path: Path to the generated project directory.

    Example:
        >>> config = {"repo_name": "test-project", ...}
        >>> with bake_project(config) as project_path:
        ...     # work with generated project
        ...     pass
        >>> # Directory is automatically cleaned up after context exits
    """
    temp = Path(tempfile.mkdtemp(suffix="data-project")).resolve()

    api_main.cookiecutter(
        str(CCDS_ROOT),
        no_input=True,
        extra_context=config,
        output_dir=temp,
        overwrite_if_exists=True,
    )

    yield temp / config["repo_name"]

    # cleanup after
    shutil.rmtree(temp)
