"""Model training pipeline for {{ cookiecutter.module_name }}.

Provides CLI interface to train models using processed features.
"""

from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm

from {{ cookiecutter.module_name }}.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    features_path: Path = PROCESSED_DATA_DIR / "features.csv", # noqa: ARG001 template arg
    labels_path: Path = PROCESSED_DATA_DIR / "labels.csv", # noqa: ARG001 template arg
    model_path: Path = MODELS_DIR / "model.pkl", # noqa: ARG001 template arg
    # -----------------------------------------
) -> None:
    """Train a model using processed features and labels.

    Args:
        features_path: Path to the processed features CSV file
        labels_path: Path to the processed labels CSV file
        model_path: Path where the trained model will be saved

    Returns:
        None
    """
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Training some model...")
    for i in tqdm(range(10), total=10):
        if i == 5:  # noqa: PLR2004 example code
            logger.info("Something happened for iteration 5.")
    logger.success("Modeling training complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
