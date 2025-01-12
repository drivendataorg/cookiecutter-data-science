# Pre-commit Hooks Collection

![pre-commit logo](https://avatars.githubusercontent.com/u/6943086?s=280&v=4)

This page explains what pre-commit hooks are, why they are used, and the specific selection I have decided to make for GOTem to keep your projects pristine with every commit. The source config file can be found [here](https://github.com/GatlenCulp/gatlens-opinionated-template/blob/master/.pre-commit-config.yaml).

![Pre-commit Final Result](./pre-commit-final-result.png)
_The final result._

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

<details markdown="1">
<summary>
Alternatives (Husky)
</summary>
[Husky](https://typicode.github.io/husky/) is an alternative to pre-commit that's primarily designed for the NodeJS ecosystem. To my knowledge, while both tools handle Git hooks effectively, pre-commit offers broader multi-language support and has become standard in the Python community.
</details>

## Installation

Projects generated with GOTem come with the `.pre-commit-config.yaml` file already configured as described below. If you would like to create your own, you can follow the instructions [here](https://pre-commit.com/#2-add-a-pre-commit-configuration).

Install the hooks with:

```bash
pre-commit install
```

You'll see hooks run automatically on every commit:
![Pre-commit Example](./pre-commit_example.png)

**Useful Commands:**

```bash
# Test hooks without committing
pre-commit run --all-files

# Commit without running hooks
git commit --no-verify
```

<details markdown="1">
<summary>
Note on security with `pre-commit autoupdate`
</summary>
`pre-commit autoupdate` will bump all of your hook versions to the latest release. Although helpful, use with caution around untrusted hooks since security vulnerabilities or malware can be introduced between versions. This is mostly a non-issue which applies to basically all software but worth mentioning.
</details>

______________________________________________________________________

## Hooks

This collection prioritizes best-in-class tools without redundancy. Rather than using multiple overlapping tools, we've selected the most effective option for each task. For example:

- Python linting uses only Ruff instead of multiple separate linters
- JSON/YAML/TOML validation uses specialized schema validators
- Security scanning uses a single comprehensive tool

All hooks labeled with `# STRICT` are commented out by default and not recommended for every project. (Ex: Code style linters are typically desired for production-grade software but not research.)

## 01 🔒 Security

**[GitLeaks](https://github.com/gitleaks/gitleaks)** is a fast, lightweight scanner that prevents secrets (passwords, API keys, tokens) from being committed to your repository.

<details markdown="1">
<summary>
Alternatives to GitLeaks (TruffleHog)
</summary>
[TruffleHog](https://github.com/trufflesecurity/trufflehog) offers more comprehensive and continuous security scanning across a variety of platforms (not just files). However, it requires more setup time and resources than GitLeaks. Consider TruffleHog for expansive projects with strict security requirements.
</details>

```yaml
- repo: https://github.com/gitleaks/gitleaks
  rev: v8.22.1
  hooks:
    - id: gitleaks
      name: "🔒 security · Detect hardcoded secrets"
```

## 02 🔍 Code Quality

This section covers tools for code formatting, linting, type checking, and schema validation across different languages and file types. Best-in-class tools were chosen, avoiding redundant functionality. I opted for remote hook downloads over local commands to make the file more portable and self-updating.

### 🐍 python

**[Ruff](https://docs.astral.sh/ruff/)** is a fast, comprehensive Python formatter and linter that replaces multiple traditional tools (Black, Flake8, isort, pyupgrade, bandit, pydoclint, mccabe complexity, and more.) While it's not yet at 100% parity with all these tools, its speed and broad coverage make it an excellent choice as the only Python linter/formatter:

- [VSCode extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- While Ruff does many things, type checking it does not... [yet](https://github.com/astral-sh/ruff/issues/3893).

<details markdown="1">
<summary>
Alternatives to Ruff (Too Many to Name)
</summary>

![ruff](https://user-images.githubusercontent.com/1309177/232603514-c95e9b0f-6b31-43de-9a80-9e844173fd6a.svg#only-dark)

Before Ruff, a typical Python project might use several separate tools:

- [Black](https://black.readthedocs.io/) for code formatting
- [isort](https://pycqa.github.io/isort/) for import sorting
- [Flake8](https://flake8.pycqa.org/) for style enforcement
- [Pylint](https://pylint.readthedocs.io/) for code analysis
- [Bandit](https://bandit.readthedocs.io/) for security checks
- [pyupgrade](https://github.com/asottile/pyupgrade) for modernizing syntax
- [pydocstyle](https://www.pydocstyle.org/) for docstring checking
- [Many more... 😵‍💫](https://docs.astral.sh/ruff/faq/#which-tools-does-ruff-replace)

While these tools are battle-tested and highly configurable, using Ruff provides several advantages:

1. **Speed**: Ruff is 10-100x faster as it's written in Rust
1. **Simplicity**: Single configuration file and consistent interface
1. **Active Development**: Rapidly adding features and reaching feature parity
1. **Modern Defaults**: Better handling of new Python features

Consider using individual tools if you need specific features not yet supported by Ruff or have complex existing configurations you need to maintain.

</details>

```yaml
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.9.1
  hooks:
    - id: ruff-format
      name: "🐍 python · Format with Ruff"
    # STRICT
    - id: ruff
      args: [ --fix ]
```

<br/>

**[Microsoft's Pyright](https://microsoft.github.io/pyright/)** handles Python type checking:

- [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=ms-pyright.pyright), but [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), the default extension for Python, has it built-in.
- _This is a community supported pre-commit hook, endorsed by microsoft_

<details markdown="1">
<summary>
Alternatives to Pyright (MyPy)
</summary>
Microsoft's [Pyright](https://microsoft.github.io/pyright/) is a [faster and more featureful](https://github.com/microsoft/pyright/blob/main/docs/mypy-comparison.md) alternative to [MyPy](https://mypy-lang.org/), but MyPy is the original type checker.
</details>

```yaml
# STRICT
- repo: https://github.com/RobertCraigie/pyright-python
  rev: v1.1.391
  hooks:
    - id: pyright
      name: "🐍 python · Check types"
```

<br/>

**[validate-pyproject](https://validate-pyproject.readthedocs.io/)** specifically handles pyproject.toml validation. In the future, I may have check-jsonschema do this as well.

```yaml
- repo: https://github.com/abravalheri/validate-pyproject
  rev: v0.23
  hooks:
    - id: validate-pyproject
      name: "🐍 python · Validate pyproject.toml"
      additional_dependencies: ["validate-pyproject-schema-store[all]"]
```

### 🟨 JavaScript & Web Tools

**[Biome](https://biomejs.dev/internals/language-support/)** is a modern, fast formatter and linter for JS/TS ecosystems (JS[X], TS[X], JSON[C], CSS, GraphQL). It provides better defaults than ESLint.

- [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=biomejs.biome)

<details markdown="1">
<summary>
Alternatives to Biome (ESLint & Prettier)
</summary>
[ESLint](https://eslint.org/) and [Prettier](https://prettier.io/) are more established alternatives with broader plugin ecosystems. While Prettier supports many file types, it can be notably slow, sometimes produces unexpected formatting, and sometimes breaks code (which I find annoying). Since this is primarily a Python-focused project template and Biome handles our JavaScript needs efficiently, we prefer it over the traditional ESLint/Prettier setup. Consider ESLint and Prettier if you need plugins, support for specific JS frameworks, or formatting for languages unsupported elsewhere. (More linters [here](https://github.com/caramelomartins/awesome-linters) as well)
</details>

```yaml
- repo: https://github.com/biomejs/pre-commit
  rev: "v0.6.1"
  hooks:
    - id: biome-check
      name: "🟨 javascript · Lint, format, and safe fixes with Biome"
      additional_dependencies: ["@biomejs/biome@1.9.4"]
```

### ✅ Data & Config Validation

**[check-jsonschema](https://check-jsonschema.readthedocs.io/)** validates various configuration files using [JSON Schema](https://json-schema.org/specification). It supports JSON, YAML, and TOML files, and includes specialized validators like the [TaskFile](https://taskfile.dev/) and [GitHub Actions](https://github.com/features/actions) checker.

- Additional JSON schema available on [Schema Store](https://json.schemastore.org/pyproject.json)
- VSCode [automatically provides intellisense and validation for JSON files with schema](https://code.visualstudio.com/docs/languages/json#_intellisense-and-validation)
- [GitHub Actions VSCode Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions) provides action YAML file intellisense and validation.

```yaml
- repo: https://github.com/python-jsonschema/check-jsonschema
  rev: 0.31.0
  hooks:
    - id: check-github-workflows
      name: "🐙 github-actions · Validate gh workflow files"
      args: ["--verbose"]
    - id: check-taskfile
      name: "✅ taskfile · Validate Task configuration"
```

### 📝 Markdown

**[mdformat](https://mdformat.readthedocs.io/)** for Markdown formatting with additional plugins for GitHub-Flavored Markdown, Ruff-style code formatting, and frontmatter support:

```yaml
- repo: https://github.com/hukkin/mdformat
  rev: 0.7.21
  hooks:
    - id: mdformat
      name: "📝 markdown · Format markdown"
      additional_dependencies:
        - mdformat-gfm          # GitHub-Flavored Markdown support
        - mdformat-ruff         # Python code formatting
        - mdformat-frontmatter  # YAML frontmatter support
        - ruff                  # Required for mdformat-ruff
```

**[Markdownlint](https://github.com/markdownlint/markdownlint/tree/main)** for Markdown linting.

- [VSCode extension](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

```yaml
- repo: https://github.com/markdownlint/markdownlint
    rev: v0.12.0
    hooks:
      - id: markdownlint
        name: "📝 markdown · Lint markdown"
```

### 🐚 Shell

**[ShellCheck](https://www.shellcheck.net/)** lints your shell scripts.

- [VSCode extension](https://marketplace.visualstudio.com/items?itemName=timonwong.shellcheck)

```yaml
# STRICT
- repo: https://github.com/shellcheck-py/shellcheck-py
  rev: v0.10.0.1
  hooks:
    - id: shellcheck
      name: "🐚 shell · Lint shell scripts"
```

**[bashate](https://github.com/openstack/bashate)** checks your shell script code style.

```yaml
# STRICT
- repo: https://github.com/openstack/bashate
  rev: 2.1.1
  hooks:
    - id: bashate
      name: "🐚 shell · Check shell script code style"
```

### 🐮 Makefile

**[Checkmake](https://github.com/mrtazz/checkmake)** for linting your Makefile.

```yaml
- repo: https://github.com/mrtazz/checkmake.git
  rev: 0.2.2
  hooks:
    - id: checkmake
      name: "🐮 Makefile · Lint Makefile"
```

### 📊 SQL Code

**[SQLFluff](https://docs.sqlfluff.com/en/stable/production/pre_commit.html)** can be used to lint and attempt to auto-fix any of your `*.sql` files automatically.

```yaml
- repo: https://github.com/sqlfluff/sqlfluff
  rev: 3.3.0
  hooks:
    - id: sqlfluff-fix
      name: "📊 SQL · Attempts to fix rule violations."
    # STRICT
    - id: sqlfluff-lint
      name: "📊 SQL · Lint SQL code files"
```

### 📓 Notebooks

**[nbQA](https://nbqa.readthedocs.io/)** for Jupyter notebook quality assurance, allowing us to use our standard Python tools on notebooks.

<details markdown="1">
<summary>
ruff supports notebooks by default
</summary>
[Ruff has built-in support for Jupyter Notebooks](https://docs.astral.sh/ruff/configuration/#jupyter-notebook-discovery), so this has been excluded from nbQA since it would be redundant. nbQA has `nbqa-ruff-format` and `nbqa-ruff-check` hooks, but these appear to be redundant.
</details>

```yaml
- repo: https://github.com/nbQA-dev/nbQA
  rev: 1.9.1
  hooks:
    - id: nbqa
      entry: nbqa mdformat
      name: "📓 notebook · Format markdown cells"
      args: ["--nbqa-md"]
      types: [jupyter]
      additional_dependencies:
        - mdformat
        - mdformat-gfm
        - mdformat-ruff
        - mdformat-frontmatter
        - ruff
    # STRICT
    # TODO: Convert to pyright
    - id: nbqa-mypy
      name: "📓 notebook · Type-check cells"
```

### 🖼️ Image Optimization

**[oxipng](https://github.com/shssoichiro/oxipng)** is a PNG optimizer written in Rust with lossy and lossless options. (The selection of arguments below are slightly lossy):

```yaml
- repo: https://github.com/shssoichiro/oxipng
  rev: v9.1.3
  hooks:
    - id: oxipng
      name: "🖼️ images · Optimize PNG files"
      args: [
        "-o", "4",
        "--strip", "safe",
        "--alpha"
      ]
```

### ✨ Additional File Types

**[Prettier](https://prettier.io/) (HTML, YAML, CSS)** handles formatting for various file types not covered by other tools. While it can be slow, sometimes produces code-breaking formatting, and I personally dislike it - it remains the standard for these file types.

- [VSCode extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

<details markdown="1">
<summary>
Future Improvements
</summary>

I might replace Prettier with more focused tools in the future (Perhaps [HTMLHint](https://htmlhint.com/) for HTML validation but it's hardly a linter.)

However, this would require managing multiple tools and dependencies, so I'm sticking with Prettier for now.

_My disatisfaction with prettier is humorously shared by pre-commit, as they [themselves no longer support the prettier hook](https://github.com/pre-commit/mirrors-prettier#archived) because "prettier made some changes that breaks plugins entirely"_

</details>

```yaml
- repo: https://github.com/pre-commit/mirrors-prettier
  rev: v4.0.0-alpha.8
  hooks:
    - id: prettier
      name: "✨ misc-files · Format misc web files"
      types_or: [yaml, html, scss]
      additional_dependencies:
        - prettier@3.4.2
```

## 03 📁 Filesystem

**[Pre-commit hooks](https://github.com/pre-commit/pre-commit-hooks)** are collection of hooks managed by the pre-commit team. These hooks help maintain repository hygiene by preventing common file-related issues:

- `check-case-conflict` - Prevents issues on case-insensitive filesystems (Windows/MacOS)
- `check-symlinks` & `destroyed-symlinks` - Maintains symlink integrity
- `check-executables-have-shebangs` - Ensures scripts are properly configured
- `check-illegal-windows-names` - Check for files that cannot be created on Windows.

```yaml
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v5.0.0
  hooks:
    - id: check-executables-have-shebangs
      name: "📁 filesystem/⚙️ exec · Verify shebang presence"
    - id: check-shebang-scripts-are-executable
      name: "📁 filesystem/⚙️ exec · Verify script permissions"
    - id: check-case-conflict
      name: "📁 filesystem/📝 names · Check case sensitivity"
    - id: check-illegal-windows-names
      name: "📁 filesystem/📝 names · Validate Windows filenames"
    - id: check-symlinks
      name: "📁 filesystem/🔗 symlink · Check symlink validity"
    - id: destroyed-symlinks
      name: "📁 filesystem/🔗 symlink · Detect broken symlinks"
    # ... More Below ...
```

## 04 🌳 Git Quality

### 🪵 Repo Constraints

**[Pre-commit hooks](https://github.com/pre-commit/pre-commit-hooks)** again, this time for branch protection restricting unwanted actions.

- `forbid-new-submodules` - Prevent addition of new git submodules (repo-in-a-repo). (Imo, Git submodules are a perfectly find practice, but
- `check-merge-conflict` - Prevents committing unresolved merge conflicts
- `no-commit-to-branch` - Protects main branches from direct commits (GitHub branch protections are for enterprise members only (sad))
- `check-added-large-files` - Prevents committing files larger than 5000KB ([Git Large File Storage (LFS)](https://git-lfs.com/) or [Data Version Control (DVC)](https://dvc.org/) should instead be used)

```yaml
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v5.0.0
  hooks:
    # ... More Above ...
    - id: check-merge-conflict
      name: "🌳 git · Detect conflict markers"
    - id: forbid-new-submodules
      name: "🌳 git · Prevent submodule creation"
    - id: no-commit-to-branch
      name: "🌳 git · Protect main branches"
      args: ["--branch", "main", "--branch", "master"]
    - id: check-added-large-files
      name: "🌳 git · Block large file commits"
      args: ['--maxkb=5000']
      
```

### 🗒️ Commit Message Standards

**[Commitizen](https://commitizen.github.io/cz-cli/)** enforces high-quality standardized commit messages that enable automatic changelog generation and semantic versioning

<details markdown="1">
<summary>
Accompanying Improved Git Commit Interface
</summary>

Commitizen comes with a built-in and customizable CLI that will walk you through making one of these standard commits. If you're using GOTem, this is preinstalled and you can run `cz commit` instead of `git commit`.

_As an alternative to commitizen, there is also [`czg`](https://cz-git.qbb.sh/) (`cz-git` improved) which has a great implementation of AI-generated commits. However, it's [extremely painful to configure outside of non-javascript projects](https://github.com/Zhengqbbb/cz-git/issues/213) whereas [commitizen is more mature in this area.](https://commitizen-tools.github.io/commitizen/customization/)_

![czg interface](https://user-images.githubusercontent.com/40693636/175753060-cf4f5e48-100d-430a-93e9-31b17f42802f.gif)

</details>

<details markdown="1">
<summary>
Alternatives to Commitizen (Commitlint)
</summary>

[commitlint](https://github.com/conventional-changelog/commitlint) is a similar project to commitizen. Many articles claim that the difference between the two are that commitizen is more of a tool to generate these fancy commits while commitlint is meant to lint the commits. However, considering `cz check` is a thing, I'm confused what the difference is. The tools can be used together. Seems like commitizen has better python support than commitlint. Projects equally popular. More research to be done on the differences!

</details>

- Pre-commit only installs hooks in the `pre-commit` git stage by default. This hook operates on the `commit-msg` stage, and thus you need to include this stage in `default_install_hook_types` as done below.

- **[cz-conventional-gitmoji](https://github.com/ljnsn/cz-conventional-gitmoji)** is [a commitizen preset](https://commitizen-tools.github.io/commitizen/third-party-commitizen/) combining [gitmoji](https://gitmoji.dev/) and [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/).

<details markdown="1">
<summary>
Click to learn how to remove **cz-conventional-gitmoji**
</summary>

Remove the name line from `pyproject.toml` which sets `cz_gitmoji` as the default for commitizen (confusingly, this is the name for cz-conventional-gitmoji)

```toml
# pyproject.toml
[tool.commitizen]
name = "cz_gitmoji"
```

And remove it as dependency from your hooks:

```yaml
# .pre-commit-config.yaml
default_install_hook_types:
  - pre-commit
  - commit-msg
repos:
# ... other hooks ...
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v4.1.0
    hooks:
      - id: commitizen
        name: "🌳 git · Validate commit message"
        stages: [commit-msg]
        # DELETE LINE BELOW
        additional_dependencies: [cz-conventional-gitmoji]
```

</details>

```yaml
default_install_hook_types:
  - pre-commit
  - commit-msg
repos:
# ... other hooks ...
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v4.1.0
    hooks:
      - id: commitizen
        name: "🌳 git · Validate commit message"
        stages: [commit-msg]
        additional_dependencies: [cz-conventional-gitmoji]
```

## 05 🧪 Fast Tests (Local)

While extensive tests may be too time consuming for a pre-commit hook, it can be helpful to run fast local tests to detect unexpected failures in your code before you are 10 commits in and unsure which one broke your code.

The example below uses `pytest`. The first hook checks that the tests don't contain any syntax errors and can be successfully collected. This should always pass.

The second hook runs all fast pytests using my custom pytest option which leverages the pytest-timeout feature you can read about [here](https://gatlenculp.github.io/gatlens-opinionated-template/pytest-customization/)

```yaml
- repo: local
  hooks:
    - id: pytest-collect
      name: 🧪 test · Validate test formatting
      entry: ./.venv/bin/pytest tests
      language: system
      types: [python]
      args: ["--collect-only"]
      pass_filenames: false
    # STRICT
    - id: pytest-fast
      name: 🧪 test · Run fast tests
      entry: ./.venv/bin/pytest tests
      language: system
      types: [python]
      args: ["--max-timeout=3"]
      pass_filenames: false
```

<!-- Also maybe add profiling? -->

## Conclusion

This is by no means an exhaustive list of great hooks. Your encouraged to pick-and-choose as desired. Hooks don't exist for all tools, so if you want to run those you can always use a local hook:

```yaml
- repo: local
  hooks:
    - id: make-lint
      name: Run 'make lint'
      entry: make
      args: ["lint"]
      language: system
```

Check below for even more wonderful pre-commit hooks!

<details markdown="1">

<summary>
View final `.pre-commit-config.yaml` file
</summary>

```yaml
exclude: |
  (?x)^(
      .*\{\{.*\}\}.*|     # Exclude any files with cookiecutter variables
      docs/site/.*|       # Exclude mkdocs compiled files
      \.history/.*|       # Exclude history files
      .*cache.*/.*|       # Exclude cache directories
      .*venv.*/.*|        # Exclude virtual environment directories
  )$
fail_fast: true
default_language_version:
  python: python3.12
default_install_hook_types:
  - pre-commit
  - commit-msg
repos:
  #
  # Documentation Here:
  # https://gatlenculp.github.io/gatlens-opinionated-template/precommit/
  #
  # ---------------------------------------------------------------------------- #
  #                              🔄 Pre-Commit Hooks                             #
  # ---------------------------------------------------------------------------- #

  # ----------------------------- 🔒 Security Tools ---------------------------- #

  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.22.1
    hooks:
      - id: gitleaks
        name: "🔒 security · Detect hardcoded secrets"

  # --------------------------- 🔍 Code Quality Tools -------------------------- #

  ### Python Tools ###
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.1
    hooks:
      - id: ruff-format
        name: "🐍 python · Format with Ruff"
      # STRICT
      # - id: ruff
      #   args: [--fix]

  # STRICT
  # - repo: https://github.com/RobertCraigie/pyright-python
  #   rev: v1.1.391
  #   hooks:
  #     - id: pyright
  #       name: "🐍 python · Check types"

  - repo: https://github.com/abravalheri/validate-pyproject
    rev: v0.23
    hooks:
      - id: validate-pyproject
        name: "🐍 python · Validate pyproject.toml"
        additional_dependencies: ["validate-pyproject-schema-store[all]"]

  ### Javascript & Web Tools ###
  - repo: https://github.com/biomejs/pre-commit
    rev: "v0.6.1"
    hooks:
      - id: biome-check
        name: "🟨 javascript · Lint, format, and safe fixes with Biome"
        additional_dependencies: ["@biomejs/biome@1.9.4"]

  ### Data & Config Validation ###
  - repo: https://github.com/python-jsonschema/check-jsonschema
    rev: 0.31.0
    hooks:
      - id: check-github-workflows
        name: "🐙 github-actions · Validate gh workflow files"
        args: ["--verbose"]
      - id: check-taskfile
        name: "✅ taskfile · Validate Task configuration"

  ### Markdown ###
  - repo: https://github.com/hukkin/mdformat
    rev: 0.7.21
    hooks:
      - id: mdformat
        name: "📝 markdown · Format markdown"
        additional_dependencies:
          - mdformat-gfm
          - mdformat-ruff
          - mdformat-frontmatter
          - ruff

  # STRICT
  # - repo: https://github.com/markdownlint/markdownlint
  #   rev: v0.12.0
  #   hooks:
  #     - id: markdownlint
  #       name: "📝 markdown · Lint markdown"

  ### Shell ###

  # STRICT
  # - repo: https://github.com/shellcheck-py/shellcheck-py
  #   rev: v0.10.0.1
  #   hooks:
  #     - id: shellcheck
  #       name: "🐚 shell · Lint shell scripts"

  # STRICT
  # - repo: https://github.com/openstack/bashate
  #   rev: 2.1.1
  #   hooks:
  #     - id: bashate
  #       name: "🐚 shell · Check shell script code style"

  ### Makefile ###
  - repo: https://github.com/mrtazz/checkmake.git
    rev: 0.2.2
    hooks:
      - id: checkmake
        name: "🐮 Makefile · Lint Makefile"

  ### SQL ###

  - repo: https://github.com/sqlfluff/sqlfluff
    rev: 3.3.0
    hooks:
      - id: sqlfluff-fix
        name: "📊 SQL · Attempts to fix rule violations."
      # STRICT
      # - id: sqlfluff-lint
      #   name: "📊 SQL · Lint SQL code files"

  ### Notebooks ###
  - repo: https://github.com/nbQA-dev/nbQA
    rev: 1.9.1
    hooks:
      - id: nbqa
        entry: nbqa mdformat
        name: "📓 notebook · Format markdown cells"
        args: ["--nbqa-md"]
        types: [jupyter]
        additional_dependencies:
          - mdformat
          - mdformat-gfm
          - mdformat-ruff
          - mdformat-frontmatter
          - ruff
      # STRICT
      # TODO: Convert to pyright
      - id: nbqa-mypy
        name: "📓 notebook · Type-check cells"

  ### PNG Images ###
  - repo: https://github.com/shssoichiro/oxipng
    rev: v9.1.3
    hooks:
      - id: oxipng
        name: "🖼️ images · Optimize PNG files"
        args: ["-o", "4", "--strip", "safe", "--alpha"]

  ### Additional File Types ###
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v4.0.0-alpha.8
    hooks:
      - id: prettier
        name: "✨ misc-files · Format misc web files"
        types_or: [yaml, html, scss]
        additional_dependencies:
          - prettier@3.4.2

  # ---------------------------- 📁 Filesystem Tools --------------------------- #

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      # Filesystem Checks
      - id: check-executables-have-shebangs
        name: "📁 filesystem/⚙️ exec · Verify shebang presence"
      - id: check-shebang-scripts-are-executable
        name: "📁 filesystem/⚙️ exec · Verify script permissions"
      - id: check-case-conflict
        name: "📁 filesystem/📝 names · Check case sensitivity"
      - id: check-illegal-windows-names
        name: "📁 filesystem/📝 names · Validate Windows filenames"
      - id: check-symlinks
        name: "📁 filesystem/🔗 symlink · Check symlink validity"
      - id: destroyed-symlinks
        name: "📁 filesystem/🔗 symlink · Detect broken symlinks"
      # ------------------------------- 🌳 Git Tools ------------------------------- #
      - id: check-merge-conflict
        name: "🌳 git · Detect conflict markers"
      - id: forbid-new-submodules
        name: "🌳 git · Prevent submodule creation"
      - id: no-commit-to-branch
        name: "🌳 git · Protect main branches"
        args: ["--branch", "main", "--branch", "master"]
      - id: check-added-large-files
        name: "🌳 git · Block large file commits"
        args: ["--maxkb=5000"]

  # ---------------------------------------------------------------------------- #
  #                            📝 Commit Message Hooks                           #
  # ---------------------------------------------------------------------------- #
  #
  # --------------------------- ✍️ Git Commit Quality -------------------------- #

  ### Commit Message Standards ###
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v4.1.0
    hooks:
      - id: commitizen
        name: "🌳 git · Validate commit message"
        stages: [commit-msg]
        additional_dependencies: [cz-conventional-gitmoji]

  # ---------------------------------------------------------------------------- #
  #                             🧪 Fast Tests (Local)                            #
  # ---------------------------------------------------------------------------- #

  - repo: local
    hooks:
      - id: pytest-collect
        name: 🧪 test · Validate test formatting
        entry: ./.venv/bin/pytest tests
        language: system
        types: [python]
        args: ["--collect-only"]
        pass_filenames: false
      # STRICT
      - id: pytest-fast
        name: 🧪 test · Run fast tests
        entry: ./.venv/bin/pytest tests
        language: system
        types: [python]
        args: ["--max-timeout=3"]
        pass_filenames: false
```

</details>

### Other hooks to consider

Here are some other hooks I haven't added but would consider adding!

**Individual Hooks**

- [buildbuf](https://github.com/bufbuild/buf) - Protobuf Linter
- [Clang](https://github.com/pre-commit/mirrors-clang-format) - C++ linter
- [gitlint](https://github.com/jorisroovers/gitlint) - Alternative to commitlint, may actually be preferred.
- [typos](https://github.com/crate-ci/typos) or [codespell](https://github.com/codespell-project/codespell) - Finds common misspellings in code and documentation. One blog post preferred Typos over codespell because it found more typos (and apparently has VSCode support?)
- [yamllint](https://github.com/adrienverge/yamllint) - YAML linter
- [yamlfmt](https://github.com/google/yamlfmt) - YAML formatter by Google
- [actionlint](https://github.com/rhysd/actionlint) - Lints github action files, may be a better checker than the currently selected one.
- [uv pre-commits](https://github.com/astral-sh/uv-pre-commit) - A collection of pre-commits for [uv](https://docs.astral.sh/uv/) by Astral
- [Vulture](https://github.com/jendrikseipp/vulture) or [Deadcode](https://github.com/albertas/deadcode) - Detect unused code in Python
- [sync-pre-commit-deps](https://github.com/mxr/sync-pre-commit-deps) - Sync pre-commit hook dependencies based on other installed hooks (to avoid installing multiple versions I assume).

<details markdown="1">
<summary>
sync-pre-commit-deps hook here
</summary>

```yaml
  - repo: https://github.com/mxr/sync-pre-commit-deps
    rev: v0.0.2
    hooks:
      - id: sync-pre-commit-deps
        name: "🪝 pre-commit · Sync hook dependencies based on other hooks"
```

</details>

<br/>

**Hook lists**

- [featured hooks](https://pre-commit.com/hooks.html) by the pre-commit team
- [first-party hooks](https://github.com/pre-commit/pre-commit-hooks) by the pre-commit team (some used in this guide).
- [Megalinter's Supported Linters](https://megalinter.io/latest/supported-linters/) - Not all of these may provide pre-commits but regardless it's a great collection of QA tools!
- (More but you'll have to find them yourself :P)

<br/>

**What's Missing?**

- File optimizers for more than just PNGs (JPG, GIF, etc.)
- Profanity checker (You'll be surprised with the amount of profanity on repos you're about to make public). This can [possibly be done with GitLeaks](https://blog.nashtechglobal.com/profanity-check-source-code-with-gitleaks-why-not/)
- ... This list could go on and on ...

**Ensemble Hooks (Linters, Formatters, etc.)**

I went a bit overboard with cherry picking my favorite formatters, linters, etc. This may lead to maintaining more hooks than is worthwhile. It's on my todo list to look at ensemble linters and formatters such as [Megalinter](https://github.com/oxsecurity/megalinter/tree/main) and [Superlinter](https://github.com/super-linter/super-linter) which would GREATLY reduce the amount of overhead for code QA and provide support to languages without hunting down mutliple hooks for each of them. These also have the added benefit of better integration to other CI/CD tools, pre-built container images, and security scanning.

> 🦙 MegaLinter analyzes 50 languages, 22 formats, 21 tooling formats, excessive copy-pastes, spelling mistakes and security issues in your repository sources with a GitHub Action, other CI tools or locally.

I'm slightly concerned that these ensemble linters might be an additional annoying piece of software to learn and configure that sets off small teams from using them entirely. Additionally, this software may not support your favorite linters - some of which mentioned in this guide include Biomejs and mdformat. I'm sure the list of available tools is extendable although I'm unsure how much effort is needed to do so.

<!-- TODO: Read this, https://kislyuk.github.io/argcomplete/ -->
