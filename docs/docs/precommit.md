# Pre-commit Hooks Collection

![pre-commit logo](https://avatars.githubusercontent.com/u/6943086?s=280&v=4)

## What are Git hooks?

[Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) are scripts that run automatically at some stage in the git-lifecycle. Most commonly, pre-commit hooks are used, running before a commit goes through. They act as a first line of defense for code quality by:

- Catching formatting issues
- Finding potential security risks
- Validating configurations
- Running quick tests
- Enforcing team standards

## Why use pre-commit?

[Pre-commit](https://pre-commit.com/) is a framework that makes these Git hooks:

1. **Easy to share** - Hooks are defined in a single YAML file
1. **Language-agnostic** - Works with Python, JavaScript, and more
1. **Fast** - Only runs on staged files and are much quicker than CI/CD
1. **Forgettable** - Team members don't need to memorize QA tools; hooks run automatically
1. **Extendable** - Large ecosystem of ready-to-use hooks

Pre-commit helps maintain code quality without slowing down development. While CI/CD pipelines might take minutes to run, pre-commit hooks provide instant feedback right when you commit. Despite the name, Pre-commit can install hooks at any stage (ex: Use a pre-push hook as a slightly more time-intensive pre-commit and push multiple commits at once.)

**Common Use Cases**

Pre-commit can be as strict as you want depending on your project's quality-time tradeoff. Here are cases where commit-level checks make more sense than pull-request level:

1. Linting/formatting code and data files
1. Re-building code or documentation
1. Making database migrations
1. Preventing secrets or large files from being committed
1. Requiring commit messages to follow a standard (Like [Commitizen](https://commitizen-tools.github.io/commitizen/))
1. Running fast tests

<details>
<summary>
Alternatives (Husky)
</summary>
[Husky](https://typicode.github.io/husky/) is an alternative to pre-commit that's primarily designed for the NodeJS ecosystem. To my knowledge, while both tools handle Git hooks effectively, pre-commit offers broader multi-language support and has become standard in the Python community.
</details>

## Installation

1. The repository comes with a `.pre-commit-config.yaml` file already configured
1. Install the hooks with:

```bash
pre-commit install
```

You'll see hooks run automatically on every commit:
![Pre-commit Example](./pre-commit_example.png)

**Useful Commands:**

```bash
# Update hooks to their latest versions
pre-commit autoupdate

# Reinstall hooks (needed after config changes)
pre-commit install

# Test hooks without committing
pre-commit run --all-files
```

## Hooks

This collection prioritizes best-in-class tools without redundancy. Rather than using multiple overlapping tools, we've selected the most effective option for each task. For example:

- Python linting uses only Ruff instead of multiple separate linters
- JSON/YAML/TOML validation uses specialized schema validators
- Security scanning uses a single comprehensive tool

### 01 Security

[GitLeaks](https://github.com/gitleaks/gitleaks) is a fast, lightweight scanner that prevents secrets (passwords, API keys, tokens) from being committed to your repository.

```yaml
- repo: https://github.com/gitleaks/gitleaks
  rev: v8.22.0
  hooks:
    - id: gitleaks
```

<details>
<summary>
Alternatives to GitLeaks (TruffleHog)
</summary>
[TruffleHog](https://github.com/trufflesecurity/trufflehog) offers more comprehensive and continuous security scanning across a variety of platforms (not just files). However, it requires more setup time and resources than GitLeaks. Consider TruffleHog for expansive projects with strict security requirements.
</details>

<!-- TODO: Read this, https://kislyuk.github.io/argcomplete/ -->

### 02 Code Quality & Formatting

This section covers tools for code formatting, linting, type checking, and schema validation across different languages and file types. Best-in-class tools were chosen, avoiding redundant functionality. I opted for remote hook downloads over local commands to make the file more portable and self-updating.

#### Python Tools

[Ruff](https://docs.astral.sh/ruff/) is a fast, comprehensive Python formatter and linter that replaces multiple traditional tools (Black, Flake8, isort, pyupgrade, bandit, pydoclint, mccabe complexity, and more.) While it's not yet at 100% parity with all these tools, its speed and broad coverage make it an excellent choice as this project's only Python linter/formatter:

```yaml
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.8.4
  hooks:
    - id: ruff
      args: [ --fix ]
    - id: ruff-format
```

[MyPy](https://mypy-lang.org/) handles Python type checking:

```yaml
- repo: https://github.com/pre-commit/mirrors-mypy
  hooks:
    - id: mypy
```

<details>
<summary>
Alternatives to MyPy (Pyright)
</summary>
Microsoft's [Pyright](https://microsoft.github.io/pyright/) is a [faster and more featureful](https://github.com/microsoft/pyright/blob/main/docs/mypy-comparison.md) alternative to MyPy. While it's the preferred choice for type checking, there isn't currently a maintained pre-commit hook available. Consider using Pyright through its [Git hook](https://github.com/microsoft/pyright/blob/main/docs/ci-integration.md) or as a local tool until a pre-commit hook is developed.
</details>

<!-- TODO: Add vulture https://github.com/jendrikseipp/vulture -->

#### JavaScript & Web Tools

[Biome](https://biomejs.dev/internals/language-support/) is a modern, fast formatter and linter for JS/TS ecosystems (JS[X], TS[X], JSON[C], CSS, GraphQL). It provides better defaults than ESLint and comes with a helpful [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=biomejs.biome):

```yaml
- repo: https://github.com/biomejs/pre-commit
  rev: "1.4.1"
  hooks:
    - id: biome-ci
    additional_dependencies: ["@biomejs/biome@1.4.1"]
```

<details>
<summary>
Alternatives to Biome (ESLint & Prettier)
</summary>
[ESLint](https://eslint.org/) and [Prettier](https://prettier.io/) are more established alternatives with broader plugin ecosystems. While Prettier supports many file types, it can be notably slow, sometimes produces unexpected formatting, and sometimes breaks code (which I find annoying). Since this is primarily a Python-focused project template and Biome handles our JavaScript needs efficiently, we prefer it over the traditional ESLint/Prettier setup. Consider ESLint and Prettier if you need plugins, support for specific JS frameworks, or formatting for languages unsupported elsewhere. (More linters [here](https://github.com/caramelomartins/awesome-linters) as well)
</details>

#### Data & Config Validation

[check-jsonschema](https://check-jsonschema.readthedocs.io/) validates various configuration files using [JSON Schema](https://json-schema.org/specification). It supports JSON, YAML, and TOML files, and includes specialized validators like the [TaskFile](https://taskfile.dev/) and [GitHub Actions](https://github.com/features/actions) checker:

```yaml
- repo: https://github.com/python-jsonschema/check-jsonschema
  rev: 0.30.0
  hooks:
    - id: check-github-workflows
      args: ["--verbose"]
    - id: check-taskfile
```

_Additional json schema available on the [Schema Store](https://json.schemastore.org/pyproject.json)_

[validate-pyproject](https://validate-pyproject.readthedocs.io/) specifically handles pyproject.toml validation. In the future, I may have check-jsonschema do this as well.

```yaml
- repo: https://github.com/abravalheri/validate-pyproject
  rev: v0.23
  hooks:
    - id: validate-pyproject
    additional_dependencies: ["validate-pyproject-schema-store[all]"]
```

<!-- Possibly worth just building? -->

#### Markdown

[mdformat](https://mdformat.readthedocs.io/) for Markdown formatting:

```yaml
- repo: https://github.com/hukkin/mdformat
  rev: 0.7.21
  hooks:
  - id: mdformat
    additional_dependencies:
    - mdformat-gfm
    - mdformat-black
```

#### Notebooks

[nbQA](https://nbqa.readthedocs.io/) for Jupyter notebook quality assurance, allowing us to use our standard Python tools on notebooks:

```yaml
- repo: https://github.com/nbQA-dev/nbQA
  rev: 1.9.1
  hooks:
    - id: nbqa-mypy
    - id: nbqa
      entry: nbqa mdformat
      name: Run 'mdformat' on a Jupyter Notebook
      types: [jupyter]
```

<details>
<summary>
ruff supports notebooks by default
</summary>
As of version x.x.x, [ruff has built-in support for Jupyter Notebooks](https://docs.astral.sh/ruff/configuration/#jupyter-notebook-discovery), so this has been excluded from nbQA. Although they do have `nbqa-ruff-format` and `nbqa-ruff-check` available as hooks, these appear to be redundant.
</details>

#### Additional File Types

[Prettier](https://prettier.io/) handles formatting for various file types not covered by other tools (HTML, CSS, YAML, etc.). While it can be slow and sometimes produces unexpected formatting, it remains the standard for these file types:

```yaml
- repo: https://github.com/pre-commit/mirrors-prettier
  rev: v3.1.0
  hooks:
    - id: prettier
      types_or: [yaml, markdown, html, css, scss, javascript, json]
      # Exclude files handled by other formatters
      exclude: |
        (?x)^(
            .*\.md$|
            .*\.ipynb$|
            .*\.py$|
            .*\.tsx?$
        )$
      additional_dependencies:
        - prettier@3.1.0
```

<details>
<summary>
Future Improvements
</summary>
I might replace Prettier with more focused tools in the future (Perhaps [HTMLHint](https://htmlhint.com/) for HTML validation but it's hardly a linter.)

However, this would require managing multiple tools and dependencies, so I'm sticking with Prettier for now.

</details>

#### Local Tools

For using tools without hooks, you can also run a local command:

```yaml
- repo: local
  hooks:
    - id: make-lint
      name: Run 'make lint'
      entry: make
      args: ["lint"]
      language: system
```

Note: If you're using [uv](https://docs.astral.sh/uv/), they [also have pre-commits](https://github.com/astral-sh/uv-pre-commit) available.

<!-- CZ git https://cz-git.qbb.sh/cli/why -->

### 03 Project and Files

These hooks help maintain repository hygiene by preventing common file-related issues:

```yaml
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.5.0
  hooks:
    - id: check-added-large-files
      args: ['--maxkb=8000']
    - id: check-case-conflict
    - id: check-symlinks
    - id: destroyed-symlinks
    - id: check-executables-have-shebangs
    - id: check-shebang-scripts-are-executable
```

- `check-added-large-files` - Prevents committing files larger than 8000KB ([Git Large File Storage (LFS)](https://git-lfs.com/) or [Data Version Control (DVC)](https://dvc.org/) should instead be used)
- `check-case-conflict` - Prevents issues on case-insensitive filesystems (Windows/MacOS)
- `check-symlinks` & `destroyed-symlinks` - Maintains symlink integrity
- `check-executables-have-shebangs` - Ensures scripts are properly configured
- `check-illegal-windows-names` - Check for files that cannot be created on Windows.

### 04 Git Commit Quality

#### Commit Message Standards

[Commitizen](https://commitizen.github.io/cz-cli/) enforces standardized commit messages that enable automatic changelog generation and semantic versioning

Additionally, I add [cz-conventional-gitmoji](https://github.com/ljnsn/cz-conventional-gitmoji), a third-party prompt template that combines the [gitmoji](https://gitmoji.dev/) and [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) standards. (More templates [here](https://commitizen-tools.github.io/commitizen/third-party-commitizen/))

```yaml
- repo: https://github.com/ljnsn/cz-conventional-gitmoji
    rev: 0.2.4
    hooks:
      - id: conventional-gitmoji
- repo: https://github.com/commitizen-tools/commitizen
  rev: v3.18.4
  hooks:
    - id: commitizen
      stages: [commit-msg]
      additional_dependencies: [cz-conventional-gitmoji]
    - id: commitizen-branch
      stages: [pre-push]
      args: [
        "--rev-range", "origin/main..", 
        "--strict"
      ]
      additional_dependencies: [cz-conventional-gitmoji]
```

<details>
<summary>
Alternatives to Commitizen (Commitlint)
</summary>
[commitlint](https://github.com/conventional-changelog/commitlint) is a similar project to commitizen. Many articles claim that the difference between the two are that commitizen is more of a tool to generate these fancy commits while commitlint is meant to lint the commits. However, considering `cz check` is a thing, I'm confused what the difference is. The tools can be used together. Seems like commitizen has better python support than commitlint. Projects equally popular. More research to be done on the differences!
</details>
<!-- TODO: Look into the differences above. Oop. -->

<!-- TODO: Also look into running pre-commit before cz even pops up, it's annoying to write things and then have it fail the pre-commit and have to rewrite. -->

For the best experience:

1. Use `cz commit` instead of `git commit`
1. Consider [czg](https://cz-git.qbb.sh/) for a better implementation of the `cz` cli

#### Branch Protection

```yaml
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.5.0
  hooks:
    - id: forbid-new-submodules
    - id: check-merge-conflict
    - id: no-commit-to-branch
      args: ['--branch', 'main', '--branch', 'master']
```

- `forbid-new-submodules` - Prevent addition of new git submodules. (I'm mixed on this one since I think this is a confusing paradigm but don't know of better alternatives.)
- `check-merge-conflict` - Prevents committing unresolved merge conflicts
- `no-commit-to-branch` - Protects main branches from direct commits (GitHub branch protections are for enterprise members only (sad))

### 05 Testing

```yaml
# TODO After completing `tests/`
# - repo: local
#   hooks:
#     - id: fast-tests
#       name: Run Fast Tests
#       entry: pytest
#       language: system
#       types: [python]
#       args: [
#         "tests/unit",  # Only run unit tests
#         "-m", "not slow",  # Skip slow-marked tests
#         "--quiet"
#       ]
#       pass_filenames: false
```

<!-- Also maybe add profiling? -->

Some inspo from [this article](https://medium.com/marvelous-mlops/welcome-to-pre-commit-heaven-5b622bb8ebce)
