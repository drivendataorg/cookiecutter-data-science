# -*- coding: utf-8 -*-
import os
import click
import logging
from dotenv import find_dotenv, load_dotenv
import yaml
import ssl
import vertica_python
import sys
import subprocess
import re
from jinja2 import Template


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


def vertica_python_conn(config: dict,
                        account: str='user',
                        server: str='vertica',
                        use_ssl: bool=False):
    """
    Generate vertica_python configuration object from configuration.

    Args:
    config -- dictionary that optionally contains config[server] details
              and config[server][account] details.

    Returns:
    conn -- database connection.
    """
    params = {
        'read_timeout': 10 * 60 * 60,
        'unicode_error': 'strict',
        'port': 5433
    }
    if server in config:
        config = config[server]
    params['host'] = config.get("host", os.environ.get("_".join([server, "host"])))
    params['database'] = config.get("database", os.environ.get("_".join([server, "database"])))
    if account in config:
        config = config[account]
    params['user'] = config.get("username", os.environ.get("_".join([server, account, "username"])))
    params['password'] = config.get("password", os.environ.get("_".join([server, account, "password"])))
    if use_ssl:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        ssl_context.verify_mode = ssl.CERT_NONE
        ssl_context.check_hostname = False
        params['ssl'] = ssl_context
    return vertica_python.connect(**params)


def vertica_python_conn_wrapper(**kwargs):
    # first, look for the YAML
    conn_info = {}
    if find_dotenv('.config.yml'):
        conn_info = yaml.safe_load(open(find_dotenv('.config.yml')))
    # also look for the bash script
    load_dotenv(find_dotenv('.config.sh'))
    return vertica_python_conn(conn_info, **kwargs)


def strip_comments(x: str):
    """Remove SQL comments from a string."""
    return re.sub("--.*?\n", "\n", x)


def single_line(x: str):
    """Convert a sql command into a single line (remove newlines)."""
    return re.sub(r'\s*\n+\s*', ' ', x)


def csv_command(query: str,
                outfile: str,
                config: dict,
                header: bool = False,
                account: str='user',
                server: str='vertica'):
    """Generate command line command for passing `query` into vsql
    and directing the output to `outfile`."""
    # print(os.environ.get("pw"))
    params = {}
    if server in config:
        config = config[server]
    params['host'] = config.get("host", os.environ.get("_".join([server, "host"])))
    params['database'] = config.get("database", os.environ.get("_".join([server, "database"])))
    if account in config:
        config = config[account]
    params['user'] = config.get("username", os.environ.get("_".join([server, account, "username"])))
    params['password'] = config.get("password", os.environ.get("_".join([server, account, "password"])))
    params['query'] = query
    params['outfile'] = outfile
    if header:
        params['header'] = ''
    else:
        params['header'] = 't'
    return """/usr/local/bin/vsql
              -h {host}
              -d {database}
              -U {user}
              -w '{password}'
              -F $'|'
              -A{header}
              -c "{query}" |
              gzip -c > data/raw/{outfile}""".format(params)


def vsql_to_csv(query: str,
                outfile: str,
                header: bool = False):
    """Run query and direct output to outfile."""
    conn_info = {}
    if find_dotenv('.config.yml'):
        conn_info = yaml.safe_load(open(find_dotenv('.config.yml')))
    command = csv_command(single_line(strip_comments(query)),
                          outfile,
                          conn_info,
                          header=header)
    print(command)
    subprocess.call(command, shell=True)


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

    con = vertica_python_conn_wrapper()

    main()
