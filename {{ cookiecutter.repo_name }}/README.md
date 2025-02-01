# {{cookiecutter.project_name}}

![Uses the Cookiecutter Data Science project template, GOTem style](https://img.shields.io/badge/GOTem-Project%20Instance-328F97?logo=cookiecutter)

<!-- ![PyPI - Version](https://img.shields.io/pypi/v/gatlens-opinionated-template?style=flat) -->

<!-- [![tests](https://github.com/GatlenCulp/gatlens-opinionated-template/actions/workflows/tests.yml/badge.svg)](https://github.com/GatlenCulp/gatlens-opinionated-template/actions/workflows/tests.yml)  -->

<!-- ![GitHub stars](https://img.shields.io/github/stars/gatlenculp/homebrew-vivaria?style=social) -->

{% if cookiecutter.environment_manager == "uv" %}
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
{% endif %}

{%- if "github" in cookiecutter.version_control and cookiecutter.docs != "none" %}

<!-- TODO: Make this update to user's GitHub. -->

https://gatlenculp.github.io/{{ cookiecutter.repo_name }}

{%- endif %}

## Project Organization

{#

<!-- (Skipping common file descriptions to be concise) -->

<!-- Created with eza --all --tree --icons --ignore-glob ".gitkeep" -->

<!-- https://github.com/mightbesimon/vscode-emoji-icons -->

<!-- TODO: In Github Actions actually have a simple test or something -->

<!-- TODO: update main.yml to use what I now have setup -->

TODO: Take inspo from [here](https://github.com/matiassingers/awesome-readme)
#}

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

{% if cookiecutter._readme_modern_header == 'y' -%}
{%- if cookiecutter._readme_include_logo == 'y' -%}

<h1 align="center">
  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}">
    <!-- Please provide path to your logo here -->
    <img src="docs/images/logo.svg" alt="Logo" width="100" height="100">
  </a>
</h1>
{% endif %}
<div align="center">
  {{cookiecutter.project_name}}
  <br />
  <a href="#about">
  {%- if cookiecutter.include_screenshots == 'y' -%}
  <strong>Explore the screenshots »</strong>
  {%- else -%}
  <strong>Explore the docs »</strong>
  {%- endif -%}
  </a>
  <br />
  <br />
  <a href="https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  {%- if cookiecutter._readme_use_github_discussions == 'y' -%}
  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/discussions">Ask a Question</a>
  {%- elif cookiecutter._readme_use_github_discussions != 'y' %}
  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
  {%- endif %}
</div>
{%- else -%}
# {{cookiecutter.project_name}}

> **[?]**
> Provide short description for your project here.

{%- endif %}
{% if cookiecutter._readme_include_badges == 'y' -%}
{%- if cookiecutter._readme_modern_header == 'y' %}

<div align="center">
{%- endif %}
<br />

[![Project license](https://img.shields.io/github/license/%7B%7Bcookiecutter._github_username%7D%7D/%7B%7Bcookiecutter._repo_slug%7D%7D.svg?style=flat-square)](LICENSE)

[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D/%7B%7Bcookiecutter.repo_name%7D%7D/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![code with love by {{cookiecutter.github_username}}](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-%7B%7Bcookiecutter._github_username%7D%7D-ff1414.svg?style=flat-square)](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D)

{% if cookiecutter._readme_modern_header == 'y' -%}

</div>
{%- endif %}
{% endif %}
{% if cookiecutter._readme_include_toc == 'y' -%}
<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Support](#support)
  {%- if cookiecutter._readme_include_project_assistance == 'y' %}
- [Project assistance](#project-assistance)
  {%- endif %}
- [Contributing](#contributing)
  {%- if cookiecutter._readme_include_authors == 'y' %}
- [Authors & contributors](#authors--contributors)
  {%- endif %}
  {%- if cookiecutter._readme_include_security == 'y' %}
- [Security](#security)
  {%- endif %}
  {%- if cookiecutter.open_source_license != 'No license file' %}
- [License](#license)
  {%- endif %}
  {%- if cookiecutter.include_acknowledgements == 'y' %}
- [Acknowledgements](#acknowledgements)
  {%- endif %}

</details>
{%- endif %}

______________________________________________________________________

## About

{% if cookiecutter._readme_table_in_about == 'y' %}

<table><tr><td>
{% endif %}
> **[?]**
> Provide general information about your project here.
> What problem does it (intend to) solve?
> What is the purpose of your project?
> Why did you undertake it?
> You don't have to answer all the questions -- just the ones relevant to your project.

{% if cookiecutter._readme_include_screenshots == 'y' -%}

<details>
<summary>Screenshots</summary>
<br>

> **[?]**
> Please provide your screenshots here.

|                               Home Page                               |                               Login Page                               |
| :-------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="docs/images/screenshot.png" title="Home Page" width="100%"> | <img src="docs/images/screenshot.png" title="Login Page" width="100%"> |

</details>
{%- endif %}
{% if cookiecutter._readme_table_in_about == 'y' %}
</td></tr></table>
{% endif %}
### Built With

> **[?]**
> Please provide the technologies that are used in the project.

## Getting Started

### Prerequisites

> **[?]**
> What are the project requirements/dependencies?

### Installation

> **[?]**
> Describe how to install and get started with the project.

## Usage

> **[?]**
> How does one go about using it?
> Provide various use cases and code examples here.

## Roadmap

See the [open issues](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D/%7B%7Bcookiecutter.repo_name%7D%7D/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D/%7B%7Bcookiecutter.repo_name%7D%7D/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D/%7B%7Bcookiecutter.repo_name%7D%7D/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D/%7B%7Bcookiecutter.repo_name%7D%7D/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Support

> **[?]**
> Provide additional ways to contact the project maintainer/maintainers.

Reach out to the maintainer at one of the following places:

{% if cookiecutter.use_github_discussions == 'y' -%}

- [GitHub Discussions](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D/%7B%7Bcookiecutter.repo_name%7D%7D/discussions)
  {%- elif cookiecutter.use_github_discussions != 'y' -%}
- [GitHub issues](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D/%7B%7Bcookiecutter.repo_name%7D%7D/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)
  {%- endif %}
- Contact options listed on [this GitHub profile](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D)

{% if cookiecutter._readme_include_project_assistance == 'y' -%}

## Project assistance

If you want to say **thank you** or/and support active development of {{cookiecutter.project_name}}:

- Add a [GitHub Star](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D/%7B%7Bcookiecutter.repo_name%7D%7D) to the project.
- Tweet about the {{cookiecutter.project_name}}.
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your personal blog.

Together, we can make {{cookiecutter.project_name}} **better**!
{% endif %}

## Contributing

{% if cookiecutter.open_source_license != 'No license file' -%}
First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.
{% endif %}

Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

{% if cookiecutter._readme_include_authors == 'y' -%}

## Authors & contributors

The original setup of this repository is by [{{cookiecutter.full_name}}](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D).

For a full list of all authors and contributors, see [the contributors page](https://github.com/%7B%7Bcookiecutter._github_username%7D%7D/%7B%7Bcookiecutter.repo_name%7D%7D/contributors).
{% endif %}
{% if cookiecutter._readme_include_security == 'y' -%}

## Security

{{cookiecutter.project_name}} follows good practices of security, but 100% security cannot be assured.
{{cookiecutter.project_name}} is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._
{% endif %}
{% if cookiecutter.open_source_license != 'No license file' -%}

## License

This project is licensed under the **{{cookiecutter.open_source_license}}**.

See [LICENSE](LICENSE) for more information.
{% endif %}
{% if cookiecutter._readme_include_acknowledgements == 'y' -%}

## Acknowledgements

> **[?]**
> If your work was funded by any organization or institution, acknowledge their support here.
> In addition, if your work relies on other software libraries, or was inspired by looking at other work, it is appropriate to acknowledge this intellectual debt too.
> {% endif %}
