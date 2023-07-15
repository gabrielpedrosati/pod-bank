// Database
resource "aws_glue_catalog_database" "pod-bank-database-raw" {
  name = "podbank_database_raw"
}

resource "aws_glue_catalog_database" "pod-bank-database-trusted" {
  name = "podbank_database_trusted"
}

resource "aws_glue_catalog_database" "pod-bank-database-curated" {
  name = "podbank_database_curated"
}

// Crawlers
resource "aws_glue_crawler" "raw-database" {
  database_name = aws_glue_catalog_database.pod-bank-database-raw.name
  name          = "crawler_raw"
  description   = "Crawler para identificar metadados dos arquivos da camada raw."
  role          = "arn:aws:iam::524095156763:role/glue-full-access"

  s3_target {
    path = "s3://${aws_s3_object.datalake-raw.bucket}/${aws_s3_object.datalake-raw.key}"
  }
}

resource "aws_glue_crawler" "trusted-database" {
  database_name = aws_glue_catalog_database.pod-bank-database-raw.name
  name          = "crawler_trusted"
  description   = "Crawler para identificar metadados dos arquivos da camada trusted."
  role          = "arn:aws:iam::524095156763:role/glue-full-access"

  s3_target {
    path = "s3://${aws_s3_object.datalake-trusted.bucket}/${aws_s3_object.datalake-trusted.key}"
  }
}

resource "aws_glue_crawler" "curated-database" {
  database_name = aws_glue_catalog_database.pod-bank-database-raw.name
  name          = "crawler_curated"
  description   = "Crawler para identificar metadados dos arquivos da camada curated."
  role          = "arn:aws:iam::524095156763:role/glue-full-access"

  s3_target {
    path = "s3://${aws_s3_object.datalake-curated.bucket}/${aws_s3_object.datalake-curated.key}"
  }
}