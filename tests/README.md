# Testing the Project Template

This directory contains tests for the project template. There are three main types of tests:

1. **Template Rendering Tests**: These tests only check if the template can be rendered without executing hooks.
1. **Basic Instantiation Tests**: These tests check if the project can be instantiated and has the basic expected structure.
1. **Detailed Verification Tests**: These tests verify the file structure, content, and functionality of the generated project.

## Running Tests

### Template Rendering Tests

To run only the template rendering tests:

```bash
pytest tests/test_template_rendering.py
```

These tests are the most minimal and only check if the template can be rendered without errors. They:

- Skip all pre/post hooks
- Only verify that the project directory is created

### Basic Instantiation Tests

To run only the basic instantiation tests:

```bash
pytest --test-type=basic
```

These tests attempt to create the project and perform basic checks, even if hooks fail. They verify:

- The project directory is created
- The module directory exists (if created)
- The `__init__.py` file exists in the module directory (if created)

### Detailed Verification Tests

To run only the detailed verification tests:

```bash
pytest --test-type=detailed
```

These tests are more comprehensive and verify:

- All expected folders exist
- All expected files exist
- Makefile commands work correctly
- No template strings remain in the generated files

### Running All Tests

To run all tests:

```bash
pytest --test-type=all
```

or simply:

```bash
pytest
```

## Additional Options

### Fast Mode

You can speed up tests by using the `--fast` or `-F` option:

```bash
pytest --fast
```

This will reduce the number of configurations tested and skip some validations.

### Maximum Timeout

You can set a maximum timeout for tests:

```bash
pytest --max-timeout=10
```

This will only run tests with a timeout less than the specified value.

## Logging in Tests

The tests use Python's standard logging module with colorized output. Logs are displayed in the console during test execution and also saved to a log file.

### Colored Output

The log messages are colorized for better readability:

- **Timestamps**: Standard color
- **Log Levels**: Color-coded (DEBUG: cyan, INFO: green, WARNING: yellow, ERROR/CRITICAL: red)
- **Context**: Module names in magenta, file names in blue
- **Messages**: Standard color

This makes it easier to identify different parts of the log messages, especially when looking for specific contexts like "cookiecutter.hooks:hooks.py".

### Log Levels

The tests use the following log levels:

- **DEBUG**: Detailed diagnostic information
- **INFO**: General information about test progress
- **WARNING**: Issues that don't fail the test but are worth noting
- **ERROR**: Errors that occur during test execution

### Viewing Logs

By default, logs at the INFO level and above are displayed in the console. To see more detailed logs, you can adjust the log level:

```bash
pytest --log-cli-level=DEBUG
```

Logs are also saved to `./logs/pytest.log` for later review.

## Test Configuration

Tests are run with various configurations generated from the `ccds.json` file. Each configuration represents a different combination of options that can be selected when creating a project.

The `config_generator` function in `conftest.py` generates these configurations.
