#!/usr/bin/env python
import subprocess
import sys

data_version_control = True if "{{ cookiecutter.DVC_setting }}" == "Yes" else False
conda_env_creation = True if "{{ cookiecutter.create_conda_env }}" == "Yes" else False

if data_version_control:
    pass

if conda_env_creation:
    try:
        exit_status = subprocess.run(["make", "create_environment"], check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)
