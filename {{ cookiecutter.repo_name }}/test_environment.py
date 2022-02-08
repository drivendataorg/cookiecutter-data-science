import sys

REQUIRED_PYTHON = "{{ cookiecutter.python_interpreter }}"


def main():
    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python":
        required_major = 2
    elif REQUIRED_PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError(f"Unrecognized python interpreter: {REQUIRED_PYTHON}")

    if system_major != required_major:
        raise TypeError(f"This project requires Python {required_major}. Found: Python {sys.version}")

    print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
