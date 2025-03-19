function run_tests () {
    python --version
    python -c "print('python runs....')"

    if [[ $(which python) == *"$1"* ]]; then
        echo "found correct python"
    else
        echo "Python env name $1 not in Python path $(which python)"
        exit 99
    fi

    # test Python version in created venv should be match configured version
    CREATED_PYTHON_VERSION=$(python -c "import platform; print(platform.python_version())")
    if [[ $(vspect parse $CREATED_PYTHON_VERSION "{major_minor_version}") == $EXPECTED_PYTHON_VERSION ]]; then
        echo "Python version $CREATED_PYTHON_VERSION matches expected $EXPECTED_PYTHON_VERSION"
    else
        echo "Python version $CREATED_PYTHON_VERSION does not match $EXPECTED_PYTHON_VERSION"
        exit 99
    fi

    # test importable
    python -c "import $2"

    # test config importable if scaffolded
    if [ -f "$2/config.py" ]; then
        python -c "from $2 import config"
    fi
}
