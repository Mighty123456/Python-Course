variable "aws_region" {
  type    = string
  default = "eu-north-1"
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "ami_id" {
  type        = string
  description = "Ubuntu 24.04 AMI ID for region"
  default     = "ami-00366d25265691d5a"
}

variable "key_name" {
  type    = string
  default = "assignment"
}
