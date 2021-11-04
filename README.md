# Cookiecutter Data Science <!-- omit in toc -->

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


Base on [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science), and modified by personal experience.

Difference with the original repository
- add [yapf](https://github.com/google/yapf), python formatter, into project structure
- add pre-commit for git hook
- change folders name that all folder names are unique within the project 

## TOC <!-- omit in toc -->
- [Requirements to use the cookiecutter template](#requirements-to-use-the-cookiecutter-template)
- [To start a new project, run:](#to-start-a-new-project-run)
- [The resulting directory structure](#the-resulting-directory-structure)
- [Installing development requirements](#installing-development-requirements)
- [Running the tests](#running-the-tests)
- [Acknowledgements](#acknowledgements)

## Requirements to use the cookiecutter template

 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


## To start a new project, run:

    cookiecutter -c v1 https://github.com/daniel-code/machine-learning-project-template.git

## The resulting directory structure

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── datasets
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── final          <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── model_weights      <- Trained and serialized models, model predictions, or model summaries
│
├── logs               <- Training logs
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to construct model modules and architecture
│   │ 
│   ├── utils          <- Scripts to help train/test pipeline
│   │
│   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
│   │   └── visualize.py
│   │
│   ├── train.py       <- Scripts to train models
│   │
│   ├── evaluate.py    <- Scripts to evaluate models
│   │
│   └── test.py        <- Scripts to predict single sample via trained models
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

## Installing development requirements

    pip install -r requirements.txt

## Running the tests

    py.test tests

## Acknowledgements
- [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)

