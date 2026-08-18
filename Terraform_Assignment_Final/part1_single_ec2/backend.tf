# S3 Backend Remote State Management Reference
terraform {
  backend "s3" {
    bucket         = "terraform-state-devops-assignment-bucket"
    key            = "part1/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
  }
}
