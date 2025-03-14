"""Main CLI interface for a {{ cookiecutter.module_name }}."""

from pathlib import Path

import typer
from loguru import logger

app = typer.Typer()


@app.command()
def hello(name: str = "World") -> None:
    """Say hello to someone.

    Args:
        name: Name of the person to greet
    """
    logger.info(f"Hello, {name}!")


if __name__ == "__main__":
    app()
