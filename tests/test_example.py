# ruff: noqa
"""Example test module demonstrating --max-timeout option for pytest."""

import pytest


@pytest.mark.timeout(10)
def test_example_slow() -> None:
    print("Running fast example test")


@pytest.mark.timeout(3)
def test_example_fast() -> None:
    print("Running slow example test")
