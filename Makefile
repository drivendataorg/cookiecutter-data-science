###     UTILITIES
_prep:
	rm -f **/*/.DS_store


###     DEV TOOLS
requirements:
	pip install -U -r dev-requirements.txt

format:
	isort ccds hooks tests
	black ccds hooks tests --exclude "hooks/post_gen_project.py"
	
lint:
	flake8 ccds hooks tests
	black --check ccds hooks tests --exclude "hooks/post_gen_project.py"


###     DOCS
docs-serve:
	cd docs && mkdocs serve

###     TESTS

test: _prep
	pytest

test-debug-last:
	pytest --lf --pdb

_clean_manual_test:
	rm -rf manual_test

manual_test: _prep _clean_manual_test
	cd manual_test && ccds 