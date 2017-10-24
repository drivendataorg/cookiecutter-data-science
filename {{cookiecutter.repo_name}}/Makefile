.PHONY: clean data lint requirements sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BUCKET = {{ cookiecutter.s3_bucket }}
PROFILE = {{ cookiecutter.aws_profile }}
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_VENV = pyenv
PYTHON_INTERPRETER = $(PYTHON_VENV)/bin/python

#################################################################################
# DATA                                                                          #
#################################################################################

## Make Dataset
data/raw/my_dataset.csv: src/data/make_dataset.py
	$(PYTHON_INTERPRETER) $< $@

#################################################################################
# MODELS                                                                        #
#################################################################################



#################################################################################
# TESTS                                                                         #
#################################################################################



#################################################################################
# SETUP COMMANDS                                                                #
#################################################################################

## Set up python interpreter environment
create_environment: requirements.txt
	pip3 install virtualenv -U
	virtualenv ${PYTHON_VENV} --python=$(shell which python3)
	${PYTHON_VENV}/bin/pip install -r requirements.txt

## Set up R environment
create_Renvironment:
	mkdir $packratdir
	cd $packratdir; Rscript -e "packrat::init()"
	cd $packratdir; Rscript -e 'install.packages("dplyr", repos = "http://cran.us.r-project.org")'

## Delete all compiled Python files
clean:
	find . -name "*.pyc" -exec rm {} \;
	find . -name "*.~" -exec rm {} \;

# Example target for creating symbolic links to shared data in Box
# ## Link box folder into local repository
# link_box:
# 	ln -sf ~/Box-Sync/Sales-and-Marketing-Domain/channel-routing/data
# 	ln -sf ~/Box-Sync/Sales-and-Marketing-Domain/channel-routing/models
# 	ln -sf ~/Box-Sync/Sales-and-Marketing-Domain/channel-routing/references

# Example target opens the relevant project webpages
# open:
# 	open --new -a "Google Chrome"
# 	atom .
# 	sleep 2
# 	open -a "Google Chrome" "https://advana.atlassian.net/wiki/spaces/AAP/pages/126066680/Channel+Routing"
# 	open -a "Google Chrome" 'https://advana.atlassian.net/projects/MCR/board'
# 	open -a "Google Chrome" 'https://github.com/massmutual/channel-routing'

## Lint using flake8 and lintr
lint:
	flake8 --exclude=$(PYTHON_VENV)/ --ignore=E501,E402 --count .
	# for R:
	# Rscript -e 'lintr::lint_package()'

## Delete all compiled Python files
clean:
	find . -name "*.pyc" -exec rm {} \;

# Example targets to move data to, from AWS
# ## Upload Data to S3
# sync_data_to_s3:
# ifeq (default,$(PROFILE))
# 	aws s3 sync data/ s3://$(BUCKET)/data/
# else
# 	aws s3 sync data/ s3://$(BUCKET)/data/ --profile $(PROFILE)
# endif
#
# ## Download Data from S3
# sync_data_from_s3:
# ifeq (default,$(PROFILE))
# 	aws s3 sync s3://$(BUCKET)/data/ data/
# else
# 	aws s3 sync s3://$(BUCKET)/data/ data/ --profile $(PROFILE)
# endif

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := show-help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
