import ast
from codecs import open
import os
import re
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = "{{ cookiecutter.repo_name }}"
about = {}
with open(os.path.join(HERE, PACKAGE_NAME, "__about__.py"), "r", "utf-8") as f:
    exec(f.read(), about)


def readme():
    with open(os.path.join(HERE, "README.md"), "r", "utf-8") as f:
        return f.read()


install_requires = ["click", "Sphinx", "coverage", "awscli", "flake8", "fire", "python-dotenv>=0.5.1"]
extra_requires = {
    "dev": ["black", "coverage", "flake8", "ipykernel", "ipython", "pytest>=5.0.0"],
    "docs": ["mock", "sphinx", "sphinx_rtd_theme", "recommonmark"],
}
extra_requires["all"] = list(set((item for value in extra_requires.values() for item in value)))

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    url=about["__url__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    license=about["__licence__"],
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=install_requires,
    extra_requires=extra_requires,
    include_package_data=False,  # True to include files listed in ./MANIFEST.in,
    entry_points="""
        [console_scripts]
        {{ cookiecutter.repo_name }}={{ cookiecutter.repo_name }}.command_line:main
    """,
)
