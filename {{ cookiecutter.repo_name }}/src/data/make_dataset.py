# -*- coding: utf-8 -*-
import os
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler

DATA_LINK = 'http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.csv'
ROOT = Path(__file__).resolve().parents[2]
TITLES = ['Mlle', 'Mrs', 'Mr', 'Miss', 'Master', 'Don', 'Rev', 'Dr', 'Mme', 'Ms', 'Major', 'Col', 'Capt', 'Countess']


def extract_title(name):
    title = 'missing'
    for item in TITLES:
        if item in name:
            title = item
    if title == 'missing':
        title = 'Mr'
    return title


def massage_data(raw_data):
    """
    preprocess the data for predictions
    """
    # Feature engineering ---
    raw_data["title"] = raw_data.apply(lambda row: extract_title(row["name"]), axis=1)  
    
    # Age: replace NaN with median
    raw_data["age"].fillna(raw_data.age.median(), inplace=True)

    # Embarked: replace NaN with the mode value
    raw_data["embarked"].fillna(raw_data.embarked.mode()[0], inplace=True)

    # Fare: replace NaN with median
    raw_data["fare"].fillna(raw_data.fare.median(), inplace=True)

    # Encode Categorical features ---

    raw_data["cabin"] = raw_data.apply(lambda obs: "No" if pd.isnull(obs['cabin']) else "Yes", axis=1)  # binarize “cabin” feature

    raw_data = pd.get_dummies(raw_data, columns=['sex', 'title', 'cabin', 'embarked'])

    # Scaling numerical features ---
    scale = StandardScaler().fit(raw_data[['age', 'fare']])
    raw_data[['age', 'fare']] = scale.transform(raw_data[['age', 'fare']])
    return raw_data


def dump_data(data, out_loc):
    """
    given a path to a datafile, either a local file path
    or a url, fetch the data and dump it to a csv
    """
    out_dir = os.path.join(ROOT, out_loc)
    data.to_csv(out_dir, index=False)


def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    raw_data = pd.read_csv(DATA_LINK)
    dump_data(raw_data, 'data/raw/titanic.csv')
    processed_data = massage_data(raw_data)
    dump_data(processed_data, 'data/processed/titanic.csv')


if __name__ == '__main__':
    main()