#!/usr/bin/env python
import subprocess

data_version_control = True if "{{ cookiecutter.DVC_setting }}" == "Yes" else False
conda_env_creation = True if "{{ cookiecutter.create_conda_env }}" == "Yes" else False

if data_version_control:
    pass

if conda_env_creation:
    print(subprocess.call(["./create_env.sh"]))
