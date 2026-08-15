# AWS DevOps Deployment Project

This repository contains the complete code for deploying a **Flask Backend** and an **Express Frontend** on **AWS** across three different deployment architectures:

1. **Task 1: Single EC2 Instance Deployment**
2. **Task 2: Separate EC2 Instances Deployment**
3. **Task 3: AWS ECR, ECS (Fargate/EC2) & VPC Containerized Deployment**

## Project Architecture

- **Backend**: Python Flask REST API running on Port `5000`.
- **Frontend**: Node.js Express Server rendering dynamic EJS UI on Port `3000`.

## Local Development (Using Docker Compose)

```bash
docker-compose up --build
```
Access Frontend at `http://localhost:3000` and Backend API at `http://localhost:5000`.
