# AGENTS.md

* **Project name:** {{ cookiecutter.project_name }}
* **Description:** {{ cookiecutter.description }}

This project was generated from the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) template. Follow the conventions below when working in this codebase.

## Key Commands

Run tasks through `make`. Key recipes:

* `make` — List all available commands
* `make requirements` — Install/update dependencies
* `make data` — Run the data processing pipeline (assumes data is present in `data/raw/`){% if cookiecutter.linting_and_formatting != 'none' %}
* `make lint` — Check code style
* `make format` — Auto-format code{% endif %}{% if cookiecutter.testing_framework != 'none' %}
* `make test` — Run the test suite{% endif %}{% if not cookiecutter.dataset_storage.none %}
* `make sync_data_down` — Pull data from cloud storage
* `make sync_data_up` — Push data to cloud storage{% endif %}
* `make create_environment` — Set up the Python environment
* `make clean` — Remove compiled Python files

Add project-specific recipes to the `Makefile` for commands that are run frequently or require multiple steps.

## Project Directory Structure

* {{ cookiecutter.repo_name }}/
  * data/           <- Data files (gitignored)
    * raw/          <- Original, immutable data. NEVER modify.
    * external/     <- Third-party data sources.
    * interim/      <- Intermediate transformed data.
    * processed/    <- Final, canonical datasets.
  * models/         <- Trained models, predictions, summaries (gitignored)
  * notebooks/      <- Jupyter notebooks for exploration
  * references/     <- Data dictionaries, manuals, documentation
  * reports/        <- Generated analysis outputs
    * figures/      <- Generated figures
  * {{ cookiecutter.module_name }}/  <- Source code for this project{%- if cookiecutter.include_code_scaffold == 'Yes' %}
    * config.py     <- Project configuration and path definitions
    * dataset.py    <- Data loading and generation
    * features.py   <- Feature engineering code
    * plots.py      <- Visualization code
    * modeling/
      * train.py    <- Model training.
      * predict.py  <- Model inference{% endif %}
  * tests/          <- Test suite

## Core Principles

Reproducibility is the most critical component of any data science project. The following principles should be followed to ensure that the project is reproducible and maintainable.

### Data analysis is a directed acyclic graph

Treat the data pipeline as a directed acyclic graph. Each step takes inputs and produces outputs with no circular dependencies. Anyone must be able to reproduce final outputs from code and raw data alone.

### Raw data is immutable

Never edit, overwrite, or manually modify files in `data/raw/`. Data flows one direction:

`data/raw/` → `data/interim/` → `data/processed/`

Intermediate outputs should be cached in `interim/`. Analysis-ready datasets that are end products in themselves or don't require any more preprocessing or feature engineering go in `processed/`.

### Data is not in source control

The `data/` and `models/` directories are gitignored. Do not commit data files, trained models, or `.env` files to git.{% if not cookiecutter.dataset_storage.none %} Use `make sync_data_down` / `make sync_data_up` to sync data with cloud storage.{% endif %}

### Use Make as the task runner

Run all tasks through `make` — see the Key Commands section above for the full list of available recipes.

### Notebooks are for exploration; source code is for repetition

Use `notebooks/` for exploratory analysis notebooks. When code is reused across notebooks, refactor it into the `{{ cookiecutter.module_name }}/` package. The project is installed as a local package, so you can import with:

```python
from {{ cookiecutter.module_name }}.dataset import main
```

Notebook naming convention: `<step>.<order>-<identifier>-<description>.ipynb` (e.g., `0.3-bull-visualize-distributions.ipynb`). Step numbers: 0=exploration, 1=cleaning/features, 2=visualizations, 3=modeling, 4=publication. Order number defines execution order within each step.

### Secrets

**NEVER** read `.env` or any secrets files directly. Code should load secrets with `python-dotenv`. Use `{{ cookiecutter.module_name }}/config.py` for project paths and configuration. Never hardcode credentials, print secrets in logs, or add them to source control.

## Development Workflow

* **Python version:** {{ cookiecutter.python_version_number }}
{% if cookiecutter.environment_manager == 'conda' %}
* **Environment:** conda. Activate with `conda activate {{ cookiecutter.repo_name }}`.
{%- elif cookiecutter.environment_manager == 'virtualenv' %}
* **Environment:** virtualenv. Activate with `workon {{ cookiecutter.repo_name }}`.
{%- elif cookiecutter.environment_manager == 'pipenv' %}
* **Environment:** pipenv. Activate with `pipenv shell`.
{%- elif cookiecutter.environment_manager == 'uv' %}
* **Environment:** uv. Activate with `source .venv/bin/activate`.
{%- elif cookiecutter.environment_manager == 'pixi' %}
* **Environment:** pixi. Activate with `pixi shell`.
{%- elif cookiecutter.environment_manager == 'poetry' %}
* **Environment:** poetry. Activate with `$(poetry env activate)` or prefix commands with `poetry run`.
{%- endif %}
{% if cookiecutter.dependency_file == 'requirements.txt' %}
* **Dependencies:** Defined in `requirements.txt`. Install with `make requirements`.
{%- elif cookiecutter.dependency_file == 'pyproject.toml' %}
* **Dependencies:** Defined in `pyproject.toml`. Install with `make requirements`.
{%- elif cookiecutter.dependency_file == 'environment.yml' %}
* **Dependencies:** Defined in `environment.yml`. Install with `make requirements`.
{%- elif cookiecutter.dependency_file == 'Pipfile' %}
* **Dependencies:** Defined in `Pipfile`. Install with `make requirements`.
{%- elif cookiecutter.dependency_file == 'pixi.toml' %}
* **Dependencies:** Defined in `pixi.toml`. Install with `make requirements`.
{%- endif %}
{% if cookiecutter.linting_and_formatting == 'ruff' %}
* **Linting/Formatting:** Uses ruff. Run `make lint` to check, `make format` to fix.
{%- elif cookiecutter.linting_and_formatting == 'flake8+black+isort' %}
* **Linting/Formatting:** Uses flake8, black, and isort. Run `make lint` to check, `make format` to fix.
{%- endif %}
{% if cookiecutter.testing_framework == 'pytest' %}
* **Testing:** Uses pytest. Run `make test`.
{%- elif cookiecutter.testing_framework == 'unittest' %}
* **Testing:** Uses unittest. Run `make test`.
{%- endif %}

Linting and testing should succeed before committing work or at the end of each session. Run `make format` to format code if linting fails.

## Version Control

* Do not push to a remote repository without asking first.
* Write concise commit messages that describe the change and why it was made.{% if cookiecutter.linting_and_formatting != 'none' %}
* Run `make lint` and `make format` before committing changes.{% endif %}{% if cookiecutter.testing_framework != 'none' %}
* Run `make test` before committing changes. Fix any failures — do not skip or disable tests.{% endif %}

## Boundaries

### Always do

* Run all Python code within the project environment. {% if cookiecutter.environment_manager == 'conda' %}Use `conda run -n {{ cookiecutter.repo_name }}` to prefix commands, or activate with `conda activate {{ cookiecutter.repo_name }}` first.{% elif cookiecutter.environment_manager == 'uv' %}Use `uv run` to prefix commands, or activate with `source .venv/bin/activate` first.{% elif cookiecutter.environment_manager == 'pipenv' %}Use `pipenv run` to prefix commands, or activate with `pipenv shell` first.{% elif cookiecutter.environment_manager == 'pixi' %}Use `pixi run` to prefix commands, or activate with `pixi shell` first.{% elif cookiecutter.environment_manager == 'poetry' %}Use `poetry run` to prefix commands.{% elif cookiecutter.environment_manager == 'virtualenv' %}Activate with `workon {{ cookiecutter.repo_name }}` first.{% endif %}
* Update the dependency file when installing new packages
* Refactor reusable notebook code into the `{{ cookiecutter.module_name }}/` package

### Ask first

* Before deleting or overwriting files in `data/processed/`
* Before adding new dependencies to the project
* Before modifying the `Makefile`
* Before creating new notebooks

### Never do

* Delete, edit, or overwrite files in `data/raw/`
* Commit data files, trained models, or `.env` to version control
* Hardcode credentials or print secrets in logs
* Skip or disable lint rules or tests to get around failures
