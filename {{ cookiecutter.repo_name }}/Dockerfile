{% if cookiecutter.python_interpreter == 'Tensorflow' %}FROM registry.git.vgregion.se/aiplattform/images/tensorflow:0.1.3{% endif %}
{% if cookiecutter.python_interpreter == 'PyTorch' %}FROM registry.git.vgregion.se/aiplattform/images/pytorch:0.1.1{% endif %}
{% if cookiecutter.python_interpreter == 'R' %}FROM registry.git.vgregion.se/aiplattform/images/r:0.1.1{% endif %}
ENV GID=1000
ENV UID=1000

RUN apt -y update \
    && apt install -y --no-install-recommends python3-pip git openssl \
    && addgroup --gid $GID researcher \
    && adduser --home /workspace --disabled-password --gecos '' --uid $UID --gid $GID researcher

ADD http://aiav2.vgregion.se/VGC%20Root%20CA%20v2.crt /tmp/vgc_root.der
ADD http://aiav2.vgregion.se/VGC%20Issuing%201%20CA%20v2.crt /tmp/vgc_issuing1.der
ADD http://aiav2.vgregion.se/VGC%20Issuing%202%20CA%20v2.crt /tmp/vgc_issuing2.der


COPY requirements.txt setup.py ./
RUN pip install -r requirements.txt \
    && openssl x509 -inform der -in /tmp/vgc_root.der -out /usr/local/share/ca-certificates/vgc_root.crt \
    && openssl x509 -inform der -in /tmp/vgc_issuing1.der -out /usr/local/share/ca-certificates/vgc_issuing1.crt \
    && openssl x509 -inform der -in /tmp/vgc_issuing2.der -out /usr/local/share/ca-certificates/vgc_issuing2.crt \
    && update-ca-certificates

USER researcher
WORKDIR /workspace