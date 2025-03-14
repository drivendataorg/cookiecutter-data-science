## 0.4.5 (2025-03-14)

### Fix

- Return the images back to the repo

## 0.4.4 (2025-03-14)

### Fix

- add tag_format to commitizen config

## 0.4.3 (2025-02-03)

### Fix

- **mkdocs**: Temporarily disabled termynal generation to get docs to render
- update README for consistent cookiecutter placeholder syntax

## 0.4.1 (2025-01-29)

### Fix

- **docs**: Updated reference in jupyter-notebooks.md file to new pre-commit.md file
- **github-actions**: Fixed pull_request_template.md being upper case now so that tests pass part 2
- **github-actions**: Fixed pull_request_template.md being upper case now so that tests pass

## 0.4.0 (2025-01-29)

### Feat

- **citation**: Add template citation to template for research papers

## 0.3.0 (2025-01-22)

### Feat

- enhance SSH config with conditional host entries
- add SSH setup instructions and remote server config examples
- clarify SSH key naming conventions and update comments
- **cookiecutter-hooks**: Added skeleton code for future SSH implementation
- add SSH key generation stubs, update config and post-gen script

## 0.2.0 (2025-01-20)

### Feate

- update Dockerfile to use dynamic GitHub username for label
- add VSCode configs for extensions, debugging, and settings
- enhance commitlint with scopes and commitizen customization

### Refactor

- remove unused author name variable and update file references
- **tests**: Update issue template filenames and add new documentation files for CODE_OF_CONDUCT, CONTRIBUTING, and SECURITY

## 0.1.0 (2025-01-11)

### chore

- update pre-commit config to always run specified hooks

## 0.0.8 (2025-01-11)

### chore

- **global**: merge origin/main onto git-support-origin, untested
- updated pre-commit config to not have invalid commitizen argument

### ci

- remove outdated pre-commit article and update configuration comments
- **pre-commit**: add SQL code checking and Makefile refactor
- **pre-commit**: add shell code style checking support to pre-commit and documentation
- **pre-commit**: Add and test shellcheck for pre-commit. Disabled until shell files can meat the standard.
- **pre-commit**: Add and test markdownlint to pre-commit-config.yaml and docs. Disabled until Markdown can be passing.
- **pre-commit**: Added syncing pre-commit dependencies
- add new tasks for documentation and testing in Taskfile.yml
- **pyproject.toml**: Added dynamic selection of default uv installation groups depending on project scaffold type

### docs

- add comprehensive guide on pre-commit hooks for developers
- refactor pre-commit hooks for clarity and consistency improvements
- **pytest-customization**: Add a pytest customization document that is hidden
- enable strict hooks and update pre-commit documentation
- update pre-commit hooks and add QA settings documentation
- enhance pre-commit docs with setup, security, and new hooks info
- **template-README**: Added some badges to the README
- **pre-commit**: Add additional hooks to consider
- **pre-commit**: Added note regarding ensemble linters/formatters and hesitations on my current approach
- **pre-commit**: Added shell check to chosen pre-commit docs
- **pre-commit**: Updated pre-commit docs to reflect new pyright hook
- set Python version to 3.12 and update documentation details
- update pre-commit configuration and enhance documentation clarity
- add pre-commit configuration and final result documentation
- fix mkdocs rendering of markdown inside of summary tags
- enhance precommit documentation with improved section titles
- update pre-commit configurations and improve documentation clarity
- **precommit.md**: Improve formatting and make more concise
- update pyproject.toml with commitizen, add more pre-commit hooks, progress on precommit.md
- add more hooks to the pre-commit documentation

### feat

- update pyproject.toml with comment
- comment out strict hooks, add local tests, and auto-format Python
- update .gitattributes to include additional LFS file types
- **vscode**: add additional default settings for python to the vscode files
- **template-pyproject**: Added pandera to template pyproject to handle pandas typing
- **root-pre-commit**: switch mypy for pyright. Add type: ignores for not-yet-fixed files for now.
- **template-pre-commit**: Added same png optimizer to template pre-commit
- **pre-commit**: add oxipng, a png optimizer to pre-commit-config
- add .pre-commit-config.yaml to test and Makefile conditionally
- **template**: :sparkles: copy makefile commands for pre-commit from root to template
- **template**: copy .pre-commit-config.yaml to project template
- update pre-commit hook names for improved clarity and format
- refactor pre-commit config for clearer section headings
- upgrade essentials before requirement
- upgrade essentials before requirement

### fix

- update welcome screen URL to use the master branch
- **pre-commit-and-tests**: remove references to non-existing .ccds-original dir in tests and switched biome to check (format + safe fixes) instead of just checking
- Update gitignore to ignore additional files
- update license order, increment version, and add biome config
- hopefully fixed git tests
- **global**: merge updated source branch onto new origin branch to fix error had previously
- **pre-commit**: remove commitizen-branch since it is too demanding to have to go back and amend
- use makefile global variable for python interpreter in help command (#392)

### refactor

- Removed .ccds-original as it is probably not needed anymore
- refactor GitHub repo configuration for improved readability and update version to 0.0.6
- **global**: add ruff as primary linter and ignore various files in serious need of refactoring but which passed using flake8 + black
- refactor pre-commit config to enhance hook naming and clarity
- Added ability to check commitizen commit messages and moved to front
- extend the `make clean` command
- extend the `make clean` command
- restrict linting to `src` directory
- restrict linting to `src` directory

### style

- enhance pre-commit config with emoji for better readability
- add gitleaks hook and enhance pre-commit configuration clarity

### test

- add CommitLint configuration for enhanced commit message validation
- Proper accounting for uv in the tests and readded to the options which it had somehow been removed from
- exclude Windows from CI; clarify pre-commit test description

### 🎨🏗️ Style & Architecture

- **pyproject.toml**: update cz to use cz_gitmoji >>> ⏰ 1m
