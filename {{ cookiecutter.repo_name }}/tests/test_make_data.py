import os
import pytest
import random
import pandas as pd
from pathlib import Path
from unittest.mock import patch
from src.data.make_dataset import extract_title, dump_data
from src.models.train_model import fetch_processed

ROOT = Path(__file__).resolve().parents[2]

@patch('src.data.make_dataset.TITLES')
def test_extract_title(mock_titles):
    mock_titles = ['Mr', 'Mrs']
    names = ['Mr Bob', 'Mrs Daisy', 'Sam']
    expected_maps = {
        'Mr Bob': 'Mr',
        'Mrs Daisy': 'Mrs',
        'Sam': 'Mr'
    }
    name = random.choice(names)
    title = extract_title(name)
    assert title == expected_maps.get(name)


@pytest.mark.usefixtures('tmp_dump_dir')
def test_dump_data(tmp_dump_dir, monkeypatch):
    def mock_path_join(*paths):
        return tmp_dump_dir
    monkeypatch.setattr(os.path, 'join', mock_path_join)
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    dump_data(df, 'foo')
    dumped = pd.read_csv(tmp_dump_dir)
    assert df.equals(dumped)

def test_check_train_and_test():
      x_train, x_test, y_train, y_test = fetch_processed('data/processed/titanic.csv')
      assert all(y_train >= 0)
      assert all(y_test >= 0)
      assert x_train.shape[0] > 0
      assert x_test.shape[0] > 0
  
