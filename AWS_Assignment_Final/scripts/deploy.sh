#!/bin/bash
# -----------------------------------------------
# deploy.sh - Manual deployment helper script
# Usage: ./scripts/deploy.sh <task1|task2|task3>
# -----------------------------------------------

set -e

TASK=${1:-task1}
REGION=${AWS_REGION:-eu-north-1}

echo "=========================================="
echo "AWS DevOps Deployment Script"
echo "Task: $TASK | Region: $REGION"
echo "=========================================="

case $TASK in
  task1)
    echo "Deploying Task 1: Single EC2 via Terraform..."
    cd terraform/part1_single_ec2
    terraform init
    terraform apply -auto-approve
    echo "Task 1 complete! Frontend: http://$(terraform output -raw instance_public_ip):3000"
    ;;

  task2)
    echo "Deploying Task 2: Dual EC2 via Terraform..."
    cd terraform/part2_separate_ec2
    terraform init
    terraform apply -auto-approve
    echo "Task 2 complete!"
    echo "  Backend:  http://$(terraform output -raw backend_public_ip):5000"
    echo "  Frontend: http://$(terraform output -raw frontend_public_ip):3000"
    ;;

  task3)
    echo "Deploying Task 3: ECR + ECS + ALB via Terraform..."
    cd terraform/part3_ecr_ecs_alb
    terraform init
    terraform apply -auto-approve
    echo "Task 3 infrastructure ready. Push images then run ECS services."
    ;;

  *)
    echo "Usage: $0 <task1|task2|task3>"
    exit 1
    ;;
esac
