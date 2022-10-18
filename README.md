# Cookiecutter Data Science

Originally dapted from [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/).

### TODO
- edit config interactions
- remove unnecessary components
- build on this- create additional cookiecutters
  - create a [user_config](https://cookiecutter.readthedocs.io/en/stable/advanced/user_config.html)
  - lots of good stuff in [hypermodern python](https://github.com/cjolowicz/cookiecutter-hypermodern-python)
    - packaging (poetry)
    - testing (nox, pytest, coverage.py, codecov)
    - linting and formating, and style guidance (flake8, black, prettier, mypy, typeguard, pyupgrade)
    - CI (GH actions, dependabot, pre-commit, github labeler)
    - docs (sphinx, read the docs, etc; xdoctest, autodoc, napolean, sphinx-click)
    - others (click, bandit, safety)
  - [python best practices](https://github.com/sourcery-ai/python-best-practices-cookiecutter)
    - pytest, black, mypy, flake8, pre-commit, docker, gh actions
  - [ML focused DS](https://github.com/crmne/cookiecutter-modern-datascience)
    - pipenv, prefect, weights and biases, fastAPI (including asyncio), Typer
    - pandas, numpy, scipy, seaborn, jupyterlab installed
    - black, autoflake, pylint, pytest, github pages
  - [jupyter driven](https://github.com/executablebooks/cookiecutter-jupyter-book)
    - alternate perspective on how something like this basic fork could have been built
  - dbt focused cookiecutter (one for each environment)
- include post hooks to create a new environment with pyenv
  - clean up requirements.txt

### Unnecessary components
- data/
  - rename directories
- docs/
  - learn sphynx or remove the whole directory and everything that installs it
- models/
  - delete
- notebooks/
- references/
- reports/
- src/
  - rename directories
- .env
  - add typical env vars (directories, db creds)
- .gitignore
- LICENSE
  - delete it and it's install parts in the slug
- Makefile
  - learn how makefiles work and then decide what to do
- README.md
  - edit as I go
- requirements.txt
  - think about how to square this with a clean version of base_data_env and then make todos
- setup.py
  - edit variables and their install parts in the slug
- test_environment.py
  - delete it and its install parts in the slug
- tox.ini
  - learn flake8 and get more opinionated about this

Everything below here has not been edited from the original


### Requirements to use the cookiecutter template:
-----------
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


### To start a new project, run:
------------

    cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)

### New version of Cookiecutter Data Science
------------
Cookiecutter data science is moving to v2 soon, which will entail using
the command `ccds ...` rather than `cookiecutter ...`. The cookiecutter command
will continue to work, and this version of the template will still be available.
To use the legacy template, you will need to explicitly use `-c v1` to select it.
Please update any scripts/automation you have to append the `-c v1` option (as above),
which is available now.


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
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
