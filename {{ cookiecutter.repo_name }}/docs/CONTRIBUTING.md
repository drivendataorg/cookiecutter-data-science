# Contributing to {{cookiecutter.project_name}}

![Uses the Cookiecutter Data Science project template, GOTem style](https://img.shields.io/badge/GOTem-Project%20Instance-328F97?logo=cookiecutter)
{% if cookiecutter.environment_manager == "uv" %}
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
{% endif %}

> [!NOTE]
> This project was created using [Gatlen's Opinionated Template (GOTem)](https://github.com/GatlenCulp/gatlens-opinionated-template), a cutting-edge project template for power users and researchers.

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.
{% if cookiecutter._readme_include_code_of_conduct == 'y' -%}
Please note we have a [code of conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.
{% endif %}

---
## 00 Table of Contents

- [Contributing to {{cookiecutter.project_name}}](#contributing-to-{{cookiecutter.project_name | lower | replace(" ", "-")}})
  - [00 Table of Contents](#00-table-of-contents)
  - [01 Development Environment Setup](#01-development-environment-setup)
    - [01.01 Prerequisites](#0101-prerequisites)
    - [01.02 Installation Steps](#0102-installation-steps)
  - [02 Project Organization](#02-project-organization)
  - [03 Built With](#03-built-with)
  - [04 Issues and Feature Requests](#04-issues-and-feature-requests)
  - [05 How to Submit a Pull Request](#05-how-to-submit-a-pull-request)
  - [06 Roadmap](#06-roadmap)
  - [07 Support](#07-support)
  - [08 Project Assistance](#08-project-assistance)
  - [09 Authors & Contributors](#09-authors--contributors)
  - [10 License](#10-license)

---
## 01 Development Environment Setup

### 01.01 Prerequisites

> **[?]**
> List all dependencies and requirements needed before setting up the development environment:
> ```bash
> # Example
> python >= 3.8
> pip >= 21.0
> git
> ```

### 01.02 Installation Steps

To set up a development environment, please follow these steps:

**01. Clone the repository**
```bash
git clone https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}
cd {{cookiecutter.repo_name}}
```

**02. Set up a virtual environment**
{% if cookiecutter.environment_manager == "uv" %}
```bash
# Using UV (recommended)
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
{% else %}
```bash
# Using venv
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
{% endif %}

**03. Install development dependencies**
{% if cookiecutter.environment_manager == "uv" %}
```bash
uv pip install -e ".[dev]"
```
{% else %}
```bash
pip install -e ".[dev]"
```
{% endif %}

**04. Set up pre-commit hooks**
```bash
pre-commit install
```

> **[?]**
> Add any additional setup steps specific to your project.

---
## 02 Project Organization

<details>
<summary>Project organization</summary>

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
│   └── ⚙️ '{{cookiecutter.repo_name}}.code-workspace'
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
└── 🚰 '{{cookiecutter.module_name}}'  <- Easily publishable source code
    ├── ⚙️ config.py                     <- Store useful variables and configuration (Preset)
    ├── 🐍 dataset.py                    <- Scripts to download or generate data
    ├── 🐍 features.py                   <- Code to create features for modeling
    ├── 📁 modeling
    │   ├── 🐍 __init__.py
    │   ├── 🐍 predict.py               <- Code to run model inference with trained models
    │   └── 🐍 train.py                 <- Code to train models
    └── 🐍 plots.py                     <- Code to create visualizations
```
</details>

---
## 03 Built With

> **[?]**
> List the key technologies, frameworks, and libraries used in this project:
> 
> - Python 3.8+
> - FastAPI for web services
> - Polars for data processing
> - Typer for CLI applications
> - Loguru for logging
> - etc.

---
## 04 Issues and Feature Requests

You've found a bug in the source code, a mistake in the documentation, or maybe you'd like a new feature? You can help us by [submitting an issue on GitHub](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/issues). Before you create an issue, make sure to search the issue archive -- your issue may have already been addressed!

Please try to create bug reports that are:

- **Reproducible.** Include steps to reproduce the problem.
- **Specific.** Include as much detail as possible: which version, what environment, etc.
- **Unique.** Do not duplicate existing opened issues.
- **Scoped to a Single Bug.** One bug per report.

**Even better: Submit a pull request with a fix or new feature!**

---
## 05 How to Submit a Pull Request

1. Search our repository for open or closed [Pull Requests](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/pulls) that relate to your submission. You don't want to duplicate effort.
2. Fork the project
3. Create your feature branch (`git checkout -b feat/amazing_feature`)
4. Commit your changes (`git commit -m 'feat: add amazing_feature'`) {% if cookiecutter._use_conventional_commits == 'y' -%}
   {{cookiecutter.project_name}} uses [conventional commits](https://www.conventionalcommits.org), so please follow the specification in your commit messages.{% endif %}
5. Push to the branch (`git push origin feat/amazing_feature`)
6. [Open a Pull Request](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/compare?expand=1)

---
## 06 Roadmap

See the [open issues](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

---
## 07 Support

> **[?]**
> Provide ways to contact the project maintainer/maintainers.

Reach out to the maintainer at one of the following places:

{% if cookiecutter._readme_use_github_discussions == 'y' -%}
- [GitHub Discussions](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/discussions)
{%- elif cookiecutter._readme_use_github_discussions != 'y' -%}
- [GitHub issues](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)
{%- endif %}
- Contact options listed on [this GitHub profile](https://github.com/{{cookiecutter._github_username}})

{% if cookiecutter._readme_include_project_assistance == 'y' -%}
---
## 08 Project Assistance

If you want to say **thank you** or/and support active development of {{cookiecutter.project_name}}:

- Add a [GitHub Star](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}) to the project.
- Tweet about the {{cookiecutter.project_name}}.
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your personal blog.

Together, we can make {{cookiecutter.project_name}} **better**!
{% endif %}

{% if cookiecutter._readme_include_authors == 'y' -%}
---
## 09 Authors & Contributors

The original setup of this repository is by [{{cookiecutter.full_name}}](https://github.com/{{cookiecutter._github_username}}).

For a full list of all authors and contributors, see [the contributors page](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/contributors).
{% endif %}

{% if cookiecutter.open_source_license != 'No license file' -%}
---
## 10 License

This project is licensed under the **{{cookiecutter.open_source_license}}**.

See [LICENSE](../LICENSE) for more information.
{% endif %}
