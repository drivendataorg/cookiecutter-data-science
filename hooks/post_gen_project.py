import os
import shutil

CWD = os.getcwd()
if '{{ cookiecutter.include_starter_proj }}' == 'N':
    shutil.rmtree(os.path.join(CWD, 'tests'))
    open(os.path.join(CWD, 'src/data/make_dataset.py'), 
        'w').close()