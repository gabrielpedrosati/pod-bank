// Groups

resource "aws_iam_group" "engenharia-de-dados" {
  name = "engenharia-de-dados"
  path = "/pod-bank/"
}

resource "aws_iam_group" "business-intelligence" {
  name = "business-intelligence"
  path = "/pod-bank/"
}

// Policies
resource "aws_iam_policy" "engenharia-de-dados" {
  name        = "EngenhariaDeDadosServices"
  path        = "/pod-bank/"
  description = "Acesso aos serviços utilizados pela equipe de Engenharia de Dados."

  policy = file("./json-policy/engenharia-de-dados-services.json")

  tags = merge(
    var.default_tags,
    {
      Equipe = "Engenharia De Dados"
    }
  )

}

// Attach policy to group
resource "aws_iam_group_policy_attachment" "engenharia-de-dados-attach" {
  group      = aws_iam_group.engenharia-de-dados.name
  policy_arn = aws_iam_policy.engenharia-de-dados.arn
}

resource "aws_iam_role" "emr_service_role" {
  name        = "${var.namespace}-${var.project}-${var.stage}-iam-emr-role"
  description = "Default service role for EMR"

  assume_role_policy = file("./permissions/EmrDefaultRole.json")
}

resource "aws_iam_role_policy" "iam_emr_service_policy" {
  name = "${var.namespace}-${var.project}-${var.stage}-iam-emr-service-policy"

  role   = aws_iam_role.emr_service_role.id
  policy = file("./permissions/EmrDefaultPolicyDeprecated.json")
}

resource "aws_iam_role" "emr_ec2_role" {
  name        = "${var.namespace}-${var.project}-${var.stage}-iam-emr-ec2-role"
  description = "Default role for EMR EC2"

  assume_role_policy = file("./permissions/EmrEc2DefaultRole.json")
}

resource "aws_iam_role_policy" "emr_profile_policy" {
  name = "${var.namespace}-${var.project}-${var.stage}-iam-emr-profile-policy"

  role   = aws_iam_role.emr_ec2_role.id
  policy = file("./permissions/EmrEc2DefaultPolicy.json")
}

resource "aws_iam_instance_profile" "emr_ec2_profile" {
  name = "${var.namespace}-${var.project}-${var.stage}-emr-ec2-profile"
  role = aws_iam_role.emr_ec2_role.name
}