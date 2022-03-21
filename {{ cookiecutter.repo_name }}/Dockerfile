{% if cookiecutter.python_interpreter == 'R' %}FROM rocker/tidyverse:4.1.2

ENV RENV_VERSION 0.15.2-2

RUN echo "options(repos = c(CRAN = 'https://ftpmirror1.infania.net/mirror/CRAN'),\
	 download.file.method = 'libcurl')" >> ${R_HOME}/etc/Rprofile.site

RUN R -e "install.packages('remotes')"
RUN R -e "remotes::install_github('rstudio/renv@${RENV_VERSION}')"

WORKDIR /home/rstudio
COPY renv.lock .
RUN R -e 'renv::activate()'
RUN R -e 'renv::restore()'

{% else %}# Ubuntu with python, git and text-editors installed
FROM nvidia/cuda:11.4.0-base-ubuntu20.04

RUN apt -y update \
    && apt install python3 python3-pip git -y \
    && apt install python-is-python3 -y \
    && addgroup --gid 999 researcher \
    && adduser --home /workspace --disabled-password --gecos '' --uid 999 --gid 999 researcher

COPY requirements.txt setup.py ./
RUN pip install -r requirements.txt

USER researcher
WORKDIR /workspace

CMD ["dvc", "repro"]

{% endif %}