# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](https://github.com/Giving-Tuesday/cookiecutter-data-science)


### Requirements to use the cookiecutter template:
-----------
 - Python 3.5+
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

    cookiecutter https://github.com/Giving-Tuesday/cookiecutter-data-science

You can create a new conda environment named after your project by running

    make create_environment

Then go to `<repo_name>/data/make_dataset.py` and define your raw data pulls from
the database and run:

    make data

### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make create_environment`
│
├── .env               <- Set your environment variables. Put database settings here
|
├── README.md          <- The top-level README for developers using this project.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so project can be imported
│
├── <repo_name>        <- Source code for use in this project.
│   ├── __init__.py    <- Makes this a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   |   └── external           <- Data from third party sources.
│   |   └── processed          <- The final, canonical data sets for modeling.
│   |   └── raw                <- The original, immutable data dump (likely from sql).
│   │   └── make_dataset.py    <- Scripts to download or generate data
│   │
│   ├── core           <- Main business logic, models, predictions, summaries, etc
│   │   └── main.py    <- Typical project entrypoint
│   │
│   ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering)
│   │                         and a short `-` delimited description, e.g.
│   │                         `1.0-initial-data-exploration`.
│   │
│   ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│   |
│   └── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│       └── figures        <- Generated graphics and figures to be used in reporting
│
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

## Contributing

Please send suggestions to Parsa or by opening an issue or PR on github

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    pytest
