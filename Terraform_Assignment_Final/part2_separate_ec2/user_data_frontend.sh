#!/bin/bash
sudo yum update -y
sudo yum install docker git -y
sudo systemctl enable --now docker
git clone https://github.com/Mighty123456/Python-Course.git /home/ec2-user/app
cd /home/ec2-user/app/AWS_Assignment_Final/frontend
sudo docker build -t express-frontend .
sudo docker run -d -p 3000:3000 -e BACKEND_URL=http://${backend_ip}:5000 --name frontend express-frontend
