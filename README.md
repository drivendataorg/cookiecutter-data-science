# Gatlen's Opinionated Template (GOTem)
_v0.0.1 is Currently not for production!_

<!-- gotem .. --output-dir ./ignore is test -->
[![tests](https://github.com/GatlenCulp/gatlens-opinionated-template/actions/workflows/tests.yml/badge.svg)](https://github.com/GatlenCulp/gatlens-opinionated-template/actions/workflows/tests.yml)

[![Uses the Cookiecutter Data Science project upstream](https://img.shields.io/badge/CCDS-Project%20fork-328F97?logo=cookiecutter)](https://cookiecutter-data-science.drivendata.org/) [![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A modern, opinionated full-stack [CookieCutter](https://www.cookiecutter.io/) project template that prioritizes developer experience and cutting-edge tools. Built on (and synced with) the foundation of [CookieCutter Data Science (CCDS) V2](https://cookiecutter-data-science.drivendata.org/), this template incorporates carefully selected defaults, dependency stack, customizations, and contemporary best practices for Python development, research projects, and academic work.

_The main functionality of this project is kept as close as possible to the CCDS template as to avoid additional maintenance on my end. This might mean a mismatch between practices I recommend and the ones they do. Ex: Makefiles on root, Taskfiles in template._

_See how CCDS compares with regular cookiecutter templates and my decisions [here](https://drivendata.co/blog/ccds-v2). For the most part, I look at CCDS as [Chesterton's Fence](https://www.lesswrong.com/tag/chesterton-s-fence), making sure to check my decisions against theirs before making changes. Still, the [CCDS team notes there's still some missing functionality](https://drivendata.co/blog/ccds-v2#whats-still-missing) including the [lack of a uv installer](https://github.com/drivendataorg/cookiecutter-data-science/discussions/403). The CCDS template still comes with some [nice features](https://drivendata.co/blog/ccds-v2#whats-new). CCDS has also considered [ruff as the default linting + formatting option](https://github.com/drivendataorg/cookiecutter-data-science/pull/387)_

<!-- TODO: Research Pachyderm -->

<!-- CCDS V2 appears not to like git lfs much, expensive. -->

## Key Features
- 🚀 Modern tooling (UV, Ruff, FastAPI, Pydantic, Typer, Loguru, Polars, etc.) over traditional defaults
- 📦 Batteries-included configuration with sensible defaults
- 🔧 Highly customizable while maintaining simplicity
- 📈 Scales from personal projects to production
- 🤝 Perfect for individuals and small teams
- 🔄 Living template that evolves with the ecosystem


## Installation

_I'm looking for a way to use [Cruft](https://cruft.github.io/cruft/) over [CookieCutter](https://www.cookiecutter.io/) + CCDS, but for now, CCDS needs to be used due to their custom configuration_



<!-- It is recommended to use [Cruft](https://cruft.github.io/cruft/) instead of [CookieCutter](https://www.cookiecutter.io/). The resulting project is the same, but with the added option of being able to sync your project with the original template if this repository updates as if it were an incomming commit.

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
``` -->
Install Gatlen's Opinionated Template (GOTem)
```bash
uv tool install gatlens-opinionated-template
```

Instantiate my project
```bash
uvx --from gatlens-opinionated-template gotem
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

## Philosophy 🧭
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
- Combines functionality of Poetry, virtualenv, and pipx (with dirt easy deployment to PyPi.)
- Created by Astral (Ruff team)
- Significant performance benefits for CI/CD
- Maintains pip compatibility

> UV represents the next generation of Python package management. While tools like Poetry are mature, UV's Rust foundation provides exceptional speed (especially important in CI/CD) while maintaining compatibility with traditional pip workflows. Being from the Astral team (creators of Ruff) gives confidence in its long-term maintenance.

<!-- TODO: Explain why not conda environment -->

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
```python
[project]
# ... other attributes ...
dependencies = [
    "loguru>=0.7.3",         # Better logging
    "plotly>=5.24.1",        # Interactive plotting
    "pydantic>=2.10.3",      # Data validation
    "rich>=13.9.4",          # Rich terminal output
]

[dependency-groups]
ai-apps = [  # AI application development packages
    "ell-ai>=0.0.15",        # AI toolkit
    "langchain>=0.3.12",     # LLM application framework
    "megaparse>=0.0.45",     # Advanced text parsing
]
ai-train = [  # Machine learning and model training packages
    "datasets>=3.1.0",           # Dataset handling
    "einops>=0.8.0",            # Tensor operations
    "jaxtyping>=0.2.36",        # Type hints for JAX
    "onnx>=1.17.0",             # ML model interoperability
    "pytorch-lightning>=2.4.0",  # PyTorch training framework
    "ray[tune]>=2.40.0",        # Distributed computing
    "safetensors>=0.4.5",       # Safe tensor serialization
    "scikit-learn>=1.6.0",      # Traditional ML algorithms
    "shap>=0.46.0",             # Model explainability
    "torch>=2.5.1",             # Deep learning framework
    "transformers>=4.47.0",     # Transformer models
    "umap-learn>=0.5.7",        # Dimensionality reduction
    "wandb>=0.19.1",            # Experiment tracking
    "nnsight>=0.3.7",           # ML Interp and Manipulation
]
async = [  # Asynchronous programming
    "uvloop>=0.21.0",           # Fast event loop implementation
]
cli = [  # Command-line interface tools
    "typer>=0.15.1",            # CLI builder
]
cloud = [  # Cloud infrastructure tools
    "ansible>=11.1.0",          # Infrastructure automation
    "boto3>=1.35.81",          # AWS SDK
]
config = [  # Configuration management
    "cookiecutter>=2.6.0",      # Project templating
    "gin-config>=0.5.0",        # Config management
    "jinja2>=3.1.4",           # Template engine
]
data = [  # Data processing and storage
    "dagster>=1.9.5",           # Data orchestration
    "duckdb>=1.1.3",           # Embedded analytics database
    "lancedb>=0.17.0",         # Vector database
    "networkx>=3.4.2",         # Graph operations
    "numpy>=1.26.4",           # Numerical computing
    "orjson>=3.10.12",         # Fast JSON parsing
    "pillow>=10.4.0",          # Image processing
    "polars>=1.17.0",          # Fast dataframes
    "pygwalker>=0.4.9.13",     # Data visualization
    "sqlmodel>=0.0.22",        # SQL ORM
    "tomli>=2.0.1",            # TOML parsing
]
dev = [  # Development tools
    "bandit>=1.8.0",           # Security linter
    "better-exceptions>=0.3.3", # Improved error messages
    "cruft>=2.15.0",           # Project template management
    "faker>=33.1.0",           # Fake data generation
    "hypothesis>=6.122.3",     # Property-based testing
    "pip>=24.3.1",             # Package installer
    "polyfactory>=2.18.1",     # Test data factory
    "pydoclint>=0.5.11",       # Docstring linter
    "pyinstrument>=5.0.0",     # Profiler
    "pyprojectsort>=0.3.0",    # pyproject.toml sorter
    "pyright>=1.1.390",        # Static type checker
    "pytest-cases>=3.8.6",     # Parametrized testing
    "pytest-cov>=6.0.0",       # Coverage reporting
    "pytest-icdiff>=0.9",      # Improved diffs
    "pytest-mock>=3.14.0",     # Mocking
    "pytest-playwright>=0.6.2", # Browser testing
    "pytest-profiling>=1.8.1", # Test profiling
    "pytest-random-order>=1.1.1", # Randomized test order
    "pytest-shutil>=1.8.1",    # File system testing
    "pytest-split>=0.10.0",    # Parallel testing
    "pytest-sugar>=1.0.0",     # Test progress visualization
    "pytest-timeout>=2.3.1",   # Test timeouts
    "pytest>=8.3.4",           # Testing framework
    "ruff>=0.8.3",             # Fast Python linter
    "taplo>=0.9.3",            # TOML toolkit
    "tox>=4.23.2",             # Test automation
    "uv>=0.5.7",               # Fast pip replacement
]
dev-doc = [  # Documentation tools
    "mdformat>=0.7.19",        # Markdown formatter
    "mkdocs-material>=9.5.48", # Documentation theme
    "mkdocs>=1.6.1",          # Documentation generator
]
dev-nb = [  # Notebook development tools
    "jupyter-book>=1.0.3",     # Notebook publishing
    "nbformat>=5.10.4",        # Notebook file format
    "nbqa>=1.9.1",             # Notebook linting
    "testbook>=0.4.2",         # Notebook testing
]
gui = [  # Graphical interface tools
    "streamlit>=1.41.1",       # Web app framework
]
misc = [  # Miscellaneous utilities
    "boltons>=24.1.0",         # Python utilities
    "cachetools>=5.5.0",       # Caching utilities
    "wrapt>=1.17.0",           # Decorator utilities
]
nb = [  # Jupyter notebook tools
    "chime>=0.7.0",            # Sound notifications
    "ipykernel>=6.29.5",       # Jupyter kernel
    "ipython>=7.34.0",         # Interactive Python shell
    "ipywidgets>=8.1.5",       # Jupyter widgets
    "jupyterlab>=4.3.3",       # Notebook IDE
]
web = [  # Web development and scraping
    "beautifulsoup4>=4.12.3",  # HTML parsing
    "fastapi>=0.115.6",        # Web framework
    "playwright>=1.49.1",      # Browser automation
    "requests>=2.32.3",        # HTTP client
    "scrapy>=2.12.0",          # Web scraping
    "uvicorn>=0.33.0",         # ASGI server
    "zrok>=0.4.42",            # Tunnel service
]

[tool.uv]
default-groups = ["dev", "data", "nb"]
```

## Contributing

We welcome contributions! [See the docs for guidelines](./CONTRIBUTING.md).

### Installing Requirements

It is recommended to use [UV](https://github.com/astral-sh/uv) for installations.

Create virtual environment
```bash
uv venv
```

<!-- Install general requirements
```bash
    uv pip install -e .
``` -->

Install dev requirements
```bash
uv pip install -r dev-requirements.txt
```

### Running the tests

<!-- uvx vs uv run https://docs.astral.sh/uv/concepts/tools/ -->

```bash
uv run pytest
```

_Note: configs[2-5] require conda to be installed. MiniConda has not yet been researched to see if it is the best option out there but it will make your run work:_
<!-- Conda-forge may be better -->
```bash
brew install --cask miniconda
```

## Inspirations & Acknowledgments 🙏

This project builds upon the excellent work of several established templates and projects:

**[cookiecutter-data-science](https://github.com/drivendataorg/cookiecutter-data-science)** 📊
- The original inspiration for this template
- Established many best practices for data science project organization
- Created by DrivenData, widely adopted in the data science community

**[cookiecutter-modern-datascience](https://github.com/crmne/cookiecutter-modern-datascience)** 🔬

**[cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv)** ⚡

**[full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template)** 🚀

> 💡 While this template draws inspiration from these excellent projects, it takes an opinionated approach to combining their best aspects while introducing modern tooling and development practices.
