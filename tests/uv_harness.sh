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
    source ".venv/Scripts/activate"
else
    source ".venv/bin/activate"
fi

make requirements
make lint
make format

run_tests $PROJECT_NAME $MODULE_NAME
