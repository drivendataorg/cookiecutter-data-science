import os
import pandas as pd
from unittest.mock import patch, Mock
from src.models.train_model import fetch_processed, fit_model


mock_data = {
   'survived': [1, 0, 0, 1],
   'name': ['John', 'Bob', 'Sam', 'Kevin'],
   'ticket': ['foo', 'bar', 'buzz', 'fizz'],
   'boat': ['y', 'n', 'm', 'y'],
   'body': ['a', 'b', 'c', 'd'],
   'home.dest': ['nyc', 'la', 'boston', 'amherst'] 
}


def test_fetch_processed(monkeypatch):
    def mock_path_join(*paths):
        return 'foo'

    def mock_read_csv(fin):
        return pd.DataFrame(mock_data)

    monkeypatch.setattr(os.path, 'join', mock_path_join)
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)
    x_train, x_test, y_train, y_test = fetch_processed('foo')
    
    assert all(y_train >= 0)
    assert all(y_test >= 0)
    assert x_train.shape[0] > 0
    assert x_test.shape[0] > 0


@patch('src.models.train_model.RandomForestClassifier')
def test_fit_model(mock_forest, monkeypatch):
    mock_model = Mock()
    attrs = {'fit.return_value': 'foo'}
    mock_model.configure_mock(**attrs)
    mock_forest.return_value = mock_model
    model = fit_model('foo', 'bar')
    assert model.fit() == 'foo'
