{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

To build a docker image:
```
docker build -t {{cookiecutter.repo_name}} -f Dockerfile .
```

To start a docker container (as your current user/group), mount current directory and connect to the container:
```
docker run -d --rm -it --user $(id -u):$(id -g) --volume $(pwd):/workspace --name {{cookiecutter.repo_name}} {{cookiecutter.repo_name}}
docker exec -it {{cookiecutter.repo_name}} /bin/bash
```

If you want to use python environments instead, use the commands below. That creates a virtual python environment in your current folder, activates it and installs dependencies with pip
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Initialize [git](https://git-scm.com/docs/gittutorial) and [DVC](https://dvc.org/doc/start) and create an initial commit before doing anything else:
```
git init
dvc init
git add .
git commit -m "Initial commit"
```

Use [doit](https://pydoit.org/usecases.html) to run linting and tests:
```
doit lint
doit pytest
```

Use [DVC](https://dvc.org/doc/start) to create reproducible ML-pipelines and experiments with git tracking:
```
dvc repro
dvc exp run
```

Use [mlflow](https://www.mlflow.org/docs/latest/tutorials-and-examples/index.html) to run lots of experiments that you do not want to track with git.

Use [mkdocs-material](https://squidfunk.github.io/mkdocs-material/reference/) structure to update the documentation. Test locally with 'serve' and build with 'build':
```
mkdocs serve
mkdocs build --site-dir public
```

Project Organization
------------

    ├── LICENSE
    ├── dodo.py            <- Makefile-like multiplatform CLI
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources (ex. script config files)
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- Documentation
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


--------

<p><small>Project based on the <a target="_blank" href="https://github.com/Vastra-Gotalandsregionen/data-science-template">data science project template</a>. #cookiecutterdatascience.</small></p>