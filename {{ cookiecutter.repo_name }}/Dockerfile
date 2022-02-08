# Ubuntu with python, git and text-editors installed
FROM ubuntu:20.04

ARG USER_ID
ARG GROUP_ID

RUN apt -y update
RUN apt install python3 python3-pip git nano vim -y
RUN apt install python-is-python3 -y

# Nvidia container examples (pick one to base your container on)
# FROM nvcr.io/nvidia/tensorflow:21.10-tf2-py3
# FROM nvcr.io/nvidia/pytorch:21.11-py3

WORKDIR /workspace

COPY requirements.txt .
COPY setup.py .

RUN pip install -r requirements.txt

RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user