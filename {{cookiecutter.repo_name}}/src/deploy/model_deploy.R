### What is the name of the model
model_name = ""

###  What is the domain - options are D (digital), I (investments),
###  O (operations), SM (sales and marketing), RP (risk and product)
domain = ""

###  What is the current model version?  Model version should take the form of {major}.{minor}
###  where both {major} and {minor} are integers.
version = ""

###  Who should be contacted in case of failure
owner = ""

###  If the primary owner cannot be contacted who should be
###  contacted in case of failure
secondary_owner = ""

###  Where is the model object being stored?
###  Typically this is a location in S3 or hdfs
location = ""

###  What date is the model being deployed?
###  Dates should be formatted as YYYY-mm-dd
deploy_date = ""

###  In order to monitor accuracy we need a baseline measurement
###  First, how are you measuring your model? AUC? RMSE? Put the name
###  of the metric below
metric = ""

###  What is the value of the metric above?  Typically this value would
###  derived by measuring performance on a held out testing set or through
###  cross validation
value = ""


###  The memo column below is optional.  It can be used to provide a brief
###  description of the deployment
memo = ""

###  What is the name of the training dataframe in R?
###  Do not enter as a string
training_data =

###  What columns should we consider categorical?  For these columns model
###  monitoring will count the number in each bin.  Include model output
###  if appropriate.  DO NOT include the true label
categorical_cols = c("", "")

###  What columns should we consider numerical?  For these columns model
###  monitoring will compute deciles and monitor the counts in these deciles over time.
###  Include model output if appropriate.  DO NOT include the true label
###  If you would like to specify your own bins please reach out to Xiaomin
###  for instruction.
continuous_cols = c("", "")

###  What columns are model output?    DO NOT include the true label
output_cols = c("", "")

### Establish a connection to vertica. The vertica connection function is not offered
### in this package. Users are encouraged to refer to other packages (e.g.,
### mmlib::vertica_connect()) for ways of connecting to vertica. batch_id and batch_pass are
### needed, though, and should be properly handled.
db <- vertica_connect(Sys.getenv("MODEL_MONITORING_BATCH"),
                      Sys.getenv("MODEL_MONITORING_PASS"))

### This is the credential needed as an input. Users are encouraged to wrap creds as an env. variable.
### NOTE: username = and password = cannot be ignored
creds <- c(username = Sys.getenv("MODEL_MONITORING_BATCH"),
           password = Sys.getenv("MODEL_MONITORING_PASS"))

### Run the following code after filling everything out above
# Execute the following command
library(mmmm)

mmmm::new_model(
  name = model_name,
  version = version,
  domain = domain,
  owner = owner,
  location = location,
  deploy_date = deploy_date,
  metric = metric,
  value = value,
  memo = memo,
  training_data = training_data,
  categorical_cols = categorical_cols,
  continuous_cols = continuous_cols,
  output_cols = output_cols,
  db = db,
  creds = creds)

