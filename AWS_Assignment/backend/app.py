import os
import socket
import logging
import time
from flask import Flask, jsonify, request

# Configure logging to assist in debugging AWS deployment logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Simple manual CORS header middleware to avoid relying heavily on external defaults
@app.after_request
def apply_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

START_TIME = time.time()

@app.route('/')
def root():
    logger.info("Received request on root route from %s", request.remote_addr)
    return jsonify({
        "status": "online",
        "service": "Flask Microservice API",
        "hostname": socket.gethostname(),
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/api/data')
def get_deployment_tasks():
    logger.info("Fetching architecture task status")
    tasks = [
        {"id": 1, "architecture": "Single EC2 Instance", "containerized": True, "status": "Deployed"},
        {"id": 2, "architecture": "Dual EC2 (Frontend + Backend)", "containerized": True, "status": "Deployed"},
        {"id": 3, "architecture": "AWS ECR + ECS Fargate + ALB", "containerized": True, "status": "Deployed"}
    ]
    return jsonify({
        "success": True,
        "tasks": tasks,
        "server": {
            "node_name": socket.gethostname(),
            "environment": os.getenv("FLASK_ENV", "production")
        }
    })

@app.route('/api/health')
def health_check():
    # Health probe endpoint for AWS ALB / Target Group health checking
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname(),
        "uptime": round(time.time() - START_TIME, 2)
    }), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    logger.info(f"Starting Flask application server on 0.0.0.0:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
