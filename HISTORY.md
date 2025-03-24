# cookiecutter-data-science Changelog

## v2.2.0 (2025-03-23)

- Added `pyproject.toml` as a dependencies file format option. (PR [#436](https://github.com/drivendataorg/cookiecutter-data-science/pull/436))
- Added choice to include scaffolding for tests, with pytest and unittest as options. (PR [#447](https://github.com/drivendataorg/cookiecutter-data-science/pull/447))
- Fixed `requires-python` in `pyproject.toml` to correctly reflect the selected Python version. (PR [#446](https://github.com/drivendataorg/cookiecutter-data-science/pull/446))

## v2.1.0 (2025-03-10)

- Changed linting and formatting to be a new configuration choice (Discussion [#374](https://github.com/drivendataorg/cookiecutter-data-science/discussions/374))
   - Added support for Ruff as a new option. 
   - Changed the default choice to be Ruff.
   - Changed the previous behavior to be named "flake8+black+isort".
- Fixed `pyproject.toml` to correctly set isort configuration. Previously, configuration was being set for `ruff.lint.isort` instead of for isort, even though isort was installed and used by `make lint`.
- Fixed obsolete `[tool.ruff.lint.isort]` configuration key names that used underscores instead of hyphens. (Issue [#388](https://github.com/drivendataorg/cookiecutter-data-science/issues/388))
- Changed import sorting in generated code scaffold to match the generated isort configuration. 
- Added support for `uv pip` as an environment manager option (Discussion [#403](https://github.com/drivendataorg/cookiecutter-data-science/discussions/403))

## v2.0.1 (2025-02-26)

- Deprecates CI & support for Python 3.8, adds CI & support for Python 3.13 (Issue [#423](https://github.com/drivendataorg/cookiecutter-data-science/issues/423))
- Fixes issue with scaffold code that import of config did not work. Adds testing of imports to test suite. (Issue [#370](https://github.com/drivendataorg/cookiecutter-data-science/issues/370))
- Create automated release mechanism (Issue [#317](https://github.com/drivendataorg/cookiecutter-data-science/issues/317)) and pin template version to installed release (Issue [#389](https://github.com/drivendataorg/cookiecutter-data-science/issues/389))

## v2.0.0 (2024-05-22)

- Released version 2.0.0! :tada: See [docs](https://cookiecutter-data-science.drivendata.org/) and [announcement blog post](https://drivendata.co/blog/ccds-v2) for more information.
