## Phony tells Makefile these aren't files to be rebuilt
.PHONY: _prep create_environment requirements format lint docs-serve test \
	test-fastest test-debug-last test-continuous _clean_manual_test manual-test manual-test-debug \
	print-welcome publish docs-publish publish-all help

## GLOBALS

PROJECT_NAME = gatlens-opinionated-template
PYTHON_VERSION = 3.10
PYTHON_INTERPRETER = python
DOCS_PORT ?= 8000


###     UTILITIES
_prep: ## Clean up .DS_Store files
	rm -f **/*/.DS_store

_welcome: ## Print a Welcome screen
	curl -s https://raw.githubusercontent.com/GatlenCulp/gatlens-opinionated-template/vscode-customization/welcome.txt

###     DEV COMMANDS

clean: _prep
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

create_environment: ## Create a new conda environment with Python $(PYTHON_VERSION) (Not really used)
	conda create --name $(PROJECT_NAME) python=$(PYTHON_VERSION) -y
	@echo ">>> conda env created. Activate with:\nconda activate $(PROJECT_NAME)"

publish: ## Build and publish package
	rm -r dist || true && \
	uv build && \
	uv publish || \
	echo "\nProject of current version may already exist. Have you tried increasing version number?"

# ## Install Python Dependencies (switched to uv)
# requirements: ## Install Python dependencies using uv
# 	uv pip install -r dev-requirements.txt

requirements: ## Install Python dependencies
	pip install -r dev-requirements.txt

## Format the code using isort and black
format: ## Format code using isort and black
	isort --profile black ccds hooks tests docs/scripts
	black ccds hooks tests docs/scripts

lint: ## Run linting checks with flake8, isort, and black
	flake8 ccds hooks tests docs/scripts
	isort --check --profile black ccds hooks tests docs/scripts
	black --check ccds hooks tests docs/scripts

# lint:
# 	ruff check hooks docs/scripts
# 	prettier --check docs

# pyright .

###     DOCS

# Switched to using uv
docs-serve: ## Serve documentation locally on port $(DOCS_PORT)
	cd docs && \
	mkdocs serve -a localhost:$(DOCS_PORT) || \
	( echo "\n\nInstance found running on $(DOCS_PORT). Here are the processes using this port:" && \
	lsof -i :$(DOCS_PORT) && \
	echo "\nTo kill a process, use: kill <PID>" )

# Makes sure docs can be served prior to actually deploying
docs-publish: ## Build and deploy documentation to GitHub Pagesa
	cd docs && \
	mkdocs build && \
	mkdocs gh-deploy --clean

###     PUBLISH ALL (Docs & Project)
publish-all: format lint publish docs-publish ## Run format, lint, publish package and docs

###     TESTS

test: _prep ## Run all tests (Use ARGS="..." for additional pytest arguments)
	pytest -vvv --durations=0 $(ARGS)

test-specific: _prep ## Run specific config (Usage: make test-config ENV=uv DEP=none DOCS=mkdocs)
	pytest -vvv -k "$(ENV)-$(DEP)-$(DOCS)" $(ARGS)

test-fastest: _prep ## Run tests with fail-fast option
	pytest -vvv -FFF

# Requires pytest-watcher (Continuous Testing for Fast Tests)
test-continuous: _prep ## Run tests in watch mode using pytest-watcher
	ptw . --now --runner pytest --config-file pyproject.toml -vvv -FFF

test-debug-last: ## Debug last failed test with pdb
	pytest --lf --pdb

test-gh-actions: lint ## Tests github actions with act if installed. Takes a while.
	act --job tests-specific --input expression=pipenv-Pipfile --input os=ubuntu-latest

_clean_manual_test:
	rm -rf manual_test


manual-test: _prep _clean_manual_test ## Run manual tests
	mkdir -p manual_test
	cd manual_test && gotem .. && cursor ./project_name

manual-test-debug: _prep _clean_manual_test ## Run manual tests with debugger
	mkdir -p manual_test
	cd manual_test && python -m pdb ../ccds/__main__.py ..

###     GIT HOOKS

pre-commit-update: ## Update, install, and test hooks w/ new config
	pre-commit autoupdate
	pre-commit install
	pre-commit run --all-files
	pre-commit run commitizen --hook-stage commit-msg --commit-msg-filename ".git/COMMIT_EDITMSG"

###     HELP

.DEFAULT_GOAL := help

help:  ## Show this help message
	@echo "\033[38;5;39m   ____  ___ _____              "
	@echo "  / ___|/ _ \_   _|__ _ __ ___  "
	@echo " | |  _| | | || |/ _ \ '_ \` _ \ "
	@echo " | |_| | |_| || |  __/ | | | | |"
	@echo "  \____|\___/ |_|\___|_| |_| |_|\033[0m"
	@echo "\n(Make sure to activate virtual environment)\n"
	@echo "\n\033[1m~ Available rules: ~\033[0m\n"
	@grep -E '^[a-zA-Z][a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[38;5;222m%-30s\033[0m %s\n", $$1, $$2}'
