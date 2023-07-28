// Database
resource "aws_glue_catalog_database" "pb-database-bronze" {
  name = "pb-database-bronze"
}

resource "aws_glue_catalog_database" "pb-database-silver" {
  name = "pb-database-silver"
}

resource "aws_glue_catalog_database" "pb-database-gold" {
  name = "pb-database-gold"
}

// Crawlers
resource "aws_glue_crawler" "pb-crawler-bronze" {
  database_name = aws_glue_catalog_database.pb-database-bronze.name
  name          = "pb-crawler-bronze"
  description   = "Crawler para identificar metadados dos arquivos da camada bronze."
  role          = "arn:aws:iam::524095156763:role/glue-full-access"

  s3_target {
    path = "s3://${aws_s3_object.pb-bucket-bronze.bucket}/${aws_s3_object.pb-bucket-bronze.key}"
  }
}

resource "aws_glue_crawler" "pb-crawler-silver" {
  database_name = aws_glue_catalog_database.pb-database-silver.name
  name          = "pb-crawler-silver"
  description   = "Crawler para identificar metadados dos arquivos da camada silver."
  role          = "arn:aws:iam::524095156763:role/glue-full-access"

  s3_target {
    path = "s3://${aws_s3_object.pb-bucket-silver.bucket}/${aws_s3_object.pb-bucket-silver.key}"
  }
}

resource "aws_glue_crawler" "pb-crawler-gold" {
  database_name = aws_glue_catalog_database.pb-database-gold.name
  name          = "pb-crawler-gold"
  description   = "Crawler para identificar metadados dos arquivos da camada gold."
  role          = "arn:aws:iam::524095156763:role/glue-full-access"

  s3_target {
    path = "s3://${aws_s3_object.pb-bucket-gold.bucket}/${aws_s3_object.pb-bucket-gold.key}"
  }
}