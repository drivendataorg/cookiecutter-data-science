#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    # if '{{ cookiecutter.use_pytest }}' == 'y':
    #     remove_file('tests/__init__.py')

    # if '{{ cookiecutter.use_sqlalchemy }}' == 'n':
    #     database = os.path.join(
    #         '{{ cookiecutter.project_slug }}', 'core', 'database.py')
    #     models = os.path.join(
    #         '{{ cookiecutter.project_slug }}', 'models.py')
    #     remove_file(database)
    #     remove_file(models)
    #     remove_file('tests/conftest.py')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')