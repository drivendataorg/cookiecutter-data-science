{% if cookiecutter.image == 'Tensorflow' -%}FROM registry.git.vgregion.se/aiplattform/images/tensorflow:0.2.1
{% elif cookiecutter.image == 'PyTorch' -%}FROM registry.git.vgregion.se/aiplattform/images/pytorch:0.3.2
{% elif cookiecutter.image == 'R' -%}FROM registry.git.vgregion.se/aiplattform/images/r:0.3.0{%- endif %}
ENV GID=1000
ENV UID=1000
{% if cookiecutter.image == 'R' %}ENV EDITOR_FOCUS_DIR="/workspace"{% endif %}

RUN apt -y update \
    && apt install -y --no-install-recommends python3-pip git openssl \{% if cookiecutter.image != 'R' %}
    && addgroup --gid $GID researcher \{% endif %}
    && useradd --home-dir /workspace --create-home --shell /bin/bash --non-unique --comment '' --uid $UID --gid $GID researcher \
    && chown -R 1000:1000 /workspace

ADD http://aiav2.vgregion.se/VGC%20Root%20CA%20v2.crt /tmp/vgc_root.der
ADD http://aiav2.vgregion.se/VGC%20Issuing%201%20CA%20v2.crt /tmp/vgc_issuing1.der
ADD http://aiav2.vgregion.se/VGC%20Issuing%202%20CA%20v2.crt /tmp/vgc_issuing2.der
ADD http://aiav2.vgregion.se/VGC%20Issuing%201%20CA%20v2(1).crt /tmp/vgc_issuing1_2.der

COPY requirements.txt {% if cookiecutter.image != 'R' %} setup.py {% endif %} ./{% if cookiecutter.image == 'R' %}
COPY renv.lock /workspace/renv.lock
COPY r-start.sh /usr/local/bin/r-start{% endif %}

RUN pip install -r requirements.txt --no-cache-dir \
    && pip install --no-cache-dir pre-commit==3.3.3 \
    && openssl x509 -inform der -in /tmp/vgc_root.der -out /usr/local/share/ca-certificates/vgc_root.crt \
    && openssl x509 -inform der -in /tmp/vgc_issuing1.der -out /usr/local/share/ca-certificates/vgc_issuing1.crt \
    && openssl x509 -inform der -in /tmp/vgc_issuing1_2.der -out /usr/local/share/ca-certificates/vgc_issuing1_2.crt \
    && openssl x509 -inform der -in /tmp/vgc_issuing2.der -out /usr/local/share/ca-certificates/vgc_issuing2.crt \
    && update-ca-certificates \
    {% if cookiecutter.image == 'R' %}&& chown -R 1000:1000 /workspace/ \
    && echo "setwd(\"/workspace/\")" > /home/rstudio/.Rprofile \
    && chmod +x /usr/local/bin/r-start \{% endif %}
    && rm requirements.txt {% if cookiecutter.image != 'R' %} setup.py {% endif %}

USER researcher
WORKDIR /workspace

{% if cookiecutter.image == 'R' %}RUN R -e 'renv::activate()' && R -e 'renv::restore()'

USER root
EXPOSE 8787

{% endif %}