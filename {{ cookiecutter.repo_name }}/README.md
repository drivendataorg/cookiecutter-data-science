{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

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
{% if cookiecutter.notebooks == 'y' %}
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
{% endif %}
{% if cookiecutter.cloud_functions == 'y' %}
    ├── cloudFunctions
    │   ├── name_cloud_function      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
{% endif %}
{% if cookiecutter.airflow_setup == 'y' %}
    ├── airflowDataProject
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
{% endif %}
{% if cookiecutter.module == 'y' %}
    └─ src                  <- Source code for use in this project.
        └── __init__.py     <- Makes src a Python module
{% endif %}



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
