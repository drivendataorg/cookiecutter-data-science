# Basic Usage:
#   make <rule>             : Run a specific rule (e.g., make test)
#   make VAR=value <rule>   : Run rule with environment variable (e.g., make DOCS_PORT=8080 docs-serve)
#
# Common Rules: help, clean, test, format, lint, docs-serve
#
# Rules can depend on other rules which run first. Rules with _ prefix are internal helpers.

PROJECT_NAME = {{ cookiecutter.repo_name }}
MODULE_NAME = {{ cookiecutter.module_name }}
PYTHON_VERSION = {{ cookiecutter.python_version_number }}
PYTHON_INTERPRETER = python
DOCS_PORT ?= 8000
.DEFAULT_GOAL := help

# ━━━━━━━━━━━━━━━━━━━━━━━━━━ Project Rules ━━━━━━━━━━━━━━━━━━━━━━━━━ #

# Write your custom rules here

{% if cookiecutter.include_code_scaffold in ("data", "ml") %}
.PHONY: data
data: requirements ## Make Dataset
	$(PYTHON_INTERPRETER) $(MODULE_NAME)/dataset.py
{%- endif %}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Utilities ━━━━━━━━━━━━━━━━━━━━━━━━━━━ #
.PHONY: all help _print-logo _welcome

all: help

help: _print-logo  ## Show this help message
	@echo "\n\033[1m~ Available rules: ~\033[0m\n"
	@echo "For VSCode/Cursor, try: ⇧ ⌘ P, Tasks: Run Task\n"
	@grep -E '^[a-zA-Z][a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[38;5;222m%-30s\033[0m %s\n", $$1, $$2}'

_welcome: ## Print a Welcome screen
	curl -s https://raw.githubusercontent.com/GatlenCulp/gatlens-opinionated-template/refs/heads/master/welcome.txt

_print-logo: ## Prints the GOTem logo
	@echo "\033[38;5;39m   ____  ___ _____"
	@echo "  / ___|/ _ \_   _|__ _ __ ___"
	@echo " | |  _| | | || |/ _ \ '_ \` _ \\"
	@echo " | |_| | |_| || |  __/ | | | | |"
	@echo "  \____|\___/ |_|\___|_| |_| |_|\033[0m"

# ━━━━━━━━━━━━━━━━━━━━━━━ Filesystem Cleaning ━━━━━━━━━━━━━━━━━━━━━━ #
.PHONY: clean _clean-mac _clean-latex _clean-python

clean: _clean-mac _clean-latex _clean-python ## Delete all compiled Python files and LaTeX build artifacts
	find . -type d -name ".cache" -delete

_clean-mac: ## Clean macOS-related files
	find . -type f -name "*.DS_store" -delete

_clean-latex: ## Clean all LaTeX helper files
	find . -type f -name "*.aux" -delete
	find . -type f -name "*.bbl" -delete
	find . -type f -name "*.bcf" -delete
	find . -type f -name "*.blg" -delete
	find . -type f -name "*.fdb_latexmk" -delete
	find . -type f -name "*.fls" -delete
	find . -type f -name "*.lof" -delete
	find . -type f -name "*.log" -delete
	find . -type f -name "*.lot" -delete
	find . -type f -name "*.out" -delete
	find . -type f -name "*.synctex.gz*" -delete
	find . -type f -name "*.toc" -delete
	find . -type d -name "_minted*" -delete

_clean-python: ## Clean all compiled Python files
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Testing ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ #

.PHONY: test test-fastest test-continuous test-debug-last _clean_manual_test

test: ## Run all tests
	pytest -vvv --durations=0

test-fastest: ## Run tests with fail-fast option
	pytest -vvv -FFF

test-continuous: ## Run tests in watch mode using pytest-watcher
	ptw . --now --runner pytest --config-file pyproject.toml -vvv -FFF

test-debug-last: ## Debug last failed test with pdb
	pytest --lf --pdb


manual-test: _clean_manual_test ## Run manual tests
	mkdir -p manual_test
	@echo "<manual-test not yet implemented>"

_clean_manual_test:
	rm -rf manual_test

# ━━━━━━━━━━━━━━━━━━━━━━━━━ Quality Assurance ━━━━━━━━━━━━━━━━━━━━━━━ #

.PHONY: lint format

lint: ## Lint using ruff (use `make format` to do formatting)
	ruff check --config pyproject.toml $(MODULE_NAME)

format: ## Format source code
	ruff format --config pyproject.toml $(MODULE_NAME)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━ Documentation ━━━━━━━━━━━━━━━━━━━━━━━━━ #

.PHONY: docs-serve docs-publish

docs-serve: ## Serve documentation locally on port $(DOCS_PORT)
	cd docs && \
	mkdocs serve -a localhost:$(DOCS_PORT) || \
	echo "\n\nInstance found running on $(DOCS_PORT), try killing process and rerun."

# Makes sure docs can be served prior to actually deploying
docs-publish: ## Build and deploy documentation to GitHub Pages
	cd docs && \
	mkdocs build && \
	mkdocs gh-deploy --clean

# ━━━━━━━━━━━━━━━━━━━━━ Packaging & Environment ━━━━━━━━━━━━━━━━━━━━ #

{% if cookiecutter.environment_manager != 'none' -%}
.PHONY: create_environment
create_environment: ## Set up python interpreter environment
	{%- if cookiecutter.environment_manager == 'conda' %}
	{%- if cookiecutter.dependency_file != 'environment.yml' %}
	conda create --name $(PROJECT_NAME) python=$(PYTHON_VERSION) -y
	{%- else %}
	conda env create --name $(PROJECT_NAME) -f environment.yml
	{%- endif %}
	@echo ">>> conda env created. Activate with:\nconda activate $(PROJECT_NAME)"
	{%- elif cookiecutter.environment_manager == 'virtualenv' %}
	@bash -c "if [ ! -z `which virtualenvwrapper.sh` ]; then source `which virtualenvwrapper.sh`; mkvirtualenv $(PROJECT_NAME) --python=$(PYTHON_INTERPRETER); else mkvirtualenv.bat $(PROJECT_NAME) --python=$(PYTHON_INTERPRETER); fi"
	@echo ">>> New virtualenv created. Activate with:\nworkon $(PROJECT_NAME)"
	{%- elif cookiecutter.environment_manager == 'pipenv' %}
	pipenv --python $(PYTHON_VERSION)
	@echo ">>> New pipenv created. Activate with:\npipenv shell"
	{%- elif cookiecutter.environment_manager == 'uv' %}
	uv venv
	@echo ">>> New virtualenv with uv created. Activate with:\nsource '.venv/bin/activate'"
	{%- endif %}
{%- endif %}

{% if cookiecutter.dependency_file != 'none' or cookiecutter.environment_manager == 'uv' %}
.PHONY: requirements
requirements:
	{% if "requirements.txt" == cookiecutter.dependency_file -%}
	{% if "uv" == cookiecutter.environment_manager -%}
	uv pip install -r requirements.txt
	{% else -%}
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	{% endif -%}
	{% elif "pyproject.toml" == cookiecutter.dependency_file -%}
	{% if "uv" == cookiecutter.environment_manager -%}
	uv sync
	{% elif "pixi" == cookiecutter.environment_manager -%}
	pixi install
	{% elif "poetry" == cookiecutter.environment_manager -%}
	poetry install
	{% else -%}
	pip install -e .
	{% endif -%}
	{% elif "environment.yml" == cookiecutter.dependency_file -%}
	conda env update --name $(PROJECT_NAME) --file environment.yml --prune
	{% elif "Pipfile" == cookiecutter.dependency_file %}
	pipenv install
	{% elif "pixi.toml" == cookiecutter.dependency_file -%}
	pixi install
{% endif %}
{% endif %}


## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

{% if cookiecutter.linting_and_formatting == 'ruff' %}
## Lint using ruff (use `make format` to do formatting)
.PHONY: lint
lint:
	ruff format --check
	ruff check

## Format source code with ruff
.PHONY: format
format:
	ruff check --fix
	ruff format
{% elif cookiecutter.linting_and_formatting == 'flake8+black+isort' %}
## Lint using flake8, black, and isort (use `make format` to do formatting)
.PHONY: lint
lint:
	flake8 {{ cookiecutter.module_name }}
	isort --check --diff {{ cookiecutter.module_name }}
	black --check {{ cookiecutter.module_name }}

## Format source code with black
.PHONY: format
format:
	isort {{ cookiecutter.module_name }}
	black {{ cookiecutter.module_name }}
{% endif %}

{% if cookiecutter.testing_framework != 'none' %}
## Run tests
.PHONY: test
test:
{%- if cookiecutter.testing_framework == 'unittest' %}
	python -m unittest discover -s tests
{%- elif cookiecutter.testing_framework == 'pytest' %}
	python -m pytest tests
{%- endif -%}
{%- endif -%}

{%- if not cookiecutter.dataset_storage.none -%}
# ━━━━━━━━━━━━━━━━━━━━━━━━━ Data Management ━━━━━━━━━━━━━━━━━━━━━━━━ #
.PHONY: sync_data_down sync_data_up

sync_data_down: ## Download Data from storage system
	{%- if cookiecutter.dataset_storage.s3 -%}
	aws s3 sync s3://{{ cookiecutter.dataset_storage.s3.bucket }}/data/ \
		data/ {% if cookiecutter.dataset_storage.s3.aws_profile != 'default' %} --profile {{ cookiecutter.dataset_storage.s3.aws_profile }}{% endif %}
	{%- elif cookiecutter.dataset_storage.azure -%}
	az storage blob download-batch -s {{ cookiecutter.dataset_storage.azure.container }}/data/ \
		-d data/
	{%- elif cookiecutter.dataset_storage.gcs -%}
	gsutil -m rsync -r gs://{{ cookiecutter.dataset_storage.gcs.bucket }}/data/ data/
	{%- endif -%}

sync_data_up: ## Upload Data to storage system
	{%- if cookiecutter.dataset_storage.s3 -%}
	aws s3 sync data/ \
		s3://{{ cookiecutter.dataset_storage.s3.bucket }}/data {% if cookiecutter.dataset_storage.s3.aws_profile != 'default' %} --profile {{ cookiecutter.dataset_storage.s3.aws_profile }}{% endif %}
	{%- elif cookiecutter.dataset_storage.azure -%}
	az storage blob upload-batch -d {{ cookiecutter.dataset_storage.azure.container }}/data/ \
		-s data/
	{%- elif cookiecutter.dataset_storage.gcs -%}
	gsutil -m rsync -r data/ gs://{{ cookiecutter.dataset_storage.gcs.bucket }}/data/
	{%- endif -%}
{%- endif %}

{% if cookiecutter.environment_manager != 'none' %}
## Set up Python interpreter environment
.PHONY: create_environment
create_environment:
	{% if cookiecutter.environment_manager == 'conda' -%}
	{% if cookiecutter.dependency_file != 'environment.yml' %}
	conda create --name $(PROJECT_NAME) python=$(PYTHON_VERSION) -y
	{% else -%}
	conda env create --name $(PROJECT_NAME) -f environment.yml
	{% endif %}
	@echo ">>> conda env created. Activate with:\nconda activate $(PROJECT_NAME)"
	{% elif cookiecutter.environment_manager == 'virtualenv' -%}
	@bash -c "if [ ! -z `which virtualenvwrapper.sh` ]; then source `which virtualenvwrapper.sh`; mkvirtualenv $(PROJECT_NAME) --python=$(PYTHON_INTERPRETER); else mkvirtualenv.bat $(PROJECT_NAME) --python=$(PYTHON_INTERPRETER); fi"
	@echo ">>> New virtualenv created. Activate with:\nworkon $(PROJECT_NAME)"
	{% elif cookiecutter.environment_manager == 'pipenv' -%}
	pipenv --python $(PYTHON_VERSION)
	@echo ">>> New pipenv created. Activate with:\npipenv shell"
	{% elif cookiecutter.environment_manager == 'uv' -%}
	uv venv --python $(PYTHON_VERSION)
	@echo ">>> New uv virtual environment created. Activate with:"
	@echo ">>> Windows: .\\\\.venv\\\\Scripts\\\\activate"
	@echo ">>> Unix/macOS: source ./.venv/bin/activate"
	{% elif cookiecutter.environment_manager == 'pixi' -%}
	{% if cookiecutter.dependency_file == 'pixi.toml' %}
	@echo ">>> Pixi environment will be created when running 'make requirements'"
	{% else %}
	@echo ">>> Pixi environment configured in pyproject.toml. Run 'make requirements' to install dependencies."
	{% endif %}
	@echo ">>> Activate with:\npixi shell"
	{% elif cookiecutter.environment_manager == 'poetry' -%}
	poetry env use $(PYTHON_VERSION)
	@echo ">>> Poetry environment created. Activate with: "
	@echo '$$(poetry env activate)'
	@echo ">>> Or run commands with:\npoetry run <command>"
{% endif %}
{% endif %}


{%- if cookiecutter.version_control != 'none' %}
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Pre-Commits ━━━━━━━━━━━━━━━━━━━━━━━━━━ #
.PHONY: pre-commit-test pre-commit-update

pre-commit-test: ## Test hooks
	pre-commit run --all-files
	git add .pre-commit-config.yaml
	pre-commit run commitizen --hook-stage commit-msg --commit-msg-filename ".git/COMMIT_EDITMSG"

pre-commit-update: ## Update, install, and test hooks w/ new config
	pre-commit autoupdate
	pre-commit install
	$(MAKE) pre-commit-test
{%- endif %}

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

{% if cookiecutter.include_code_scaffold == 'Yes' %}
## Make dataset
.PHONY: data
data: requirements
	$(PYTHON_INTERPRETER) {{ cookiecutter.module_name }}/dataset.py
{% endif %}

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
