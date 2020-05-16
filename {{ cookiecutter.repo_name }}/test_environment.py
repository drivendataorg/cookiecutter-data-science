import sys

REQUIRED_PYTHON_MAJOR_VERSION = 3

def main():
    system_major = sys.version_info.major
    if system_major != REQUIRED_PYTHON_MAJOR_VERSION:
        raise TypeError(
            "This project requires Python 3. Found: Python {}".format(
                REQUIRED_PYTHON_MAJOR_VERSION, sys.version
            )
        )
    else:
        print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
