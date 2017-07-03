# loading the local scripts
source('R/utils.R')

library(devtools)

# load package w/o installing
load_all('R')

# get vertica connection
# make sure you've sourced the root .env file first
# NOTE: first install mmlib!
con <- mmlib::vertica_connect(Sys.getenv("user"), Sys.getenv("pw"), "jdbc:vertica://vertica:5433/advana")
