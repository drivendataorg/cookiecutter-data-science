import os
import io
import requests
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler

DATA_LINK = 'https://archive.ics.uci.edu/ml/machine-learning-databases/blood-transfusion/transfusion.data'
ROOT = Path(__file__).resolve().parents[2]

def massage_data(raw_data):
    """ Preprocess the data for predictions
    """
    raw_data.rename(index=str, columns={"whether he/she donated blood in March 2007": "label"}, inplace = True)
  
    # generate features for year for time columns
    for x,y in zip(['time_years','recency_years'],['Time (months)', 'Recency (months)']):
        raw_data[x] = (raw_data[y]/12).astype('int')
 
    # generate features for quarter for time columns (3 month periods)
    for x,y in zip(['time_quarters','recency_quarters'],['Time (months)', 'Recency (months)']):
        raw_data[x] = (raw_data[y]/3).astype('int')

    return raw_data

def dump_data(data, out_loc):
    """ Given a path to a datafile, either a local file path
    or a url, fetch the data and dump it to a csv
    """
    out_dir = os.path.join(ROOT, out_loc)
    data.to_csv(out_dir, index=False)


def main():
    """ Retrieves data and runs processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    s=requests.get(DATA_LINK).content
    raw_data = pd.read_csv(io.StringIO(s.decode('utf-8')))

    dump_data(raw_data, 'data/raw/transfusion_data_raw.csv')
    processed_data = massage_data(raw_data)
    dump_data(processed_data, 'data/processed/transfusion_data.csv')


if __name__ == '__main__':
    main()
