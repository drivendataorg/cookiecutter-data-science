.PHONY: clean data lint requirements sync_s3

data:

experiment:

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BUCKET = {{ cookiecutter.s3_bucket }}
PROFILE = {{ cookiecutter.aws_profile }}
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}
SLASH = /

BASE_IMAGE_NAME=analytics-base
BASE_TAG=latest
AWS_IMAGE_PREFIX=datascience
AWS_ECR_SERVER=${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com
BASE_AWS_TAG=${AWS_ECR_SERVER}/${AWS_IMAGE_PREFIX}/${BASE_IMAGE_NAME}:${BASE_TAG}

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################



#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
requirements: test_environment
	pip install -r requirements.txt

## Delete all compiled Python files
clean:
	find . -name "*.pyc" -exec rm {} \;

## Lint using flake8
lint:
	flake8 --exclude=lib/,bin/,docs/conf.py .

sync_s3: sync_data_to_s3 sync_data_from_s3 sync_models_to_s3 sync_models_from_s3 \
	sync_references_to_s3 sync_references_from_s3

## Upload Data to S3
sync_data_to_s3:
ifeq (default,$(PROFILE))
	aws s3 sync data/ s3://$(BUCKET)/data/
else
	aws s3 sync data/ s3://$(BUCKET)/data/ --profile $(PROFILE)
endif

## Download Data from S3
sync_data_from_s3:
ifeq (default,$(PROFILE))
	aws s3 sync s3://$(BUCKET)/data/ data/
else
	aws s3 sync s3://$(BUCKET)/data/ data/ --profile $(PROFILE)
endif

## Upload models to S3
sync_models_to_s3:
ifeq (default,$(PROFILE))
	aws s3 sync models/ s3://$(BUCKET)/models/
else
	aws s3 sync models/ s3://$(BUCKET)/models/ --profile $(PROFILE)
endif

## Download models from S3
sync_models_from_s3:
ifeq (default,$(PROFILE))
	aws s3 sync s3://$(BUCKET)/models/ models/
else
	aws s3 sync s3://$(BUCKET)/models/ models/ --profile $(PROFILE)
endif

## Upload references to S3
sync_references_to_s3:
ifeq (default,$(PROFILE))
	aws s3 sync references/ s3://$(BUCKET)/references/
else
	aws s3 sync references/ s3://$(BUCKET)/references/ --profile $(PROFILE)
endif

## Download references from S3
sync_references_from_s3:
ifeq (default,$(PROFILE))
	aws s3 sync s3://$(BUCKET)/references/ references/
else
	aws s3 sync s3://$(BUCKET)/references/ references/ --profile $(PROFILE)
endif


## Upload logs to S3
sync_logs_to_s3:
ifeq (default,$(PROFILE))
	aws s3 sync logs/ s3://$(BUCKET)/logs/
else
	aws s3 sync logs/ s3://$(BUCKET)/logs/ --profile $(PROFILE)
endif

## Download references from S3
sync_logs_from_s3:
ifeq (default,$(PROFILE))
	aws s3 sync s3://$(BUCKET)/logs/ logs/
else
	aws s3 sync s3://$(BUCKET)/logs/ logs/ --profile $(PROFILE)
endif

## Log in to our ECR registry with docker
docker_login:
	$$(aws ecr get-login --no-include-email)

## pull the analytics-base image
pull_base_image: docker_login
	docker pull ${BASE_AWS_TAG}

## Set up docker environment
create_docker: pull_base_image
	docker build --build-arg directory=$(SLASH)$(PROJECT_DIR) -t $(PROJECT_NAME) .

## Run docker in container
run_docker:
	docker run -ti -p 7777:8888 --name=$(PROJECT_NAME) $(PROJECT_NAME):latest

## Enter the running docker container
enter_docker:
	docker exec -it $(PROJECT_NAME) bash

## Test python environment is setup correctly
test_environment:
	$(PYTHON_INTERPRETER) test_environment.py

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
