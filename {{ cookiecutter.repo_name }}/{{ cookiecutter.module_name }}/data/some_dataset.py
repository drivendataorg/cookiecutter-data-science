from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from {{ cookiecutter.module_name }}.config import RAW_DATA_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "some_dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "some_dataset.csv",
):
    #### REPLACE THIS WITH YOUR OWN CODE ####
    logger.info("Processing some dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Processing some dataset complete.")
    #########################################


if __name__ == "__main__":
    app()
