# Pytest Customization

## 00 Extensions

```toml
[
    "pytest-cases>=3.8.6",     # Parametrized testing
    "pytest-cov>=6.0.0",       # Coverage reporting
    "pytest-icdiff>=0.9",      # Improved diffs
    "pytest-mock>=3.14.0",     # Mocking
    "pytest-playwright>=0.6.2", # Browser testing
    "pytest-profiling>=1.8.1", # Test profiling
    "pytest-random-order>=1.1.1", # Randomized test order
    "pytest-shutil>=1.8.1",    # File system testing
    "pytest-split>=0.10.0",    # Parallel testing
    "pytest-sugar>=1.0.0",     # Test progress visualization
    "pytest-timeout>=2.3.1",   # Test timeouts
    "pytest>=8.3.4",           # Testing framework
]
```

<!-- TODO: Add explanation -->

## 01 Custom Option: `--max-timeout=SECONDS`

In Pytest, [it's common to make custom markers for slow and fast tests](https://docs.pytest.org/en/7.1.x/example/markers.html#registering-markers) and then filter for which ones you would like to run. I prefer a bit more granularity and to instead say "run tests that take less than $t$ seconds". To do this, I piggyback off of the [pytest-timeout](https://pypi.org/project/pytest-timeout/) package (which will need to be installed) to save some effort, making my own filter for tests with a timeout above a specified threshold.

### Example

```python
### test_example.py ###
"""Example test module demonstrating --max-timeout option for pytest."""

import pytest


@pytest.mark.timeout(10)
def test_example_slow() -> None:
    print("Running fast example test")


@pytest.mark.timeout(3)
def test_example_fast() -> None:
    print("Running slow example test")
```

Deselect the slow test by setting `--max-timeout=5`

```bash
pytest tests/test_example.py --max-timeout=5 --collect-only

# Test session starts (platform: darwin, Python 3.10.16, pytest 7.4.4, pytest-sugar 1.0.0)
# cachedir: .pytest_cache
# rootdir: /Users/gat/work/gatlens-opinionated-template
# configfile: pyproject.toml
# plugins: sugar-1.0.0, anyio-4.7.0, timeout-2.3.1
# collected 2 items / 1 deselected / 1 selected                                                                                                                                                                                                                

# <Module tests/test_example.py>
#   Example test module demonstrating logging configuration.
#   <Function test_example_fast>
#     Example test that uses the configured logger.


# Results (0.03s):
#        1 deselected
```

### Pytest Add Option

Adding the code to your `conftest.py` file should add the functionality:

```python
### conftest.py ###
def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Filter test items based on their timeout marker value.

    This pytest hook modifies the test collection by removing tests whose timeout
    value exceeds the maximum specified timeout, as well as tests without any
    timeout marker. The maximum timeout can be set using the --max-timeout command
    line option. If --max-timeout is not provided, all tests will run regardless
    of their timeout value.

    Args:
        config: The pytest configuration object containing test session information
        items: List of collected test items to be filtered

    Note:
        Tests are marked with @pytest.mark.timeout(value) decorator. If a test's
        timeout value is greater than max_timeout or if it has no timeout marker,
        it will be deselected.
    """
    max_timeout = config.getoption("--max-timeout")
    if max_timeout is None:
        return

    all_items = set(items)
    deselected_tests = {
        item
        for item in items
        if not item.get_closest_marker("timeout")  # Remove tests without timeout marker
        or item.get_closest_marker("timeout").args[0]
        > max_timeout  # Remove tests exceeding max_timeout
    }

    if deselected_tests:
        config.hook.pytest_deselected(items=list(deselected_tests))
        items[:] = list(all_items - deselected_tests)


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add custom command line options to pytest.

    This function registers two custom command line options:
    - --max-timeout: Set maximum allowed timeout for tests (default: None, run all tests)

    Args:
        parser: The pytest command line parser to which options will be added

    Example:
        Run tests with a maximum timeout of 10 seconds:
        pytest --max-timeout=10

        Run all tests regardless of timeout:
        pytest  # without --max-timeout option
    """
    parser.addoption(
        "--max-timeout",
        action="store",
        default=None,
        type=int,
        help="Only run tests with timeout less than this value. If not provided, run all tests.",
    )
```
