# Jupyter Notebooks Guide

This project has a specific selection of Jupyter notebook extensions and practices which are expanding. Since this is a project for research, this is taken to be as important as the app building prospects of this template.

Jupyter Notebooks are extremely powerful for data exploration, making full websites, and so much more.

### nbdev

[nbdev](https://github.com/AnswerDotAI/nbdev) is a notebook-driven development platform. Simply write notebooks with lightweight markup and get high-quality documentation, tests, continuous integration, and packaging. It's likely the most popular tool of it's type, it's modern yet has a mature ecosystem.

Also solves the git + notebooks problem. Also managed by the fast AI people

Some alternatives include:

**Publishing**

- [Quarto](https://quarto.org/) - Publish reproducible, production quality articles, presentations, dashboards, websites, blogs, and books in HTML, PDF, MS Word, ePub, and more. This is a tool that nbdev actually uses in the background. [Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)
- [Jupyter Book](https://github.com/jupyter-book/jupyter-book) is an open-source tool for building publication-quality books and documents from computational material. It's more of a replacement for Quarto than a replacement for nbdev. After researching this software option, I feel fairly excited about this teams continued development and support of this project. Currently they're in the process of upgrading from version 1 to version 2 with a whole host of stunning features. Jupyter Book v2 is currently in alpha and I would consider working with it once it is fully released.

**Scripting**

`nbdev_export` does this

- [Jupytext](https://jupytext.readthedocs.io/en/latest/) converts notebooks back and forth between python scripts (or Julia or R).
- [nbconvert](<>) pretty sure the same as above but built in, not as fun.

**Parameterizing**

Pretty sure nbdev does NOT do this.

### Jupyter Notebook Extensions

### Notebook Quality Assurance & Linting

See [pre-commit](./pre-commit.md) for more information
