import pytest
import shutil
from pathlib import Path


@pytest.fixture(scope='function')
def tmp_dump_dir(tmpdir):
    temp = tmpdir.mkdir('data')
    out_dir = Path(temp).resolve()
    yield out_dir / 'foo.csv'
    shutil.rmtree(out_dir)