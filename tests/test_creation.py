import os
import pytest
import shutil
from pathlib import Path

from cookiecutter import main

CCDS_ROOT = Path(__file__).parents[1].resolve()


@pytest.fixture(scope='function')
def default_baked_project(tmpdir):
    temp = tmpdir.mkdir('data-project')
    out_dir = Path(temp).resolve()

    main.cookiecutter(
        str(CCDS_ROOT),
        no_input=True,
        extra_context={},
        output_dir=out_dir
    )

    # default project name is project_name
    yield out_dir / 'project_name'

    # cleanup after
    shutil.rmtree(out_dir)


def test_readme(default_baked_project):
    readme_path = default_baked_project / 'README.md'

    assert readme_path.exists()
    assert no_curlies(readme_path)


def test_license(default_baked_project):
    license_path = default_baked_project / 'LICENSE'

    assert license_path.exists()
    assert no_curlies(license_path)


def test_requirements(default_baked_project):
    reqs_path = default_baked_project / 'requirements.txt'

    assert reqs_path.exists()
    assert no_curlies(reqs_path)


def test_makefile(default_baked_project):
    makefile_path = default_baked_project / 'Makefile'

    assert makefile_path.exists()
    assert no_curlies(makefile_path)


def test_folders(default_baked_project):
    expected_dirs = [
        'data',
        'data/external',
        'data/interim',
        'data/processed',
        'data/raw',
        'docs',
        'models',
        'notebooks',
        'references',
        'reports',
        'reports/figures',
        'src',
        'src/data',
        'src/features',
        'src/models',
        'src/visualization',
    ]

    ignored_dirs = [
        str(default_baked_project)
    ]

    abs_expected_dirs = [str(default_baked_project / d) for d in expected_dirs]
    abs_dirs, _, _ = list(zip(*os.walk(default_baked_project)))
    assert len(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)) == 0


def no_curlies(filepath):
    """ Utility to make sure no curly braces appear in a file.
        That is, was jinja able to render everthing?
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
        '{{',
        '}}',
        '{%',
        '%}'
    ]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)
