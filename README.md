# Data Science Template

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._

_Adapted to Region Västra Götaland's data science processes._

## Start your new PyTorch, Tensorflow or R project from our template!
You can choose which language to use when selecting interpreter. By using our template you can easily create reproducible data science projects to share with your colleagues.

You will get:
 - Folder structure
 - Documentation
 - Tools for reproducibility
 - (if selected) Dockerfile with PyTorch + Jupyter installed
 - (if selected) Dockerfile with Tensorflow + Jupyter installed
 - (if selected) Dockerfile with R + RStudio Server installed

You will **NOT** get:
 - Messy projects
 - Things that only work on your machine

### Requirements to install and use the project templating tool:
-----------
 - Python 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

### To start a new project, run:
------------

    cookiecutter https://github.com/Vastra-Gotalandsregionen/data-science-template

[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)


### The resulting directory structure
------------

The directory structure of your new project looks like this: 
```
    ├── LICENSE
    ├── dodo.py            <- Makefile-like multiplatform CLI
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources (ex. script config files)
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- Documentation template with hints
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
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
    ├── {{ cookiecutter.module_name }}                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes {{ cookiecutter.module_name }} a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │                     predictions
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    |
    ├── Dockerfile         <- Dockerfile with settings to run scripts in Docker container
    ├── dvc.yaml           <- DVC pipeline; see dvc.org
    ├── params.yaml        <- Parameter values (things like hyperparameters) used by DVC pipeline
    ├── setup.cfg          <- config file with settings for running pylint, flake8 and bandit
    └── pytest.ini         <- config file with settings for running pytest
```

## Contributing

If you work at Västra Götalandsregionen, or you simply want to use and develop this template, feel free to make a pull request with your suggested changes.

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests

#### [Original project homepage](http://drivendata.github.io/cookiecutter-data-science/)
#### [Original fork with doit, loguru, dvc, mlflow, pylint, etc](https://github.com/iKintosh/cookiecutter-data-science)