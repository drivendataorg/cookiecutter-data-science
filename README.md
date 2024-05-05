# Cookiecutter Simple Data Science

A **simple** project structure for doing and sharing data science work.

The easy way to start a data science:
- pet project
- competition
- homework
- etc


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

    cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science


TODO: simple gif or video


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`.
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be
│                         imported.
│
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── misc               <- Miscellaneous files: figures, docker files, additional markdown files, etc.
│
└── customlib          <- Source code for use in this project. The written name of the project
   │                      will be used.
   ├── __init__.py     <- Makes src a Python module.
   │
   ├── data            <- Module to download, generate data or turn raw data into features
   │   │                  for modeling.
   │   ├── make_dataset.py
   │   └── build_features.py
   │
   ├── models          <- Module to train models and then use trained models to make
   │   │                  predictions.
   │   └── baseline.py
   │
   └── visualization   <- Scripts to create exploratory and results oriented visualizations.
       └── visualize.py
```

## Contributing

We welcome contributions!
    


### Installing development requirements
------------

    pip install -r requirements.txt
