#!/usr/bin/env python
import os

data_version_control = True if "{{ cookiecutter.DVC_setting }}" == "Yes" else False
conda_env_creation = True if "{{ cookiecutter.create_conda_env }}" == "Yes" else False

if data_version_control:
    pass

if conda_env_creation:
    print(os.system("make create_environment"))
