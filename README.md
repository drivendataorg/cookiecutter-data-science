# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._

A video showing how to start a project using these docs is [on Vimeo here](https://vimeo.com/225258953).

The slides from a presentation of this project (including the video) are in the `docs/` folder here.

#### Based on a project from Driven Data: [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip:

``` bash
$ pip install cookiecutter
```

### To start a new project, run:
------------

    cookiecutter https://github.com/massmutual/cookiecutter-data-science

### The resulting directory structure
------------

The directory structure of your new project looks like this:

```
.
├── Makefile
├── README.md
├── data
│   ├── external
│   ├── interim
│   ├── predictions
│   ├── processed
│   └── raw
├── models
├── references
├── reports
│   ├── figures
│   └── tables
├── requirements.txt
├── src
│   ├── data
│   │   ├── R
│   │   │   └── utils.R
│   │   ├── __init__.py
│   │   ├── make_dataset.R
│   │   └── make_dataset.py
│   ├── exploratory
│   │   └── __init__.py
│   ├── features
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── predict_model.py
│   │   ├── test_model.py
│   │   └── train_model.py
│   └── vis
│       ├── __init__.py
│       └── visualize.py
├── test_environment.py
└── tox.ini
```

Here is some reference about those files:

```
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

