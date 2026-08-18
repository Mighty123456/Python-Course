import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Flask Backend provisioned via Terraform!",
        "hostname": socket.gethostname(),
        "service": "Flask REST API"
    })

@app.route('/api/data')
def get_data():
    return jsonify({
        "items": [
            {"id": 1, "name": "Part 1: Single EC2 Deployment", "status": "Terraformed"},
            {"id": 2, "name": "Part 2: Separate EC2 Instances + Custom VPC", "status": "Terraformed"},
            {"id": 3, "name": "Part 3: ECR, ECS & ALB Architecture", "status": "Terraformed"}
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
