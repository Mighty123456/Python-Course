#!/bin/bash
# EC2 Instance User Data Bootstrapping Script
sudo yum update -y
sudo yum install docker git -y
sudo systemctl enable --now docker
sudo usermod -aG docker ec2-user

# Install docker-compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Clone project & start containers
git clone https://github.com/Mighty123456/Python-Course.git /home/ec2-user/app
cd /home/ec2-user/app/AWS_Assignment_Final
sudo /usr/local/bin/docker-compose up -d --build
