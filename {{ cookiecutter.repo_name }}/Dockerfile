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

RUN apt -y update
RUN apt install python3 python3-pip git nano vim -y
RUN apt install python-is-python3 -y

COPY requirements.txt .
RUN pip install -r requirements.txt

{% endif %}{% if cookiecutter.python_interpreter == 'python3' %}FROM nvidia/cuda:11.4.0-base-ubuntu20.04

ENV KUBECONFIG="/tmp/kube.config"

COPY kube.template /tmp/kube.template

RUN apt -y update \
    && apt install python3 python3-pip git -y \
    && apt install python-is-python3 -y \
    && apt-get install -y curl gettext-base \
    && addgroup --gid 999 researcher \
    && adduser --home /workspace --disabled-password --gecos '' --uid 999 --gid 999 researcher \
    && curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/ \
    && curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash \
    && curl -L -o runai.tar.gz https://github.com/run-ai/runai-cli/releases/download/v2.3.4/runai-cli-v2.3.4-linux-amd64.tar.gz \
    && tar xvzf runai.tar.gz \
    && ./install-runai.sh \
    && envsubst < /tmp/kube.template > /tmp/kube.config

COPY requirements.txt setup.py ./
RUN pip install -r requirements.txt

USER researcher
WORKDIR /workspace

CMD ["dvc", "repro"]
{% endif %}
