resource "aws_s3_bucket" "datalake" {
  bucket = var.s3_bucket_datalake

  tags = var.default_tags

}

resource "aws_s3_object" "datalake-raw" {
  key    = var.s3_bucket_datalake_raw
  bucket = var.s3_bucket_datalake

  depends_on = [aws_s3_bucket.datalake]
}

resource "aws_s3_object" "datalake-trusted" {
  key    = var.s3_bucket_datalake_trusted
  bucket = var.s3_bucket_datalake

  depends_on = [aws_s3_bucket.datalake]
}

resource "aws_s3_object" "datalake-curated" {
  key    = var.s3_bucket_datalake_curated
  bucket = var.s3_bucket_datalake

  depends_on = [aws_s3_bucket.datalake]
}