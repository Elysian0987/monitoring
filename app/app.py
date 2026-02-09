from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random
import logging
import os
import threading
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Logging setup
os.makedirs("/app/logs", exist_ok=True)

logging.basicConfig(
    filename="/app/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# Prometheus metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ['method', 'endpoint']
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Request latency in seconds",
    ['endpoint']
)

# Flask routes
@app.route("/")
def hello():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    
    with REQUEST_LATENCY.labels(endpoint='/').time():
        time.sleep(random.uniform(0.1, 1.5))
    
    logging.info("GET / called")
    return "Greetings from the observable universe! Your metrics are looking sharp today."

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# Dummy log generator
def generate_dummy_logs():
    messages = [
        "Dummy log for Loki test",
        "Another test log entry",
        "Metrics route checked",
        "Periodic background log"
    ]
    
    while True:
        msg = random.choice(messages)
        logging.info(msg)
        time.sleep(5) # adjust interval as needed

# Run Flask
if __name__ == "__main__":
    # Start dummy logging in background
    threading.Thread(target=generate_dummy_logs, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)