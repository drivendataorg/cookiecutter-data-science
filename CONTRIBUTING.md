# Contributing

This is a very small project. If you have large Pull Requests to make, I recommend making them over with the upstream at [CookieCutter Data Science (CCDS)](https://github.com/drivendataorg/cookiecutter-data-science). If you have recommendations/changes/particular issues with my implementation, feel free to leave an issue but I'm not sure if I will be able to get around to it.

## Dev Instructions

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

```bash
uv run pytest
```

_Note: Some of the configs require conda to be installed. MiniConda or MiniForge are lightly recommended._
<!-- Conda-forge may be better -->

```bash
brew install --cask miniconda
```


## Contributing to CookieCutter Data Science (CCDS)
> The Cookiecutter Data Science project is opinionated, but not afraid to be wrong. Best practices change, tools evolve, and lessons are learned. **The goal of this project is to make it easier to start, structure, and share an analysis.** [Pull requests](https://github.com/drivendataorg/cookiecutter-data-science/pulls) and [filing issues](https://github.com/drivendataorg/cookiecutter-data-science/issues) is encouraged. We'd love to hear what works for you, and what doesn't.
> 
> If you use the Cookiecutter Data Science project, link back to this page or [give us a holler](https://twitter.com/drivendataorg) and [let us know](mailto:info@drivendata.org)!

<!-- TODO: Perhaps use this: https://cookiecutter.readthedocs.io/en/stable/advanced/human_readable_prompts.html -->