## Unreleased

## 0.5.1 (2025-09-03)

### Fix

- Fix documentation generation from json. Update version.

## 0.5.0 (2025-08-08)

### Feat

- fix tests
- got template to work with updates
- update pre-commit
- skeleton code for choosing between trunk and pre-commit
- added skeleton code for typst
- Added typst support for template
- had gemini try matching the Makefile features
- Added skeleton code for selecting the task manager
- add template.env
- Update cursor integration readmes
- Create obsidian pre-configuration as an experimental feature
- Playing with devenv
- add pydantic cursor rules
- add initial cursor rules and artifacts for project structure and guidelines
- experimenting with megalinter and trunk.io
- final updates to cursor rules. most are experimental and probably should not be used
- Added skeleton code for a direnv setup
- Add skeleton code for an experimental CNAME file
- Add skeleton code for an experiment homebrew configuration
- Add skeleton code for an experiment install.sh configuration
- Make dependency-groups also appear conitionally, not just the default ones

### Fix

- Progress towards working tests
- Update readme to use github reference for pypi

### Refactor

- Remove old unused files

## 0.4.5 (2025-03-14)

### Fix

- Return the images back to the repo

## 0.4.4 (2025-03-14)

### Fix

- add tag_format to commitizen config

## 0.4.3 (2025-03-14)

### Feat

- **scaffold_cleaner**: add secrets manager selection functionality and update cleaning operations
- Add experimental nix flake configuration
- correct the cli implementation so it works out of the box
- Create CLI scaffolding and rename AI scaffolding to data
- Scaffold cleaner extracts selected module files. Template Makefile refactor
- **template**: Pin python version number for each project (typically helpful for testing the lowest version number
- Add new dynamic quality assurance templating tag to control pre-commit. Also update tests to use better logging I believe
- Add 007_educational-hinting system
- Add cursor rules to template to improve agent responses and functionality. Includes artifacts, memory, style, etc.
- remove more unneeded files based on scaffolding type
- remove even more code scaffolding depending on the project type
- apply new .cursor/rules setup to template
- make course cleaning operations
- Broken skeleton code for scaffold cleaning
- add frozen requirements.txt and fix template files

### Fix

- update Makefile to use 'ruff format' for code formatting, add new ignore rules in pyproject.toml, and create __init__.py for data module
- **pyproject,template**: correct pyproject syntax errors part 4
- **pyproject,template**: correct pyproject syntax errors part 3
- **pyproject,template**: correct pyproject syntax errors part 2
- **pyproject,template**: correct pyproject syntax errors
- fix removing all scaffolding
- **mkdocs**: Temporarily disabled termynal generation to get docs to render
- update README for consistent cookiecutter placeholder syntax

### Refactor

- Update devcontainer.json to be better organized
- Remove history and flake linter
- **vscode**: reorganize extension recommendations and update task details to use 'ruff' for linting and formatting
- **pyproject,template**: Reorganize pyproject.toml settings, improve Ruff configuration, more.
- **.gitignore**: Refactor template gitignore
- **pyproject.toml**: Add commitizen and pre-commit to the dev requirements. Disable typical packages for less bloat.
- **pyproject.toml**: Label default dependency group packs and disable them to avoid unnecessary bloat
- **pyproject.toml**: Label default dependency group packs and disable them to avoid unnecessary bloat

## 0.4.1 (2025-01-31)

### Feat

- **cookiecutter**: Add automatic description to the github upload
- **citation**: Add template citation to template for research papers
- enhance SSH config with conditional host entries
- add SSH setup instructions and remote server config examples
- clarify SSH key naming conventions and update comments
- **cookiecutter-hooks**: Added skeleton code for future SSH implementation
- add SSH key generation stubs, update config and post-gen script
- update Dockerfile to use dynamic GitHub username for label
- add VSCode configs for extensions, debugging, and settings
- enhance commitlint with scopes and commitizen customization

### Fix

- exclude mdformat for Jinja tags and fix README placeholders
- remove unused GNN image from problem set directory
- fix inconsistent Jinja2 syntax in README.md template
- fix description handling by adding quotes in GitHub repo config
- **vcs**: Made github only provide --description flag if there is a description
- Deleted favicon file that was not needed and for some reason missing in git lfs. Would be smart to clone from repo as a test in the future.
- Hopefully updated missing git lfs files to work
- **docs**: Updated reference in jupyter-notebooks.md file to new pre-commit.md file
- **github-actions**: Fixed pull_request_template.md being upper case now so that tests pass part 2
- **github-actions**: Fixed pull_request_template.md being upper case now so that tests pass

### Refactor

- **template**: Updated pre-commit config to selectively ignore certain tests on files isntead of completely ignoring template. Deleted corrupted png files.
- **pyproject.toml**: Updated build to not include unnecessary directories
- remove unused author name variable and update file references
- **tests**: Update issue template filenames and add new documentation files for CODE_OF_CONDUCT, CONTRIBUTING, and SECURITY

## 0.0.8 (2025-01-11)

### Feat

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

### Fix

- update welcome screen URL to use the master branch
- **pre-commit-and-tests**: remove references to non-existing .ccds-original dir in tests and switched biome to check (format + safe fixes) instead of just checking
- Update gitignore to ignore additional files
- update license order, increment version, and add biome config
- hopefully fixed git tests
- **global**: merge updated source branch onto new origin branch to fix error had previously
- **pre-commit**: remove commitizen-branch since it is too demanding to have to go back and amend
- use makefile global variable for python interpreter in help command (#392)

### Refactor

- Removed .ccds-original as it is probably not needed anymore
- refactor GitHub repo configuration for improved readability and update version to 0.0.6
- **global**: add ruff as primary linter and ignore various files in serious need of refactoring but which passed using flake8 + black
- refactor pre-commit config to enhance hook naming and clarity
- Added ability to check commitizen commit messages and moved to front
- extend the `make clean` command
- restrict linting to `src` directory
