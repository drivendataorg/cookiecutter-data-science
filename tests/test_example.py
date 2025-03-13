# mypy: ignore-errors
# ruff: noqa
import pytest
import time


@pytest.mark.timeout(1)
@pytest.mark.basic
def test_fast_basic():
    """A fast test with a timeout of 1 second, marked as basic."""
    time.sleep(0.5)
    assert True


@pytest.mark.timeout(5)
@pytest.mark.detailed
def test_slow_detailed():
    """A slower test with a timeout of 5 seconds, marked as detailed."""
    time.sleep(2)
    assert True


@pytest.mark.timeout(10)
@pytest.mark.basic
def test_very_slow_basic():
    """A very slow test with a timeout of 10 seconds, marked as basic."""
    time.sleep(5)
    assert True


@pytest.mark.timeout(3)
@pytest.mark.detailed
def test_medium_detailed():
    """A medium test with a timeout of 3 seconds, marked as detailed."""
    time.sleep(1)
    assert True
