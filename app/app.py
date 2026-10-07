from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        {
            "application": "Production DevOps Platform",
            "status": "running",
            "version": os.getenv("APP_VERSION", "1.0.0"),
            "hostname": socket.gethostname(),
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.get("/ready")
def ready():
    return jsonify({"status": "ready"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
