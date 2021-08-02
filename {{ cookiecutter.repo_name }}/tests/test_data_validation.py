import os
os['PIPELINE_ENGINE'] = 'local'

from {{cookiecutter.project_name}}_pipeline import validate_data

def test_data_validation(self):
    assert validate_data()