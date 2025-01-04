# Gatlen's Opinionated Template (GOTem)

_Cutting-edge, opinionated, and ambitious project builder for power users and researchers. Built on (and synced with) the foundation of [CookieCutter Data Science (CCDS) V2](https://cookiecutter-data-science.drivendata.org/), this template incorporates carefully selected defaults, dependency stack, customizations, and contemporary best practices for Python development, research projects, and academic work._

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Quickstart

Gatlen's Opinionated Template (GOTem) works on all platforms w/ Python 3.10+. While I try my best to keep in-sync with the upstream [CookieCutter Data Science (CCDS) V2](https://cookiecutter-data-science.drivendata.org/), being a one-man-maintainer on this project means I may neglect features I tend not to use and deviations from what I use may not receive as thorough testing. If you wish to change any of the defaults, I recommend forking this project.

I recommend installing gotem it with [uv](https://github.com/astral-sh/uv). GOTem is [Available on PyPi here](https://pypi.org/project/gatlens-opinionated-template/).

<!-- uvx --from gatlens-opinionated-template gotem -->

=== "With uv (recommended)"

````
```bash
uv pip install gatlens-opinionated-template

# From the parent directory where you want your project
gotem
```
````

=== "With pipx"

````
```bash
pipx install gatlens-opinionated-template

# From the parent directory where you want your project
gotem
```
````

=== "With pip"

````
```bash
pip install gatlens-opinionated-template

# From the parent directory where you want your project
gotem
```
````

=== "With conda (coming soon!)"

````
```bash
# conda install cookiecutter-data-science -c conda-forge

# From the parent directory where you want your project
# ccds
```
````

## Starting a new project

Starting a new project is as easy as running this command at the command line. No need to create a directory first, the cookiecutter will do it for you.

```bash
gotem
```

The `gotem` commandline tool defaults to the GOTem template, but you can pass your own template as the first argument if you want. The CCDS team has built significant tooling around Cookiecutter to make it easier to use and more customizable.

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
📁 .
├── ⚙️ .cursorrules                    <- LLM instructions for Cursor IDE
├── 💻 .devcontainer                   <- Devcontainer config
├── ⚙️ .gitattributes                  <- GIT-LFS Setup Configuration
├── 🧑‍💻 .github
│   ├── ⚡️ actions
│   │   └── 📁 setup-python-env       <- Automated python setup w/ uv
│   ├── 💡 ISSUE_TEMPLATE             <- Templates for Raising Issues on GH
│   ├── 💡 pull_request_template.md   <- Template for making GitHub PR
│   └── ⚡️ workflows                  
│       ├── 🚀 main.yml               <- Automated cross-platform testing w/ uv, precommit, deptry, 
│       └── 🚀 on-release-main.yml    <- Automated mkdocs updates
├── 💻 .vscode                        <- Preconfigured extensions, debug profiles, workspaces, and tasks for VSCode/Cursor powerusers
│   ├── 🚀 launch.json
│   ├── ⚙️ settings.json
│   ├── 📋 tasks.json
│   └── ⚙️ '{{ cookiecutter.repo_name }}.code-workspace'
├── 📁 data
│   ├── 📁 external                      <- Data from third party sources
│   ├── 📁 interim                       <- Intermediate data that has been transformed
│   ├── 📁 processed                     <- The final, canonical data sets for modeling
│   └── 📁 raw                           <- The original, immutable data dump
├── 🐳 docker                            <- Docker configuration for reproducability
├── 📚 docs                              <- Project documentation (using mkdocs)
├── 👩‍⚖️ LICENSE                           <- Open-source license if one is chosen
├── 📋 logs                              <- Preconfigured logging directory for
├── 👷‍♂️ Makefile                          <- Makefile with convenience commands (PyPi publishing, formatting, testing, and more)
├── 🚀 Taskfile.yml                    <- Modern alternative to Makefile w/ same functionality
├── 📁 notebooks                         <- Jupyter notebooks
│   ├── 📓 01_name_example.ipynb
│   └── 📰 README.md
├── 🗑️ out
│   ├── 📁 features                      <- Extracted Features
│   ├── 📁 models                        <- Trained and serialized models
│   └── 📚 reports                       <- Generated analysis
│       └── 📊 figures                   <- Generated graphics and figures
├── ⚙️ pyproject.toml                     <- Project configuration file w/ carefully selected dependency stacks
├── 📰 README.md                         <- The top-level README
├── 🔒 secrets                           <- Ignored project-level secrets directory to keep API keys and SSH keys safe and separate from your system (no setting up a new SSH-key in ~/.ssh for every project)
│   └── ⚙️ schema                         <- Clearly outline expected variables
│       ├── ⚙️ example.env
│       └── 🔑 ssh
│           ├── ⚙️ example.config.ssh
│           ├── 🔑 example.something.key
│           └── 🔑 example.something.pub
└── 🚰 '{{ cookiecutter.module_name }}'  <- Easily publishable source code
    ├── ⚙️ config.py                     <- Store useful variables and configuration (Preset)
    ├── 🐍 dataset.py                    <- Scripts to download or generate data
    ├── 🐍 features.py                   <- Code to create features for modeling
    ├── 📁 modeling
    │   ├── 🐍 __init__.py
    │   ├── 🐍 predict.py               <- Code to run model inference with trained models
    │   └── 🐍 train.py                 <- Code to train models
    └── 🐍 plots.py                     <- Code to create visualizations
```
