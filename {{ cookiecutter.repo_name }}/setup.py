from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.license == 'MIT' %}MIT{% elif cookiecutter.license == 'BSD-3-Clause' %}BSD-3{% endif %}',
)
