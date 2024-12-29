#!/bin/bash
set -ex

PROJECT_NAME=$(basename $1)
CCDS_ROOT=$(dirname $0)
MODULE_NAME=$2

# Configure exit / teardown behavior
function finish {
    # Deactivate venv if we're in one
    if [[ $(which python) == *"$PROJECT_NAME"* ]]; then
        deactivate
    fi
    # Clean up venv directory
    if [ -d ".venv" ]; then
        rm -rf .venv
    fi
}
trap finish EXIT

# Source the steps in the test
source $CCDS_ROOT/test_functions.sh

# Navigate to the generated project and run make commands
cd $1
make

# Create and activate virtual environment
make create_environment


# Check if running on Windows and use appropriate activate path
if [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "cygwin"* ]]; then
    VENV_PATH=".venv/Scripts/activate"
else
    VENV_PATH=".venv/bin/activate"
fi

make requirements

# Verify venv exists before attempting to activate
if [ ! -f "$VENV_PATH" ]; then
    echo "Virtual environment activation script not found at $VENV_PATH"
    exit 1
fi

# Activate the virtual environment
source "$VENV_PATH"

