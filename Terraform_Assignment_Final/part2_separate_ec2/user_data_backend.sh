#!/bin/bash
sudo yum update -y
sudo yum install docker git -y
sudo systemctl enable --now docker
git clone https://github.com/Mighty123456/Python-Course.git /home/ec2-user/app
cd /home/ec2-user/app/AWS_Assignment_Final/backend
sudo docker build -t flask-backend .
sudo docker run -d -p 5000:5000 --name backend flask-backend
