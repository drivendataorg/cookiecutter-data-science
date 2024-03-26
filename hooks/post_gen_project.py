import os

REMOVE_PATHS = [
    '{% if cookiecutter.zillow_project != "true" %} .gitlab-ci.yml {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)