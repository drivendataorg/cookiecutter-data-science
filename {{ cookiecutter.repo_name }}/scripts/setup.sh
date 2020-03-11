#!/bin/bash
# Borrowed from Julius Busecke's cookiecutter.
curl -u '{{ cookiecutter.github_username }}' https://api.github.com/user/repos -d '{"name":"{{ cookiecutter.project_name.lower().replace(' ', '_') }}", "private":{{ cookiecutter.repo_private }}}'

# Link local repository to git
git init
git add *
git add .gitignore .pre-commit-config.yaml
git commit -m 'first commit'
git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_name.lower().replace(' ', '_') }}.git
git push -u origin master
