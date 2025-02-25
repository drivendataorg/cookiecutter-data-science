#!/bin/bash
set -ex

PROJECT_NAME=$(basename $1)
CCDS_ROOT=$(dirname $0)
MODULE_NAME=$2

# configure exit / teardown behavior
function finish {
    if [[ -d ".venv" ]]; then
        rm -rf .venv
    fi
}
trap finish EXIT

# source the steps in the test
source $CCDS_ROOT/test_functions.sh

# navigate to the generated project and run make commands 
cd $1
make
make create_environment

# Activate the virtual environment
source .venv/bin/activate

make requirements

run_tests $PROJECT_NAME $MODULE_NAME 