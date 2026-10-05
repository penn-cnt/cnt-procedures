terraform {
  required_version = ">= 1.6"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
  # State is kept locally (terraform.tfstate, gitignored). To share it, move it to an S3 backend:
  # backend "s3" { bucket = "<state-bucket>" key = "cnt-procedures/terraform.tfstate" region = "us-east-1" }
}

# CloudFront certificates and WAF for CloudFront must live in us-east-1.
provider "aws" {
  region = "us-east-1"
  default_tags {
    tags = { Project = var.project, ManagedBy = "terraform", Repository = var.github_repo }
  }
}
