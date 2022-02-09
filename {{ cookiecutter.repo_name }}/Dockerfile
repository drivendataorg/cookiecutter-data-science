{% if cookiecutter.python_interpreter == 'R' %}FROM rocker/rstudio:4.1.2

ENV RENV_VERSION 0.15.2-2
RUN R -e "install.packages('remotes', repos = c(CRAN = 'https://cloud.r-project.org'))"
RUN R -e "remotes::install_github('rstudio/renv@${RENV_VERSION}')"

WORKDIR /home/rstudio
COPY renv.lock .
RUN R -e 'renv::restore()'
{% else %}# Ubuntu with python, git and text-editors installed
FROM ubuntu:20.04

# Nvidia container examples (pick one to base your container on)
# FROM nvcr.io/nvidia/tensorflow:21.10-tf2-py3
# FROM nvcr.io/nvidia/pytorch:21.11-py3

ARG USER_ID
ARG GROUP_ID
WORKDIR /workspace
COPY setup.py .{% endif %}

RUN apt -y update
RUN apt install python3 python3-pip git nano vim -y
RUN apt install python-is-python3 -y

COPY requirements.txt .
RUN pip install -r requirements.txt
{% if cookiecutter.python_interpreter == 'python3' %}
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user
WORKDIR /workspace
{% endif %}