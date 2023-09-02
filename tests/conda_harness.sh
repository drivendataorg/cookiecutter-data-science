#!/bin/bash
set -ex

: "${CONDA_EXECUTABLE:=conda}"

eval "$(conda shell.bash hook)"

PROJECT_NAME=$(basename $1)
CCDS_ROOT=$(dirname $0)

# configure exit / teardown behavior
function finish {
    if [[ $(which python) == *"$PROJECT_NAME"* ]]; then
        conda deactivate  # Mamba still has you use conda activate/deactivate
    fi

    $CONDA_EXECUTABLE env remove -n $PROJECT_NAME -y
}
trap finish EXIT

# source the steps in the test
source $CCDS_ROOT/test_functions.sh

# navigate to the generated project and run make commands
cd $1

# Fix for conda issue https://github.com/conda/conda/issues/7267 on MacOS
if [ -e /usr/local/miniconda ]; then
    sudo chown -R $USER /usr/local/miniconda
fi
if [ -e $CONDA_PREFIX ]; then
    sudo chown -R $USER $CONDA_PREFIX
fi


echo "Creating environment..."
make create_environment CONDA_EXECUTABLE=$CONDA_EXECUTABLE

echo "Activating environment..."
conda activate $PROJECT_NAME  # Mamba still has you use conda activate/deactivate

echo "Installing requirements..."
make requirements CONDA_EXECUTABLE=$CONDA_EXECUTABLE

echo "Running tests..."
run_tests $PROJECT_NAME
