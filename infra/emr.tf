resource "aws_emr_cluster" "cluster" {
  name = "${var.namespace}-${var.project}-${var.stage}-emr"
  depends_on = [
    aws_subnet.public_subnet,
    aws_security_group.security_group_spark,
    aws_key_pair.emr_key_pair,
    aws_iam_role.emr_service_role,
    aws_iam_instance_profile.emr_ec2_profile
  ]

  release_label = var.emr_release
  applications  = var.emr_applications
  service_role  = aws_iam_role.emr_service_role.arn
  auto_termination_policy = {
    idle_timeout = 3600
  }

  termination_protection            = false
  step_concurrency_level            = 1
  keep_job_flow_alive_when_no_steps = true
  log_uri                           = "s3://${aws_s3_bucket.pb-datalake.bucket}/${aws_s3_object.pb-bucket-services.key}emr/${var.s3_log_uri}"

  ec2_attributes {
    subnet_id                         = element(aws_subnet.public_subnet.*.id, 0)
    emr_managed_master_security_group = aws_security_group.security_group_spark.id
    emr_managed_slave_security_group  = aws_security_group.security_group_spark.id
    instance_profile                  = aws_iam_instance_profile.emr_ec2_profile.arn
    key_name                          = aws_key_pair.emr_key_pair.key_name
  }

  master_instance_group {
    instance_type = var.emr_master_instance_type
  }

  core_instance_group {
    instance_type  = var.emr_core_instance.type
    instance_count = var.emr_core_instance.count
  }

  tags = merge(var.default_tags, {
    category                                 = "processing",
    resource                                 = "spark",
    for-use-with-amazon-emr-managed-policies = true
  })
}