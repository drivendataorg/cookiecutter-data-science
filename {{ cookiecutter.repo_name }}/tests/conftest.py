"""Configure pytest fixtures and settings for all tests.

This module contains shared fixtures that are automatically available to all test files.
"""

from pathlib import Path

import pytest
from loguru import logger


@pytest.fixture(scope="session", autouse=True)
def setup_logging() -> None:
    """Configure logging for tests."""
    logger.add(
        Path("logs") / "tests.log",
        rotation="1 day",
        level="DEBUG",
    )
