import os
import shutil

DIRS = ['src/data', 'src/models']
CWD = os.getcwd()

if '{{ cookiecutter.include_starter_proj }}' == 'N':
    shutil.rmtree(os.path.join(CWD, 'tests'))
    for directory in DIRS:
        files_path = os.path.join(CWD, directory)
        for file in os.listdir(files_path):
            if file.endswith('.py'):
                open(os.path.join(CWD, files_path, file), 
                    'w').close()