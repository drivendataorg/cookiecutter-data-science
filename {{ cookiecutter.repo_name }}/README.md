{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Organization
------------

    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed goes.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter or Beaker notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── references         <- Reports, data dictionaries, manuals, and all other explanatory materials.
    └── src                <- Source code. Possible subdirectories might be `scripts` or `API` for
                              projects with larger codebases.

Basic Commands
--------------

### Syncing data to S3

* `make sync_data_to_s3` will use `s3cmd` to recursively sync files in `data/` up to `s3://{{ cookiecutter.s3_bucket }}/data/`.
* `make sync_data_from_s3` will use `s3cmd` to recursively sync files from `s3://{{ cookiecutter.s3_bucket }}/data/` to `data/`.