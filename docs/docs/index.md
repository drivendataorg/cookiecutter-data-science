# Cookiecutter Data Science

_A logical, flexible, and reasonably standardized project structure for doing and sharing data science work._

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

!!! info "CCDS V2 Announcement"

    Version 2 of Cookiecutter Data Science has launched recently. To learn more about what's different and what's in progress, see the [announcement blog post for more information](https://drivendata.co/blog/ccds-v2).


## Quickstart

Cookiecutter Data Science v2 requires Python 3.8+. Since this is a cross-project utility application, we recommend installing it with [pipx](https://pypa.github.io/pipx/). Installation command options:

=== "With pipx (recommended)"

    ```bash
    pipx install cookiecutter-data-science

    # From the parent directory where you want your project
    ccds
    ```

=== "With pip"

    ```bash
    pip install cookiecutter-data-science
    `
    # From the parent directory where you want your project
    ccds
    ```

=== "With conda (coming soon!)"

    ```bash
    # conda install cookiecutter-data-science -c conda-forge

    # From the parent directory where you want your project
    # ccds
    ```

=== "Use the v1 template"

    ```bash
    pip install cookiecutter

    # From the parent directory where you want your project
    cookiecutter https://github.com/drivendataorg/cookiecutter-data-science -c v1
    ```

!!! info "Use the ccds command-line tool"

    Cookiecutter Data Science v2 now requires installing the new `cookiecutter-data-science` Python package, which extends the functionality of the [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/README.html) templating utility. Use the provided `ccds` command-line program instead of `cookiecutter`.


## Starting a new project

Starting a new project is as easy as running this command at the command line. No need to create a directory first, the cookiecutter will do it for you.

```bash
ccds
```

The `ccds` commandline tool defaults to the Cookiecutter Data Science template, but you can pass your own template as the first argument if you want.


## Example

<!-- TERMYNAL OUTPUT -->


Now that you've got your project, you're ready to go! You should do the following:

 - **Check out the directory structure** below so you know what's in the project and how to use it.
 - **Read the [opinions](opinions.md)** that are baked into the project so you understand best practices and the philosophy behind the project structure.
 - **Read the [using the template](using-the-template.md) guide** to understand how to get started on a project that uses the template.


 Enjoy!


## Directory structure

The directory structure of your new project will look something like this (depending on the settings that you choose):

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         {{ cookiecutter.module_name }} and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── {{ cookiecutter.module_name }}   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes {{ cookiecutter.module_name }} a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations   
```
