import warnings

try:
    from ccds import __version__
except ModuleNotFoundError:
    __version__ = None  # ccds is not installed
except ImportError:
    __version__ = "2.0.0"  # ccds is installed but version is 2.0.0

if __name__ == "__main__":
    if __version__ is not None and __version__ < "2.0.1":
        warnings.warn(
            "You're currently using a CCDS version that always applies the "
            "newest template. For more stable behavior, upgrade to "
            "CCDS version 2.0.1 or later with your package manager. "
            "For example, with pip, run: pip install -U cookiecutter-data-science.",
            DeprecationWarning,
        )
