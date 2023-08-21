"""init_py}}"""
import sys
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from loguru import logger

DOTENV_PATH = find_dotenv()
load_dotenv(DOTENV_PATH)

FMT_ = "{time:YYYY-MM-DD HH:mm:ss} "\
    "| {level} | {name} :: {module} :: {function} :: {line} - {message}"


CONFIG_ = {
    "handlers": [
        {"sink": sys.stdout, "level": "DEBUG"},
        {"sink": "log.log", "format": FMT_, "level": "DEBUG"},
    ]
}

logger.configure(**CONFIG_)

SOURCE_PATH = Path(__file__).resolve().parents[1]
