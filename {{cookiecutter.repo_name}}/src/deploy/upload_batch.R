library(mmmm)

## There are two ways to load new batches data for scoring,
## 1. user needs to provide model_name, model_version and model_domain.
##    These three inputs will automatically generate a model_id.
##    MMMM then will check if this model_id has been registered, if not,
##    a warning message will pop up.
## 2. user is allowed to provide model_id directly, and no need to provide
##    model_name, model_version and model_domain. Further steps will be identical to 1.
## Suppose db is already available, for example
## library(mmlib)
## db <- vertica_connect(user = "model_monitoring_batch",
##                       pass = [you need to ask for it])
## creds <- c(username = "model_monitoring_batch",
##            password = [you need to ask for it])



# The 1st way
mmmm::new_batch(
  batch_data = batch_data, # an R dataframe
  model_name = "titanic",
  model_version = "1.0",
  model_domain = "SM",
  batch_date = Sys.time(),
  db = db,
  creds = creds)

# The 2nd way
mmmm::new_batch(
  batch_data = batch_data, # an R dataframe
  model_id = "SM-titanic-1.0",
  batch_date = Sys.time(),
  db = db,
  creds = creds)
