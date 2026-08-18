provider "aws" {
  region = var.aws_region
}

resource "aws_ecr_repository" "flask_backend" {
  name                 = "aws-assignment/flask-backend"
  image_tag_mutability = "MUTABLE"
}

resource "aws_ecr_repository" "express_frontend" {
  name                 = "aws-assignment/express-frontend"
  image_tag_mutability = "MUTABLE"
}

resource "aws_vpc" "ecs_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags                 = { Name = "ecs-vpc" }
}

resource "aws_subnet" "ecs_subnet_a" {
  vpc_id                  = aws_vpc.ecs_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "${var.aws_region}a"
  map_public_ip_on_launch = true
}

resource "aws_subnet" "ecs_subnet_b" {
  vpc_id                  = aws_vpc.ecs_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "${var.aws_region}b"
  map_public_ip_on_launch = true
}

resource "aws_internet_gateway" "ecs_igw" {
  vpc_id = aws_vpc.ecs_vpc.id
}

resource "aws_route_table" "ecs_rt" {
  vpc_id = aws_vpc.ecs_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.ecs_igw.id
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.ecs_subnet_a.id
  route_table_id = aws_route_table.ecs_rt.id
}

resource "aws_route_table_association" "b" {
  subnet_id      = aws_subnet.ecs_subnet_b.id
  route_table_id = aws_route_table.ecs_rt.id
}

resource "aws_security_group" "alb_sg" {
  name   = "alb-sg"
  vpc_id = aws_vpc.ecs_vpc.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_lb" "ecs_alb" {
  name               = "ecs-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_sg.id]
  subnets            = [aws_subnet.ecs_subnet_a.id, aws_subnet.ecs_subnet_b.id]
}

resource "aws_ecs_cluster" "main_cluster" {
  name = "tf-ecs-cluster"
}
