# monitoring

Complete observability stack demonstrating metrics and log monitoring using Prometheus, Loki, and Grafana.

## Overview

This project implements a full observability solution with:
- **Metrics Monitoring**: Prometheus metrics collection from Flask app
- **Log Aggregation**: Loki for centralized log storage
- **Log Shipping**: Promtail to collect and forward logs
- **Visualization**: Grafana for unified metrics and logs dashboards

## Architecture

The stack consists of 5 containerized services:

### 1. **Flask App** (`app/`)
   - Web application exposing `/` endpoint
   - Prometheus metrics endpoint at `/metrics`
   - Structured logging to `/app/logs/app.log`
   - Background thread generating dummy logs for testing
   - Tracks HTTP request counts and latency
   - Port: 5000

### 2. **Prometheus** 
   - Scrapes metrics from Flask app every 5 seconds
   - Time-series metrics database
   - UI for querying and alerting
   - Port: 9090

### 3. **Loki**
   - Log aggregation system
   - Stores logs with metadata indexing
   - Retention: 7 days (168h)
   - Port: 3100

### 4. **Promtail**
   - Log collector and shipper
   - Monitors Docker container logs
   - Reads Flask app logs from `/var/log`
   - Forwards logs to Loki
   - Port: 9080

### 5. **Grafana**
   - Unified visualization platform
   - Connects to both Prometheus and Loki
   - Create dashboards combining metrics and logs
   - Port: 3000

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
- **Loki**: http://localhost:3100
- **Grafana**: http://localhost:3000

### Grafana Setup

1. Open Grafana at http://localhost:3000
2. Default credentials: `admin`/`admin`
3. Add data sources:
   
   **Prometheus Data Source:**
   - Type: Prometheus
   - URL: `http://prometheus:9090`
   
   **Loki Data Source:**
   - Type: Loki
   - URL: `http://loki:3100`

4. Create dashboards:
   - Query Prometheus for metrics visualization
   - Query Loki for log exploration
   - Combine both for correlation analysis

## Available Metrics

- `http_requests_total`: Counter of HTTP requests by method and endpoint
- `http_request_latency_seconds_sum`: Total sum of request latencies
- `http_request_latency_seconds_count`: Total count of requests
- `http_request_latency_seconds_bucket`: Latency histogram buckets

## Log Management

- **App Logs**: Written to `./logs/app.log` (mounted volume)
- **Log Format**: `timestamp level message`
- **Retention**: 7 days configured in Loki
- **Query Logs**: Use Grafana's Explore view with Loki data source

## Project Structure

```
.
├── docker-compose.yml          # Orchestrates all 5 services
├── prometheus.yml              # Prometheus scrape configuration
├── loki-config.yml             # Loki storage and retention settings
├── promtail-config.yml         # Promtail log collection rules
├── logs/                       # App logs (volume mount)
└── app/
    ├── app.py                  # Flask app with Prometheus client
    ├── Dockerfile              # App container definition
    └── requirements.txt        # Python dependencies
```

## Technology Stack

- **Application**: Flask (Python)
- **Metrics**: Prometheus + prometheus_client
- **Logs**: Loki + Promtail
- **Visualization**: Grafana
- **Containerization**: Docker + Docker Compose