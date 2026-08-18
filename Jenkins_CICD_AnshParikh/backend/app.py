import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/')
def index():
    return jsonify({
        "status": "running",
        "service": "Flask Backend API",
        "hostname": socket.gethostname()
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
