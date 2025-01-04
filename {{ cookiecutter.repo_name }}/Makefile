#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_VERSION = {{ cookiecutter.python_version_number }}
PYTHON_INTERPRETER = python
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
requirements: ## Install Python Dep
	{% if cookiecutter.environment_manager == 'uv' %}
	uv sync
	{% elif "requirements.txt" == cookiecutter.dependency_file -%}
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	{% elif "environment.yml" == cookiecutter.dependency_file -%}
	conda env update --name $(PROJECT_NAME) --file environment.yml --prune
	{% elif "Pipfile" == cookiecutter.dependency_file %}
	pipenv install
	{% endif %}
{% endif %}


publish-all: format lint publish docs-publish ## Run format, lint, publish package and docs

#################################################################################
# CLEAN COMMANDS                                                                #
#################################################################################


.PHONY: clean
clean: ## Delete all compiled Python files
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


.PHONY: lint ## Lint using ruff (use `make format` to do formatting)
lint:
	ruff check --config pyproject.toml {{ cookiecutter.module_name }}
{#
# TODO: Add prettier support
# prettier --check {{ cookiecutter.module_name }}

# TODO: Add pyright support	
# pyright {{ cookiecutter.module_name }}
#}

.PHONY: format ## Format source code with black
format:
	ruff --config pyproject.toml {{ cookiecutter.module_name }}

#################################################################################
# DOCS COMMANDS                                                                 #
#################################################################################

# Switched to using uv
docs-serve: ## Serve documentation locally on port $(DOCS_PORT)
	cd docs && \
	mkdocs serve -a localhost:$(DOCS_PORT) || \
	echo "\n\nInstance found running on $(DOCS_PORT), try killing process and rerun."

# Makes sure docs can be served prior to actually deploying
docs-publish: ## Build and deploy documentation to GitHub Pages
	cd docs && \
	mkdocs build && \
	mkdocs gh-deploy --clean

#################################################################################
# DATA COMMANDS                                                                 #
#################################################################################

{%- if not cookiecutter.dataset_storage.none -%}

.PHONY: sync_data_down
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

.PHONY: sync_data_up
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

#################################################################################
# TEST COMMANDS                                                                 #
#################################################################################

test: _prep ## Run all tests
	pytest -vvv --durations=0

test-fastest: _prep ## Run tests with fail-fast option
	pytest -vvv -FFF

# Requires pytest-watcher (Continuous Testing for Fast Tests)
test-continuous: _prep ## Run tests in watch mode using pytest-watcher
	ptw . --now --runner pytest --config-file pyproject.toml -vvv -FFF

test-debug-last: ## Debug last failed test with pdb
	pytest --lf --pdb

_clean_manual_test:
	rm -rf manual_test

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

{%- if cookiecutter.include_code_scaffold != 'No' %}

.PHONY: data ## Make Dataset
data: requirements
	$(PYTHON_INTERPRETER) {{ cookiecutter.module_name }}/dataset.py
{%- endif %}


{%- if cookiecutter.use_github == 'Yes' %}
#################################################################################
# PRE-COMMIT COMMANDS                                                           #
#################################################################################

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
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

help:  ## Show this help message
	@echo "\033[38;5;39m   ____  ___ _____              "
	@echo "  / ___|/ _ \_   _|__ _ __ ___  "
	@echo " | |  _| | | || |/ _ \ '_ \` _ \ "
	@echo " | |_| | |_| || |  __/ | | | | |"
	@echo "  \____|\___/ |_|\___|_| |_| |_|\033[0m"
	@echo "\n\033[1m~ Available rules: ~\033[0m\n"
	@echo "For VSCode/Cursor, try: ⇧ ⌘ P, Tasks: Run Task\n"
	@grep -E '^[a-zA-Z][a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[38;5;222m%-30s\033[0m %s\n", $$1, $$2}'
