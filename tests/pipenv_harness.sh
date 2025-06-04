#!/bin/bash
set -ex

PROJECT_NAME=$(basename $1)
CCDS_ROOT=$(dirname $0)
MODULE_NAME=$2

# configure exit / teardown behavior
function finish {
    if [[ $(which python) == *"$PROJECT_NAME"* ]]; then
        exit
    fi
    
    pipenv --rm
}
trap finish EXIT

# source the steps in the test
source $CCDS_ROOT/test_functions.sh

# navigate to the generated project and run make commands 
cd $1
make
echo "Pipenv Python environment variable is set to: $PIPENV_PYTHON"
echo "$PATH"

# Debug pythonfinder and Python discovery
echo "=== DEBUGGING PYTHON DISCOVERY ==="

# 1. Install pythonfinder and list all Python versions with paths
echo "--- Installing pythonfinder and listing versions ---"
python -c "
import pythonfinder
finder = pythonfinder.Finder()
pythons = finder.find_all_python_versions()
for python in pythons:
    print(f'Found Python {python.version}: {python.path} (arch: {python.architecture})')
"

# 2. Use pipenv's vendored pythonfinder
echo "--- Using pipenv's vendored pythonfinder ---"
python -c "
import sys
import os
# Add pipenv to path to access its vendored modules
import pipenv
pipenv_path = os.path.dirname(pipenv.__file__)
vendor_path = os.path.join(pipenv_path, 'vendor')
if vendor_path not in sys.path:
    sys.path.insert(0, vendor_path)

try:
    from pipenv.vendor import pythonfinder
    finder = pythonfinder.Finder()
    pythons = finder.find_all_python_versions()
    print('Pipenv vendored pythonfinder results:')
    for python in pythons:
        print(f'  Python {python.version}: {python.path} (arch: {getattr(python, \"architecture\", \"unknown\")})')
except Exception as e:
    print(f'Error with pipenv vendored pythonfinder: {e}')
    # Fallback to pipenv.vendor.pythonfinder if import path is different
    try:
        import pipenv.vendor.pythonfinder as pythonfinder
        finder = pythonfinder.Finder()
        pythons = finder.find_all_python_versions()
        print('Pipenv vendored pythonfinder results (alt import):')
        for python in pythons:
            print(f'  Python {python.version}: {python.path}')
    except Exception as e2:
        print(f'Fallback also failed: {e2}')
"

# 3. Figure out where in PATH these Python installations are coming from
echo "--- Analyzing PATH for Python locations ---"
echo "Current PATH:"
echo "$PATH" | tr ':' '\n' | nl
echo ""

echo "Python executables found in PATH order:"
IFS=':' read -ra ADDR <<< "$PATH"
for dir in "${ADDR[@]}"; do
    if [ -d "$dir" ]; then
        # Look for python executables in this directory
        find "$dir" -maxdepth 1 -name "python*" -executable 2>/dev/null | while read -r python_exe; do
            if [ -x "$python_exe" ]; then
                version=$("$python_exe" --version 2>&1 | grep -o '[0-9]\+\.[0-9]\+\.[0-9]\+' || echo "unknown")
                arch=$("$python_exe" -c "import platform; print(platform.architecture()[0])" 2>/dev/null || echo "unknown")
                echo "  $dir -> $python_exe (version: $version, arch: $arch)"
            fi
        done
    fi
done

echo "--- Which python resolves to ---"
which python
python --version
python -c "import platform; print(f'Architecture: {platform.architecture()}')"

echo "=== END DEBUGGING ==="
echo ""

make create_environment


# can happen outside of environment since pipenv knows based on Pipfile
make requirements

# linting + formatting must happen inside environment
pipenv run make lint
pipenv run make format

# test with pipenv run
pipenv run python -c "import sys; assert \"$PROJECT_NAME\" in sys.executable"

# test importable
pipenv run python -c "import $MODULE_NAME"

# test config importable if scaffolded
if [ -f "$MODULE_NAME/config.py" ]; then
    pipenv run python -c "from $MODULE_NAME import config"
fi
