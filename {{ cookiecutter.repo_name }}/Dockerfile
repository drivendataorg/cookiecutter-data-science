# Ubuntu 16.04 (xenial) from 2018-02-28
# https://github.com/docker-library/official-images/commit/8728671fdca3dfc029be4ab838ab5315aa125181
FROM ubuntu:xenial-20180228@sha256:e348fbbea0e0a0e73ab0370de151e7800684445c509d46195aef73e090a49bd6

LABEL maintainer="Neighborhoods <neighborhoods.engineering@neighborhoods.com>"

USER root
EXPOSE 80

ARG directory

WORKDIR $directory

ADD . $directory

# Install all OS dependencies for notebook server
# features (e.g., download as all possible file formats)
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation \
    build-essential \
    git \
    inkscape \
    libsm6 \
    libxext-dev \
    libxrender1 \
    lmodern \
    netcat \
    pandoc \
    python-dev \
    python3-pip \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-generic-recommended \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-xetex \
    unzip \
    vim \
    fonts-dejavu \
    tzdata \
    gfortran \
    gcc \
    libav-tools \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# Configure environment
ENV SHELL=/bin/bash \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

# Python Setup
RUN pip3 install setuptools
RUN pip3 install -r requirements.txt

# R Setup
RUN apt-get update && \
    apt-get install -y r-base=3.2.3-4
    # && \
    # Rscript install_packages.R

CMD jupyter-notebook --ip=0.0.0.0 --port=80 --no-browser --allow-root