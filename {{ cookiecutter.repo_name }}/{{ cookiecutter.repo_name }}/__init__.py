import os
import logging

from dotenv import load_dotenv

from "{{ cookiecutter.repo_name }}".__about__ import __author__, __author_email__, __description__, __title__, __url__, __version__

PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def init_logger(level="WARN"):
    """
    Do not call logging.basicConfig as it is global for the python interpreter and cannot be overwritten

    Args:
        level ():
    References:
        https://docs.python.org/3.5/howto/logging.html
    """
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % level)
    logger = logging.getLogger(__name__)
    logger.setLevel(numeric_level)

    # Create formatter
    format_ = "%(asctime)s- %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(format_)

    # Create console handler and formatter and level
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)


init_logger()
load_dotenv(verbose=True)

if __name__ == "__main__":
    pass
