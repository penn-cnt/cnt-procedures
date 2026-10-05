output "site_url" {
  value = var.domain_name == "" ? "https://${aws_cloudfront_distribution.site.domain_name}" : "https://${var.domain_name}"
}
output "cloudfront_domain" { value = aws_cloudfront_distribution.site.domain_name }

# Copy these three into GitHub → repository → Settings → Secrets and variables → Actions → Variables
# (they are identifiers, not secrets).
output "AWS_ROLE_ARN" { value = aws_iam_role.deploy.arn }
output "S3_BUCKET" { value = aws_s3_bucket.site.bucket }
output "CLOUDFRONT_DISTRIBUTION_ID" { value = aws_cloudfront_distribution.site.id }
