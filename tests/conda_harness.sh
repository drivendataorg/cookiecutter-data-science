#!/bin/bash
set -ex

# enable conda commands inside the script
eval "$(conda shell.bash hook)"

PROJECT_NAME=$(basename $1)
CCDS_ROOT=$(dirname $0)

# configure exit / teardown behavior
function finish {
    if [[ $(which python) == *"$PROJECT_NAME"* ]]; then
        conda deactivate
    fi
    
    conda env remove -n $PROJECT_NAME -y
}
trap finish EXIT

# source the steps in the test
source $CCDS_ROOT/test_functions.sh

# navigate to the generated project and run make commands 
cd $1
make create_environment
conda activate $PROJECT_NAME
make requirements

run_tests $PROJECT_NAME
