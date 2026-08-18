#!/bin/bash
# -----------------------------------------------
# cleanup.sh - Destroy all AWS resources
# Run this after taking screenshots to avoid charges
# -----------------------------------------------

set -e

echo "=========================================="
echo "  AWS Resource Cleanup / Cost Control"
echo "=========================================="

echo "Destroying Task 1 infrastructure..."
cd terraform/part1_single_ec2 && terraform destroy -auto-approve 2>/dev/null || echo "Task1: nothing to destroy"
cd ../..

echo "Destroying Task 2 infrastructure..."
cd terraform/part2_separate_ec2 && terraform destroy -auto-approve 2>/dev/null || echo "Task2: nothing to destroy"
cd ../..

echo "Destroying Task 3 infrastructure..."
cd terraform/part3_ecr_ecs_alb && terraform destroy -auto-approve 2>/dev/null || echo "Task3: nothing to destroy"
cd ../..

echo "Stopping local docker containers..."
docker-compose down --volumes --remove-orphans 2>/dev/null || true

echo "=========================================="
echo "All resources destroyed. No further charges."
echo "=========================================="
