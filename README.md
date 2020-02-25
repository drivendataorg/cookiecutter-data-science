# Cookiecutter Machine Learning research
> _Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>._

_A more robust ML starting point._


## Prerequisites:
-----------
 - Cookiecutter

``` bash
    $ pip install cookiecutter
```


## To start a new project, run:
------------

    cookiecutter https://github.com/davebulaval/cookiecutter-data-science.git

### The arguments definitions
 - project_name: The name to be given to the project.
 - author_name: The name to be shown into the README as the author.
 - description: The description of the project to be shown into the README.
 - open_source_license: The license to be set into the project.
 - DVC_setting: The setting parameter to initialize the Data Version Control (DVC) into the repository.
 - python_interpreter: The python3 version to be used for the configuration.
 - create_conda_env: The setting parameter to initialize a conda environment using the project name. It also install the basic requirements packages for any ML projects.
 - git_remote_url: The url for the Git remote to be set to. This will also do the initial commit of the repo.

*The Makefile is still in development.*

### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
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
├── src  <- Source code for use in this project.
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

