"""Data processing pipeline for {{ cookiecutter.module_name }}.

Provides CLI interface to transform raw data into processed format.
"""

from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from {{ cookiecutter.module_name }}.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv", # noqa: ARG001 template arg
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv", # noqa: ARG001 template arg
    # ----------------------------------------------
) -> None:
    """Process raw dataset and save to processed data directory.

    Args:
        input_path: Path to the raw input data file
        output_path: Path where the processed dataset will be saved

    Returns:
        None

    Examples:
        >>> main(input_path="data/raw/dataset.csv",
        ...      output_path="data/processed/dataset.csv")
    """
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Processing dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5: # noqa: PLR2004 example code
            logger.info("Something happened for iteration 5.")
    logger.success("Processing dataset complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
