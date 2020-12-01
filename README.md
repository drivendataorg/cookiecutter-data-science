# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
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

    cookiecutter https://github.com/drivendata/cookiecutter-data-science


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)


### The resulting directory structure
------------

The directory structure of your new project looks like this:

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── CHANGELOG.md          <- The top-level README for developers using this project.
├── env.default  				<- Environment vars definition
├── Makefile           			<- Makefile with commands
├──.editorconfig				<- Helps maintain consistent coding styles
├── Dockerfile         			<- Environment definition
├── docker-compose.yml  			<- Environment definition
├── .dockerignore  			<- files don't want to copy inside container
├── .gitignore  				<- files don't want to copy in githubs
├── .github  				<- github configs
│   └── pull_request_template.md
├── requirements.txt / setup.py   	<- The requirements or config file
├── setup.cfg   				<- The requirements file
├── docs 					<- A default Sphinx project.
│   └── __init__.py
├── test                			<- Test setup folder using pytest
│   └── __init__.py
├── tox.ini            			<- tox file with settings for running tox;
|
├── data
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
|
├── notebooks           <- Naming convention is a number (for ordering),
│   │                     the creator's initials, and a short `-` delimited e.g.
│   │                     `1.0-jqp-initial-data-exploration`.
│   │
│   ├──jupyter_notebook_config.py
│   ├── template_notebooks <- where the notebooks template will live.
│   │
│   ├── Lab                <- Testing and development
│   │
│   └── Final            <- The final cleaned notebooks for reports/ designers /
|				   developers etc.
│
├── cloudFunctions
│   ├── name_cloud_function      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── airflowDataProject
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
└─ src                  <- Source code for use in this project.
    └── __init__.py     <- Makes src a Python module

```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
