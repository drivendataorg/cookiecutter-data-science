#! /bin/bash

# Initial sync of data folder to project specific prefix under the manifold-projects bucket
echo "Creating shared data folders at s3://manifold-projects/{{ cookiecutter.repo_name }}..."
aws s3 sync data s3://manifold-projects/{{ cookiecutter.repo_name }} 
echo "Done."

# Log in to ECR 
echo "Performing docker login to AWS container registry..."
aws ecr get-login --no-include-email | sh
echo "Done."

echo "All set! Run the start.sh script and open Kitematic from the Docker minibar menu to make sure your container is running the Jupyter service."
