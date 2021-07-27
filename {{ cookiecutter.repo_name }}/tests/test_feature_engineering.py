import os
os['PIPELINE_ENGINE'] = 'local'

from pipeline import feature_engineering

def test_ingest_data(self):
    data = feature_engineering()
    assert not data.empty