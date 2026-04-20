module "secrets-manager" {
  source  = "terraform-aws-modules/secrets-manager/aws"
  version = "2.1.0"

  name_prefix = "demo"
  description = "Example Secrets Manager secret"

  secret_string         = jsonencode({ username = "update-me" })
  ignore_secret_changes = true

  tags = {
    Environment = "Development"
    Project     = "Example"
  }
}