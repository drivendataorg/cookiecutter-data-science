from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from {{ cookiecutter.module_name }}.config import PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    input_path: Path = PROCESSED_DATA_DIR / "some_dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "some_features.csv",
):
    #### REPLACE THIS WITH YOUR OWN CODE ####
    logger.info("Generating some features from some dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Some features generation complete.")
    #########################################


if __name__ == "__main__":
    app()
