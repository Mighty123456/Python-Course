# AWS DevOps Multi-Architecture Deployment

A containerized full-stack application deployed across **3 distinct AWS architectures**, demonstrating real DevOps skills including Infrastructure as Code (Terraform), CI/CD automation (GitHub Actions), container orchestration (ECS Fargate), and deployment automation scripts.

**Stack:** Python Flask (REST API) + Node.js Express (Web Frontend) + Docker + AWS

---

## 📁 Project Structure

```
AWS_Assignment/
├── backend/
│   ├── app.py              # Flask REST API
│   ├── Dockerfile          # Container definition
│   └── requirements.txt    # Python deps
├── frontend/
│   ├── server.js           # Express web server
│   ├── Dockerfile          # Container definition
│   ├── package.json
│   └── views/index.ejs     # Dashboard UI
├── terraform/
│   ├── part1_single_ec2/   # Task 1 - Single EC2 IaC
│   ├── part2_separate_ec2/ # Task 2 - Dual EC2 + custom VPC IaC
│   └── part3_ecr_ecs_alb/  # Task 3 - ECR + ECS + ALB IaC
├── .github/workflows/
│   └── deploy.yml          # CI/CD pipeline
├── scripts/
│   ├── deploy.sh           # Deployment automation
│   └── cleanup.sh          # Resource teardown
├── Screenshots/            # Deployment evidence
└── docker-compose.yml      # Local dev orchestration
```

---

## 🚀 Quick Start (Local)

```bash
docker-compose up --build
```
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000/api/data
- Health check: http://localhost:5000/api/health

---

## 🏗 Task 1: Single EC2 Instance

Both services run on **one EC2 instance** using Docker Compose.

**Security Group ports:** 22 (SSH), 3000 (frontend), 5000 (backend)

```bash
# Provision with Terraform
cd terraform/part1_single_ec2
terraform init && terraform apply

# Or use the automation script
./scripts/deploy.sh task1
```

**Verification URLs after deployment:**
- `http://<EC2-PUBLIC-IP>:3000` → Express Dashboard
- `http://<EC2-PUBLIC-IP>:5000/api/health` → Flask health check

---

## 🔗 Task 2: Separate EC2 Instances (Custom VPC)

Flask Backend and Express Frontend run on **separate EC2 instances** inside a **custom VPC** (`10.0.0.0/16`).

The backend security group only accepts port 5000 traffic from instances in the same VPC — frontend communicates via the backend's **public IP** passed as `BACKEND_URL` env variable.

```bash
cd terraform/part2_separate_ec2
terraform init && terraform apply
```

**Verification:**
- `http://<FRONTEND-IP>:3000` → should show "Connected to Flask API" with backend's IP

---

## 📦 Task 3: ECR + ECS Fargate + ALB

Docker images pushed to **Amazon ECR**, deployed as services in an **ECS Fargate cluster**, with an **Application Load Balancer** routing traffic.

```bash
# 1. Provision ECR, VPC, ECS cluster, ALB
cd terraform/part3_ecr_ecs_alb
terraform init && terraform apply

# 2. Push images to ECR
aws ecr get-login-password --region eu-north-1 | \
  docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.eu-north-1.amazonaws.com

docker build -t aws-assignment/flask-backend ./backend
docker tag aws-assignment/flask-backend:latest \
  <ACCOUNT_ID>.dkr.ecr.eu-north-1.amazonaws.com/aws-assignment/flask-backend:latest
docker push <ACCOUNT_ID>.dkr.ecr.eu-north-1.amazonaws.com/aws-assignment/flask-backend:latest

# Repeat for frontend...
```

**Verification:**
- ALB DNS: `http://<ALB-DNS-NAME>` → Express Dashboard

---

## 🤖 CI/CD Pipeline (GitHub Actions)

On every push to `main`:
1. **Lint** — validates Python and Node.js syntax
2. **Build** — builds Docker images
3. **Push** — pushes images to ECR with `latest` tag

Required GitHub Secrets: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`

---

## 💰 Cost Optimization & Teardown

After completing the assignment and taking screenshots, destroy all resources:

```bash
./scripts/cleanup.sh
```

Or manually:
```bash
# Stop ECS services (set desired count to 0)
# Terminate EC2 instances
# Delete ECS cluster
cd terraform/part1_single_ec2 && terraform destroy -auto-approve
cd terraform/part2_separate_ec2 && terraform destroy -auto-approve
cd terraform/part3_ecr_ecs_alb && terraform destroy -auto-approve
```

**Cost estimate for ~1 hour of deployment:** ~₹0–₹5 (using t3.micro free tier)

---

## 📸 Screenshots

All deployment evidence screenshots are in the `Screenshots/` folder.
See `DEPLOYMENT_GUIDE.md` for the full step-by-step deployment log with annotated screenshots.
