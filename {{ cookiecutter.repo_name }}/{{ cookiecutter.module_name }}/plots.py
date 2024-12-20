"""
Command-line plotting utilities for {{ cookiecutter.module_name }}.

Usage:
    $ python -m {{ cookiecutter.module_name }}.plots [--input-path PATH] [--output-path PATH]
"""

from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm

from {{ cookiecutter.module_name }}.config import FIGURES_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = PROCESSED_DATA_DIR / "dataset.csv", # noqa: ARG001 template arg
    output_path: Path = FIGURES_DIR / "plot.png", # noqa: ARG001 template arg
    # -----------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Generating plot from data...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Plot generation complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
