{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

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
├── tests              <- Where to place tests. Preferably use pytest
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so project can be imported
│
├── {{cookiecutter.project_name}}        <- Source code for use in this project.
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

--------




Feel free to ignore anything you don't need/understand, this is supposed to make your life easier ;)

<p><small>Project based on the <a target="_blank" href="https://github.com/Giving-Tuesday/cookiecutter-data-science">
Giving Tuesdays' cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
