// Data Lake
resource "aws_s3_bucket" "pb-datalake" {
  bucket = var.s3_bucket_datalake

  tags = var.default_tags

}

// Repositories

resource "aws_s3_object" "pb-bucket-bronze" {
  key    = var.s3_bucket_datalake_bronze
  bucket = var.s3_bucket_datalake

  depends_on = [aws_s3_bucket.pb-datalake]
}

resource "aws_s3_object" "pb-bucket-silver" {
  key    = var.s3_bucket_datalake_silver
  bucket = var.s3_bucket_datalake

  depends_on = [aws_s3_bucket.pb-datalake]
}

resource "aws_s3_object" "pb-bucket-gold" {
  key    = var.s3_bucket_datalake_gold
  bucket = var.s3_bucket_datalake

  depends_on = [aws_s3_bucket.pb-datalake]
}

resource "aws_s3_object" "pb-bucket-resources" {
  key    = "resources/"
  bucket = var.s3_bucket_datalake

  depends_on = [aws_s3_bucket.pb-datalake]
}

resource "aws_s3_object" "pb-bucket-services" {
  key    = var.s3_bucket_datalake_services
  bucket = var.s3_bucket_datalake
  force_destroy = true

  depends_on = [aws_s3_bucket.pb-datalake]
}

// Departaments
resource "aws_s3_object" "pb-bucket-bronze-credito" {
  key    = "${var.s3_bucket_datalake_bronze}/credito/"
  bucket = var.s3_bucket_datalake

  depends_on = [aws_s3_bucket.pb-datalake]
}

resource "aws_s3_object" "pb-bucket-silver-credito" {
  key    = "${var.s3_bucket_datalake_silver}/credito/"
  bucket = var.s3_bucket_datalake

  depends_on = [aws_s3_bucket.pb-datalake]
}
