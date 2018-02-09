"""This is a deployment file for mmmm package
"""
from mmmm import new_model
import os
import sys
import vertica_python


def run_from_ipython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False


if run_from_ipython():
    from IPython import get_ipython
    ipython = get_ipython()
    ipython.magic("matplotlib inline")
    project_dir = os.getcwd()
else:
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
src_dir = os.path.join(project_dir, "src")
sys.path.append(src_dir)


# What is the name of the model
model_name = ''

# What is the domain - options are D (digital), I (investments),
# O (operations), SM (sales and marketing), RP (risk and product)
domain = ''

# What is the current model version?  Model version should take the form of
# {major}.{minor} where both {major} and {minor} are integers.
version = ''

# Who should be contacted in case of failure
owner = ''

# If the primary owner cannot be contacted who should be
# contacted in case of failure
secondary_owner = ''

# Where is the model object being stored?
# Typically this is a location in S3 or hdfs
location = ''

# What date is the model being deployed?
# Dates should be formatted as YYYY-mm-dd
deploy_date = ''

# In order to monitor accuracy we need a baseline measurement
# First, how are you measuring your model? AUC? RMSE? Put the name
# of the metric below
metric = ''

# What is the value of the metric above?  Typically this value would
# derived by measuring performance on a held out testing set or through
# cross validation
value = ''


# The memo column below is optional. It can be used to provide a brief
# description of the deployment
memo = ''

# What is the name of the training pd.Dataframe in Python?
# Do not enter as a string
training_data =

# What columns should we consider categorical?  For these columns model
# monitoring will count the number in each bin.  Include model output
# if appropriate.  DO NOT include the true label
categorical_cols = ['', '', ...]

# What columns should we consider numerical?  For these columns model
# monitoring will compute deciles and monitor the counts in these deciles over
# time. Include model output if appropriate.  DO NOT include the true label
# If you would like to specify your own bins please reach out to Xiaomin
# for instruction.
continuous_cols = ['', '', ...]

# What columns are model output? DO NOT include the true label
output_cols = ['', '', ...]


# Establish a connection to vertica
db_conn = vertica_python.connect(
    host='vertica.private.massmutual.com',
    port=int("5433"),
    user='model_monitoring_batch',
    password='[ask Adam]',
    database='advana'
)

# Execute this function, given user does not offer self-defined bins
new_model(
    model_name,
    version,
    domain,
    owner=owner,
    secondary_owner=secondary_owner,
    location=location,
    deploy_date=deploy_date,
    metric=metric,
    value=value,
    memo=memo,
    categorical_cols=categorical_cols,
    continuous_cols=continuous_cols,
    output_cols=output_cols,
    db_conn=db_conn)

db_conn.close()
