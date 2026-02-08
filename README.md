# monitoring

A demonstration project showcasing application monitoring using Prometheus and Grafana.

## Overview

This project demonstrates a complete observability stack with:
- Flask application instrumented with Prometheus metrics
- Prometheus for metrics collection and storage
- Grafana for visualization and dashboards

## Architecture

The stack consists of three containerized services:

1. **Flask App** (`app/`)
   - Simple web application with `/` endpoint
   - Exposes metrics at `/metrics` endpoint
   - Tracks HTTP request counts and latency
   - Runs on port 5000

2. **Prometheus** (`prometheus/`)
   - Scrapes metrics from the Flask app every 5 seconds
   - Stores time-series data
   - UI available on port 9090

3. **Grafana**
   - Visualization platform for creating dashboards
   - UI available on port 33000
   - Can connect to Prometheus as data source

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Running the Stack

```bash
docker-compose up
```

### Accessing the Services

- **Flask App**: http://localhost:5000
- **Metrics Endpoint**: http://localhost:5000/metrics
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:33000

### Grafana Setup

1. Open Grafana at http://localhost:33000
2. Default credentials: `admin`/`admin`
3. Add Prometheus as a data source:
   - URL: `http://prometheus:9090`
4. Create dashboards to visualize:
   - `http_requests_total` - Total request count
   - `http_request_latency_seconds` - Request latency distribution

## Metrics Available

- `http_requests_total`: Counter tracking total HTTP requests by method and endpoint
- `http_request_latency_seconds_sum`: Sum of all request latencies
- `http_request_latency_seconds_count`: Count of all requests
- `http_request_latency_seconds_bucket`: Latency distribution buckets

## Project Structure

```
.
├── docker-compose.yml       # Orchestrates all services
├── app/
│   ├── app.py              # Flask application with Prometheus instrumentation
│   ├── Dockerfile          # Container definition for the app
│   └── requirements.txt    # Python dependencies
└── prometheus/
    └── prometheus.yml      # Prometheus configuration
```