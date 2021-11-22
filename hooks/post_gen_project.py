#!/usr/bin/env python
"""Script that runs after the project generation phase."""
import os
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

if "{{ cookiecutter.license }}" == "Not open source":
    (PROJECT_DIRECTORY / "LICENSE").unlink()

if "{{ cookiecutter.git_setup }}" == "Yes":
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'initial commit'")

if "{{ cookiecutter.environment_setup }}" == "Yes":
    os.system("make init")

