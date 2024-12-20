"""
Feature engineering pipeline for {{ cookiecutter.module_name }}.

Provides CLI interface to generate features from processed dataset.
"""

from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm

from {{ cookiecutter.module_name }}.config import PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = PROCESSED_DATA_DIR / "dataset.csv", # noqa: ARG001 template arg
    output_path: Path = PROCESSED_DATA_DIR / "features.csv", # noqa: ARG001 template arg
    # -----------------------------------------
):
    """Generate features from the processed dataset and save to specified output path.

    Args:
        input_path: Path to the processed input dataset
        output_path: Path where the generated features will be saved

    Returns:
        None

    Examples:
        >>> main(input_path="data/processed/dataset.csv", 
        ...      output_path="data/processed/features.csv")
    """
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Generating features from dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Features generation complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
