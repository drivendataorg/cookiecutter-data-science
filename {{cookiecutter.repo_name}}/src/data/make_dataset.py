# -*- coding: utf-8 -*-
import os
import click
import logging
from dotenv import find_dotenv, load_dotenv
import yaml
import ssl
import vertica_python
import sys


def run_from_ipython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False


if run_from_ipython():
    from IPython import get_ipython
    ipython = get_ipython()
    ipython.magic("matplotlib inline")
    project_dir = os.getcwd()
else:
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
src_dir = os.path.join(project_dir, "src")
sys.path.append(src_dir)


def get_vertica_python_conn(cfg=None):
    cfg = cfg or default_cfg
    params = {
        'host': cfg['host'],
        'port': 5433,
        'database': cfg['database'],
        'read_timeout': 600,
        'unicode_error': 'strict',
        'password': cfg['password'],
        'user': cfg['user']}
    if 'VERTICA_NO_SSL' not in cfg.keys():
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        ssl_context.verify_mode = ssl.CERT_NONE
        ssl_context.check_hostname = False
        params['ssl'] = ssl_context
    conn = vertica_python.connect(**params)
    return conn


def vertica_python_conn(config, account='user', server='vertica'):
    """
    Generate vertica_python configuration object from configuration.

    Args:
    config -- database configuation.

    Returns:
    conn -- database connection.
    """
    params = {
        'host': config[server]['host'],
        'port': 5433,
        'database': config[server]['database'],
        'read_timeout': 10 * 60 * 60,
        'unicode_error': 'strict',
        'user': config[server][account]['username'],
        'password': config[server][account]['password']
    }
    conn = vertica_python.connect(**params)
    return conn


def vertica_python_conn_wrapper(**kwargs):
    conn_info = yaml.safe_load(open(find_dotenv('.config.yml')))
    return vertica_python_conn(conn_info, **kwargs)


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    with open(input_filepath, "r") as f:
        query = f.read()

    df = pd.read_sql_query(query, con)
    df.to_pickle(output_filepath)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    # this will work if user and pw are defined in the root .env
    conn_info = {'host': 'vertica.private.massmutual.com',
                 'port': 5433,
                 'user': os.environ.get("user"),
                 'password': os.environ.get("pw"),
                 'database': 'advana',
                 # 100 minutes timeout on queries
                 'read_timeout': 6000,
                 # default throw error on invalid UTF-8 results
                 'unicode_error': 'strict',
                 # SSL is disabled by default
                 'ssl': True}

    con = get_vertica_python_conn(conn_info)

    # OR

    con = vertica_python_conn_wrapper()

    main()
