import warnings

from ccds.version import __version__ as version

if __name__ == "__main__":
    if version < "2.0.1":
        warnings.warn(
            "You're currently using a CCDS version that always applies the "
            "newest template. For more stable behavior, upgrade to "
            "CCDS version 2.0.1 or later with your package manager. "
            "For example, with pip, run: pip install -U cookiecutter-data-science.",
            DeprecationWarning,
        )
