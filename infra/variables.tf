// Budgets
variable "budget_email" {
  description = "Email to receive budgets notifications."
  type        = string
  default     = "gabrielpedrosati@gmail.com"
}

// S3
variable "s3_bucket_datalake" {
  default     = "pod-bank-datalake-524095156763"
  description = "S3 bucket data lake."
}

variable "s3_bucket_datalake_raw" {
  default     = "raw/"
  description = "Bucket to store landing data."
}

variable "s3_bucket_datalake_trusted" {
  default     = "trusted/"
  description = "Bucket to store transformed data."
}

variable "s3_bucket_datalake_curated" {
  default     = "curated/"
  description = "Bucke to store data ready to be consumed."
}

// Default tags
variable "default_tags" {
  default = {
    Empresa = "PoD Bank"
    Projeto = "Datalake"
  }
}