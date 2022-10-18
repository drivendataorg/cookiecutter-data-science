import sys
import pytest
import shutil
from pathlib import Path
from cookiecutter import main

CCDS_ROOT = Path(__file__).parents[1].resolve()

tensorflow_args = {
    "project_name": "DrivenData",
    "author_name": "DrivenData",
    "open_source_license": "BSD-3-Clause",
    "image": "Tensorflow",
}


def system_check(basename):
    platform = sys.platform
    if "linux" in platform:
        basename = basename.lower()
    return basename


# One case with defaults args, one with specific args
@pytest.fixture(scope="class", params=[{}, tensorflow_args])
def tensorflow_project(tmpdir_factory, request):
    temp = tmpdir_factory.mktemp("data-project")
    out_dir = Path(temp).resolve()

    pytest.param = request.param
    main.cookiecutter(
        str(CCDS_ROOT), no_input=True, extra_context=pytest.param, output_dir=out_dir
    )

    pn = pytest.param.get("project_name") or "project_name"

    # project name gets converted to lower case on Linux but not Mac
    pn = system_check(pn)

    proj = out_dir / pn
    request.cls.path = proj
    yield

    # cleanup after
    shutil.rmtree(out_dir)

pytorch_args = {
    "project_name": "DrivenData",
    "author_name": "DrivenData",
    "open_source_license": "MIT",
    "image": "PyTorch",
}

# One case with defaults args, one with specific args
@pytest.fixture(scope="class", params=[pytorch_args])
def pytorch_project(tmpdir_factory, request):
    temp = tmpdir_factory.mktemp("data-project")
    out_dir = Path(temp).resolve()

    pytest.param = request.param
    main.cookiecutter(
        str(CCDS_ROOT), no_input=True, extra_context=pytest.param, output_dir=out_dir
    )

    pn = pytest.param.get("project_name") or "project_name"

    # project name gets converted to lower case on Linux but not Mac
    pn = system_check(pn)

    proj = out_dir / pn
    request.cls.path = proj
    yield

    # cleanup after
    shutil.rmtree(out_dir)


r_args = {
    "project_name": "r_project_name",
    "author_name": "r_author",
    "image": "R",
}


@pytest.fixture(scope="class", params=[r_args])
def r_project(tmpdir_factory, request):
    temp = tmpdir_factory.mktemp("data-project")
    out_dir = Path(temp).resolve()

    pytest.param = request.param
    main.cookiecutter(
        str(CCDS_ROOT), no_input=True, extra_context=pytest.param, output_dir=out_dir
    )

    pn = pytest.param.get("project_name") or "project_name"

    # project name gets converted to lower case on Linux but not Mac
    pn = system_check(pn)

    proj = out_dir / pn
    request.cls.path = proj
    yield

    # cleanup after
    shutil.rmtree(out_dir)
