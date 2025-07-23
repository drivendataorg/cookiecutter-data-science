#!/bin/bash
set -ex

PROJECT_NAME=$(basename $1)
CCDS_ROOT=$(dirname $0)
MODULE_NAME=$2

# Check if pixi is installed
if ! command -v pixi &> /dev/null; then
    echo "pixi is not installed. Please install pixi first:"
    echo "  macOS/Linux: curl -fsSL https://pixi.sh/install.sh | sh"
    echo "  Windows: powershell -ExecutionPolicy ByPass -c \"irm -useb https://pixi.sh/install.ps1 | iex\""
    exit 1
fi

# Configure exit / teardown behavior
function finish {
    # Cleanup pixi environment
    if [ -d ".pixi" ]; then
        rm -rf .pixi
    fi
    if [ -f "pixi.lock" ]; then
        rm -f pixi.lock
    fi
}
trap finish EXIT

# Source the steps in the test
source $CCDS_ROOT/test_functions.sh

# Navigate to the generated project and run make commands
cd $1

make
make create_environment
make requirements

# Run pixi-specific tests with simpler commands
pixi run python --version
echo "Testing basic import..."
pixi run python -c "import $MODULE_NAME"

# Test config importable if scaffolded  
if [ -f "$MODULE_NAME/config.py" ]; then
    echo "Testing config import..."
    pixi run python -c "from $MODULE_NAME import config"
fi

# Run linting and formatting through pixi
pixi run make lint
pixi run make format

# Custom pixi test function to avoid issues with test_functions.sh
# Check that python is available in pixi environment
echo "Testing pixi python availability..."
if pixi run python -c "import sys" > /dev/null 2>&1; then
    echo "Python is available in pixi environment"
else
    echo "ERROR: Python not available in pixi environment" 
    exit 1
fi

echo "All done!"
