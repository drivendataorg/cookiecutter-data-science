#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROFILE = {{ cookiecutter.aws_profile }}
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_VERSION = {{ cookiecutter.python_interpreter }}
VIRTUALENV := build/virtualenv

#################################################################################
# COMMANDS                                                                      #
#################################################################################

# Set the default location for the virtualenv to be stored
# Create the virtualenv by installing the requirements and test requirements

$(VIRTUALENV)/.installed: requirements.txt
	@if [ -d $(VIRTUALENV) ]; then rm -rf $(VIRTUALENV); fi
	@mkdir -p $(VIRTUALENV)
	virtualenv --python $(PYTHON_VERSION) $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip3 install -r requirements.txt
	$(VIRTUALENV)/bin/pip3 install -r requirements_test.txt
	$(VIRTUALENV)/bin/pip3 install -e .
	touch $@

# Update the requirements to latest. This is required because typically we won't
# want to incldue test requirements in the requirements of the application, and
# because it makes life much easier when we want to keep our dependencies up to
# date.

.PHONY: update-requirements-txt
update-requirements-txt: VIRTUALENV := /tmp/update-requirements-virtualenv
update-requirements-txt:
	@if [ -d $(VIRTUALENV) ]; then rm -rf $(VIRTUALENV); fi
	@mkdir -p $(VIRTUALENV)
	virtualenv --python $(PYTHON_VERSION) $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip3 install -r unpinned_requirements.txt
	echo "# Created by 'make update-requirements-txt'. DO NOT EDIT!" > requirements.txt
	$(VIRTUALENV)/bin/pip freeze | grep -v pkg-resources==0.0.0 >> requirements.txt

.PHONY: virtualenv
virtualenv: $(VIRTUALENV)/.installed

# Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

# Lint using flake8
.PHONY: lint
lint:
	flake8 src

