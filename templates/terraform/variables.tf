# Proposed Terraform/OpenTofu variables generated for Daedalus review.
# Do not store secrets directly in this file.

variable "environment" {
  description = "Target environment name."
  type        = string
  default     = "lab"
}
