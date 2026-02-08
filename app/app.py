from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest
import time
import random
from flask import Response

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint']
)

REQUEST_LATENCY = Histogram(
    'http_request_latency_seconds',
    'Request latency'
)

@app.route("/")
def hello():
    REQUEST_COUNT.labels('GET', '/').inc()
    with REQUEST_LATENCY.time():
        time.sleep(random.uniform(0.1, 1.5))  # simulate latency
    return "Hello SRE 👋"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
