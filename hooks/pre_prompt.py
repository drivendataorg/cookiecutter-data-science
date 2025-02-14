import warnings

from ccds.version import __version__ as version


if __name__ == "__main__":
    if version <= "2.0.0":
        warnings.warn(
            DeprecationWarning(
                "It looks like you're using a version of CCDS that "
                "always uses the latest template. For more stable behavior, "
                "update to a newer version of CCDS."
            )
        )
