#! /bin/bash
set -e

lc(){
    echo "$1" |tr '[:upper:]' '[:lower:]'
}

# Initial sync of data folder to project specific prefix under the manifold-projects bucket
if [[ $(lc "{{ cookiecutter.s3_bucket }}") != "[optional]"* ]] ;
then
    S3_PATH="s3://{{ cookiecutter.s3_bucket }}/{{ cookiecutter.repo_name }}"
    echo "Creating shared data folders at $S3_PATH..."
    aws s3 sync data "$S3_PATH" --profile {{ cookiecutter.aws_profile }}
    echo "Done."
fi

# Log in to ECR
echo "Performing docker login to AWS container registry..."
aws ecr get-login --no-include-email --profile {{ cookiecutter.aws_profile }}| sh
echo "Done."

echo "All set! Run the start.sh script and open Kitematic from the Docker minibar menu to make sure your container is running the Jupyter service."
