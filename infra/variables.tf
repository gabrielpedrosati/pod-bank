// Global variables
variable "namespace" {
  description = "Namespace prefix"
  type        = string
  default     = "pb"
}

variable "stage" {
  description = "Stage prefix"
  type        = string
  default     = "dev"
}

variable "project" {
  description = "Application name prefix"
  type        = string
  default     = "dl"
}

// AWS region
variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "availability_zones" {
  description = "AWS region availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d"]
}

// EC2 key pair
variable "ec2_key_pair" {
  description = "EMR Cluster EC2 key pair name"
  type        = string
  default     = "emr-cluster"
}

// VPC subnets
variable "public_subnets" {
  description = "ERM vpc public subnets"
  type        = list(string)
  default     = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
}

variable "private_subnets" {
  description = "ERM vpc private subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

// EMR settings
variable "emr_release" {
  description = "ERM cluster release version"
  type        = string
  default     = "emr-6.7.0"
}

variable "emr_applications" {
  description = "ERM cluster application list"
  type        = list(string)
  default     = ["Hadoop", "Spark", "Zeppelin"]
}

variable "emr_master_instance_type" {
  description = "ERM master EC2 instance type"
  type        = string
  default     = "m4.large"
}

variable "emr_core_instance" {
  description = "ERM worker EC2 instance settings"
  type        = object({ type = string, count = number })
  default = {
    type  = "m4.large"
    count = 2
  }
}

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

variable "s3_bucket_datalake_bronze" {
  default     = "bronze/"
  description = "Bucket to store landing data."
}

variable "s3_bucket_datalake_silver" {
  default     = "silver/"
  description = "Bucket to store transformed data."
}

variable "s3_bucket_datalake_gold" {
  default     = "gold/"
  description = "Bucket to store data ready to be consumed."
}

variable "s3_bucket_datalake_services" {
  default     = "services/"
  description = "Bucket to store services output data."
}

variable "s3_log_uri" {
  description = "S3 EMR log bucket"
  type        = string
  default     = "cluster/logs"
}

// Default tags
variable "default_tags" {
  default = {
    namespace = "pb"
    project   = "dl"
    stage     = "dev"
  }
}