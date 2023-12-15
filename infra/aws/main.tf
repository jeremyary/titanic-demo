provider "aws" {
  region = "us-west-1"
}

resource "aws_s3_bucket_ownership_controls" "feast_bucket_acl" {
  bucket = aws_s3_bucket.feast_bucket.bucket
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket" "feast_bucket" {
  bucket        = "titanic-ml-${var.project_name}"
  force_destroy = true
}

resource "aws_s3_bucket_acl" "feast_bucket_acl" {
  bucket = aws_s3_bucket.feast_bucket.bucket
  acl    = "private"
}

resource "aws_s3_object" "survivors_upload" {
  bucket = aws_s3_bucket.feast_bucket.bucket
  key    = "survivors_source.parquet"
  source = "${path.module}/../../data/survivors_source.parquet"
}

resource "aws_s3_object" "demographics_upload" {
  bucket = aws_s3_bucket.feast_bucket.bucket
  key    = "demographics_source.parquet"
  source = "${path.module}/../../data/demographics_source.parquet"
}

resource "aws_s3_object" "genealogy_upload" {
  bucket = aws_s3_bucket.feast_bucket.bucket
  key    = "genealogy_source.parquet"
  source = "${path.module}/../../data/genealogy_source.parquet"
}

resource "aws_s3_object" "trip_upload" {
  bucket = aws_s3_bucket.feast_bucket.bucket
  key    = "trip_source.parquet"
  source = "${path.module}/../../data/trip_source.parquet"
}


