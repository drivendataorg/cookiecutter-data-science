{% if cookiecutter.python_interpreter == 'Tensorflow' %}FROM registry.git.vgregion.se/aiplattform/images/tensorflow:0.1.2{% endif %}
{% if cookiecutter.python_interpreter == 'PyTorch' %}FROM registry.git.vgregion.se/aiplattform/images/pytorch:0.1.1{% endif %}
{% if cookiecutter.python_interpreter == 'R' %}FROM registry.git.vgregion.se/aiplattform/images/r:0.1.1{% endif %}
ENV GID=1000
ENV UID=1000

RUN apt -y update \
    && apt install python3-pip git -y \
    && addgroup --gid $GID researcher \
    && adduser --home /workspace --disabled-password --gecos '' --uid $UID --gid $GID researcher

COPY requirements.txt setup.py ./
RUN pip install -r requirements.txt

USER researcher
WORKDIR /workspace