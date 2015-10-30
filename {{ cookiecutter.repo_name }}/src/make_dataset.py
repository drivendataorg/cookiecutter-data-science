# -*- coding: utf-8 -*-
import click
import logging


@click.command()
@click.argument('input_filepath', type=str)
@click.argument('output_filepath', type=str)
def main(input_filepath, output_filepath):
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()

