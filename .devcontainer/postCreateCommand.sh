#! /usr/bin/env bash

# Install Dependencies
make create_environment
make requirements
# uv pip install -r dev-requirements.txt

# source './.venv/bin/activate'

# # Install pre-commit hooks
# uv run pre-commit install --install-hooks
