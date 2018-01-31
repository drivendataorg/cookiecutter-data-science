library(mmmm)

## There are two ways to load scores of a model

# The 1st way
mmmm::new_score(
  model_name = "titanic",
  model_version = "1.0",
  model_domain = "SM",
  score_date = Sys.time(),
  scores = c(0.87, 0.83, 0.83, 0.87),
  link = c("ABC123", "ABC124", "ABC125", "ABC123"), # should be carefully created and documented
  db = db,
  creds = creds)

# The 2nd way,
mmmm::new_score(
  model_id = "SM-titanic-1.0",
  score_date = Sys.time(),
  scores = c(0.87, 0.83, 0.83, 0.87),
  link = c("ABC123", "ABC124", "ABC125", "ABC123"), # should be carefully created and documented
  db = db,
  creds = creds)
