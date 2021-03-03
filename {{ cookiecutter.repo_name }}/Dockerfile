FROM python:3.9-slim

RUN apt update && apt install -y \
    sudo

ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN adduser ${USERNAME} --gecos "" --disabled-password &&\
    echo ${USERNAME} ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} &&\
    chmod 0440 /etc/sudoers.d/${USERNAME}

USER ${USERNAME}
RUN echo 'export PS1="🐳 \[\033[1;36m\][\u@docker] \[\033[1;34m\]\W\[\033[0;35m\] # \[\033[0m\]"' >> /home/${USERNAME}/.bashrc

WORKDIR /app
RUN sudo chown -R ${USERNAME} .

COPY --chown=${USERNAME} requirements.txt setup.py ./
COPY --chown=${USERNAME} src/__init__.py src/

RUN pip3 install -r requirements.txt

COPY --chown=${USERNAME} . .

CMD ["python3", "jupyterlab"]