import click
import logging
import pathlib
import os
import pandas as pd
import psycopg2
from dotenv import find_dotenv, load_dotenv


def process_data():
    """
    Define any data processing from 
    data/raw to data/processed you'd like here
    """
    pass  

def fetch_raw_data(db_conn):
    """
    Define your raw data pulls here
    """
    queries = [
        ("sampleFile.csv", 
        """
            select *
            from mstr
            limit 100;
        """)
    , ]

    return [fetch_from_psql(query, filename, db_conn) for filename, query in queries]

def fetch_from_psql(sql_string, result_name, db_conn, cache=True):
    """
    Fetches `sql_string` results from `db_conn` and saves results
    as a csv to `result_name`. 

    If cache is true, will return existing result_name file if exists

    Returns the query as a dataframe
    """
    data_dir = pathlib.Path(__file__).parent.absolute() # Find folder this file is in

    if not result_name.endswith(".csv"):
        result_name = result_name + ".csv"

    filepath = os.path.join(data_dir, "raw", result_name)

    if cache and os.path.isfile(filepath):
        return pd.read_csv(filepath)

    df = pd.read_sql(sql_string, db_conn)
    
    df.to_csv(filepath, index=False)
    
    return df  

# Specify input_filepath and output_filepath in cli. See Makefile
@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def make_data(input_filepath="data/raw", output_filepath="data/processed"):
    """ Runs data processing scripts to turn raw data from (./raw) into
        cleaned data ready to be analyzed (saved in ./processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('Fetching raw data from sql database')

    db = os.environ.get("DATABASE_NAME")
    user = os.environ.get("DATABASE_USERNAME")
    password = os.environ.get("DATABASE_PASSWORD")
    host = os.environ.get("DATABASE_HOST")
    port = os.environ.get("DATABASE_PORT")

    con = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)

    fetch_raw_data(con)

    logger.info('Processing data')

    process_data()


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    make_data()

