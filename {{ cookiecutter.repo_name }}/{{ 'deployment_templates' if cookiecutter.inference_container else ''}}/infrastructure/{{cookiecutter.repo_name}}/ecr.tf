resource "aws_ecr_repository" "ml-{{ cookiecutter.aws_infra_name }}" {
  name = "contentful/data/ml-{{ cookiecutter.aws_infra_name }}"
}