.PHONY: clean data requirements sync_data_to_s3 sync_data_from_s3

requirements:
	pip install -r requirements.txt

data: requirements
	python src/make_dataset.py

clean:
	find . -name "*.pyc" -exec rm {} \;

sync_data_to_s3:
	s3cmd sync --recursive data/ s3://{{ cookiecutter.s3_bucket }}/data/

sync_data_from_s3:
	s3cmd sync --recursive s3://{{ cookiecutter.s3_bucket }}/data/ data/
