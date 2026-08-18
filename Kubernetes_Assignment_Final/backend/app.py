import os
import socket
import time
from flask import Flask, jsonify

# Simple Flask app for Kubernetes assignment
app = Flask(__name__)

# Manual CORS header setup
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/')
def index():
    return jsonify({
        "message": "Flask backend running in Kubernetes!",
        "pod_name": socket.gethostname(),
        "status": "active"
    })

@app.route('/api/data')
def get_data():
    return jsonify({
        "items": [
            {"id": 1, "task": "Pod Orchestration", "status": "Completed"},
            {"id": 2, "task": "Service Discovery", "status": "Completed"},
            {"id": 3, "task": "Kubernetes Ingress & ConfigMap", "status": "Completed"}
        ],
        "pod": socket.gethostname()
    })

# Liveness probe endpoint for K8s
@app.route('/healthz')
def healthz():
    return jsonify({"status": "healthy"}), 200

# Readiness probe endpoint for K8s
@app.route('/ready')
def ready():
    return jsonify({"status": "ready"}), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
