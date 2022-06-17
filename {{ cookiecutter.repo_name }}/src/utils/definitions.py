import os
import subprocess
""" This module loads folder structure and specific paths """

# First level dirs
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)) 
ROOT_DIR = os.path.abspath(os.path.join(SRC_DIR,os.pardir)) 
DATA_DIR = os.path.join(ROOT_DIR,'data')
REPORTS_DIR = os.path.join(ROOT_DIR,'reports')


## DATA subdirs
FIG_DIR = os.path.join(DATA_DIR,'figures')
PARS_DIR = os.path.join(DATA_DIR,'params')

## REPORTS subdirs
IMG_DIR = os.path.join(REPORTS_DIR,'img')
RMD_DIR = os.path.join(REPORTS_DIR,'rmd')

#GIT
GIT_PATH = os.path.join(ROOT_DIR,'.git')
REPO_URL = subprocess.run(["git", "config", "--get", "remote.origin.url"],
                            capture_output=True, text=True).stdout.strip("\n")
