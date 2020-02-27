#!/bin/bash
set -e

PROJECT_NAME=$(basename $1)
CCDS_ROOT=$(dirname $0)

# configure exit / teardown behavior
function finish {
    if [[ $(which python) == *"$PROJECT_NAME"* ]]; then
        deactivate
    fi

    rmvirtualenv $PROJECT_NAME
}
trap finish EXIT

# source the steps in the test
source $CCDS_ROOT/test_functions.sh

# navigate to the generated project and run make commands
cd $1

TEMP_ENV_ROOT=$(mktemp -d "${TMPDIR:-/tmp/}$(basename $0).XXXXXXXXXXXX")
export WORKON_HOME=$TEMP_ENV_ROOT

# virtualenvwrapper.sh must be on the PATH on the test host machine,
# which should be the case if virtualenvwrapper is pip installed in
# the base Python
source $(which virtualenvwrapper.sh)

make create_environment

# workon not sourced
. $TEMP_ENV_ROOT/$PROJECT_NAME/bin/activate
make requirements

run_tests $PROJECT_NAME
