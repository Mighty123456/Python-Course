# Terraform AWS Infrastructure Provisioning Assignment

**Repository Link**: https://github.com/Mighty123456/Python-Course

This repository contains the complete Infrastructure as Code (IaC) implementation for provisioning a containerized microservice application (Flask REST API + Express Frontend) across three distinct AWS deployment architectures using **Terraform**.

---

## 📁 Repository Architecture

```
Terraform_Assignment/
├── backend/
│   ├── app.py                  # Flask backend REST API
│   ├── Dockerfile              # Backend container build instructions
│   └── requirements.txt
├── frontend/
│   ├── server.js               # Express frontend web server
│   ├── Dockerfile              # Frontend container build instructions
│   ├── package.json
│   └── views/index.ejs
├── part1_single_ec2/
│   ├── main.tf                 # Part 1: Single EC2 + Security Group
│   ├── variables.tf            # Parameterized variables
│   ├── outputs.tf              # EC2 IP and URL outputs
│   ├── backend.tf              # S3 remote state configuration
│   └── user_data.sh            # User data bootstrapping script
├── part2_separate_ec2/
│   ├── main.tf                 # Part 2: Dual EC2s + Custom VPC
│   ├── variables.tf
│   ├── outputs.tf
│   ├── backend.tf
│   ├── user_data_backend.sh    # Backend provisioning script
│   └── user_data_frontend.sh   # Frontend provisioning script
├── part3_ecr_ecs_alb/
│   ├── main.tf                 # Part 3: ECR repos, ECS Fargate cluster, ALB
│   ├── variables.tf
│   ├── outputs.tf
│   └── backend.tf
├── docker-compose.yml          # Local development reference
└── screenshots/                # AWS Console execution proof
```

---

## 🚀 How to Provision Infrastructure with Terraform

### Part 1: Single EC2 Deployment (Docker Compose)
```bash
cd part1_single_ec2
terraform init
terraform plan
terraform apply -auto-approve
```
*Outputs*: `ec2_public_ip`, `frontend_url` (`http://<IP>:3000`), `backend_api_url` (`http://<IP>:5000`)

---

### Part 2: Separate EC2 Instances (Custom VPC)
```bash
cd part2_separate_ec2
terraform init
terraform plan
terraform apply -auto-approve
```
*Infrastructure Created*: Custom VPC (`10.0.0.0/16`), Public Subnet (`10.0.1.0/24`), Internet Gateway, Route Table, 2 Security Groups, 2 EC2 Instances (`Task2-Backend-EC2` & `Task2-Frontend-EC2`).

---

### Part 3: ECR + ECS Fargate + ALB Infrastructure
```bash
cd part3_ecr_ecs_alb
terraform init
terraform plan
terraform apply -auto-approve
```
*Infrastructure Created*: 2 ECR Repositories (`aws-assignment/flask-backend`, `aws-assignment/express-frontend`), ECS Cluster (`aws-devops-cluster`), Application Load Balancer (`ecs-alb`).

---

## 🛡 Security & State Management
1. **Parameterization**: Credentials and instance types are managed via `variables.tf`.
2. **Remote State**: S3 backend configuration (`backend.tf`) ensures remote state locking and tracking.
3. **Security Groups**: Principle of least privilege applied across ports `22`, `80`, `3000`, and `5000`.
