FROM python:3.9-slim

# Sets the name for the user to be used in the container.
# In order to have no problems with file permision make sure that
# the USER_UID matches your ID if you are using a ~unix system.
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Gets all updates and installs sudo
RUN apt update && apt install -y sudo

# Adds the user and allows it sudo privileges without needing a password
RUN adduser ${USERNAME} --gecos "" --disabled-password &&\
    echo ${USERNAME} ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} &&\
    chmod 0440 /etc/sudoers.d/${USERNAME}

WORKDIR /app

# It copies all the files that do not change often. Speeds up rebuild process.
# The flag --chown copies the file directly as the wanted user
COPY --chown=${USERNAME} requirements.txt setup.py ./
COPY --chown=${USERNAME} src/__init__.py src/

# Install requirements
RUN pip3 install -r requirements.txt

# Copy the rest of the files and directories
COPY --chown=${USERNAME} . .

# Recursively change permisions in folder in case there are files
# that still belong to root
RUN sudo chown -R ${USERNAME} .

# Switches to the user
USER ${USERNAME}
# Makes out a nice prompt in case you have to go inside of the container for any reason
RUN echo 'export PS1="🐳 \[\033[1;36m\][\u@docker] \[\033[1;34m\]\W\[\033[0;35m\] # \[\033[0m\]"' >> ~/.bashrc

# Runs jupyter lab inside the container. The -ip flag is needed to allow external access
# to jupyter lab. In our case that is our localhost connecting to the container.
CMD ["jupyter", "lab", "--ip=0.0.0.0"]
