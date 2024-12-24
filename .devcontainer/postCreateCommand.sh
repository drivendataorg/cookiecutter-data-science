#! /usr/bin/env bash

# Install Dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install --install-hooks
