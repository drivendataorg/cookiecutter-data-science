import os
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
import subprocess

# Remove R stuff if not going to be used
if '{{ cookiecutter.include_r_boilerplate }}'.lower() == 'false':
    subprocess.call("rm -r src/*/*R",shell=True)
    # os.remove(os.path.join(
    #     PROJECT_DIRECTORY, 'src','data','R','utils.R'
    # ))
    # os.remove(os.path.join(
    #     PROJECT_DIRECTORY, 'src','data','make_dataset.R'
    # ))
    # os.remove(os.path.join(
    #     PROJECT_DIRECTORY, 'src','features','build_features.R'
    # ))
    # os.remove(os.path.join(
    #     PROJECT_DIRECTORY, 'src','models','test_model.R'
    # ))
    # os.remove(os.path.join(
    #     PROJECT_DIRECTORY, 'src','models','train_model.R'
    # ))
    # os.remove(os.path.join(
    #     PROJECT_DIRECTORY, 'src','vis','visualize.R'
    # ))
    # for folder in ["data","exploratory","features","models","vis"]:
    #     os.rmdir(os.path.join(
    #         PROJECT_DIRECTORY, 'src',folder,'R'
    #     ))

# Remove python stuff if not going to be used
if '{{ cookiecutter.include_python_boilerplate }}'.lower() == 'false':
    subprocess.call("rm -r src/*/*.py",shell=True)    
