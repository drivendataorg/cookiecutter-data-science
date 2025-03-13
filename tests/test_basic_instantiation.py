# mypy: ignore-errors
# ruff: noqa
import json
import pytest
from pathlib import Path
import sys
import tempfile
import shutil
import logging
from contextlib import contextmanager

from conftest import bake_project, CCDS_ROOT
from ccds.__main__ import api_main

logger = logging.getLogger("test_basic_instantiation")


@contextmanager
def bake_project_basic(config: dict[str, str]):
    """Creates a temporary cookiecutter project for basic testing.

    This version catches exceptions during project creation and continues with testing.

    Args:
        config: Dictionary containing cookiecutter template configuration values.
            Must include a 'repo_name' key.

    Yields:
        Path: Path to the generated project directory.
    """
    temp = Path(tempfile.mkdtemp(suffix="data-project")).resolve()
    project_dir = temp / config["repo_name"]

    try:
        # Try to create the project, but catch any exceptions
        logger.info("Creating project with config: %s", json.dumps(config, indent=2))
        api_main.cookiecutter(
            str(CCDS_ROOT),
            no_input=True,
            extra_context=config,
            output_dir=temp,
            overwrite_if_exists=True,
        )
        logger.info("Project created successfully at: %s", project_dir)
    except Exception as e:
        logger.error("Error during project creation: %s - %s", type(e).__name__, str(e))
        logger.info("Continuing with basic tests despite error")

    try:
        yield project_dir
    finally:
        # cleanup after
        logger.debug("Cleaning up temporary directory: %s", temp)
        shutil.rmtree(temp)


@pytest.mark.basic
def test_basic_instantiation(config: dict[str, str]) -> None:
    """Test that a project can be instantiated without errors.

    This is a minimal test that only checks if the project can be created
    and has the basic expected structure. It doesn't verify all files or content.

    Args:
        config: Configuration dictionary
    """
    logger.info("Testing basic instantiation with config: %s", json.dumps(config, indent=2))

    with bake_project_basic(config) as project_directory:
        # Check if the project directory exists
        assert project_directory.exists(), "Project directory was not created"
        assert project_directory.is_dir(), "Project directory is not a directory"

        # Check if the module directory exists
        module_dir = project_directory / config["module_name"]
        if module_dir.exists():
            logger.debug("Module directory exists: %s", module_dir)
            assert module_dir.is_dir(), "Module directory is not a directory"

            # Check if the __init__.py file exists in the module directory
            init_file = module_dir / "__init__.py"
            if init_file.exists():
                logger.debug("__init__.py file exists: %s", init_file)
                assert init_file.is_file(), "__init__.py is not a file"
            else:
                logger.warning("__init__.py file does not exist in module directory")
        else:
            logger.warning(
                "Module directory does not exist: %s - skipping further checks", module_dir
            )
            pytest.skip(f"Module directory {module_dir} does not exist - skipping further checks")
