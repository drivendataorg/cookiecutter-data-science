###     UTILITIES
_prep:
	rm -f **/*/.DS_store


###     DEV TOOLS
requirements:
	pip install -U -r dev-requirements.txt

format:
	isort ccds hooks tests
	black ccds hooks tests setup.py
	
lint:
	flake8 ccds hooks tests setup.py
	black --check ccds hooks tests setup.py


###     DOCS

docs-serve:
	cd docs && mkdocs serve

###     TESTS

test: _prep
	pytest -vvv

test-fastest: _prep
	pytest -vvv -FFF

test-debug-last:
	pytest --lf --pdb

_clean_manual_test:
	rm -rf manual_test

manual-test: _prep _clean_manual_test
	mkdir -p manual_test
	cd manual_test && python -m ccds ..

manual-test-debug: _prep _clean_manual_test
	mkdir -p manual_test
	cd manual_test && python -m pdb ../ccds/__main__.py ..