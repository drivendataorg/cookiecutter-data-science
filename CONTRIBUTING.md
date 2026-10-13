# Contributing to Cookiecutter Data Science

Thank you for your interest in contributing to **Cookiecutter Data Science (CCDS)**! CCDS is a project template that helps data scientists organize their work in a logical, reasonably standardized, and flexible way. Every contribution — from fixing a typo in the template to proposing a new directory convention — makes the project better for the community.

This document explains how to set up a development environment, run the tests, propose changes, and submit a pull request.

---

## Table of contents

1. [Code of conduct](#code-of-conduct)
2. [Where to start](#where-to-start)
3. [Development setup](#development-setup)
4. [Project layout](#project-layout)
5. [Running the tests](#running-the-tests)
6. [Code style and quality](#code-style-and-quality)
7. [Submitting a pull request](#submitting-a-pull-request)
8. [Reporting bugs](#reporting-bugs)
9. [Suggesting enhancements](#suggesting-enhancements)
10. [Release process](#release-process)
11. [License](#license)

---

## Code of conduct

This project is released under the MIT License and is intended to be a welcoming, harassment-free experience for everyone, regardless of background or experience level. By participating, you agree to treat fellow contributors with respect and to give and receive constructive feedback gracefully.

## Where to start

- **Look for `good first issue` labels** on the [issue tracker](https://github.com/drivendataorg/cookiecutter-data-science/issues?q=is%3Aopen+label%3A%22good+first+issue%22). These are curated to be approachable for newcomers.
- **File an issue first** for any non-trivial change. Discussing the approach in an issue before opening a PR saves time for everyone.
- **Keep changes focused.** A pull request that fixes one thing is much easier to review than one that fixes seven things.

## Development setup

CCDS requires Python 3.9+ on Linux, macOS, or Windows. We recommend using a virtual environment so dependencies do not leak into your global Python install.

```bash
# 1. Fork the repository on GitHub, then clone your fork.
git clone https://github.com/<your-username>/cookiecutter-data-science.git
cd cookiecutter-data-science

# 2. Add the upstream repository as a remote named "upstream".
git remote add upstream https://github.com/drivendataorg/cookiecutter-data-science.git

# 3. Create and activate a virtual environment.
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate

# 4. Install the project together with development and documentation dependencies.
pip install -r dev-requirements.txt
```

`dev-requirements.txt` installs CCDS in editable mode (`-e .`) along with the testing and documentation tooling used by the CI pipeline.

## Project layout

The repository is laid out as follows:

```
├── ccds/                        # Python package that powers the `ccds` CLI
│   └── hook_utils/              # Hooks that run before/after project generation
├── {{ cookiecutter.repo_name }}/  # The actual project template rendered for users
├── tests/                       # Pytest suite covering the package and template
├── docs/                        # MkDocs site (cookiecutter-data-science.drivendata.org)
├── hooks/                       # Cookiecutter pre/post hooks
├── .github/workflows/           # CI: tests.yml + release.yml
├── pyproject.toml               # Build metadata, black/ruff/isort config
├── dev-requirements.txt         # Dev/test/doc dependencies
├── ccds.json / cookiecutter.json  # Cookiecutter template variables
└── Makefile                     # Convenience targets: requirements, lint, test, docs, dist
```

Most contributions either modify the Python package under `ccds/`, the template under `{{ cookiecutter.repo_name }}/`, or the documentation under `docs/`.

## Running the tests

We use [pytest](https://docs.pytest.org/). The full suite is also run via the `Makefile`:

```bash
# Run the full test suite (fast, local).
make test

# Or run pytest directly for a single file or pattern.
pytest tests/test_cookiecutter.py -x

# Run a single test by name.
pytest tests/ -k "test_module_name"
```

On the CI the tests are run across a matrix of Python 3.9–3.13 and the three major operating systems (Ubuntu, macOS, Windows). Make sure your change passes locally before pushing.

## Code style and quality

We follow the configuration baked into `pyproject.toml`. The project is configured for:

- **[Black](https://black.readthedocs.io/)** — opinionated code formatter, line length 99.
- **[isort](https://pycqa.github.io/isort/)** — import sorter, profile set to `black`.
- **[flake8](https://flake8.pycqa.org/)** — linting (configured in `setup.cfg`).
- **[ruff](https://docs.astral.sh/ruff/)** — fast additional linter (where applicable).

Before opening a PR please run:

```bash
make lint
```

This will format and lint your changes. The CI pipeline will reject PRs that fail the lint job. If you are adding new Python code, please include docstrings in the existing project style and keep functions small and focused.

### Documentation style

User-facing docs live under `docs/` and are rendered with MkDocs. To preview the docs locally:

```bash
make docs
```

The site will be available at `http://127.0.0.1:8000/`.

## Submitting a pull request

1. **Create a topic branch** off `master` with a descriptive name:
   ```bash
   git fetch upstream
   git checkout -b fix/short-descriptive-name upstream/master
   ```
   Branch prefixes we use: `feat/`, `fix/`, `docs/`, `ci/`, `refactor/`, `test/`.

2. **Make your changes.** Keep commits small and atomic. Write commit messages in the imperative mood (`Add CONTRIBUTING.md`, not `Added …`).

3. **Run the test suite and linter** locally before pushing:
   ```bash
   make lint
   make test
   ```

4. **Push to your fork** and open a pull request against `drivendataorg/cookiecutter-data-science:master`.

5. **Fill out the PR template.** Describe what you changed and why. Reference any related issue with `Fixes #123` or `Refs #123` so the issue is auto-closed when the PR merges.

6. **Respond to review feedback.** Push additional commits to the same branch rather than force-pushing during review; this makes it easier for reviewers to see what changed since their last look.

## Reporting bugs

Open an issue on the [issue tracker](https://github.com/drivendataorg/cookiecutter-data-science/issues) using the **Bug report** template. Please include:

- Your CCDS version (`ccds --version` or `pip show cookiecutter-data-science`).
- Your operating system and Python version.
- The exact command you ran and the full output, including any traceback.
- A minimal example that reproduces the problem.

## Suggesting enhancements

For new features or template changes, please open an issue with the **Feature request** template first. Discussing the proposal before implementation helps align on the design and avoids wasted effort. For CCDS, especially consider:

- Will the change be useful for **most** users, or should it be opt-in via a new cookiecutter variable?
- Does it break any existing user's project layout?
- Is it covered by tests?

## Release process

CCDS follows semantic versioning. New versions are cut from `master` and published to PyPI by the maintainers. The `RELEASING.md` document in this repository describes the internal release procedure in detail; you do not need to follow it for a normal contribution.

## License

By contributing to Cookiecutter Data Science, you agree that your contributions will be licensed under the MIT License (see [`LICENSE`](./LICENSE)) — the same license that covers the project. If you are adding a new dependency, please confirm its license is compatible with MIT.

---

Thank you again for contributing. Happy hacking! 🚀
