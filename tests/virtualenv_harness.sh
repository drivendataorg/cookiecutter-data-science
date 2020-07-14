#!/bin/bash
set -e

PROJECT_NAME=$(basename $1)
CCDS_ROOT=$(dirname $0)

# configure exit / teardown behavior
function finish {
    if [[ $(which python) == *"$PROJECT_NAME"* ]]; then
        deactivate
    fi

    if [ ! -z `which rmvirtualenv` ]; then
        rmvirtualenv $PROJECT_NAME
    elif [ ! -z `which rmvirtualenv.bat` ]; then
        rmvirtualenv.bat $PROJECT_NAME
    fi
}
trap finish EXIT

# source the steps in the test
source $CCDS_ROOT/test_functions.sh

# navigate to the generated project and run make commands
cd $1

if [ -z $TMPDIR ]
then
    windowstmpdir=/c/Users/VssAdministrator/AppData/Local/Temp
    if [ -e $windowstmpdir ]
    then
        export TMPDIR=$windowstmpdir
    fi
fi

TEMP_ENV_ROOT=$(mktemp -d "${TMPDIR:-/tmp/}$(basename $0).XXXXXXXXXXXX")
export WORKON_HOME=$TEMP_ENV_ROOT

# virtualenvwrapper.sh must be on the PATH on the test host machine,
# which should be the case if virtualenvwrapper is pip installed in
# the base Python
# if [ -z $(which virtualenvwrapper.sh) ]; then
#     for path in ${PATH//:/ }; do
#         if [ -d "$path" ]; then
#             echo "Searching $path for virtualenvwrapper.sh"
#             FIND_RESULT=$(find $path -maxdepth 1 -name "virtualenvwrapper.sh")
#             if [[ "$FIND_RESULT" ]]; then
#                 VIRTUALENVWRAPPER_SCRIPT=$FIND_RESULT
#                 echo VIRTUALENVWRAPPER_SCRIPT=$VIRTUALENVWRAPPER_SCRIPT
#                 # Add shebang to top of virtualenvwrapper.sh
#                 # Windows bash needs this to know it's executable
#                 sed -i '1s/^/#!\/bin\/sh\n/' "$VIRTUALENVWRAPPER_SCRIPT"
#                 head "$VIRTUALENVWRAPPER_SCRIPT"
#                 break
#             fi
#         fi
#     done
# fi

if [ ! -z `which virtualenvwrapper.sh` ]
then
    source `which virtualenvwrapper.sh`
fi

make create_environment

# workon not sourced

if [ -e $TEMP_ENV_ROOT/$PROJECT_NAME/bin/activate ]
then
    . $TEMP_ENV_ROOT/$PROJECT_NAME/bin/activate
else
    . $TEMP_ENV_ROOT/$PROJECT_NAME/Scripts/activate
fi

make requirements

run_tests $PROJECT_NAME
