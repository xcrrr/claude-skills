---
name: monitoring-setup
description: "Use this skill when designing or improving observability stacks with Prometheus, Grafana, Loki, Jaeger, or configuring alerting rules and SLIs/SLOs. Not for application code debugging or infrastructure provisioning. Not for log analysis of already-collected logs."
version: 1.0.0
author: community
tags: [devops, monitoring, observability, prometheus, grafana]
license: MIT
---

# Monitoring Setup

## Overview
This skill covers end-to-end design and implementation of observability stacks for production systems. It helps teams instrument services with metrics, logs, and traces; define Service Level Indicators (SLIs) and Objectives (SLOs); build Grafana dashboards; configure Prometheus alerting rules; set up distributed tracing with Jaeger; and implement structured logging with Loki. The goal is to give engineering teams full visibility into system health, performance regressions, and incidents before customers notice them.

## When to Use
- Designing a new observability stack for a greenfield service or platform
- Adding Prometheus metrics and Grafana dashboards to an existing service
- Defining SLIs and SLOs for reliability engineering or SRE onboarding
- Writing or tuning Prometheus alerting rules and Alertmanager routing
- Setting up structured (JSON) logging and shipping logs to Loki
- Configuring distributed tracing with Jaeger or OpenTelemetry
- Reviewing alert fatigue and reducing noisy or redundant alerts
- Building runbooks linked to alert definitions

## When NOT to Use
- Debugging application logic bugs (use code review or debugging skills)
- Provisioning cloud infrastructure (use Terraform or cloud-specific skills)
- Analyzing already-collected logs interactively (use log analysis skills)
- Choosing a monitoring vendor or SaaS product (use vendor comparison skills)
- Setting up APM agents for a specific language runtime without a broader stack context

## Quick Reference
| Task | Approach |
|------|----------|
| Expose metrics from a service | Instrument with Prometheus client library; expose `/metrics` endpoint |
| Scrape metrics into Prometheus | Add a `scrape_config` job in `prometheus.yml` or PodMonitor CRD |
| Visualize metrics | Create Grafana datasource pointing to Prometheus; build panels with PromQL |
| Ship logs to Loki | Deploy Promtail or use Alloy; configure pipeline stages and labels |
| Add distributed tracing | Instrument with OpenTelemetry SDK; export spans to Jaeger or Tempo |
| Define an SLO | Identify SLI (e.g., request success rate), set target (e.g., 99.5%), burn-rate alert |
| Page on-call appropriately | Configure Alertmanager routes, inhibition rules, and receiver integrations |

## Instructions

1. **Identify observability pillars needed** — Determine which of the three pillars (metrics, logs, traces) are required. Most production services need all three; internal tools may need only metrics and logs.

2. **Instrument the service with metrics** — Add the Prometheus client library for your language (Go: `prometheus/client_golang`, Python: `prometheus_client`, Java: `micrometer`). Expose the four golden signals: latency, traffic, errors, and saturation. Use histograms for latency (not gauges), counters for request totals, and gauges for queue depths.

3. **Configure Prometheus scraping** — In `prometheus.yml`, add a `scrape_configs` entry with the target host:port and path. In Kubernetes, prefer `ServiceMonitor` or `PodMonitor` CRDs from the Prometheus Operator. Set `scrape_interval` based on metric freshness needs (15s–60s typical).

4. **Design PromQL queries and Grafana dashboards** — Organize dashboards into rows: Overview (golden signals), Saturation (resource limits), Errors (rate and 5xx breakdown), Latency percentiles (p50/p95/p99). Use dashboard variables for environment and instance filtering. Export dashboards as JSON and version-control them.

5. **Define SLIs and SLOs** — Identify user-facing SLIs (e.g., `rate(http_requests_total{code=~"5.."}[5m]) / rate(http_requests_total[5m])` for error rate). Set SLO targets aligned with business requirements (e.g., 99.9% availability). Calculate error budgets and use multi-window burn-rate alerts (1h + 6h windows) to page appropriately.

6. **Write Prometheus alerting rules** — Create `PrometheusRule` YAML files with alert groups. Each alert needs: `expr` (PromQL), `for` (pending duration), `labels` (severity, team), and `annotations` (summary, description, runbook URL). Avoid alerting on instantaneous spikes — use `for: 5m` or longer.

7. **Configure Alertmanager routing** — Define routes based on label matchers to send critical alerts to PagerDuty, warnings to Slack, and info alerts to a logging channel. Use inhibition rules to suppress child alerts when a parent fires (e.g., suppress pod alerts when the node is down).

8. **Set up structured logging** — Switch application logs to JSON format with standard fields: `timestamp`, `level`, `service`, `trace_id`, `span_id`, `message`. Deploy Promtail (or Grafana Alloy) as a DaemonSet to scrape pod logs and forward to Loki with `__path__` and Kubernetes metadata labels.

9. **Add distributed tracing** — Instrument the service with OpenTelemetry SDK. Configure an OTLP exporter to send spans to a Jaeger or Grafana Tempo backend. Propagate trace context headers (`traceparent`) across service boundaries. Link trace IDs in Grafana by correlating Loki logs with Tempo traces using `derived fields`.

10. **Validate and iterate** — Fire test alerts using `amtool` or `curl` against Alertmanager. Inject synthetic errors to confirm dashboards and alerts react. Review alert fatigue weekly and silence or tune alerts that fire without actionable outcomes.

## Examples

### Example 1: Prometheus + Grafana Setup for a Python Web Service
**Input:** A FastAPI service running in Kubernetes needs metrics, dashboards, and an alert for high error rate.

**Output:**

**Step 1 — Instrument the service:**
```python
from prometheus_client import Counter, Histogram, start_http_server
import time

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status_code']
)
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    REQUEST_COUNT.labels(request.method, request.url.path, response.status_code).inc()
    REQUEST_LATENCY.labels(request.method, request.url.path).observe(duration)
    return response
```

**Step 2 — ServiceMonitor CRD:**
```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: fastapi-service
  namespace: production
spec:
  selector:
    matchLabels:
      app: fastapi-service
  endpoints:
    - port: metrics
      path: /metrics
      interval: 15s
```

**Step 3 — Prometheus alerting rule:**
```yaml
groups:
  - name: fastapi-service.rules
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status_code=~"5.."}[5m]))
          /
          sum(rate(http_requests_total[5m])) > 0.01
        for: 5m
        labels:
          severity: critical
          team: backend
        annotations:
          summary: "High error rate on fastapi-service"
          description: "Error rate is {{ $value | humanizePercentage }} (threshold 1%)"
          runbook_url: "https://wiki.example.com/runbooks/high-error-rate"
```

**Step 4 — Grafana dashboard PromQL panels:**
- Request rate: `sum(rate(http_requests_total[5m])) by (endpoint)`
- Error rate: `sum(rate(http_requests_total{status_code=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))`
- p99 latency: `histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, endpoint))`

### Example 2: Structured Logging with Loki and Log-Based Alerting
**Input:** A Node.js microservice writes plain-text logs. The team wants JSON logs, Loki ingestion, and an alert when error logs exceed 10/min.

**Output:**

**Step 1 — Switch to JSON logging with Winston:**
```javascript
const winston = require('winston');
const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  defaultMeta: { service: 'order-service', version: '2.1.0' },
  transports: [new winston.transports.Console()]
});

// Usage — includes trace_id for correlation
logger.error('Payment failed', {
  trace_id: req.headers['x-trace-id'],
  order_id: order.id,
  error: err.message
});
```

**Step 2 — Promtail configuration (DaemonSet):**
```yaml
scrape_configs:
  - job_name: kubernetes-pods
    kubernetes_sd_configs:
      - role: pod
    pipeline_stages:
      - json:
          expressions:
            level: level
            service: service
            trace_id: trace_id
      - labels:
          level:
          service:
      - match:
          selector: '{level="error"}'
          stages:
            - metrics:
                error_lines_total:
                  type: Counter
                  description: "Total error log lines"
                  config:
                    action: inc
```

**Step 3 — LogQL query in Grafana:**
```logql
# Count error logs per service in last 5 minutes
sum by (service) (count_over_time({namespace="production"} | json | level="error" [5m]))
```

**Step 4 — Loki-based alert rule:**
```yaml
groups:
  - name: log-alerts
    rules:
      - alert: HighErrorLogRate
        expr: |
          sum(count_over_time({namespace="production", service="order-service"}
            | json | level="error" [1m])) > 10
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "Elevated error log rate in order-service"
```

## Best Practices
- Always use histograms (not summaries) for latency metrics — they support aggregation across instances
- Label cardinality matters: never use user IDs or request IDs as Prometheus label values
- Store Grafana dashboards as JSON in version control alongside the service code
- Use burn-rate alerts (multi-window) for SLO violations instead of raw threshold alerts
- Link every alert annotation to a runbook URL so on-call engineers know what to do
- Set `for: 5m` or longer on alerts to avoid flapping from transient spikes
- Use Grafana folder permissions to separate team dashboards and prevent accidental edits
- Correlate metrics, logs, and traces using a shared `trace_id` field for faster incident resolution

## Common Mistakes
- Using `rate()` on a gauge instead of a counter — only counters should use `rate()`
- Alerting on every error log line — always aggregate over a time window first
- Creating dashboards with no variable templating — hard to reuse across environments
- Setting `scrape_interval` too low (< 10s) causing high cardinality and storage costs
- Forgetting to set `honor_labels: true` when federating Prometheus instances
- Using `average()` instead of percentiles for latency — averages hide tail latency problems
- Defining SLOs without an error budget policy — teams won't know when to stop feature work

## Tips & Tricks
- Use `absent()` in alert rules to detect when a metric stops being scraped entirely
- `topk(5, ...)` in PromQL is useful for finding the top offenders in dashboards
- Grafana's Explore mode is excellent for ad-hoc PromQL and LogQL queries during incidents
- Use `record` rules in Prometheus to pre-compute expensive PromQL queries used in dashboards
- Jaeger's `Find Traces` UI supports filtering by minimum duration — great for finding slow outliers
- Tag Grafana annotations with deployment events to visually correlate deploys with metric changes
- Use `mimirtool` or `promtool` to lint and test alerting rules in CI pipelines

## Related Skills
- [ci-cd-helper](../../devops/ci-cd-helper/SKILL.md)
- [kubernetes-helper](../../devops/kubernetes-helper/SKILL.md)
- [docker-expert](../../devops/docker-expert/SKILL.md)
