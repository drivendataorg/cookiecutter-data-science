#!/usr/bin/env python
"""Script that runs after the project generation phase."""
import os
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

if "{{ cookiecutter.license }}" == "Not open source":
    (PROJECT_DIRECTORY / "LICENSE").unlink()

if "{{ cookiecutter.setup_project }}" == "Yes - select this":
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'initial commit'")
    os.system("make init")
