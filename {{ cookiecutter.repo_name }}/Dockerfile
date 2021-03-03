FROM python:3.9-slim


# Gets all updates if needed
RUN apt update && apt install -y 

# Makes out a nice prompt in case you have to go inside of the container for any reason
RUN echo 'export PS1="🐳 \[\033[1;36m\][\u@docker] \[\033[1;34m\]\W\[\033[0;35m\] # \[\033[0m\]"' >> ~/.bashrc

WORKDIR /app

# It copies all the files that do not change often. Speeds up rebuild process
COPY requirements.txt setup.py ./
COPY src/__init__.py src/

# Install requirements
RUN pip3 install -r requirements.txt

# Copy the rest of the files and directories
COPY . .

# Runs jupyter lab inside the container as the root user. Flag is needed since running a container as root is not recomended
CMD ["jupyter", "lab", "--allow-root", "--ip=0.0.0.0"]