# Terraform AWS Deployment Guide & Documentation

This directory contains the complete infrastructure as code (IaC) configuration for deploying Flask and Express across 3 AWS architectures using Terraform.

---

## 📌 Structure Overview
- **`part1_single_ec2/`**: Single EC2 instance provisioning + Cloud-init Docker setup.
- **`part2_separate_ec2/`**: Custom VPC + 2 EC2 instances (1 Flask, 1 Express) + Security Groups.
- **`part3_ecr_ecs_alb/`**: ECR Repositories + VPC + ECS Fargate Cluster + Application Load Balancer.

---

## 🚀 Execution Steps

### 1. Initialize Terraform:
```bash
cd part1_single_ec2
terraform init
```

### 2. Preview Infrastructure Plan:
```bash
terraform plan
```

### 3. Apply and Provision Resources:
```bash
terraform apply -auto-approve
```

### 4. Destroy Resources (Avoid AWS Charges):
```bash
terraform destroy -auto-approve
```
