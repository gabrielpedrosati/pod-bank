// Groups

resource "aws_iam_group" "engenharia-de-dados" {
  name = "engenharia-de-dados"
  path = "/pod-bank/"
}

resource "aws_iam_group" "business-intelligence" {
  name = "business-intelligence"
  path = "/pod-bank/"
}

// Group Policies


