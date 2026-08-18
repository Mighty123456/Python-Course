# Kubernetes Microservices Assignment

**Repository Link**: https://github.com/Mighty123456/Python-Course

This project demonstrates a multi-container microservice application deployed on **Kubernetes (Minikube)**. It consists of a **Flask REST API (Backend)** and an **Express.js (Frontend)** communicating inside a Minikube cluster.

---

## 🛠 Project Structure

```
Kubernetes_Assignment/
├── backend/
│   ├── app.py                  # Flask backend with /healthz and /ready endpoints
│   ├── Dockerfile              # Commented Dockerfile for backend
│   └── requirements.txt
├── frontend/
│   ├── server.js               # Express server with /healthz endpoint
│   ├── Dockerfile              # Commented Dockerfile for frontend
│   ├── package.json
│   └── views/index.ejs         # Web interface template
├── k8s/
│   ├── 00-namespace.yaml       # Namespace isolation (devops-assignment)
│   ├── 01-configmap.yaml       # ConfigMap for application environment variables
│   ├── 02-secret.yaml          # Kubernetes Secret management
│   ├── 03-backend-deployment.yaml  # Backend Deployment + ClusterIP Service + Probes + Limits
│   ├── 04-frontend-deployment.yaml # Frontend Deployment + NodePort Service + Probes + Limits
│   └── 05-ingress.yaml         # Ingress Routing Rules
├── scripts/
│   ├── build.sh                # Script to build images inside Minikube
│   └── deploy.sh               # Script to apply all manifests in sequence
└── docker-compose.yml          # Local development reference file
```

---

## 🚀 How to Run locally with Minikube

### Step 1: Start Minikube & point Docker daemon
```bash
minikube start
eval $(minikube docker-env)
```

### Step 2: Build images inside Minikube
```bash
./scripts/build.sh
```

### Step 3: Deploy Kubernetes Manifests
```bash
./scripts/deploy.sh
```

### Step 4: Access the Frontend
```bash
minikube service express-frontend-service -n devops-assignment
```

---

## 🔒 Key Kubernetes Features Demonstrated

1. **Namespace Isolation**: Resources are deployed under `devops-assignment` namespace.
2. **Configuration Management**: `ConfigMap` supplies `BACKEND_URL` to frontend pods.
3. **Health & Readiness Checks**:
   - `livenessProbe` checks if container is alive.
   - `readinessProbe` ensures pod only receives traffic when ready.
4. **Resource Quotas**: Memory and CPU requests (`64Mi`/`100m`) and limits (`128Mi`/`250m`) defined per pod.
5. **Deployment Strategy**: `RollingUpdate` enables zero-downtime updates.
6. **Ingress Routing**: NGINX Ingress rules route `/` to frontend and `/api` to backend.
