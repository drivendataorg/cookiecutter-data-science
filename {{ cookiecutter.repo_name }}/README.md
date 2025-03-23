# {{cookiecutter.project_name}}

![Uses the Cookiecutter Data Science project template, GOTem style](https://img.shields.io/badge/GOTem-Project%20Instance-328F97?logo=cookiecutter)
{% if cookiecutter.environment_manager == "uv" %}
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
{% endif %}

<!-- [![tests](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/actions/workflows/tests.yml/badge.svg)](https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}/actions/workflows/tests.yml) -->
<!-- ![GitHub stars](https://img.shields.io/github/stars/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}?style=social) -->

> [!NOTE]
> This project was created using [Gatlen's Opinionated Template (GOTem)](https://github.com/GatlenCulp/gatlens-opinionated-template), a cutting-edge project template for power users and researchers.

{% if cookiecutter._readme_include_logo == 'y' -%}

<div align="center">
  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}">
    <!-- Please provide path to your logo here -->
    <img src="https://picsum.photos/id/237/200/300" alt="Logo" style="max-width: 250px;"/>
  </a>
  <br/>
  <b>{{cookiecutter.project_name}}</b>
</div>
<br>
{% endif %}

> **[?]**
> Provide a brief description of your project here. What does it do? Why is it useful?

{%- if "github" in cookiecutter.version_control and cookiecutter.docs != "none" %}
**[View the full documentation here](https://{{ cookiecutter.author_name }}.github.io/{{ cookiecutter.repo_name }}) ➡️**
{%- endif %}

---

## 00 Table of Contents

- [{{cookiecutter.project_name}}](#{{cookiecutter.project_name | lower | replace(" ", "-")}})
  - [00 Table of Contents](#00-table-of-contents)
  - [01 About](#01-about)
  - [02 Getting Started](#02-getting-started)
    - [02.01 Prerequisites](#0201-prerequisites)
    - [02.02 Installation](#0202-installation)
  - [03 Usage](#03-usage)
  - [04 Project Structure](#04-project-structure)
  - [05 Contributing](#05-contributing)
  - [06 License](#06-license)

---

## 01 About

> **[?]**
> Provide detailed information about your project here.
>
> - What problem does it solve?
> - What makes it unique?
> - What are its key features?
> - Who is it for?

{% if cookiecutter._readme_include_screenshots == 'y' -%}

<details>
<summary>📸 Screenshots</summary>
<br>

> **[?]**
> Please provide your screenshots here.

|                                    Home Page                                    |                                    Login Page                                    |
| :-----------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |
| <img src="https://picsum.photos/id/237/200/300" title="Home Page" width="100%"> | <img src="https://picsum.photos/id/237/200/300" title="Login Page" width="100%"> |

</details>
{%- endif %}

---

## 02 Getting Started

### 02.01 Prerequisites

> **[?]**
> List all dependencies and requirements needed before installing the project:
>
> ```bash
> # Example
> python >= 3.8
> pip >= 21.0
> ```

### 02.02 Installation

> **[?]**
> Provide step-by-step installation instructions:
>
> **01. Clone the repository**
>
> ```bash
> git clone https://github.com/{{cookiecutter._github_username}}/{{cookiecutter.repo_name}}.git
> cd {{cookiecutter.repo_name}}
> ```
>
> **02. Install dependencies**
>
> ```bash
> pip install -e .
> ```

---

## 03 Usage

> **[?]**
> Provide basic usage examples with code snippets:
>
> ```python
> from {{cookiecutter.module_name}} import example
>
> # Initialize
> example.start()
>
> # Run a basic operation
> result = example.process("data")
> print(result)
> ```

---

## 04 Project Structure

This project follows the structure of [Gatlen's Opinionated Template (GOTem)](https://github.com/GatlenCulp/gatlens-opinionated-template):

```
📁 .
├── 📁 data               <- Data directories for various stages
├── 📚 docs               <- Documentation
├── 📋 logs               <- Log files
├── 📁 notebooks          <- Jupyter notebooks
├── 🗑️ out                <- Output files, models, etc.
└── 🚰 {{cookiecutter.module_name}}  <- Source code
    ├── ⚙️ config.py      <- Configuration settings
    ├── 🐍 dataset.py     <- Data processing
    ├── 🐍 features.py    <- Feature engineering
    ├── 📁 modeling       <- Model training and prediction
    └── 🐍 plots.py       <- Visualization code
```

For a more detailed explanation of the project structure, see the [CONTRIBUTING.md](docs/CONTRIBUTING.md) file.

---

## 05 Contributing

We welcome contributions to this project! Please see our [contribution guidelines](docs/CONTRIBUTING.md) for detailed information on how to:

- Set up your development environment
- Submit issues and feature requests
- Create pull requests
- Get support

---

## 06 License

{% if cookiecutter.open_source_license != 'No license file' %}
This project is licensed under the {{cookiecutter.open_source_license}} - see the [LICENSE](LICENSE) file for details.
{% else %}

> **[?]**
> Specify the license under which your project is available.
> {% endif %}
