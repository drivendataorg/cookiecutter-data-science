import os
import shutil

CWD = os.getcwd()
if '{{ cookiecutter.include_starter_proj }}' == 'N':
    shutil.rmtree(os.path.join(CWD, 'sample_project'))
