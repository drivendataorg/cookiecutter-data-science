import json
from pathlib import Path
import pytest
import sys
import shutil

from click.testing import CliRunner

from ccds.__main__ import main


import yaml

CCDS_ROOT = Path(__file__).parents[1].resolve()

args = {'default_context': {
        'project_name': 'DrivenData',
        'author_name': 'DrivenData',
        'open_source_license': 'BSD-3-Clause',
        'description' : 'Test project',
        'data_storage': {'s3': {'bucket': 'test-bucket', 'aws_profile': 'default'}}
        }
}


def system_check(basename):
    platform = sys.platform
    if 'linux' in platform:
        basename = basename.lower()
    return basename


@pytest.fixture(scope='class', params=[{}, args])
def default_baked_project(tmpdir_factory, request):
    temp = tmpdir_factory.mktemp('data-project')
    config_dir = tmpdir_factory.mktemp('config')

    out_dir = Path(temp).resolve()

    pytest.param = request.param

    config_path = Path(config_dir) / 'config.yml'
    with open(config_path, 'w') as f:
        yaml.dump(pytest.param, f)

    runner = CliRunner()
    result = runner.invoke(
        main,
        ['--no-input',
         '-o', str(out_dir),
         str(CCDS_ROOT)],
        catch_exceptions=False,
    )

    # import pdb; pdb.set_trace()

    # assert result.output == ""
    assert result.exit_code == 0

    # main(
    #     str(CCDS_ROOT),
    #     pytest.param,
    #     True,
    #     None,
    #     False,
    #     False,
    #     out_dir,
    #     None,
    #     True,
    #     None
    # )

    pn = pytest.param.get('project_name') or 'project_name'
    
    # project name gets converted to lower case on Linux but not Mac
    pn = system_check(pn)

    proj = out_dir / pn
    request.cls.path = proj
    yield 

    # cleanup after
    print("=======> ", out_dir)
    # shutil.rmtree(out_dir)
    # shutil.rmtree(config_dir)
