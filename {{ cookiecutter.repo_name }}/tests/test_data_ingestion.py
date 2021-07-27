import os
os['PIPELINE_ENGINE'] = 'local'

from pipeline import ingest_data

def test_ingest_data(self):
    data = ingest_data()
    assert not data.empty