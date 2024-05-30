function run_tests () {
    python --version
    python -c "print('python runs....')"

    if [[ $(which python) == *"$1"* ]]; then
        echo "found correct python"
    else
        echo "Python env name $1 not in Python path $(which python)"
        exit 99
    fi

    # test importable
    python -c "import $2"

    # test config importable if scaffolded
    if [ -f "$2/config.py" ]; then
        python -c "from $2 import config"
    fi
}