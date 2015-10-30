.PHONY: clean data sync_data_to_s3 sync_data_from_s3

data:
	python src/make_dataset.py

clean:
	find . -name "*.pyc" -exec rm {} \;

sync_data_to_s3:
	s3cmd sync --recursive data/ s3://{{ cookiecutter.s3_bucket }}/data/

sync_data_from_s3:
	s3cmd sync --recursive s3://{{ cookiecutter.s3_bucket }}/data/ data/
