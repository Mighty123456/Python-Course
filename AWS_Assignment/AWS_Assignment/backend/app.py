from flask import Flask, jsonify
from flask_cors import CORS
import os
import socket

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Flask Backend is running successfully on AWS!",
        "hostname": socket.gethostname(),
        "service": "Flask REST API",
        "version": "1.0.0"
    })

@app.route('/api/data')
def get_data():
    return jsonify({
        "items": [
            {"id": 1, "name": "Task 1: Single EC2 Deployment", "status": "Ready"},
            {"id": 2, "name": "Task 2: Separate EC2 Instances", "status": "Ready"},
            {"id": 3, "name": "Task 3: ECR, ECS & VPC Deployment", "status": "Ready"}
        ],
        "server_info": {
            "environment": os.getenv("FLASK_ENV", "production"),
            "host": socket.gethostname()
        }
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
