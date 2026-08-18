import os
import socket
import logging
import time
from flask import Flask, jsonify, request

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# handle CORS manually so i understand what its doing
@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    return response

start_time = time.time()

@app.route('/')
def home():
    logger.info("root hit from %s", request.remote_addr)
    return jsonify({
        "status": "running",
        "host": socket.gethostname(),
        "uptime": round(time.time() - start_time, 1),
        "note": "Flask microservice - AWS DevOps assignment"
    })

@app.route('/api/data')
def api_data():
    logger.info("data endpoint called")
    return jsonify({
        "success": True,
        "deployments": [
            {"task": 1, "name": "Single EC2 + Docker Compose", "status": "done"},
            {"task": 2, "name": "Dual EC2 - Frontend/Backend split", "status": "done"},
            {"task": 3, "name": "ECR + ECS Fargate cluster", "status": "done"}
        ],
        "server": {
            "hostname": socket.gethostname(),
            "env": os.getenv("FLASK_ENV", "production")
        }
    })

@app.route('/api/health')
def health():
    # this endpoint is used by ALB target group health checks
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname(),
        "uptime_sec": round(time.time() - start_time, 1)
    }), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    logger.info("starting server on port %d", port)
    app.run(host='0.0.0.0', port=port, debug=False)
