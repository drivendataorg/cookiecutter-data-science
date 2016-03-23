cookiecutter-data-science
-------------------------

An opinionated, but not-afraid-to-be-wrong project template for data science projects. Pull requests welcome. Debate encouraged.


Requirements to create project:
-----------
 - Python 2.7 or 3.5
 - [cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html): `pip install cookiecutter`


To start a new project:
------------

    cookiecutter https://github.com/drivendata/cookiecutter-data-science


<script type="text/javascript" src="https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02.js" id="asciicast-9bgl5qh17wlop4xyxu9n9wr02" async></script>


Data
----------
** By default, the `data` folder is included in the `.gitignore` file.** If you have a small amount of data that rarely changes, you may want to include the data in the repository. Github currently warns if files are over 50MB and rejects files over 100MB. Some other options for storing large data include [AWS S3](https://aws.amazon.com/s3/) with a syncing tool (e.g., [`s3cmd`](http://s3tools.org/s3cmd)), [Git Large File Storage](https://git-lfs.github.com/), [Git Annex](https://git-annex.branchable.com/), and [dat](http://dat-data.com/).

The prefered workflow if data is not in the repository is to have a make command `make data` that will download or create the relevant datasets.
