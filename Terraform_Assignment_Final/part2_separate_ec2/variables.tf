variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "ami_id" {
  type    = string
  default = "ami-0c7217cdde317cfec"
}

variable "key_name" {
  type    = string
  default = "aws_ansh"
}
