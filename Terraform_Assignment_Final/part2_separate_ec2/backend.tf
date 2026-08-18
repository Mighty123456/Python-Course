terraform {
  backend "s3" {
    bucket         = "terraform-state-devops-assignment-bucket"
    key            = "part2/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
  }
}
