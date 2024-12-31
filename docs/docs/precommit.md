# Pre-commit Hooks Collection


## What is pre-commit and why would I want to use it?
![pre-commit logo](https://avatars.githubusercontent.com/u/6943086?s=280&v=4)

[Pre-commit](https://pre-commit.com/) is a framework for managing and maintaining multi-language pre-commit git hooks, which are essentially pieces of code that are run right before you commit on your local machine and can even prevent you from committing if rules are not met. This is a feature of Git itself, and Pre-commit builds on it, simplifies it, and makes these hooks more reusable. (And despite its name, pre-commit can set up hooks at (any?) stage in the git pipeline, prior to commit tends to be the most common however.)

![Git Hooks](https://d8it4huxumps7.cloudfront.net/uploads/images/652f8091f32cc_git_hooks_06.jpg?d=2000x2000)

These are very easy to set up and there is a large ecosystem of ready-to-go hooks. They're a nice low-code way of maintaining quality and enforcing standards, especially on small, quickly moving projects. They tend to be fast and light-weight as opposed to CI/CD testing with something like [GitHub Actions](https://github.com/features/actions) which might take minutes. It's common to include these same pre-commit tests in GitHub Actions with [pre-commit ci](https://pre-commit.ci/) on top of the more expensive tests.

Pre-commit can be as nitpicky as you want it to be depending on quality-time tradeoff you're making on your project. But it can be helpful for a number of cases, of which might make sense to issue on a commit-level rather than a pull-request level:
1. Linting/formatting code and data files (json, etc.)
2. Re-building code or documentation.
3. Making database migrations
4. Preventing secrets or large files from being committed
5. Requiring commit messages to follow a standard (Like [Commitizen](https://commitizen-tools.github.io/commitizen/))
6. More

It's also nice because you can run a bunch of QA tools your research team doesn't care or know much about without them having to learn the tool.

This page describes the collection of pre-commit hooks selected for this project.

<details>
<summary>
Alternatives (Husky)
</summary>
[Husky](https://typicode.github.io/husky/) is an alternative to pre-commit. My understanding of the differences is that it is mainly geared towards the NodeJS community while pre-commit is multi-language, a bit simpler, a bit more popular, and tends to be the go-to for the Python community, hency why I chose it.
</details>

## Install
The repository should already be configured with a `.pre-commit-config.yaml` file and can be installed with `pre-commit install`. That's basically it, then whenever you commit you should see something like:

![Pre-commit Example](./pre-commit_example.png)

## Hooks

### 01 Security


### 02 Formatting


### 03 Git
