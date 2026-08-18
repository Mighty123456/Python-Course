#!/bin/bash
# Script to build Docker images directly into Minikube environment

set -e

echo "Pointing shell to Minikube's Docker daemon..."
eval $(minikube docker-env)

echo "Building Flask Backend container image..."
docker build -t flask-backend:latest ./backend

echo "Building Express Frontend container image..."
docker build -t express-frontend:latest ./frontend

echo "Container images built successfully in Minikube!"
docker images | grep -E "flask-backend|express-frontend"
