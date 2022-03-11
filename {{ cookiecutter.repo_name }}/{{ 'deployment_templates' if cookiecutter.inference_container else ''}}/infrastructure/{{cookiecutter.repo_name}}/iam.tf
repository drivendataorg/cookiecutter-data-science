resource "aws_iam_role" "airflow-{{ cookiecutter.aws_infra_name }}" {
  name               = "airflow-{{ cookiecutter.aws_infra_name }}"
  assume_role_policy = var.k8s_trust_relationship_policy
}

resource "aws_iam_role_policy_attachment" "airflow_{{ cookiecutter.repo_name }}" {
  role       = aws_iam_role.airflow-{{ cookiecutter.aws_infra_name }}.name
  policy_arn = aws_iam_policy.airflow-{{ cookiecutter.aws_infra_name }}.arn
}

resource "aws_iam_policy" "airflow_{{ cookiecutter.repo_name }}" {
  name        = "airflow_{{ cookiecutter.repo_name }}"
  description = "Permissions granted to {{ cookiecutter.project_name }} IAM role (e.g. S3 access)"
  policy = templatefile("${path.module}/policies/{{ cookiecutter.repo_name }}_access_policy.tpl", {
    ml_{{ cookiecutter.repo_name }}_bucket = local.ml_{{ cookiecutter.repo_name }}_bucket_name
  })
}
