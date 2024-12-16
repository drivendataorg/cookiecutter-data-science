# Gatlen's Opinionated Template (GOTem)
_Currently not for production!_

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20fork-328F97?logo=cookiecutter" />
</a>

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


A fork of the gold standard [CookieCutter Data Science](https://cookiecutter-data-science.drivendata.org/) template complete with Gatlen's preferred defaults, software, and customizations for any Python, Research, or School Project.

This project is based on [CookieCutter](https://www.cookiecutter.io/), a Python based project boilerplate and templating tool. I'm writing this project so I can easily instantiate new projects with my preferred defaults, provide this to colleagues as a solid jumping off point, and to quickly adapt my preferred settings to other projects that I join.

This is a living project, constantly to be updated as better packages and standards come out and as my preferences change. Note that even though this originated from [CookieCutter Data Science](https://cookiecutter-data-science.drivendata.org/), this is a general template and CCDS was chosen for its high quality starting point.

## Installation

It is recommended to use [Cruft](https://cruft.github.io/cruft/) instead of [CookieCutter](https://www.cookiecutter.io/). The resulting project is the same, but with the added option of being able to sync your project with the original template if this repository updates as if it were an incomming commit.
```bash
    cruft create https://github.com/GatlenCulp/gatlens-opinionated-template
```

### The resulting directory structure

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
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations   
```

## Philosophy

This project is more of a hobby and research project more than it is a practical template. Gatlen really enjoys the occasional research on the tooling ecosystem and understanding which tools solve what problems and how. He tends to have a very prefectionist perspective on projects beyond what is practical. Many of the packages included in this project, Gatlen has not yet used, but rather examined and compared against other tools and determined to be something to leverage once the need arises. The selection of packages and tools are in a way, a reminder of what resources he has have determined in advance to likely be helpful.

Here are a few guiding principles of this template to determine whether or not you should use it:
1. **Modern and Supported over Ubiquitous** -- Many of the packages and tools I have chosen for this package are NOT the defaults. (Another possible name for this template was "Everything but Defaults"). Unless I deem a built-in library to be the best of its type, it is likely unused. Instead of Logging I used Loguru. Instead of MatPlotLib I use Plotly. Instead of json I used orjson. Instead of pip I used UV. Instead of Django or Flask I used FastAPI. Instead of Argparse I use Typer.  Instead of Time, I use Arrow. Instead of Pandas I use Polars. It's not that these packages aren't used, they are extremely popular and indeed tend to offer better speed and functionality than the "defaults." Perhaps this is simply a selection of trendy packages that add unnecessary bloat and learning curves. But I think these packages can be a helpful learning experience that help me and others leverage the power this new rust-powered python ecosystem of tools that will become increasingly popular with time. Yes, these might not have as much developer documentation or extensions built up around it, but I think they important nonetheless and the novelty is also a plus in the sense that a lot of baggage and backwards-compatability that comes with an established package is not there. There aren't a lot of shitty tutorials from 15 years ago and a bloated API. Instead there is a very clear cut API with great defaults. Often times these packages work just with the sam syntax as the old greats do.
2. **Aspirational over Practical** --...
3. **Simplicity** -- I tend to pick packages that offer a lot of power with very simple and non-intrusive syntax. As an example, Django is a popular web framework that is very opinionated and requires a particular project structure and syntax to play nicely. Indeed, much of what it does is batteries-included best practice with tons of extensions made by the community, but it is also a very heavy library and once you start with a Django project, it is very hard to switch. I try to make it as easy as possible to switch in and out whatever you want to use.
4. **Good Defaults** -- To me, it's important to have good defaults on the packages I have set up so I can just import them and know I'm getting the best experience out of the box. A lot of this is the reason why I choose these modern packages -- because instead of having to bend over backwards to make things backwards compatible, the package can get a hard restart with decades of learning what the established greats did. I think about it this way: If The reset button were to be hit right now on the what tools and packages people used in Python, what do I wish they did?
5. **Customizability** -- I love customizing my tools and opt for tools where I can do a lot of customization and fiddling.
6. **Small Teams / Individual** -- As someone who personally tends to work by myself or with a few people on research projects, I gear this template towards iterating quickly and with high quality. If a tool requires such deep knowledge that someone has to spend a day researching it just to use, I don't want it.
7. **Scalable** -- As noted above, this is mainly geared to individuals and small teams. However, in the case you want to scale production or team size or even if you move to a new and larger organization, I want those skills to transfer and for there to be little more to learn and so that you don't have to learn an entirely new skillset or library.

## Core Tools Outside Python

**UV**
Unlike CCDS, this tool was written expecting use with [UV](https://github.com/astral-sh/uv/tree/main), An extremely fast Python package and project manager, written in Rust which is a virtual environment tool, build tool, and more all wrapped into one. It's similar to Poetry or Rye + Virtual Environments + PipX + More but with massive speed benefits and interoperability with normal pip, written by team Astral, the same organization behind the ruff linter. UV has been increasing in popularity as of late and seems like it could be on the way to be one of the more ubiquitous tools around the python ecosystem. While I will try to allow for the other installation tools. When using tools like Docker or CI/CD, this time becomes important.

**Taskfile**
Task is a task runner / build tool that aims to be simpler and easier to use than, for example, GNU Make. This was chosen over PoeThePoet, Makefiles, and other similar tools for its out-of-the box simplicity and operability on Windows. This makes work with Github actions much simpler. The syntax is so simple I don't think anyone will have trouble with it.

**GitHub Actions**
For CI/CD I opted for GitHub Actions. I haven't used any of the other tools but given how simple, widespread, customizable, integrated, and portable GitHub actions are, I decided to include it as the defaults

**Cursor/VS Code**
Cursor is a fork on VS Code with better AI integration, compatible of using all the same extensions, settings, etc. Included in this project are some bootstrapped workspace, settings, and debug profiles. I tend to use VSCode/Cursor for everything I do for a variety of reasons including that it is extremely hackable, easy to write extensions for, has a great ecosystem, it can work on remote servers, and more. I don't even use JupyterLab for notebooks, opting to use VSCode's ecosystem so I can take advantage of the AI integration and all my preexisting settings.

**Docker (Orbstack)**

Docker is a containerization platform, helpful for launching apps in an isolated environment that will work anywhere. Building an app image allows you to quickly deploy and move operations.

Orbstack is a super lightweight alternative to Docker Desktop for MacOS with the added ability for use with VMs.

**AWS**

AWS is literally just so ubiquitous and mature and offers so many integrated services with easy configuration that I have decided to use this for launching infrastructure. Perhaps this will change with time but for now, this seems good. Much of the code in this template is NOT tied to AWS.

**Dev Containers**

I haven't needed to use this much but I have been curious.

**Git + GitHub**

Git is pretty good. GitHub is pretty good. Both are ubiqituous and have good options. I'm happy with this.

## Chosen Stack


## Contributing

We welcome contributions! [See the docs for guidelines](./CONTRIBUTING.md).

### Installing development requirements

```bash
pip install -r dev-requirements.txt
```

### Running the tests

```bash
pytest tests
```
### Inspirations
- https://github.com/crmne/cookiecutter-modern-datascience
- https://github.com/drivendataorg/cookiecutter-data-science
- https://github.com/fpgmaas/cookiecutter-uv
- https://github.com/fastapi/full-stack-fastapi-template