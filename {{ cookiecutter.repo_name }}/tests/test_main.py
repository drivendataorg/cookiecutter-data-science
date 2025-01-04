"""Example test module demonstrating logging configuration."""

from loguru import logger


def test_example() -> None:
    """Example test that uses the configured logger."""
    logger.info("Running example test")
    logger.debug("This debug message will be captured in logs/tests.log")

    # Your actual test assertions would go here
    assert True, "This test should always pass"
