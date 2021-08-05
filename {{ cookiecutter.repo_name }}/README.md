{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
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
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── pyproject.toml     <- makes project poetry and pip installable (poetry install) so src can be imported
                              also containing dependencies
    ├── {{ cookiecutter.repo_name }} <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

## How to start
Either use `Makefile` (type `make` in your terminal), which will show you available commands and use `make create_enviroment` or if you prefer, run these
manually:

* poetry install
* poetry run pre-commit install
* poetry run pre-commit install --hook-type commit-msg


**Important note**: After running these commands you will need to run git commit either using poetry (`poetry run git commit`) or enable venv in your terminal (`poetry shell`)


### Python and missing imports

Because of use of virtualenv editor will probably not see any imports correctly. To fix that in VSCode you need to choose interpreter.
Here's an instruction how to do it: https://code.visualstudio.com/docs/python/environments

**It might require restart of VSCode after poetry install** (only install is problematic when new virtualenv is created, but further updates are handled correctly)

## Work conventions

 * Each task should be done in a separate branch
 * Merge to master should be done after a review and at least one aprove and without unresolved issues
 * You should test your code if possible - use pytest for that
 * Whether possible - typehint your code. It's MUCH easier later to debug stuff.
 * If necessary, install our existing code (from other repositories in NaturalAntibody workspace) using poetry (git+https protocol)
 * In your commit message, on a first line, try to add task number like NARD-<number>. This way it should link to an issue in JIRA


## Suggested editor extensions
We're mostly using VSCode in our workflow. These extensions should be installed at minimum:

 * Editorconfig (code conventions)
 * Mypy (typings verifier)
 * Python extension
 * Jupyter (should be installed by python extension)
 * Pylance (should be installed by python extension)

Other extensions that could be installed are:

 * Project manager (easily switch between projects)
 * Docker extension
 * Remote containers editing
 * GitLens - some additional info about commits inside your editor
