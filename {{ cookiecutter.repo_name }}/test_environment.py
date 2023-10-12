import sys


def main():
    system_major = sys.version_info.major
    required_major = 3

    if system_major != required_major:
        raise TypeError(f"This project requires Python {required_major}. Found: Python {sys.version}")

    print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
