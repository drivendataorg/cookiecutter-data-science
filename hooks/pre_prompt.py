import warnings

from ccds.version import __version__ as version

if __name__ == "__main__":
    if version < "2.0.1":
        warnings.warn(
            "It looks like you're using a version of CCDS that "
            "defaults to using the latest template. For more stable behavior, "
            "update to CCDS version 2.0.1 or later. To upgrade to the latest "
            "version, run 'pip install -U cookiecutter-data-science'",
            DeprecationWarning,
        )
