# Kubernetes Minikube Deployment Guide & Documentation

This document serves as the complete step-by-step guide and submission template for the Kubernetes Minikube DevOps assignment.

---

## 📌 Project Overview
- **Backend Service**: Python Flask REST API running in Kubernetes Pods (Port `5000`, Service: `flask-backend-service`)
- **Frontend Service**: Express.js server rendering dynamic EJS UI (Port `3000`, NodePort Service: `30080`)
- **Orchestration**: Minikube local Kubernetes cluster

---

## 🚀 Master Step-by-Step Execution Plan

### Step 1: Start Minikube Cluster
```bash
minikube start --driver=docker
kubectl get nodes
```

### Step 2: Build & Load Docker Images inside Minikube
```bash
# Option A: Build inside minikube environment
eval $(minikube -p minikube docker-env)
docker build -t flask-backend:latest ./backend
docker build -t express-frontend:latest ./frontend

# Option B: Load existing Docker images into Minikube
minikube image load flask-backend:latest
minikube image load express-frontend:latest
```

### Step 3: Apply Kubernetes Manifests
```bash
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/frontend-deployment.yaml
```

### Step 4: Verify Deployments, Pods, and Services
```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

### Step 5: Access Application
```bash
minikube service express-frontend-service --url
```
Open the returned URL in your browser (e.g. `http://127.0.0.1:30080` or Minikube IP) to view your live full-stack Kubernetes application!
