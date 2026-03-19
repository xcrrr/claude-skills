---
name: docker-expert
description: "Use this skill when writing optimized Dockerfiles, multi-stage builds, Docker Compose configurations, or applying container security and performance best practices. Triggers: 'write a Dockerfile for', 'optimize my Docker image', 'set up Docker Compose for', 'containerize my app'. Not for writing Kubernetes manifests, provisioning cloud container services (ECS, Cloud Run), or designing CI/CD pipelines."
version: 1.0.0
author: community
tags: [devops, docker, containers, docker-compose]
license: MIT
---

# Docker Expert

## Overview
The Docker Expert skill produces optimized, production-ready Dockerfiles and Docker Compose configurations for any application stack. It applies container best practices: minimal base images (Alpine, Distroless, slim variants), multi-stage builds to minimize final image size, non-root user execution for security, strategic layer ordering to maximize cache reuse, `.dockerignore` files to exclude unnecessary build context, and health check definitions for orchestrator integration. The skill handles single-service containerization and multi-service local development environments with Docker Compose, including networking, volumes, secrets, and environment variable management.

## When to Use
- Writing a new Dockerfile for any application (Node.js, Python, Java, Go, Ruby, etc.)
- Reducing Docker image size with multi-stage builds and minimal base images
- Applying container security hardening (non-root user, read-only filesystem, dropped capabilities)
- Configuring a `docker-compose.yml` for local development with databases, caches, and app services
- Writing `.dockerignore` files to reduce build context size and prevent secret leakage
- Adding `HEALTHCHECK` instructions for container health monitoring
- Troubleshooting slow builds, large images, or container startup failures
- Converting a non-containerized app to run in Docker for the first time

## When NOT to Use
- Writing Kubernetes manifests or Helm charts (use the kubernetes-helper skill)
- Provisioning managed container services (AWS ECS, Google Cloud Run, Azure Container Apps)
- Designing CI/CD pipelines that build and push Docker images (use the ci-cd-helper skill)
- Setting up container registries (ECR, GCR, GHCR) from scratch
- Orchestrating containers at scale in production (use Kubernetes)

## Quick Reference
| Task | Approach |
|------|----------|
| Minimize image size | Use multi-stage build; copy only compiled artifacts to a minimal final stage (Alpine/Distroless) |
| Run as non-root | Add `RUN addgroup -S app && adduser -S app -G app` then `USER app` before `CMD` |
| Maximize layer cache | Order instructions: `COPY` lockfile → `RUN install` → `COPY` source code |
| Exclude build context files | Create `.dockerignore` listing `node_modules/`, `.git/`, `*.log`, `.env`, `dist/` |
| Health check | `HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -f http://localhost:8080/health` |
| Multi-service dev env | Use `docker-compose.yml` with `depends_on:`, named volumes, and a shared network |
| Pin base image versions | Use `node:20.14.0-alpine3.19` not `node:latest` for reproducible builds |

## Instructions

1. **Identify the application stack and runtime** — Confirm the language, framework, package manager, and build output format (e.g., "Node.js 20 with npm, Express app, no build step" or "Python 3.11 with Poetry, FastAPI, no compiled artifacts"). This determines the appropriate base image family.

2. **Choose the base image strategy** — Select the smallest suitable base image: use language-specific Alpine or slim variants for interpreted languages (e.g., `python:3.11-slim`, `node:20-alpine`). For compiled languages (Go, Rust), use a full build image for the build stage and `gcr.io/distroless/static` or `scratch` for the final stage.

3. **Design a multi-stage build** — Use at minimum a `builder` stage (full SDK image for installing dependencies and compiling) and a `runner` stage (minimal image for running the app). Copy only production artifacts from builder to runner: `COPY --from=builder /app/dist ./dist`.

4. **Optimize layer caching** — Order `COPY` and `RUN` instructions from least-frequently-changed to most-frequently-changed. Always copy the dependency manifest first, run the install, then copy source code. This ensures a dependency cache hit on every commit that only changes source code.

5. **Harden for security** — Create a dedicated non-root user and group; switch to it with `USER` before the `CMD` or `ENTRYPOINT`. Avoid running as `root`. Consider adding `--cap-drop=ALL` and `--read-only` at runtime for sensitive services.

6. **Write a `.dockerignore` file** — Exclude: `.git/`, `node_modules/` (or language equivalent), `*.log`, `.env*`, `dist/`, `coverage/`, IDE config files (`.vscode/`, `.idea/`), and any files with secrets. A small build context speeds up builds and prevents accidental secret inclusion.

7. **Define environment variables correctly** — Use `ENV` for runtime configuration defaults that are safe to bake into the image. Use `ARG` for build-time variables that should not persist in the final image. Never use `ENV` or `ARG` for secrets — pass secrets at runtime via `--env-file` or Docker secrets.

8. **Add a `HEALTHCHECK` instruction** — Define a health check command so Docker and orchestrators can detect when the container is ready and unhealthy. Use the application's own health endpoint or a lightweight check (`wget -qO- http://localhost:PORT/health`).

9. **Configure Docker Compose for multi-service environments** — Define services, expose ports, configure named volumes for persistent data, and link services via a shared named network. Use `depends_on: condition: service_healthy` to enforce startup ordering.

10. **Validate and document the setup** — Provide the build command (`docker build -t myapp:latest .`), run command (`docker run -p 3000:3000 myapp:latest`), and Compose command (`docker compose up -d`). Note any required environment variables and how to supply them securely.

## Examples

### Example 1: Production-Optimized Node.js Dockerfile
**Input:** "Write a production Dockerfile for a Node.js 20 Express app using npm. The app runs on port 3000. Include multi-stage build, non-root user, health check, and .dockerignore."

**Output:**
```dockerfile
# .dockerignore
node_modules/
npm-debug.log*
.git/
.gitignore
.env*
dist/
coverage/
.nyc_output/
*.md
.vscode/
.idea/
```

```dockerfile
# Dockerfile
# ── Stage 1: Install dependencies ────────────────────────────────────────────
FROM node:20-alpine3.19 AS deps

WORKDIR /app

# Copy manifests first to leverage layer cache — reinstall only when deps change
COPY package.json package-lock.json ./
RUN npm ci --omit=dev          # Install production deps only; --omit=dev skips devDependencies

# ── Stage 2: Build (if applicable — e.g., TypeScript, webpack) ───────────────
FROM node:20-alpine3.19 AS builder

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci                      # Install ALL deps (including devDependencies) for build step
COPY . .
RUN npm run build               # Compiles TS, runs webpack, etc. Remove if no build step.

# ── Stage 3: Production runtime ──────────────────────────────────────────────
FROM node:20-alpine3.19 AS runner

# Create a dedicated non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Copy production node_modules from deps stage
COPY --from=deps /app/node_modules ./node_modules
# Copy built application from builder stage
COPY --from=builder /app/dist ./dist
COPY package.json ./

# Switch to non-root user before starting the app
USER appuser

EXPOSE 3000

# Health check — orchestrators use this to know when the app is ready
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
  CMD wget -qO- http://localhost:3000/health || exit 1

# Use exec form (array) to ensure signals (SIGTERM) reach the Node process
CMD ["node", "dist/server.js"]
```

```bash
# Build
docker build -t myapp:latest .

# Run (pass secrets via --env-file, never bake them into the image)
docker run -d \
  -p 3000:3000 \
  --env-file .env.production \
  --read-only \
  --tmpfs /tmp \
  --name myapp \
  myapp:latest
```

**Result:** Final image is ~180 MB (vs ~1.1 GB with a full Node image and no multi-stage build). Runs as non-root `appuser`. Health check enables Kubernetes/Docker Swarm readiness detection.

### Example 2: Python Flask App with Docker Compose (App + Postgres + Redis)
**Input:** "Set up Docker Compose for a Python 3.11 Flask app (using pip and requirements.txt) with a Postgres 15 database and Redis 7 cache. The Flask app should hot-reload in development."

**Output:**
```dockerfile
# Dockerfile (development — hot reload via Flask dev server)
FROM python:3.11-slim AS base

# Install system dependencies required by psycopg2 and other packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev curl \
 && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r flaskuser && useradd -r -g flaskuser flaskuser

WORKDIR /app

# Install Python dependencies (cached layer — only reinstalls when requirements.txt changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .
RUN chown -R flaskuser:flaskuser /app

USER flaskuser

EXPOSE 5000

HEALTHCHECK --interval=20s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

CMD ["flask", "run", "--host=0.0.0.0"]
```

```yaml
# docker-compose.yml
version: '3.9'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: flask-app
    ports:
      - "5000:5000"
    environment:
      FLASK_ENV: development
      FLASK_APP: app:create_app
      DATABASE_URL: postgresql://postgres:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
      REDIS_URL: redis://redis:6379/0
    env_file:
      - .env.development          # Contains POSTGRES_PASSWORD, SECRET_KEY, etc.
    volumes:
      - .:/app                    # Mount source for hot-reload in development
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - backend

  db:
    image: postgres:15-alpine
    container_name: flask-db
    environment:
      POSTGRES_DB: ${POSTGRES_DB:-myapp}
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend

  redis:
    image: redis:7-alpine
    container_name: flask-redis
    command: ["redis-server", "--save", "60", "1", "--loglevel", "warning"]
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3
    networks:
      - backend

volumes:
  postgres_data:
  redis_data:

networks:
  backend:
    driver: bridge
```

```bash
# Start all services
docker compose up -d

# View logs
docker compose logs -f app

# Run database migrations
docker compose exec app flask db upgrade

# Tear down (keep volumes)
docker compose down

# Tear down and delete all data volumes
docker compose down -v
```

## Best Practices
- Always pin base image versions (`node:20.14.0-alpine3.19` not `node:latest`) for reproducible builds
- Use multi-stage builds for every app that has a build step — the difference in final image size is dramatic
- Run containers as a non-root user in every environment, including development
- Copy dependency manifests before source code to maximize Docker layer cache utilization
- Always include a `.dockerignore` file — without it, `node_modules/` or `.git/` can be sent as build context
- Use `HEALTHCHECK` in every production Dockerfile so orchestrators can detect unhealthy containers
- Prefer `CMD` in exec form (`["node", "server.js"]`) over shell form (`node server.js`) so signals propagate correctly

## Common Mistakes
- Using `COPY . .` before installing dependencies — breaks layer caching; every source change triggers a full reinstall
- Running containers as root (default if `USER` is not set) — significant security vulnerability
- Using `:latest` tags for base images — leads to non-reproducible builds as upstream images update
- Storing secrets in `ENV` instructions — they are visible in `docker inspect` and image layers
- Not using `--no-cache-dir` for `pip install` — wastes image space on cached wheel files
- Installing development tools (curl, vim, git) in production images — increases attack surface and image size
- Forgetting to clean up apt/apk cache in the same `RUN` layer that installs packages

## Tips & Tricks
- Use `docker image history myapp:latest` to see each layer's size and identify what to optimize
- Use `docker buildx build --platform linux/amd64,linux/arm64` to build multi-architecture images for Apple Silicon and cloud compatibility
- Use Docker's `--build-arg` with `ARG` to pass build-time configuration (e.g., environment name, version tag) without baking it into `ENV`
- Use `docker compose watch` (Compose v2.22+) for smarter file-watching hot reload that avoids volume mount pitfalls
- Add `--squash` or use BuildKit's `--mount=type=cache` to further optimize image size and build speed
- Use `docker scout cves myapp:latest` to scan your built image for known CVEs before pushing
- In multi-stage builds, name stages with `AS name` and reference them in `COPY --from=name` for clarity and build targeting

## Related Skills
- [ci-cd-helper](../ci-cd-helper/SKILL.md)
- [kubernetes-helper](../kubernetes-helper/SKILL.md)
- [security-auditor](../security-auditor/SKILL.md)
