from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.library_name }}',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
    install_requires=[]
)
