import os
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# Remove R stuff if not going to be used
if '{{ cookiecutter.include_r_boilerplate }}'.lower() == 'false':
    os.remove(os.path.join(
        PROJECT_DIRECTORY, 'src','data','R','utils.R'
    ))
    os.remove(os.path.join(
        PROJECT_DIRECTORY, 'src','data','make_dataset.R'
    ))
    os.rmdir(os.path.join(
        PROJECT_DIRECTORY, 'src','data','R'
    ))
