locals {
  ml_{{ cookiecutter.repo_name }}_bucket_name = "{{ 'ml-' ~ cookiecutter.aws_infra_name ~ '-${var.environment}' }}"
}


module "ml_{{ cookiecutter.repo_name }}" {
  source = "../../../s3_bucket"

  bucket_name          = local.ml_{{ cookiecutter.repo_name }}
  s3_audit_logs_bucket = var.s3_audit_logs_bucket
  lifecycle_rules = [
    {
      id      = "bucket_cleanup"
      enabled = true

      prefix = "/"
      expiration = {
        days = 7
      }
    }
  ]
}
