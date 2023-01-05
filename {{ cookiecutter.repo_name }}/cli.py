import subprocess

import click

from {{ cookiecutter.repo_name }}.settings import settings

DATA_S3_URI = "s3://{{ cookiecutter.s3_bucket }}/{{ cookiecutter.repo_name }}/data/"


@click.group()
def cli():
    pass


@cli.command()
def sync_data_to_s3():
    command = ["aws", "s3", "sync", f"{settings.get('DATA_PATH')}/", DATA_S3_URI]
    subprocess.run(  # pylint: disable=subprocess-run-check
        command,
        stdout=subprocess.PIPE,
    )


@cli.command()
def sync_data_from_s3():
    command = ["aws", "s3", "sync", DATA_S3_URI, f"{settings.get('DATA_PATH')}/"]
    subprocess.run(  # pylint: disable=subprocess-run-check
        command,
        stdout=subprocess.PIPE,
    )

if __name__ == "__main__":
    cli()
