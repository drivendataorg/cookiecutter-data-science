#!/bin/bash
set -ex

PROJECT_NAME=$(basename $1)
CCDS_ROOT=$(dirname $0)
MODULE_NAME=$2

# Configure exit / teardown behavior
function finish {
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
uv venv
source .venv/bin/activate

# Install dependencies using uv
uv pip install -r requirements.txt

# Test python executable path
python -c "import sys; assert \"$PROJECT_NAME\" in sys.executable"

# Test module importability
python -c "import $MODULE_NAME"

# Test config importability if scaffolded
if [ -f "$MODULE_NAME/config.py" ]; then
    python -c "from $MODULE_NAME import config"
fi