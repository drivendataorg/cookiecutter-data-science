#!/bin/bash
set -ex

# Set conda executable default if environment variable not defined
: "${CONDA_EXECUTABLE:=conda}"
echo CONDA_EXECUTABLE=$CONDA_EXECUTABLE

echo conda_harness PATH=$PATH
which make

# enable conda commands inside the script
eval "$($CONDA_EXECUTABLE shell.bash hook)"

PROJECT_NAME=$(basename $1)
CCDS_ROOT=$(dirname $0)

# configure exit / teardown behavior
function finish {
    if [[ $(which python) == *"$PROJECT_NAME"* ]]; then
        $CONDA_EXECUTABLE deactivate
    fi

    $CONDA_EXECUTABLE env remove -n $PROJECT_NAME -y
}
trap finish EXIT

# source the steps in the test
source $CCDS_ROOT/test_functions.sh

# navigate to the generated project and run make commands
cd $1

# Fix for conda issue https://github.com/conda/conda/issues/7267 on MacOS
if [ -e /usr/local/miniconda ]
then
    sudo chown -R $USER /usr/local/miniconda
fi

make create_environment
$CONDA_EXECUTABLE activate $PROJECT_NAME
make requirements

run_tests $PROJECT_NAME
