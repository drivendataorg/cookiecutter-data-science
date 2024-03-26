ARG SERVICE_VERSION
ARG POETRY_VERSION="==1.18"
# build environment  # TODO: REPLACE WITH zgny-docker image
{% if cookiecutter.zillow_project == 'true' %}
FROM devex-docker.artifactory.zgtools.net/devex/docker-images/python3.10-build-debian11
{% else %}
FROM python:3.10
{% endif %}

ENV SERVICE_VERSION=${SERVICE_VERSION}

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV VIRTUALENV_ACTIVATE_FILE=/app/.venv/bin/activate

ARG POETRY_VERSION_SPECIFIER=POETRY_VERSION
RUN pip install "poetry$POETRY_VERSION_SPECIFIER"

COPY pyproject.toml poetry.lock ./
COPY src ./src
COPY README.md ./README.md
RUN poetry version ${SERVICE_VERSION} && poetry install --no-interaction --no-ansi -vvv
