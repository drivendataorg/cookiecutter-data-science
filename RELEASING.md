# Information for releases and versioning of ccds

## Background

The release of [ccds v2](https://drivendata.co/blog/ccds-v2) introduced the `ccds` utility and the concept of versioning to cookiecutter data science. Prior to this release, cookiecutter-data-science only provided a project template, which the generic [cookiecutter](https://github.com/cookiecutter/cookiecutter) utility could use to instantiate a project. Branches and forks could be used in the usual way to get different versions of the template.

To give the utility and the template a bit more stability, PR [#336](https://github.com/drivendataorg/cookiecutter-data-science/pull/336) created automated release mechanics for publishing new releases and, by default, pinned the template used by the `ccds` utility to the installed version. 

## Issuing a new release

`ccds` uses [semantic versioning](https://semver.org/). When issuing a new release, **ensure that your release version tag has the format `vMAJOR.MINOR.PATCH`. The `v` prefix is important because the utility will look for the tag with that name to download by default.