#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_VERSION = {{ cookiecutter.python_version_number }}
PYTHON_INTERPRETER = python
{#-
PYTHON_INTERPRETER = uv python
{%- if cookiecutter.environment_manager == 'uv' %}
{%- else %}
{%- endif %}
#}
DOCS_PORT ?= 8000

#################################################################################
# UTILITIES                                                                     #
#################################################################################

_prep: ## Clean up .DS_Store files
	rm -f **/*/.DS_store

_welcome: ## Print a Welcome screen
	curl -s https://raw.githubusercontent.com/GatlenCulp/gatlens-opinionated-template/vscode-customization/welcome.txt

#################################################################################
# PACKAGE COMMANDS                                                              #
#################################################################################

{% if cookiecutter.environment_manager != 'none' -%}
## Set up python interpreter environment
.PHONY: create_environment
create_environment:
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
## Install Python Dependencies
.PHONY: requirements
requirements:
	{%- if cookiecutter.environment_manager == 'uv' %}
	uv sync
	{% elif "requirements.txt" == cookiecutter.dependency_file -%}
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	{% elif "environment.yml" == cookiecutter.dependency_file -%}
	conda env update --name $(PROJECT_NAME) --file environment.yml --prune
	{% elif "Pipfile" == cookiecutter.dependency_file -%}
	pipenv install
	{% endif %}
{% endif %}

###     PUBLISH ALL (Docs & Project)
publish-all: format lint publish docs-publish ## Run format, lint, publish package and docs

#################################################################################
# CLEAN COMMANDS                                                                #
#################################################################################

## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8 and black (use `make format` to do formatting)
.PHONY: lint
lint:
	ruff check --config pyproject.toml {{ cookiecutter.module_name }}
{#
# TODO: Add prettier support
# prettier --check {{ cookiecutter.module_name }}

# TODO: Add pyright support	
# pyright {{ cookiecutter.module_name }}
#}
## Format source code with black
.PHONY: format
format:
	ruff --config pyproject.toml {{ cookiecutter.module_name }}

#################################################################################
# DOCS COMMANDS                                                                 #
#################################################################################

# Switched to using uv
docs-serve: ## Serve documentation locally on port $(DOCS_PORT)
	cd docs && \
	uv run mkdocs serve -a localhost:$(DOCS_PORT) || \
	echo "\n\nInstance found running on $(DOCS_PORT), try killing process and rerun."

# Makes sure docs can be served prior to actually deploying
docs-publish: ## Build and deploy documentation to GitHub Pages
	cd docs && \
	uv run mkdocs build && \
	uv run mkdocs gh-deploy --clean

#################################################################################
# DATA COMMANDS                                                                 #
#################################################################################

{%- if not cookiecutter.dataset_storage.none -%}
## Download Data from storage system
.PHONY: sync_data_down
sync_data_down:
	{%- if cookiecutter.dataset_storage.s3 -%}
	aws s3 sync s3://{{ cookiecutter.dataset_storage.s3.bucket }}/data/ \
		data/ {% if cookiecutter.dataset_storage.s3.aws_profile != 'default' %} --profile {{ cookiecutter.dataset_storage.s3.aws_profile }}{% endif %}
	{%- elif cookiecutter.dataset_storage.azure -%}
	az storage blob download-batch -s {{ cookiecutter.dataset_storage.azure.container }}/data/ \
		-d data/
	{%- elif cookiecutter.dataset_storage.gcs -%}
	gsutil -m rsync -r gs://{{ cookiecutter.dataset_storage.gcs.bucket }}/data/ data/
	{%- endif -%}

## Upload Data to storage system
.PHONY: sync_data_up
sync_data_up:
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

#################################################################################
# TEST COMMANDS                                                                 #
#################################################################################

test: _prep ## Run all tests
	uv run pytest -vvv --durations=0

test-fastest: _prep ## Run tests with fail-fast option
	uv run pytest -vvv -FFF

# Requires pytest-watcher (Continuous Testing for Fast Tests)
test-continuous: _prep ## Run tests in watch mode using pytest-watcher
	uv run ptw . --now --runner pytest --config-file pyproject.toml -vvv -FFF

test-debug-last: ## Debug last failed test with pdb
	uv run pytest --lf --pdb

_clean_manual_test:
	rm -rf manual_test

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

{%- if cookiecutter.include_code_scaffold == 'Yes' %}
## Make Dataset
.PHONY: data
data: requirements
	$(PYTHON_INTERPRETER) {{ cookiecutter.module_name }}/dataset.py
{%- endif %}

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# define PRINT_HELP_PYSCRIPT
# import re, sys; \
# lines = '\n'.join([line for line in sys.stdin]); \
# matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
# print('Available rules:\n'); \
# print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
# endef
# export PRINT_HELP_PYSCRIPT

# help:
# 	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)

help:  ## Show this help message
	@echo "\033[38;5;39m   ____  ___ _____              "
	@echo "  / ___|/ _ \_   _|__ _ __ ___  "
	@echo " | |  _| | | || |/ _ \ '_ \` _ \ "
	@echo " | |_| | |_| || |  __/ | | | | |"
	@echo "  \____|\___/ |_|\___|_| |_| |_|\033[0m"
	@echo "\n\033[1m~ Available Commands ~\033[0m\n"
	@grep -E '^[a-zA-Z][a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[38;5;222m%-30s\033[0m %s\n", $$1, $$2}'
