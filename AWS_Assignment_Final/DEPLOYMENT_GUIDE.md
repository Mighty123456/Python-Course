# Deployment Guide & Evidence Log

This document shows my actual deployment process across all 3 AWS architectures with verification screenshots.

---

## Architecture Overview

```
TASK 1: Single EC2
  └── EC2 (t3.micro, Ubuntu)
        ├── Docker: flask-backend (port 5000)
        └── Docker: express-frontend (port 3000)

TASK 2: Dual EC2 + Custom VPC (10.0.0.0/16)
  ├── EC2-A (Backend) → flask-backend container (port 5000)
  │     └── Security Group: port 5000 open to VPC
  └── EC2-B (Frontend) → express-frontend container (port 3000)
        └── BACKEND_URL=http://<EC2-A-IP>:5000

TASK 3: ECR + ECS Fargate + ALB
  ├── ECR: aws-assignment/flask-backend
  ├── ECR: aws-assignment/express-frontend
  ├── ECS Cluster: aws-devops-cluster (Fargate)
  │     ├── Service: flask-backend-service
  │     └── Service: express-frontend-service
  └── ALB: routes port 80 → ECS target group (port 3000)
```

---

## Security Group Rules Reference

| Task | Resource | Port | Source | Purpose |
|------|----------|------|--------|---------|
| Task 1 | single-ec2-sg | 22 | 0.0.0.0/0 | SSH access |
| Task 1 | single-ec2-sg | 3000 | 0.0.0.0/0 | Frontend |
| Task 1 | single-ec2-sg | 5000 | 0.0.0.0/0 | Backend API |
| Task 2 | backend-sg | 5000 | 0.0.0.0/0 | Backend API |
| Task 2 | frontend-sg | 3000 | 0.0.0.0/0 | Frontend |
| Task 3 | alb-sg | 80 | 0.0.0.0/0 | ALB HTTP |
| Task 3 | ecs-tasks-sg | 3000 | alb-sg | ECS tasks |

---

## Task 1: Single EC2 Deployment

### Steps I followed:

1. Ran `terraform apply` in `terraform/part1_single_ec2/`
2. SSH'd into the instance using the `.pem` key
3. Cloud-init user_data automatically ran docker-compose on boot
4. Verified both services running with `docker ps`
5. Opened browser to EC2 public IP on ports 3000 and 5000

**Evidence:** See screenshots `task1_ec2_running.png`, `task1_frontend_live.png`, `task1_backend_health.png`

---

## Task 2: Separate EC2 Instances

### Steps I followed:

1. Ran `terraform apply` in `terraform/part2_separate_ec2/`
2. Terraform created: custom VPC, subnet, IGW, route table, 2 security groups, 2 EC2 instances
3. User_data on Backend EC2 auto-ran the backend container
4. User_data on Frontend EC2 auto-ran the frontend container with `BACKEND_URL=http://<backend-ip>:5000`
5. Confirmed frontend dashboard showed "Connected to Flask API" with backend hostname

**Key learning:** The frontend container needs the backend EC2's *public* IP passed as env variable at launch time.

**Evidence:** See screenshots `task2_both_ec2_running.png`, `task2_frontend_connected.png`, `task2_backend_health.png`, `task2_vpc_config.png`

---

## Task 3: ECR + ECS Fargate

### Steps I followed:

1. Ran `terraform apply` in `terraform/part3_ecr_ecs_alb/` to create ECR repos, VPC, ECS cluster, ALB
2. Authenticated Docker to ECR with `aws ecr get-login-password`
3. Built and pushed both images to ECR repositories
4. Created ECS task definitions for both services
5. Created ECS services with desired count = 1 each
6. Waited for tasks to reach RUNNING state

**Evidence:** See screenshots `task3_ecr_repos.png`, `task3_ecr_images_pushed.png`, `task3_ecs_cluster_active.png`, `task3_ecs_services_running.png`, `task3_ecs_tasks_running.png`

---

## Cost Optimization

After collecting all screenshots, I ran `./scripts/cleanup.sh` which:
1. Ran `terraform destroy` on all 3 parts
2. Stopped all ECS services and tasks
3. Terminated both EC2 instances
4. Removed Docker local caches

**Total AWS cost for this assignment session:** ~₹2-3 (under 2 hours of t3.micro usage)
