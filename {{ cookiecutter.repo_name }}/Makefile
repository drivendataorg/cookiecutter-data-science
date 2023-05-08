p-yapf:
	poetry run yapf . -r -i --style={column_limit:120}

build: # build wheel package in dist
	poetry build -f wheel

p-tests: # run pytest and generate coverage report
	poetry run pytest tests --cov="grab" --cov-fail-under=70

p-install: # install dev dependencies
	pip install poetry && poetry install

p-lock:
	poetry lock --no-update

preview-docs:
	cd techdocs && mkdocs serve -a localhost:8004

gen-release-docs:
	@read -p "Enter rollback release version: " ROLLBACKVER; \
	read -p "Enter new release version: " NEWVER; \
	sh ./release-log-generator.sh "grab" "v$${ROLLBACKVER}" "v$${NEWVER}";
