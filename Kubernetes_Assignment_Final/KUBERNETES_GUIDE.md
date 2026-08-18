# Kubernetes Deployment & Debugging Log

## What I Learned
During this assignment, I learned how to move from simple Docker containers to orchestrating microservices in Kubernetes using Minikube. Key learnings include:

1. **Service Discovery**: Internal DNS inside Kubernetes allows the Express frontend to locate the Flask backend using `flask-backend-service:5000` rather than hardcoded IP addresses.
2. **Probes**: Adding `readinessProbe` fixed an issue where the frontend tried to reach the backend before Gunicorn had fully initialized.
3. **Resource Control**: Setting `cpu` and `memory` limits prevents pods from consuming excessive host memory.
4. **ConfigMaps**: Decoupling configuration from container images allows changing environment settings without rebuilding Docker images.

---

## Debugging Process & Challenges Faced

### Challenge 1: Minikube Image Pull Error (`ImagePullBackOff`)
- **Problem**: Kubernetes couldn't pull `flask-backend:latest` because it was built on host Docker instead of Minikube's Docker daemon.
- **Fix**: Executed `eval $(minikube docker-env)` before running `docker build`. Also set `imagePullPolicy: IfNotPresent`.

### Challenge 2: Service Connection Timeout
- **Problem**: Frontend couldn't reach Flask API inside Minikube.
- **Fix**: Replaced `localhost:5000` with Kubernetes ClusterIP service DNS name `http://flask-backend-service:5000`.

---

## Verification Commands Run

```bash
# Check all resources in namespace
kubectl get all -n devops-assignment

# Inspect pod logs if errors occur
kubectl logs -l app=flask-backend -n devops-assignment

# Describe pod to verify readiness probe status
kubectl describe pod -l app=express-frontend -n devops-assignment
```
