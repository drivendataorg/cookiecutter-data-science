#! /usr/bin/env bash

# Install Dependencies
uv sync --dev
source './.venv/bin/activate'
pre-commit install
