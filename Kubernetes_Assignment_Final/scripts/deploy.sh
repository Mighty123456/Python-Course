#!/bin/bash
# Script to apply all Kubernetes manifests in proper sequence

set -e

echo "Applying Kubernetes manifests to Minikube..."

kubectl apply -f k8s/00-namespace.yaml
kubectl apply -f k8s/01-configmap.yaml
kubectl apply -f k8s/02-secret.yaml
kubectl apply -f k8s/03-backend-deployment.yaml
kubectl apply -f k8s/04-frontend-deployment.yaml
kubectl apply -f k8s/05-ingress.yaml

echo "Waiting for pods to be ready in namespace 'devops-assignment'..."
kubectl rollout status deployment/flask-backend-deployment -n devops-assignment
kubectl rollout status deployment/express-frontend-deployment -n devops-assignment

echo "All deployments are up and running!"
kubectl get pods,svc,ingress -n devops-assignment
