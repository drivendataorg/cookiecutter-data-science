
from {{ cookiecutter.repo_name }}.core.main import sample_function

def test_main():
    assert sample_function() == True