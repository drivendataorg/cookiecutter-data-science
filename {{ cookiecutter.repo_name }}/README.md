{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

```
├── LICENSE
│
|
├── README.md          <- The top-level README for developers using this project.
│
├── docs               <- Databricks Notebooks explaining things or visualizations. Reports also go here
│
├── tests              <- Where to place tests. To be expanded
│
├── requirements.txt   <- The requirements file. This should be pretty minimal given databricks will handle most things. The exception is typically in-house packages like classpy
│
├── setup.py           <- makes project pip installable (pip install -e .) so project can be imported. Should not be used in databricks
│
├── {{cookiecutter.project_name}}        <- Source code for use in this project.
│   ├── __init__.py    <- Makes this a Python module
│   │
│   ├── main.py    <- Typical project entrypoint
│   │
│   ├── ingestion           <- Initial ingestion of data, and standardization into either DBFS or Hive
│   │
│   ├── annotation           <- Intermediary results, manipulations, and validation
│   │
│   └── results           <- Generation of clean and final data, outputs
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

```

--------




Feel free to ignore anything you don't need/understand, this is supposed to make your life easier ;)

<p><small>Project based on the <a target="_blank" href="https://github.com/Giving-Tuesday/cookiecutter-data-science">
Giving Tuesdays' cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
