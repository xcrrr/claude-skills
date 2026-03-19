---
name: kubernetes-helper
description: "Use this skill when generating, explaining, or troubleshooting Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, Ingress, HPA, and Helm chart structures. Triggers: 'write a Kubernetes manifest for', 'create a Helm chart', 'my pod is CrashLoopBackOff', 'set up autoscaling in K8s'. Not for provisioning Kubernetes clusters themselves, managing cloud provider control planes, or writing CI/CD pipelines that deploy to K8s."
version: 1.0.0
author: community
tags: [devops, kubernetes, k8s, helm, containers]
license: MIT
---

# Kubernetes Helper

## Overview
The Kubernetes Helper skill generates, explains, and troubleshoots Kubernetes manifests and Helm chart structures for containerized applications. It covers the full spectrum of K8s resource types: Deployments, StatefulSets, DaemonSets, Services (ClusterIP, NodePort, LoadBalancer), Ingress controllers, ConfigMaps, Secrets, Persistent Volume Claims, Horizontal Pod Autoscalers (HPA), Vertical Pod Autoscalers (VPA), Pod Disruption Budgets, and RBAC resources. The skill also helps diagnose common failure modes (CrashLoopBackOff, ImagePullBackOff, OOMKilled, pending pods, networking issues) and design Helm chart structures for reusable, parameterized deployments.

## When to Use
- Writing Kubernetes manifests (YAML) for a new application deployment
- Configuring Services and Ingress for internal and external traffic routing
- Setting up Horizontal Pod Autoscaling (HPA) based on CPU, memory, or custom metrics
- Creating ConfigMaps and Secrets for environment-specific configuration
- Diagnosing pod failures: CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending
- Designing a Helm chart structure for a reusable, parameterizable application
- Configuring resource requests and limits, liveness/readiness probes, and pod affinity rules
- Implementing rolling update strategies, PodDisruptionBudgets, and zero-downtime deployments

## When NOT to Use
- Provisioning or upgrading Kubernetes clusters (EKS, GKE, AKS, kubeadm) — use cloud provider tools or Terraform
- Writing application code that runs inside pods
- Designing CI/CD pipelines that build images and deploy them to Kubernetes (use the ci-cd-helper skill)
- Managing Kubernetes cluster add-ons like CNI plugins, storage CSI drivers, or the cluster autoscaler at the infrastructure level
- Building service meshes from scratch (Istio, Linkerd configuration at the cluster level)

## Quick Reference
| Task | Approach |
|------|----------|
| Expose app externally | Use `Ingress` with a hostname + `Service` of type `ClusterIP`; avoid `LoadBalancer` per service |
| Autoscale pods | Create `HorizontalPodAutoscaler` targeting the Deployment; set CPU/memory thresholds |
| Non-sensitive config | Store in `ConfigMap`; mount as `envFrom` or a volume at `/etc/config` |
| Sensitive config | Store in `Secret` (base64-encoded); mount via `secretRef` or projected volume |
| Persist data | Use `PersistentVolumeClaim` with a `StorageClass`; mount to `StatefulSet` volumeClaimTemplates |
| Rolling zero-downtime deploy | Set `strategy.type: RollingUpdate` with `maxUnavailable: 0` and `maxSurge: 1` |
| Debug failing pod | `kubectl describe pod <name>` → `kubectl logs <name> --previous` → check events |

## Instructions

1. **Identify the workload type and resource requirements** — Confirm whether the app is stateless (use `Deployment`) or stateful (use `StatefulSet`). Determine replica count, CPU/memory requests and limits (expressed in millicores and mebibytes), and whether persistent storage is required.

2. **Write the Deployment or StatefulSet manifest** — Include `metadata.labels` matching `spec.selector.matchLabels`. Set `spec.replicas`, `spec.strategy` (RollingUpdate with appropriate surge/unavailable values), and a full `spec.template.spec.containers` block with image, ports, environment variables, resource requests/limits, and volume mounts.

3. **Define liveness and readiness probes** — Configure `readinessProbe` to delay traffic until the app is ready, and `livenessProbe` to restart containers that become unresponsive. Use HTTP GET probes for web apps (`path: /health`, `port: 8080`); use exec probes for non-HTTP workloads.

4. **Configure resource requests and limits** — Always set both `requests` (guaranteed) and `limits` (ceiling) for CPU and memory. Size requests based on typical load; set limits to 2–3x requests to absorb traffic spikes without OOMKilling pods.

5. **Create ConfigMaps and Secrets for configuration** — Place non-sensitive configuration (feature flags, log levels, base URLs) in a `ConfigMap`. Place sensitive values (passwords, API keys, TLS certs) in a `Secret`. Reference them via `envFrom`, `env.valueFrom`, or volume mounts.

6. **Define a Service resource** — For internal communication, use `type: ClusterIP`. For external access via an Ingress controller, pair a `ClusterIP` Service with an `Ingress`. Avoid `type: LoadBalancer` for every service as it provisions a cloud load balancer per service.

7. **Configure Ingress for external traffic** — Write an `Ingress` manifest specifying `ingressClassName`, hostname rules, path prefixes, and the backend Service name/port. Add TLS termination using a `cert-manager` Certificate or a manually created Secret for production HTTPS.

8. **Set up Horizontal Pod Autoscaling** — Create an `HPA` targeting the Deployment with `minReplicas`, `maxReplicas`, and `metrics` (CPU utilization target, memory, or custom metrics). Ensure resource requests are set on the Deployment — HPA cannot function without them.

9. **Apply security hardening** — Set `securityContext` at pod and container levels: `runAsNonRoot: true`, `runAsUser: 1000`, `readOnlyRootFilesystem: true`, `allowPrivilegeEscalation: false`, and `capabilities.drop: ["ALL"]`. Use `NetworkPolicy` to restrict pod-to-pod traffic to only what is required.

10. **Diagnose and troubleshoot failures** — For pod failures, follow: `kubectl get pods -n <ns>` → `kubectl describe pod <name> -n <ns>` (check Events section) → `kubectl logs <name> -n <ns> --previous` (crash logs). Common causes: wrong image tag (ImagePullBackOff), missing Secret/ConfigMap (CreateContainerConfigError), OOM (OOMKilled), failing probes (CrashLoopBackOff).

## Examples

### Example 1: Deploying a Web App with Service and Ingress
**Input:** "Write Kubernetes manifests to deploy a web app image `myorg/webapp:1.4.2` with 3 replicas. Expose it at `app.example.com` via HTTPS. The app listens on port 8080 and has a `/health` endpoint. Needs DATABASE_URL from a Secret and LOG_LEVEL from a ConfigMap."

**Output:**
```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: webapp-config
  namespace: production
data:
  LOG_LEVEL: "info"
  APP_ENV: "production"
```

```yaml
# secret.yaml  (values are base64-encoded; use Sealed Secrets or External Secrets in real clusters)
apiVersion: v1
kind: Secret
metadata:
  name: webapp-secrets
  namespace: production
type: Opaque
stringData:                        # stringData auto-encodes to base64
  DATABASE_URL: "postgresql://user:password@db-service:5432/myapp"
  SECRET_KEY: "replace-with-real-secret"
```

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
  namespace: production
  labels:
    app: webapp
    version: "1.4.2"
spec:
  replicas: 3
  selector:
    matchLabels:
      app: webapp
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 0            # Never reduce below desired replicas during update
      maxSurge: 1                  # Allow one extra pod during rollout

  template:
    metadata:
      labels:
        app: webapp
        version: "1.4.2"
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 1000

      containers:
        - name: webapp
          image: myorg/webapp:1.4.2
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
              name: http

          envFrom:
            - configMapRef:
                name: webapp-config  # Injects LOG_LEVEL, APP_ENV
            - secretRef:
                name: webapp-secrets # Injects DATABASE_URL, SECRET_KEY

          resources:
            requests:
              cpu: "250m"
              memory: "256Mi"
            limits:
              cpu: "500m"
              memory: "512Mi"

          readinessProbe:            # Pod receives traffic only when this passes
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 10
            failureThreshold: 3

          livenessProbe:             # Pod is restarted if this fails
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 20
            failureThreshold: 3

          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: ["ALL"]

          volumeMounts:
            - name: tmp
              mountPath: /tmp       # Required for readOnlyRootFilesystem apps that need /tmp

      volumes:
        - name: tmp
          emptyDir: {}
```

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: webapp-svc
  namespace: production
spec:
  selector:
    app: webapp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP                   # Internal only; Ingress handles external traffic
```

```yaml
# ingress.yaml  (requires nginx ingress controller and cert-manager)
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: webapp-ingress
  namespace: production
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - app.example.com
      secretName: webapp-tls        # cert-manager will populate this Secret with the cert
  rules:
    - host: app.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: webapp-svc
                port:
                  number: 80
```

### Example 2: HPA Configuration for Autoscaling
**Input:** "Add an HPA to the webapp Deployment from Example 1. Scale between 3 and 15 pods, targeting 60% CPU utilization. Also add a memory-based metric: scale up if average memory exceeds 400Mi."

**Output:**
```yaml
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: webapp-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: webapp

  minReplicas: 3                    # Match the replica count in the Deployment
  maxReplicas: 15

  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 60    # Scale up when average CPU across pods exceeds 60%

    - type: Resource
      resource:
        name: memory
        target:
          type: AverageValue
          averageValue: 400Mi       # Scale up when average memory usage exceeds 400Mi/pod

  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60   # Wait 60s before acting on scale-up signals (smoothing)
      policies:
        - type: Pods
          value: 2
          periodSeconds: 60            # Add at most 2 pods per 60 seconds
    scaleDown:
      stabilizationWindowSeconds: 300  # Wait 5 min before scaling down (prevents flapping)
      policies:
        - type: Pods
          value: 1
          periodSeconds: 120           # Remove at most 1 pod per 2 minutes
```

```bash
# Verify HPA is working after applying:
kubectl get hpa webapp-hpa -n production
# Expected output shows TARGETS (current/target), MINPODS, MAXPODS, REPLICAS

# Watch scaling events in real time:
kubectl describe hpa webapp-hpa -n production

# Simulate load to test scale-up (in a test environment):
kubectl run load-gen --image=busybox --rm -it --restart=Never -- \
  /bin/sh -c "while sleep 0.01; do wget -q -O- http://webapp-svc/; done"
```

**Key considerations:**
- HPA requires metric-server to be installed in the cluster (`kubectl top pods` must work)
- Memory-based HPA requires Kubernetes 1.23+ with the `autoscaling/v2` API
- The `stabilizationWindowSeconds` prevents rapid scale-up/scale-down oscillation (flapping)
- Set `minReplicas` to at least 2 for production availability; 3+ for cross-AZ resilience

## Best Practices
- Always set `resources.requests` and `resources.limits` — HPA cannot work without requests, and unlimited resources cause noisy-neighbor issues
- Use `readinessProbe` to prevent routing traffic to pods that are not yet ready during rolling updates
- Pin image tags to a specific version digest (`myorg/webapp:1.4.2` or `sha256:abc123`) — never use `:latest` in production
- Set `minReplicas` to at least 2 for production workloads to survive a single pod failure
- Use namespaces to logically isolate environments (dev, staging, production) within the same cluster
- Prefer `ConfigMap` and `Secret` volume mounts over `env:` blocks for large configurations — they support live updates without pod restarts (with appropriate polling)
- Always define a `PodDisruptionBudget` for production Deployments to prevent all pods being evicted simultaneously during node drain

## Common Mistakes
- Setting `resources.limits` without `resources.requests` — K8s uses requests for scheduling; without them, pods land on any node regardless of actual capacity
- Using `type: LoadBalancer` for every internal service — each one provisions a costly cloud load balancer; use `ClusterIP` + `Ingress` instead
- Not setting `readinessProbe` — new pods receive traffic immediately on start, before the app is initialized, causing 503s during deployments
- Storing secrets in `ConfigMap` — ConfigMaps are not encrypted at rest; use `Secret` type or an external secret manager (Vault, AWS SSM)
- Using `:latest` image tags in production — prevents deterministic rollbacks and causes unpredictable behavior when the upstream image changes
- Setting `maxUnavailable: 1` without sufficient replica headroom — a 2-replica deployment with maxUnavailable=1 goes to 0 replicas during maintenance
- Forgetting resource `namespace:` — resources applied without a namespace go to `default`, creating hard-to-find misconfigurations

## Tips & Tricks
- Use `kubectl diff -f manifest.yaml` to preview what will change before applying — like a dry-run with diff output
- Use `kubectl rollout status deployment/webapp` to watch a rollout in real time and detect stalls
- Use `kubectl rollout undo deployment/webapp` for an instant rollback to the previous ReplicaSet
- Use `kubectl top pods -n production --sort-by=memory` to quickly identify memory-hungry pods
- Add `kubectl.kubernetes.io/last-applied-configuration` annotation tracking by always using `kubectl apply`, not `kubectl create`
- Use `kustomize` overlays to manage environment-specific differences (replica counts, resource limits) without duplicating base manifests
- Use `kubectl explain deployment.spec.strategy` for built-in K8s API documentation directly in the terminal

## Related Skills
- [docker-expert](../docker-expert/SKILL.md)
- [ci-cd-helper](../ci-cd-helper/SKILL.md)
- [monitoring-setup](../monitoring-setup/SKILL.md)
