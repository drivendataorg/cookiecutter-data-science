import os
import subprocess
from pathlib import Path


def configure_uv_venv(
    directory: str | Path,
) -> bool:
    # Change to specified directory
    os.chdir(directory)
    subprocess.run(["uv", "venv"])
    subprocess.run(["uv", "pip", "install", "-e", "."])
