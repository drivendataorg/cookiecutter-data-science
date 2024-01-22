# Cookiecutter Data Science

_A logical and flexible project structure for doing and sharing data science work._

[![tests](https://github.com/drivendata/cookiecutter-data-science/workflows/tests/badge.svg?branch=v2)](https://github.com/drivendata/cookiecutter-data-science/actions/workflows/tests.yml?query=branch%3Av2)

## Quickstart

!!! info "Changes in v2"

    Cookiecutter Data Science v2 now requires installing the new `cookiecutter-data-science` Python package, which extends the functionality of the [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/README.html) templating utility. Use the provided `ccds` command-line program instead of `cookiecutter`.

=== "With pipx (recommended)"

    ```bash
    pipx install cookiecutter-data-science

    # From the parent directory where you want your project
    ccds https://github.com/drivendata/cookiecutter-data-science
    ```

=== "With pip"

    ```bash
    pip install cookiecutter-data-science
    `
    # From the parent directory where you want your project
    ccds https://github.com/drivendata/cookiecutter-data-science
    ```

=== "With conda (coming soon!)"

    ```bash
    # conda install cookiecutter-data-science -c conda-forge

    # From the parent directory where you want your project
    # ccds https://github.com/drivendata/cookiecutter-data-science
    ```

=== "Use the v1 template"

    ```bash
    pip install cookiecutter

    # From the parent directory where you want your project
    cookiecutter https://github.com/drivendata/cookiecutter-data-science -c v1
    ```

## Installation

Cookiecutter Data Science v2 requires Python 3.7+. Since this is a cross-project utility application, we recommend installing it with [pipx](https://pypa.github.io/pipx/). Installation command options:

```bash
# With pipx from PyPI (recommended)
pipx install cookiecutter-data-science

# With pip from PyPI
pip install cookiecutter-data-science

# With conda from conda-forge (coming soon)
# conda install cookiecutter-data-science -c conda-forge
```

## Starting a new project

Starting a new project is as easy as running this command at the command line. No need to create a directory first, the cookiecutter will do it for you.

```bash
ccds https://github.com/drivendata/cookiecutter-data-science
```

## Example

<!-- TERMYNAL OUTPUT -->

## Directory structure

The directory structure of your new project will look something like this (depending on the settings that you choose):

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         {{ cookiecutter.module_name }} and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── {{ cookiecutter.module_name }}   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes {{ cookiecutter.module_name }} a Python module
    │
    ├── data                    <- Scripts to download or generate data
    │   └── make_dataset.py
    │
    ├── features                <- Scripts to turn raw data into features for modeling
    │   └── build_features.py
    │
    ├── models                  <- Scripts to train models and then use trained models 
    │   ├── predict_model.py       to make predictions
    │   └── train_model.py
    │
    └── visualization           <- Scripts to create exploratory and results-oriented 
        └── visualize.py           visualizations
```
