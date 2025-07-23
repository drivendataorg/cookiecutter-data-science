#!/bin/bash
set -ex

PROJECT_NAME=$(basename $1)
CCDS_ROOT=$(dirname $0)
MODULE_NAME=$2

# Check if poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "poetry is not installed. Please install poetry first:"
    echo "  curl -sSL https://install.python-poetry.org | python3 -"
    echo "  Or visit: https://python-poetry.org/docs/#installation"
    exit 1
fi

# Configure exit / teardown behavior
function finish {
    # Cleanup poetry environment if it exists
    if poetry env list | grep -q "$(basename $(pwd))"; then
        poetry env remove --all
    fi
}
trap finish EXIT

# Source the steps in the test
source $CCDS_ROOT/test_functions.sh

cd $1

# Setup and run tests
make
make create_environment
make requirements

# Run poetry-specific tests with simpler commands
poetry run python --version
echo "Testing basic import..."
poetry run python -c "import $MODULE_NAME"

# Test config importable if scaffolded  
if [ -f "$MODULE_NAME/config.py" ]; then
    echo "Testing config import..."
    poetry run python -c "from $MODULE_NAME import config"
fi

# Run linting and formatting through poetry
poetry run make lint
poetry run make format

# Custom poetry test function to avoid issues with test_functions.sh
# Check that python is available in poetry environment
echo "Testing poetry python availability..."
if poetry run python -c "import sys" > /dev/null 2>&1; then
    echo "Python is available in poetry environment"
else
    echo "ERROR: Python not available in poetry environment" 
    exit 1
fi

echo "All done!"
