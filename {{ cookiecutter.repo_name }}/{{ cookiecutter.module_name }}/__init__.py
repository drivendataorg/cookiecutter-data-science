"""init-py"""
import sys
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from loguru import logger

DOTENV_PATH = find_dotenv()
load_dotenv(DOTENV_PATH)

FMT = "{time:YYYY-MM-DD HH:mm:ss} "\
    "| {level} | {name} :: {module} :: {function} :: {line} - {message}"


CONFIG = {
    "handlers": [
        {"sink": sys.stdout, "level": "DEBUG"},
        {"sink": "log.log", "format": FMT, "level": "DEBUG"},
    ]
}

logger.configure(**CONFIG)

SOURCE_PATH = Path(__file__).resolve().parents[1]
