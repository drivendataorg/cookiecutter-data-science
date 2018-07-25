from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    install_requires=['{% if cookiecutter.include_starter_proj == "Y" %}scikit-learn[alldeps]{% endif %}'],
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.open_source_license == "MIT" %}MIT{% elif cookiecutter.open_source_license == "BSD-3-Clause" %}BSD-3{% endif %}',
)
