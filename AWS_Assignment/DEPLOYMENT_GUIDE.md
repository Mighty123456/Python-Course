# AWS DevOps Deployment Project Guide & Documentation

This document serves as the complete step-by-step guide and submission template for the AWS DevOps assignment.

---

## 📌 Project Overview
- **Frontend**: Node.js Express server + EJS views (Port `3000`)
- **Backend**: Python Flask REST API (Port `5000`)
- **Containerization**: Docker & Docker Compose setup included

---

## 🚀 Task 1: Deploying on a Single Amazon EC2 Instance

### Objective
Host both the Flask backend and Express frontend on one Ubuntu 24.04 LTS / Amazon Linux 2023 EC2 instance.

### Step-by-Step Instructions
1. **Launch EC2 Instance**:
   - OS: Ubuntu 24.04 LTS (Free tier eligible `t2.micro` or `t3.micro`).
   - Security Group Rules:
     - SSH (Port 22) - `0.0.0.0/0`
     - HTTP (Port 80) - `0.0.0.0/0`
     - Custom TCP (Port 3000) - `0.0.0.0/0`
     - Custom TCP (Port 5000) - `0.0.0.0/0`

2. **SSH into Instance & Clone Repo**:
   ```bash
   ssh -i "your-key.pem" ubuntu@<EC2-PUBLIC-IP>
   sudo apt update && sudo apt install -y git docker.io docker-compose
   sudo usermod -aG docker ubuntu
   git clone <YOUR_GITHUB_REPO_URL>
   cd AWS_Assignment
   ```

3. **Run using Docker Compose**:
   ```bash
   sudo docker-compose up -d --build
   ```

4. **Verification**:
   - Access Express Frontend: `http://<EC2-PUBLIC-IP>:3000`
   - Access Flask Backend: `http://<EC2-PUBLIC-IP>:5000`

---

## 🚀 Task 2: Deploying on Separate EC2 Instances

### Objective
Host Flask Backend on **EC2 Instance A** and Express Frontend on **EC2 Instance B**.

### Step-by-Step Instructions
1. **EC2 Instance A (Backend)**:
   - Security Group: Allow Port 5000 (from EC2 Instance B Public/Private IP or `0.0.0.0/0`).
   - Commands:
     ```bash
     cd AWS_Assignment/backend
     sudo docker build -t flask-backend .
     sudo docker run -d -p 5000:5000 flask-backend
     ```
   - Note the Public IP of Instance A (e.g. `http://<BACKEND-EC2-IP>:5000`).

2. **EC2 Instance B (Frontend)**:
   - Security Group: Allow Port 3000 (`0.0.0.0/0`).
   - Commands:
     ```bash
     cd AWS_Assignment/frontend
     sudo docker build -t express-frontend .
     sudo docker run -d -p 3000:3000 -e BACKEND_URL="http://<BACKEND-EC2-IP>:5000" express-frontend
     ```

3. **Verification**:
   - Access `http://<FRONTEND-EC2-IP>:3000`. You should see "Backend Status: Connected" pointing to EC2 Instance A.

---

## 🚀 Task 3: Deploying Containers using AWS ECR, ECS & VPC

### Objective
Push Docker images to AWS ECR and deploy container tasks using AWS ECS (Fargate) within a custom or default VPC.

### Step-by-Step Instructions
1. **AWS ECR Setup**:
   - Authenticate AWS CLI to ECR:
     ```bash
     aws ecr get-login-password --region <YOUR-REGION> | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com
     ```
   - Create ECR Repositories:
     ```bash
     aws ecr create-repository --repository-name flask-backend
     aws ecr create-repository --repository-name express-frontend
     ```
   - Tag and Push Images:
     ```bash
     docker tag backend:latest <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/flask-backend:latest
     docker push <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/flask-backend:latest

     docker tag frontend:latest <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/express-frontend:latest
     docker push <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/express-frontend:latest
     ```

2. **AWS ECS Cluster & Task Definition**:
   - Create an ECS Cluster named `aws-devops-cluster`.
   - Create ECS Task Definition (Fargate) containing two container definitions or separate services for backend and frontend.
   - Configure environment variable `BACKEND_URL` in the frontend task.

3. **Deploy ECS Services**:
   - Launch Tasks/Services in your default VPC & subnets with Security Groups exposing Ports 3000 and 5000.

---

## 📦 Final Zip Submission Steps
1. Create a root directory `AWS_YourName` (e.g. `AWS_Nirav Patel`).
2. Put the full project source code inside (`backend`, `frontend`, `docker-compose.yml`, `README.md`).
3. Export or copy your completed Word/PDF document containing screenshots into `AWS_YourName/`.
4. Compress into `AWS_YourName.zip`.
