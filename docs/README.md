Generating the docs
----------

Install development requirements:

    pip install -r dev-requirements.txt

Change directories into the docs folder:

    cd docs

Use [mkdocs](https://www.mkdocs.org/) structure to update the documentation. Test locally with:

    mkdocs serve

The [hosted docs](https://cookiecutter-data-science.drivendata.org/) are deployed via [render](render.com) when the `master` branch is updated.