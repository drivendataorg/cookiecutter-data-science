"""Main CLI interface for a {{ cookiecutter.module_name }}."""

import typer
from loguru import logger

app = typer.Typer()


# {#
# TODO: Update to have a simple version command that gnabs the version
# from the pyproject.toml file.
# }
@app.command()
def hello(name: str = "World") -> None:
    """Say hello to someone.

    Args:
        name: Name of the person to greet
    """
    logger.info(f"Hello, {name}!")


if __name__ == "__main__":
    app()
