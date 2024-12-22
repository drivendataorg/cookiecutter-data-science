# Core Tools & Infrastructure 🛠️

This page explains the chosen tools and why they were chosen.

<!-- Other names: GaTem (Gatlen's Template) GOATemplate? Idk-->
<!-- gotem .. --output-dir ./ignore is test -->
<!-- https://github.com/Ileriayo/markdown-badges -->
<!-- https://shields.io/badges/static-badge -->
<!-- https://github.com/alexandresanlim/Badges4-README.md-Profile -->
<!-- https://github.com/PatrickJS/awesome-cursorrules/tree/main?tab=readme-ov-file -->


<!-- 
Badges that need to be rearranged in stack. -->
<!-- https://img.shields.io/badge/Cookiecutter-D4AA00?style=for-the-badge&logo=Cookiecutter&logoColor=white -->
<!-- I love badges if not already clear lol -->
<!-- **OSes**
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Widnows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

**Languages**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)

**Packages**
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3) 
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![WandB](https://img.shields.io/badge/Weights_&_Biases-FFBE00?style=for-the-badge&logo=WeightsAndBiases&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=Pydantic&logoColor=white)

**Docs**
![Github Pages](https://img.shields.io/badge/GitHub%20Pages-222222?style=for-the-badge&logo=github%20Pages&logoColor=white)


**ML Packages**
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) 

**IDE**
![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white) 

**Install Options**
![PyPi](https://img.shields.io/badge/pypi-%23ececec.svg?style=for-the-badge&logo=pypi&logoColor=1f73b7)
![Homebrew](https://img.shields.io/badge/homebrew-FBB040?style=for-the-badge&logo=homebrew&logoColor=white)

**VCS + CI/CD**
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/Github%20Actions-282a2e?style=for-the-badge&logo=githubactions&logoColor=367cfe)

**Containerization**
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
https://img.shields.io/badge/Kubernetes-3069DE?style=for-the-badge&logo=kubernetes&logoColor=white

**Databases**
![DuckDB](https://img.shields.io/badge/Duckdb-000000?style=for-the-badge&logo=Duckdb&logoColor=yellow)
https://img.shields.io/badge/Ansible-000000?style=for-the-badge&logo=ansible&logoColor=white


**Lint**
![Prettier](https://img.shields.io/badge/prettier-1A2C34?style=for-the-badge&logo=prettier&logoColor=F7BA3E)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) -->



## 01 IDE

**[VS Code](https://code.visualstudio.com/) / [Cursor](https://www.cursor.com/)** 🖥️
- Primary IDE with full ecosystem support
- Cursor fork provides enhanced AI integration
- Includes pre-configured workspace settings and debug profiles
- Supports remote development and notebook integration
- Replaces traditional Jupyter environments

> While many IDEs exist, VS Code's hackability, extensive ecosystem, and remote capabilities make it ideal for modern development. Cursor extends this with AI features while maintaining full VS Code compatibility. The decision to use VS Code even for notebooks (over JupyterLab) allows for a consistent development experience with all settings and extensions available.


<!-- TODO: Explain why not conda environment -->


## 02 Task Running

**[Task](https://taskfile.dev/)** 🎯
- Modern alternative to Make/Poetry scripts
- Simple, cross-platform task runner
- Excellent GitHub Actions integration
- Clean, intuitive YAML syntax

> Task was chosen over alternatives like Make, Poetry scripts, or Poe the Poet for its simplicity and cross-platform support. Its YAML syntax is immediately understandable, and it works seamlessly on Windows - a common pain point with Makefiles.


## 03 VCS

**[Git](https://git-scm.com/) + [GitLFS](https://git-lfs.com/) + [GitHub](https://github.com/)** 📚
- Industry standard version control
- Extensive ecosystem and integrations
- Built-in project management features
- Git Large File Storage (LFS) is a little-setup solution for file larger than the typical script like JSON files or Python Notebooks. Even larger files are recommended to use another storage solution such as a database or ignoring.

## 04 CI/CD

**[GitHub Actions](https://github.com/features/actions)** 🔄
- Integrated CI/CD solution
- Simple configuration and maintenance
- Native GitHub integration
- Extensive marketplace of actions

> While there are many CI/CD solutions available, GitHub Actions provides the tightest integration with our repository platform. Its marketplace of pre-built actions and simple YAML configuration makes it ideal for small teams who need professional CI/CD without dedicated DevOps resources.

## 05 Containerization

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

## 06 Cloud Services

**[AWS](https://www.geeksforgeeks.org/aws-vs-google-cloud-platform-vs-azure/#)** ☁️
- Mature cloud infrastructure platform
- Comprehensive service ecosystem
- Industry standard tooling
- Template remains cloud-agnostic where possible

> AWS was selected for its maturity and comprehensive service offering. However, recognizing that cloud preferences vary, the template maintains cloud-agnostic patterns where possible, allowing for easy adaptation to other providers.

> 💡 These tool selections reflect a balance between modern capabilities, developer experience, and professional requirements. Each choice prioritizes simplicity and maintainability while ensuring scalability for growing projects.

## 07 Python Dependencies

**[UV](https://github.com/astral-sh/uv)** ⚡
- Ultra-fast Rust-based Python package manager
- Combines functionality of Poetry, virtualenv, and pipx (with dirt easy deployment to PyPi.)
- Created by Astral (Ruff team)
- Significant performance benefits for CI/CD
- Maintains pip compatibility

> UV represents the next generation of Python package management. While tools like Poetry are mature, UV's Rust foundation provides exceptional speed (especially important in CI/CD) while maintaining compatibility with traditional pip workflows. Being from the Astral team (creators of Ruff) gives confidence in its long-term maintenance.

### 07.01 Core Dependencies
Essential packages used across the project:
```toml
dependencies = [
    "loguru>=0.7.3",         # Better logging with rich formatting and easy setup
    "plotly>=5.24.1",        # Interactive visualization library
    "pydantic>=2.10.3",      # Data validation and settings management
    "rich>=13.9.4",          # Rich text and beautiful formatting in terminal
]
```

### 07.02 Application Development
Tools for building AI-powered applications:
```toml
ai-apps = [
    "ell-ai>=0.0.15",        # Unified AI toolkit for rapid development
    "langchain>=0.3.12",     # Framework for building LLM applications
    "megaparse>=0.0.45",     # Advanced text parsing and extraction
]
```

### 07.03 Training & Research
Packages for machine learning model development and research:
```toml
ai-train = [
    "datasets>=3.1.0",           # Efficient dataset handling and processing
    "einops>=0.8.0",            # Clear tensor manipulation operations
    "jaxtyping>=0.2.36",        # Type hints for tensor operations
    "onnx>=1.17.0",             # Model format for cross-platform compatibility
    "pytorch-lightning>=2.4.0",  # PyTorch training framework with less boilerplate
    "ray[tune]>=2.40.0",        # Distributed computing and hyperparameter tuning
    "safetensors>=0.4.5",       # Secure tensor serialization
    "scikit-learn>=1.6.0",      # Traditional ML algorithms and utilities
    "shap>=0.46.0",             # Model interpretability and explanations
    "torch>=2.5.1",             # Deep learning framework
    "transformers>=4.47.0",     # State-of-the-art transformer models
    "umap-learn>=0.5.7",        # Dimensionality reduction
    "wandb>=0.19.1",            # Experiment tracking and visualization
    "nnsight>=0.3.7",           # Neural network interpretation tools
]
```

### 07.04 Async Support
```toml
async = [
    "uvloop>=0.21.0",           # High-performance event loop replacement
]
```

### 07.05 CLI Tools
```toml
cli = [
    "typer>=0.15.1",            # Modern CLI builder with type hints
]
```

### 07.06 Cloud Infrastructure
```toml
cloud = [
    "ansible>=11.1.0",          # Infrastructure as code automation
    "boto3>=1.35.81",          # AWS SDK for Python
]
```

### 07.07 Configuration Management
```toml
config = [
    "cookiecutter>=2.6.0",      # Project template engine
    "gin-config>=0.5.0",        # Dependency injection configuration
    "jinja2>=3.1.4",           # Template engine for code generation
]
```

### 07.08 Data Management
```toml
data = [
    "dagster>=1.9.5",           # Data orchestration and pipelines
    "duckdb>=1.1.3",           # Fast analytical database
    "lancedb>=0.17.0",         # Vector database for embeddings
    "networkx>=3.4.2",         # Graph and network analysis
    "numpy>=1.26.4",           # Numerical computing foundation
    "orjson>=3.10.12",         # High-performance JSON operations
    "pillow>=10.4.0",          # Image processing utilities
    "polars>=1.17.0",          # Fast DataFrame operations
    "pygwalker>=0.4.9.13",     # Interactive data visualization
    "sqlmodel>=0.0.22",        # SQL database ORM
    "tomli>=2.0.1",            # TOML file parsing
]
```

### 07.09 Core Development
```toml
dev = [                        # Development tools
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
```

### 07.10 Documentation
```toml
dev-doc = [
    "mdformat>=0.7.19",        # Markdown formatting
    "mkdocs-material>=9.5.48", # Documentation theme
    "mkdocs>=1.6.1",          # Documentation site generator
]
```

### 07.11 Notebook Development
```toml
dev-nb = [
    "jupyter-book>=1.0.3",     # Notebook documentation publishing
    "nbformat>=5.10.4",        # Notebook file handling
    "nbqa>=1.9.1",             # Notebook code quality tools
    "testbook>=0.4.2",         # Notebook testing framework
]
```

### 07.12 GUI Applications
```toml
gui = [
    "streamlit>=1.41.1",       # Rapid web app development
]
```

### 07.13 Notebook Environment
```toml
nb = [
    "chime>=0.7.0",            # Audio notifications
    "ipykernel>=6.29.5",       # Jupyter kernel
    "ipython>=7.34.0",         # Enhanced interactive shell
    "ipywidgets>=8.1.5",       # Interactive widgets
    "jupyterlab>=4.3.3",       # Modern notebook interface
]
```

### 07.14 Web Development
```toml
web = [
    "beautifulsoup4>=4.12.3",  # HTML parsing and scraping
    "fastapi>=0.115.6",        # Modern web API framework
    "playwright>=1.49.1",      # Browser automation
    "requests>=2.32.3",        # HTTP client
    "scrapy>=2.12.0",          # Web scraping framework
    "uvicorn>=0.33.0",         # ASGI server
    "zrok>=0.4.42",            # Tunnel service for local development
]
```

### 07.15 Utilities
```toml
misc = [
    "boltons>=24.1.0",         # Python utility functions
    "cachetools>=5.5.0",       # Caching decorators and utilities
    "wrapt>=1.17.0",           # Decorator utilities
]
```

<!-- TODO: Research Pachyderm -->

<!-- CCDS V2 appears not to like git lfs much, expensive. -->

<!-- Maybe I should add an automatic folder icon creator? -->