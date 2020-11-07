from contextlib import contextmanager
from itertools import product
import json
from pathlib import Path
import shutil
import sys
import tempfile

from ccds.__main__ import api_main


CCDS_ROOT = Path(__file__).parents[1].resolve()


default_args = {
    'project_name': 'my_test_project',
    'repo_name': 'my-test-repo',
    'module_name': 'project_module',
    'author_name': 'DrivenData',
    'description': 'A test project',
    'open_source_license' : 'MIT',
    'dataset_storage': {"azure": {"container": "container-name"}},
}

def config_generator():
    cookiecutter_json = json.load((CCDS_ROOT / 'ccds.json').open('r'))

    # python versions for the created environment; match the root
    # python version since Pipenv needs to be able to find an executable
    running_py_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    py_version = [('python_version_number', v) for v in [running_py_version]]

    configs = product(
        py_version,
        [('environment_manager', opt) for opt in cookiecutter_json['environment_manager']],
        [('dependency_file', opt) for opt in cookiecutter_json['dependency_file']],
        [('pydata_packages', opt) for opt in cookiecutter_json['pydata_packages']],
    )

    def _is_valid(config):
        config = dict(config)
        #  Pipfile + pipenv only valid combo for either
        if (config['environment_manager'] == 'pipenv') ^ (config['dependency_file'] == 'Pipfile'):
            return False
        # conda is the only valid env manager for environment.yml
        if (config['dependency_file'] == 'environment.yml') and (config['environment_manager'] != 'conda'):
            return False
        return True

    # remove invalid configs
    configs = [
        c for c in configs if _is_valid(c)
    ]

    for c in configs:
        config = dict(c)
        config.update(default_args)
        yield config


@contextmanager
def bake_project(config):
    temp = Path(tempfile.mkdtemp(suffix='data-project')).resolve()

    api_main.cookiecutter(
        str(CCDS_ROOT),
        no_input=True,
        extra_context=config,
        output_dir=temp,
        overwrite_if_exists=True
    )

    yield temp /  config['repo_name']

    # cleanup after
    shutil.rmtree(temp)