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