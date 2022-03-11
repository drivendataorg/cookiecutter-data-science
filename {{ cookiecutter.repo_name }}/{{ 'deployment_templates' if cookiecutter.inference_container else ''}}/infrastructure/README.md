# Infrastructure

This directory contains the Terraform code to create the necessary infrastructure for this project in our AWS 
accounts. To deploy this infrastructure you will need to copy this directory to the [data-infrastructure](https://github.com/contentful/data-infrastructure) repo.

Follow these steps:
1. clone the repo:  
```git clone https://github.com/contentful/data-infrastructure```


2. copy the templates over:  
`cp .{{ cookiecutter.repo_name }} <path_to_data_infrastructure_repo>/src/modules/dags/ml-predictions/`

3. add the following module to `<path_to_data_infrastructure_repo>/src/modules/dags/main.tf`:  
```terraform
module "{{ 'ml-' ~ cookiecutter.aws_infra_name }}" {
  source                        = "{{'./ml-predictions/' ~ cookiecutter.aws_infra_name }}"
  environment                   = var.environment
  s3_audit_logs_bucket          = var.s3_audit_logs_bucket
  k8s_trust_relationship_policy = var.k8s_trust_relationship_policy
}
```

4. add the following to `<path_to_data_infrastructure_repo>/src/production/us-east-1/airflow/ecr-repositories.tf`:
```terraform
module "{{'ml-' ~ cookiecutter.aws_infra_name }}" {
  source = "../../../modules/ecr"
  ecr_name = "{{ 'contentful/data/ml-' ~ cookiecutter.aws_infra_name }}"
}
```

5. create a branch, commit and make a PR. Once it is accepted and merged the infrastructure will be available.
