#! /usr/bin/env bash

# Install Dependencies
uv sync
source './.venv/bin/activate'
pre-commit install
