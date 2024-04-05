import importlib.metadata
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger


# Load environment variables from .env file if it exists
load_dotenv()


# Check if the package is installed as editable
def _is_editable():
    # https://peps.python.org/pep-0660/#frontend-requirements
    try:
        dist = importlib.metadata.distribution("{{ cookiecutter.module_name }}")
        direct_url_data = dist.read_text("direct_url.json")
        if direct_url_data is None:
            return False
        return json.loads(direct_url_data).get("dir_info", {}).get("editable", False)
    except importlib.metadata.PackageNotFoundError:
        return False


IS_EDITABLE = _is_editable()

# Determine PROJ_ROOT path
if os.getenv("PROJ_ROOT"):
    logger.debug("Reading PROJ_ROOT from environment variable.")
    PROJ_ROOT = Path(os.getenv("PROJ_ROOT"))
elif IS_EDITABLE:
    logger.debug("Setting PROJ_ROOT relative to editable package.")
    PROJ_ROOT = Path(__file__).resolve().parents[1]
else:
    logger.debug("Using current working directory as PROJ_ROOT.")
    PROJ_ROOT = Path.cwd()
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

## Paths
DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass
