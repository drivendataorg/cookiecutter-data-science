{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

To build a docker image:
```{% if cookiecutter.python_interpreter == 'R' %}
docker build -t {{cookiecutter.repo_name}} -f Dockerfile .{% else %}
docker build -t {{cookiecutter.repo_name}} --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -f Dockerfile .{% endif %}
```

To start a docker container, mount current directory and connect to the container:
{% if cookiecutter.python_interpreter == 'R' %}```
docker run --rm -d -p 8787:8787 -it --volume $(pwd):/home/rstudio -e PASSWORD=yourpasswordhere -e USERID=$(id -u) -e GROUPID=GROUP_ID=$(id -g) --name {{cookiecutter.repo_name}} {{cookiecutter.repo_name}}
```
Visit [localhost:8787](http://localhost:8787) in your browser and log in with username ```rstudio``` and the password you set when starting the container. Use the terminal in RStudio to run things like ```git``` and ```dvc```.{% else %}```
docker run -d --rm -it --volume $(pwd):/workspace --name {{cookiecutter.repo_name}} {{cookiecutter.repo_name}}
docker exec -it {{cookiecutter.repo_name}} /bin/bash
```{% endif %}
{% if cookiecutter.python_interpreter == 'R' %}
Install packages as you normally do in R, then save a list of installed packages and versions with ```renv::snapshot()```, you can then rebuild your docker image to have your packages installed for the next time you restart your container.
See [RStudio-reproducibility](https://rstudio.github.io/renv/articles/renv.html#reproducibility) for more details on R-package management.
{% endif %}
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
{% if cookiecutter.python_interpreter == 'python3' %}
Use [mlflow](https://www.mlflow.org/docs/latest/tutorials-and-examples/index.html) to run lots of experiments that you do not want to track with git.
{% endif %}
Use [mkdocs-material](https://squidfunk.github.io/mkdocs-material/reference/) structure to update the documentation. Test locally with 'serve' and build with 'build':
```
mkdocs serve
mkdocs build --site-dir public
```

Project Organization
------------
{% if cookiecutter.python_interpreter == 'python3' %}
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
    ├── {{ cookiecutter.module_name }}   <- Source code for use in this project.
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
{% else %}
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
    ├── renv.lock          <- R packages for reproducing the analysis environment, e.g.
    |                         generated with `renv::restore()`
    |
    ├── requirements.txt   <- Python requirements file for reproducing the analysis environment. 
    |                         Used in **addition** to R for things like documentation and DVC.
    │
    ├── {{ cookiecutter.module_name }}  <- Source code for use in this project.
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
    ├── dvc.yaml           <- DVC pipeline; see [dvc.org](https://dvc.org/)
    └── params.yaml        <- Parameter values (things like hyperparameters) used by DVC pipeline
{% endif %}
--------

<p><small>Project based on the <a target="_blank" href="https://github.com/Vastra-Gotalandsregionen/data-science-template">data science project template</a>. #cookiecutterdatascience.</small></p>