variable environment {
  type        = string
  description = "indicates whether resource is deployed on production or staging"
  validation {
    condition     = contains(["production", "staging"], var.environment)
    error_message = "Valid values for var environment are production/staging."
  }
}

variable k8s_trust_relationship_policy {}

variable s3_audit_logs_bucket {
  description = "bucket name used for storing audit logs"
}