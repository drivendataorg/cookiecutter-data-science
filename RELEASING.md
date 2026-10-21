# Information for releases and versioning of ccds

## Background

The release of [ccds v2](https://drivendata.co/blog/ccds-v2) introduced the `ccds` utility and the concept of versioning to cookiecutter data science. Prior to this release, cookiecutter-data-science only provided a project template, which the generic [cookiecutter](https://github.com/cookiecutter/cookiecutter) utility could use to instantiate a project. Branches and forks could be used in the usual way to get different versions of the template.

To give the utility and the template a bit more stability, PR [#336](https://github.com/drivendataorg/cookiecutter-data-science/pull/336) created automated release mechanics for publishing new releases and, by default, pinned the template used by the `ccds` utility to the installed version. 

## Issuing a new release

 - [ ] Update version in `pyproject.toml` file
 - [ ] Ensure `HISTORY.md` is up to date with the changes in this release and add version info and release date
 - [ ] Create new release on the GitHub [releases page](https://github.com/drivendataorg/cookiecutter-data-science/releases) with the tag `vMAJOR.MINOR.PATCH` (e.g., `v2.3.0`) and the contents of the relevant `HISTORY.md` section as the release notes.
 - [ ] Confirm release action runs successfully and the new release is available on [PyPI](https://pypi.org/project/cookiecutter-data-science/).

`ccds` uses [semantic versioning](https://semver.org/). When issuing a new release, **ensure that your release version tag has the format `vMAJOR.MINOR.PATCH`. The `v` prefix is important because the utility will look for the tag with that name to download by default.