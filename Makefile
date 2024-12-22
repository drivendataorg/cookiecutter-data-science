.PHONY: _prep create_environment requirements format lint docs docs-serve test \
	test-fastest test-debug-fastest _clean_manual_test manual-test manual-test-debug

## GLOBALS

PROJECT_NAME = gatlens-opinionated-template
PYTHON_VERSION = 3.10
PYTHON_INTERPRETER = python


###     UTILITIES
_prep:
	rm -f **/*/.DS_store


###     DEV COMMANDS

## Set up python interpreter environment
create_environment:
	conda create --name $(PROJECT_NAME) python=$(PYTHON_VERSION) -y
	@echo ">>> conda env created. Activate with:\nconda activate $(PROJECT_NAME)"

publish:
	uv build
	uv publish

## Install Python Dependencies
requirements:
	$(PYTHON_INTERPRETER) -m pip install -r dev-requirements.txt

## Format the code using isort and black
format:
	isort --profile black ccds hooks tests docs/scripts
	black ccds hooks tests docs/scripts

lint:
	flake8 ccds hooks tests docs/scripts
	isort --check --profile black ccds hooks tests docs/scripts
	black --check ccds hooks tests docs/scripts

# lint:
# 	ruff check hooks docs/scripts
# 	prettier --check docs

# pyright .

###     DOCS

docs:
	cd docs && mkdocs build

docs-serve:
	cd docs && mkdocs serve

uv-docs:
	cd docs && uv run mkdocs build

uv-docs-serve:
	cd docs && uv run mkdocs serve

uv-docs-deploy:
	cd docs && uv run mkdocs build && uv run mkdocs gh-deploy --clean


###     TESTS

test: _prep
	pytest -vvv --durations=0

test-fastest: _prep
	pytest -vvv -FFF

test-debug-last:
	pytest --lf --pdb

_clean_manual_test:
	rm -rf manual_test

manual-test: _prep _clean_manual_test
	mkdir -p manual_test
	cd manual_test && python -m ccds ..

manual-test-debug: _prep _clean_manual_test
	mkdir -p manual_test
	cd manual_test && python -m pdb ../ccds/__main__.py ..
