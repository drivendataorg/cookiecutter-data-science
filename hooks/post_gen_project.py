#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath), ignore_errors=True, onerror=None)


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'n' == '{{ cookiecutter.notebooks|lower }}':
        remove_dir('notebooks')

    if 'n' == '{{ cookiecutter.module|lower }}':
        remove_dir('{{ cookiecutter.project_slug }}')

    if 'n' == '{{ cookiecutter.airflow_setup|lower }}':
        remove_dir('airflow_setup')

    if 'n' == '{{ cookiecutter.cloud_functions|lower }}':
        remove_dir('cloud_functions')
