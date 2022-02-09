import os

REMOVE_PATHS = [
    {% if cookiecutter.python_interpreter == "R" %}
    "setup.py",
    "setup.cfg",
    "pytest.ini",
    "{{ cookiecutter.module_name }}/__init__.py",
    "{{ cookiecutter.module_name }}/data/__init__.py",
    "{{ cookiecutter.module_name }}/data/make_dataset.py",
    "{{ cookiecutter.module_name }}/features/__init__.py",
    "{{ cookiecutter.module_name }}/features/build_features.py",
    "{{ cookiecutter.module_name }}/models/__init__.py",
    "{{ cookiecutter.module_name }}/models/evaluate_model.py",
    "{{ cookiecutter.module_name }}/models/predict_model.py",
    "{{ cookiecutter.module_name }}/models/train_model.py",
    "{{ cookiecutter.module_name }}/visualization/__init__.py",
    "{{ cookiecutter.module_name }}/visualization/visualize.py",
    "tests/__init__.py",
    {% else %}
    "renv.lock",
    "{{ cookiecutter.module_name }}/data/make_dataset.R",
    {% endif %}
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)