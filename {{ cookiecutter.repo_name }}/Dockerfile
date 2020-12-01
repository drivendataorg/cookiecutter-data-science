FROM python:3.8.6 as user
RUN pip install --upgrade pip
RUN pip install pytest
ARG HOST_UID=4000
ARG HOST_USER=nodummy
RUN useradd -ms /bin/bash ${HOST_USER} --create-home
WORKDIR /home/${HOST_USER}
RUN mkdir projects
COPY . projects/{{cookiecutter.repo_name}}
RUN pip install wheel -r projects/{{cookiecutter.repo_name}}/requirements.txt
RUN cd projects/{{cookiecutter.repo_name}} {% if cookiecutter.module == 'y' %} && pip install -e .{% endif %}
