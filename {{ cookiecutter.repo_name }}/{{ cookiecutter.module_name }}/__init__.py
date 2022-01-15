import sys
from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from loguru import logger

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

fmt = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} :: {module} :: {function} :: {line} - {message}"

config = {
    "handlers": [
        {"sink": sys.stdout, "level": "DEBUG"},
        {"sink": "log.log", "format": fmt, "level": "DEBUG"},
    ]
}

logger.configure(**config)

source_path = Path(__file__).resolve().parents[1]
