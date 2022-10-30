# Databricks notebook source
# MAGIC %md
# MAGIC Install dependancies as shown below. Ensure project root has a requirements.txt file like normal - except only include "unusual" dependancies that wouldn't expect on a stock databricks cluster. If it need a custom repo that pip wouldn't ordinarily be able to access (like classypy in this example), ensure it is cloned into your own repos folder.
# MAGIC 
# MAGIC This first cell should be at the top of all your pipelines if your requirements.txt file is not empty.

# COMMAND ----------

# MAGIC %sh python ./install_requirements.py

# COMMAND ----------

# MAGIC %md
# MAGIC This following allows you to make changes to the repo and immediately run them with detaching and re-attaching the notebook to the cluster. You still have to "reimport" the functions which you have changed, so its recommended you import the functions where you call them

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# MAGIC %md
# MAGIC On databricks, there is no need to install the package like you might assume when developing locally. This is because the repo root is a part of the `$PYTHONPATH` by default when running a notebook within a repo

# COMMAND ----------

from test_repo.main import main
main()