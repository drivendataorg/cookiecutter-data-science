# Gatlen's Opinionated Template (GOTem)
_Currently not for production!_

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20fork-328F97?logo=cookiecutter" />
</a>

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A modern, opinionated full-stack [CookieCutter](https://www.cookiecutter.io/) project template that prioritizes developer experience and cutting-edge tools. Built on the foundation of [CookieCutter Data Science](https://cookiecutter-data-science.drivendata.org/), this template incorporates carefully selected defaults, dependency stack, customizations, and contemporary best practices for Python development, research projects, and academic work.

## Key Features
- 🚀 Modern tooling (UV, Ruff, FastAPI, Pydantic, Typer, Loguru, Polars, etc.) over traditional defaults
- 📦 Batteries-included configuration with sensible defaults
- 🔧 Highly customizable while maintaining simplicity
- 📈 Scales from personal projects to production
- 🤝 Perfect for individuals and small teams
- 🔄 Living template that evolves with the ecosystem


## Installation

It is recommended to use [Cruft](https://cruft.github.io/cruft/) instead of [CookieCutter](https://www.cookiecutter.io/). The resulting project is the same, but with the added option of being able to sync your project with the original template if this repository updates as if it were an incomming commit.

Install Cruft
```bash
    # MacOS Homebrew
    brew install cruft
```

```bash
    # Pip
    pip install cruft
```


Clone using Cruft
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
<!-- 
This project is more of a hobby and research project more than it is a practical template. Gatlen really enjoys the occasional research on the tooling ecosystem and understanding which tools solve what problems and how. He tends to have a very prefectionist perspective on projects beyond what is practical. Many of the packages included in this project, Gatlen has not yet used, but rather examined and compared against other tools and determined to be something to leverage once the need arises. The selection of packages and tools are in a way, a reminder of what resources he has have determined in advance to likely be helpful.

Here are a few guiding principles of this template to determine whether or not you should use it:
1. **Modern and Supported over Ubiquitous** -- Many of the packages and tools I have chosen for this package are NOT the defaults. (Another possible name for this template was "Everything but Defaults"). Unless I deem a built-in library to be the best of its type, it is likely unused. Instead of Logging I used Loguru. Instead of MatPlotLib I use Plotly. Instead of json I used orjson. Instead of pip I used UV. Instead of Django or Flask I used FastAPI. Instead of Argparse I use Typer.  Instead of Time, I use Arrow. Instead of Pandas I use Polars. It's not that these packages aren't used, they are extremely popular and indeed tend to offer better speed and functionality than the "defaults." Perhaps this is simply a selection of trendy packages that add unnecessary bloat and learning curves. But I think these packages can be a helpful learning experience that help me and others leverage the power this new rust-powered python ecosystem of tools that will become increasingly popular with time. Yes, these might not have as much developer documentation or extensions built up around it, but I think they important nonetheless and the novelty is also a plus in the sense that a lot of baggage and backwards-compatability that comes with an established package is not there. There aren't a lot of shitty tutorials from 15 years ago and a bloated API. Instead there is a very clear cut API with great defaults. Often times these packages work just with the sam syntax as the old greats do.
2. **Aspirational over Practical** --...
3. **Simplicity** -- I tend to pick packages that offer a lot of power with very simple and non-intrusive syntax. As an example, Django is a popular web framework that is very opinionated and requires a particular project structure and syntax to play nicely. Indeed, much of what it does is batteries-included best practice with tons of extensions made by the community, but it is also a very heavy library and once you start with a Django project, it is very hard to switch. I try to make it as easy as possible to switch in and out whatever you want to use.
4. **Good Defaults** -- To me, it's important to have good defaults on the packages I have set up so I can just import them and know I'm getting the best experience out of the box. A lot of this is the reason why I choose these modern packages -- because instead of having to bend over backwards to make things backwards compatible, the package can get a hard restart with decades of learning what the established greats did. I think about it this way: If The reset button were to be hit right now on the what tools and packages people used in Python, what do I wish they did?
5. **Customizability** -- I love customizing my tools and opt for tools where I can do a lot of customization and fiddling.
6. **Small Teams / Individual** -- As someone who personally tends to work by myself or with a few people on research projects, I gear this template towards iterating quickly and with high quality. If a tool requires such deep knowledge that someone has to spend a day researching it just to use, I don't want it.
7. **Scalable** -- As noted above, this is mainly geared to individuals and small teams. However, in the case you want to scale production or team size or even if you move to a new and larger organization, I want those skills to transfer and for there to be little more to learn and so that you don't have to learn an entirely new skillset or library. -->


## Philosophy 🧭

This template is primarily a research and learning project that explores modern Python development tools and practices. Rather than focusing solely on practical, production-ready solutions, it represents an aspirational view of Python development that emphasizes cutting-edge tools and emerging best practices.

### Core Principles 🎯

1. **Reset-Button Development** 🔄
   - Reimagines Python tooling without legacy constraints
   - Selects tools leveraging decades of lessons from established tools while avoiding their compromises

2. **Research-Driven Exploration** 🔬
   - Functions as a living laboratory for modern Python development
   - No default goes unscruitinized, with curated promising technologies based on careful comparative analysis

3. **Individual and Small Team Focus with Scalability** 👥
   - Optimized for personal projects and small research teams
   - Maintains professional standards that scale to larger organizations
   - Prioritizes tools that don't require deep expertise to start using and are helpful at any scale.

4. **Aspirational Over Practical** 🌟
   - Embraces perfectionist ideals in tooling choices
   - Values learning opportunities over conventional solutions
   - Willing to trade immediate familiarity for better long-term solutions

5. **Thoughtfully Opinionated** 🤔
   - Provides carefully selected defaults based on extensive research
   - Maintains modularity and avoids vendor lock-in
   - Prefers simple, non-intrusive APIs over heavyweight frameworks
   - Examples: Loguru > logging, Polars > Pandas, UV > pip, FastAPI > Flask

6. **Quality Driven** ✨
   - Emphasizes clean, maintainable code
   - Incorporates professional-grade tooling and practices
   - Focuses on developer experience without sacrificing robustness

7. **Sexy**
    - Just because coding is work doesn't mean it can't be fun. Sometimes you need those `pretty colors` and fancy ~graphs~ if you want that ADHD brain of yours pumped full of happy juice. I want my code to be like the notes of your overachieving classmate with a bullet journal.

> ⚠️ Note: This template intentionally prioritizes exploration and learning over immediate practicality. While all included tools have been carefully researched, not all have been extensively tested in production environments. Users should view this as a forward-looking reference implementation rather than a production-ready solution.

## Core Tools & Infrastructure 🛠️

**[VS Code](https://code.visualstudio.com/) / [Cursor](https://www.cursor.com/)** 🖥️
- Primary IDE with full ecosystem support
- Cursor fork provides enhanced AI integration
- Includes pre-configured workspace settings and debug profiles
- Supports remote development and notebook integration
- Replaces traditional Jupyter environments

> While many IDEs exist, VS Code's hackability, extensive ecosystem, and remote capabilities make it ideal for modern development. Cursor extends this with AI features while maintaining full VS Code compatibility. The decision to use VS Code even for notebooks (over JupyterLab) allows for a consistent development experience with all settings and extensions available.

**[UV](https://github.com/astral-sh/uv)** ⚡
- Ultra-fast Rust-based Python package manager
- Combines functionality of Poetry, virtualenv, and pipx
- Created by Astral (Ruff team)
- Significant performance benefits for CI/CD
- Maintains pip compatibility

> UV represents the next generation of Python package management. While tools like Poetry are mature, UV's Rust foundation provides exceptional speed (especially important in CI/CD) while maintaining compatibility with traditional pip workflows. Being from the Astral team (creators of Ruff) gives confidence in its long-term maintenance.

**[Task](https://taskfile.dev/)** 🎯
- Modern alternative to Make/Poetry scripts
- Simple, cross-platform task runner
- Excellent GitHub Actions integration
- Clean, intuitive YAML syntax

> Task was chosen over alternatives like Make, Poetry scripts, or Poe the Poet for its simplicity and cross-platform support. Its YAML syntax is immediately understandable, and it works seamlessly on Windows - a common pain point with Makefiles.

**[Git](https://git-scm.com/) + [GitLFS](https://git-lfs.com/) + [GitHub](https://github.com/)** 📚
- Industry standard version control
- Extensive ecosystem and integrations
- Built-in project management features
- Git Large File Storage (LFS) is a little-setup solution for file larger than the typical script like JSON files or Python Notebooks. Even larger files are recommended to use another storage solution such as a database or ignoring.

**[GitHub Actions](https://github.com/features/actions)** 🔄
- Integrated CI/CD solution
- Simple configuration and maintenance
- Native GitHub integration
- Extensive marketplace of actions

> While there are many CI/CD solutions available, GitHub Actions provides the tightest integration with our repository platform. Its marketplace of pre-built actions and simple YAML configuration makes it ideal for small teams who need professional CI/CD without dedicated DevOps resources.

**[Docker](https://www.docker.com/) + [Orbstack](https://orbstack.dev/)** 🐳
- Standard containerization platform
- Orbstack for MacOS (lighter Docker Desktop alternative)
- VM support through Orbstack
- Consistent development environments

> Docker remains the standard for containerization, but Docker Desktop can be resource-intensive. Orbstack provides a lightweight alternative for MacOS users while maintaining full Docker compatibility and adding convenient VM capabilities. Kubernetes is being explored but may not be the best setup for small development.

**[Dev Containers](https://containers.dev/)** 📦
- Standardized development environments
- VS Code integration
- *Note: Under evaluation*

> While Dev Containers show promise for standardizing development environments, they're included as an optional feature pending further evaluation by Gatlen.

**[AWS](https://www.geeksforgeeks.org/aws-vs-google-cloud-platform-vs-azure/#)** ☁️
- Mature cloud infrastructure platform
- Comprehensive service ecosystem
- Industry standard tooling
- Template remains cloud-agnostic where possible

> AWS was selected for its maturity and comprehensive service offering. However, recognizing that cloud preferences vary, the template maintains cloud-agnostic patterns where possible, allowing for easy adaptation to other providers.

> 💡 These tool selections reflect a balance between modern capabilities, developer experience, and professional requirements. Each choice prioritizes simplicity and maintainability while ensuring scalability for growing projects.

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