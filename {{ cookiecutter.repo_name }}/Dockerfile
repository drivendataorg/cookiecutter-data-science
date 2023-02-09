{% if cookiecutter.image == 'Tensorflow' %}FROM registry.git.vgregion.se/aiplattform/images/tensorflow:0.2.0{% endif %}
{% if cookiecutter.image == 'PyTorch' %}FROM registry.git.vgregion.se/aiplattform/images/pytorch:0.3.0{% endif %}
{% if cookiecutter.image == 'R' %}FROM registry.git.vgregion.se/aiplattform/images/r:0.2.0{% endif %}
ENV GID=1000
ENV UID=1000

RUN apt -y update \
    && apt install -y --no-install-recommends python3-pip git openssl {% if cookiecutter.image != 'R' %}\
    && addgroup --gid $GID researcher \
    && adduser --home /workspace --shell /bin/bash --disabled-password --gecos '' --uid $UID --gid $GID researcher
    {% endif %}

ADD http://aiav2.vgregion.se/VGC%20Root%20CA%20v2.crt /tmp/vgc_root.der
ADD http://aiav2.vgregion.se/VGC%20Issuing%201%20CA%20v2.crt /tmp/vgc_issuing1.der
ADD http://aiav2.vgregion.se/VGC%20Issuing%202%20CA%20v2.crt /tmp/vgc_issuing2.der
ADD http://aiav2.vgregion.se/VGC%20Issuing%201%20CA%20v2(1).crt /tmp/vgc_issuing1_2.der

COPY requirements.txt {% if cookiecutter.image != 'R' %} setup.py {% endif %} ./
RUN pip install -r requirements.txt --no-cache-dir \
    && openssl x509 -inform der -in /tmp/vgc_root.der -out /usr/local/share/ca-certificates/vgc_root.crt \
    && openssl x509 -inform der -in /tmp/vgc_issuing1.der -out /usr/local/share/ca-certificates/vgc_issuing1.crt \
    && openssl x509 -inform der -in /tmp/vgc_issuing1_2.der -out /usr/local/share/ca-certificates/vgc_issuing1_2.crt \
    && openssl x509 -inform der -in /tmp/vgc_issuing2.der -out /usr/local/share/ca-certificates/vgc_issuing2.crt \
    && update-ca-certificates \
    && rm requirements.txt setup.py

USER researcher
WORKDIR /workspace