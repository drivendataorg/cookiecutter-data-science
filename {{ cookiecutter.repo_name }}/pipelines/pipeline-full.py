# Databricks notebook source
"""
On databricks, there is no need to install the package
as an editable package like you might assume when developing locally.
This is because the repo root is a part of the $PYTHONPATH by default
when running a notebook within a repo
"""
from {{ cookiecutter.repo_name }} import main

# COMMAND ----------

"""
This main function is defined in the main.py
file located at the first level level of the project.
We can import it directly from {{ cookiecutter.repo_name }}
because of the __init__.py file which exposes everything in 
main.py to the {{ cookiecutter.repo_name }} package, including
the function called "main" we invoke here
"""
main()
