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
    with open("README.md", "r", "utf-8") as f:
        return f.read()


def parse_requirements():
    """
    Reads requirements.txt and preprocess it
    to be feed into setuptools.

    References:
        https://github.com/pypa/pip/issues/3610#issuecomment-356687173

    Warnings:
        to make pip respect the links, you have to use
        `--process-dependency-links` switch. So e.g.:
        `pip install --process-dependency-links {git-url}`

    Returns:
         tuple of list: first list is regular package name on pypi. SEcond list are package with git urls
    """
    default = open("requirements.txt", "r").readlines()
    packages_name = []
    private_packages = []

    for resource in default:
        if "git+ssh" in resource:
            private_packages.append(resource.strip().replace("-e ", ""))
            packages_name.append(resource.split("egg=")[-1].rsplit("-", 1)[0])
        else:
            packages_name.append(resource.strip())

    return packages_name, private_packages


public_packages, private_packages = parse_requirements()


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
    install_requires=public_packages,
    dependency_links=private_packages,
    include_package_data=False,  # True to include files listed in ./MANIFEST.in,
    entry_points="""
        [console_scripts]
        s1m=s1m.cli:main
    """,
)
