
# Core Tools & Infrastructure 🛠️

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