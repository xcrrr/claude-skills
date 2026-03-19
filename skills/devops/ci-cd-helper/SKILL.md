---
name: ci-cd-helper
description: "Use this skill when designing, writing, or troubleshooting CI/CD pipelines for GitHub Actions, GitLab CI, CircleCI, Jenkins, and similar platforms. Triggers: 'set up a CI pipeline', 'write a GitHub Actions workflow', 'my pipeline is failing', 'automate my deployment'. Not for provisioning cloud infrastructure from scratch, writing application code, or designing database migration strategies."
version: 1.0.0
author: community
tags: [devops, ci-cd, github-actions, automation]
license: MIT
---

# CI/CD Helper

## Overview
The CI/CD Helper skill designs, writes, and debugs continuous integration and continuous delivery pipelines across the most widely used platforms: GitHub Actions, GitLab CI/CD, CircleCI, Jenkins, Bitbucket Pipelines, and Azure DevOps. It covers the full pipeline lifecycle — workflow triggers, job dependencies, matrix builds, secrets management, caching strategies, artifact handling, environment promotion, and deployment gates. The skill produces production-ready YAML configurations with inline comments explaining each decision, following security and performance best practices such as least-privilege secrets scoping, dependency caching, and ephemeral environment teardown.

## When to Use
- Writing a new CI/CD pipeline YAML from scratch for any supported platform
- Adding a build, test, lint, or security scan stage to an existing pipeline
- Implementing CD stages with environment promotion (dev → staging → production)
- Troubleshooting pipeline failures: failed steps, flaky tests, misconfigured secrets
- Optimizing pipeline performance with caching, parallelism, or job concurrency limits
- Setting up matrix builds to test across multiple OS, language, or dependency versions
- Configuring secrets management, environment variables, and OIDC-based cloud authentication
- Adding deployment steps for Docker, Kubernetes, AWS, GCP, Azure, Heroku, or Vercel

## When NOT to Use
- Provisioning cloud infrastructure from scratch (use Terraform or CloudFormation skills instead)
- Writing the application code that the pipeline builds and tests
- Designing database schema migrations or rollback strategies
- Managing artifact repositories (Nexus, Artifactory) from scratch
- Setting up monitoring and alerting post-deployment (use the monitoring-setup skill)

## Quick Reference
| Task | Approach |
|------|----------|
| GitHub Actions new workflow | Create `.github/workflows/ci.yml`; specify `on:` triggers, `jobs:`, `steps:` |
| GitLab CI new pipeline | Create `.gitlab-ci.yml` at repo root; use `stages:` and `script:` blocks |
| Secrets management | Use platform secret store; reference as `${{ secrets.MY_SECRET }}` (GHA) or `$MY_SECRET` (GitLab) |
| Dependency caching | Use `actions/cache@v4` (GHA) or `cache:` key (GitLab); key on lockfile hash |
| Matrix builds | Define `strategy.matrix` in GHA or `parallel:matrix:` in GitLab CI |
| OIDC cloud auth (no keys) | Use `aws-actions/configure-aws-credentials` with `role-to-assume` for keyless AWS access |
| Conditional deployment | Use `if: github.ref == 'refs/heads/main'` (GHA) or `only: [main]` (GitLab) |

## Instructions

1. **Identify the platform and language ecosystem** — Confirm the CI/CD platform (GitHub Actions, GitLab CI, etc.), the primary programming language and package manager (Node.js/npm, Python/pip, Java/Maven, etc.), and the deployment target (Docker registry, Kubernetes cluster, cloud PaaS, static hosting).

2. **Define pipeline triggers** — Determine when the pipeline should run: on push to specific branches, on pull/merge requests, on a schedule (cron), on manual dispatch, or on tag creation for release pipelines. Avoid running expensive jobs on every commit to every branch.

3. **Design the job graph** — Map out jobs and their dependencies: typically lint → test → build → security-scan → deploy. Use `needs:` (GHA) or `dependencies:` / `stages:` (GitLab) to enforce ordering. Identify which jobs can run in parallel to minimize total pipeline time.

4. **Configure the runner environment** — Select the appropriate runner OS (`ubuntu-latest`, `windows-latest`, `macos-latest` for GHA; GitLab shared runners or self-hosted). Specify the language runtime version explicitly (e.g., `actions/setup-node@v4` with `node-version: '20'`) to ensure reproducible builds.

5. **Implement dependency caching** — Cache package manager caches keyed on the lockfile hash (e.g., `package-lock.json`, `requirements.txt`, `Pipfile.lock`, `pom.xml`). A cache hit on unchanged dependencies can reduce job time by 60–90%.

6. **Write the test and lint steps** — Run linters (ESLint, Flake8, Pylint, Checkstyle) and the full test suite. Configure test reporters to produce JUnit XML artifacts for pipeline test reporting dashboards. Set coverage thresholds and fail the pipeline if coverage drops below the threshold.

7. **Add security scanning steps** — Integrate SAST tools (Semgrep, CodeQL, Bandit), dependency vulnerability scanners (npm audit, pip-audit, Trivy, Snyk), and container image scanning (Trivy, Grype) into the pipeline. Place these in a parallel job to avoid adding to the critical path.

8. **Configure secrets and environment variables** — Store all sensitive values in the platform's secret store (never hardcode). Use OIDC-based authentication for cloud providers instead of long-lived access keys. Scope secrets to the minimum required environments and branches.

9. **Build and push artifacts** — Build Docker images using multi-stage Dockerfiles; push to a registry (GHCR, Docker Hub, ECR, GCR) tagged with the Git SHA and a semantic version tag on releases. Sign images with Cosign or Docker Content Trust for supply chain security.

10. **Implement deployment stages** — Deploy to dev on every merge to `main`; require a manual approval gate before promoting to staging and production. Use rolling deployments or blue/green strategies. Implement a rollback step triggered on deployment failure.

## Examples

### Example 1: Node.js CI Pipeline with GitHub Actions
**Input:** "Create a GitHub Actions CI pipeline for a Node.js 20 project using npm. It should lint with ESLint, run Jest tests with coverage, and build on PRs and pushes to main. Cache node_modules."

**Output:**
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    name: Lint & Test (Node ${{ matrix.node-version }})
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: ['18', '20']   # Test against LTS versions

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'              # Built-in caching keyed on package-lock.json

      - name: Install dependencies
        run: npm ci                 # Prefer ci over install for reproducible builds

      - name: Run ESLint
        run: npm run lint

      - name: Run Jest tests with coverage
        run: npm test -- --coverage --coverageReporters=text --coverageReporters=lcov

      - name: Upload coverage report
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report-node${{ matrix.node-version }}
          path: coverage/lcov.info
          retention-days: 7

  build:
    name: Build
    runs-on: ubuntu-latest
    needs: lint-and-test          # Only build if lint + tests pass

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js 20
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build production bundle
        run: npm run build

      - name: Upload build artifact
        uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: dist/
          retention-days: 7
```

### Example 2: Python Test + Deploy Pipeline (GitHub Actions)
**Input:** "Write a GitHub Actions pipeline for a Python 3.11 Flask app. Run pytest with coverage, check with flake8, build and push a Docker image to GHCR on merge to main, then deploy to a staging server via SSH."

**Output:**
```yaml
# .github/workflows/ci-cd.yml
name: CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  lint:
    name: Lint (flake8)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'
      - run: pip install flake8
      - run: flake8 . --max-line-length=120 --exclude=.git,__pycache__,venv

  test:
    name: Test (pytest)
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'
      - name: Install dependencies
        run: pip install -r requirements.txt -r requirements-test.txt
      - name: Run pytest with coverage
        run: pytest --cov=app --cov-report=xml --cov-fail-under=80
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}

  build-and-push:
    name: Build & Push Docker image
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main'   # Only on merges to main
    permissions:
      contents: read
      packages: write

    steps:
      - uses: actions/checkout@v4

      - name: Log in to GHCR
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}  # GITHUB_TOKEN auto-provided

      - name: Extract Docker metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=sha,prefix=sha-
            type=raw,value=latest

      - name: Build and push image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  deploy-staging:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    needs: build-and-push
    environment: staging           # Requires environment protection rules in GitHub

    steps:
      - name: Deploy via SSH
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.STAGING_HOST }}
          username: ${{ secrets.STAGING_USER }}
          key: ${{ secrets.STAGING_SSH_KEY }}
          script: |
            docker pull ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
            docker stop flask-app || true
            docker rm flask-app || true
            docker run -d --name flask-app \
              -p 5000:5000 \
              --env-file /etc/flask-app/.env \
              --restart unless-stopped \
              ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
```

## Best Practices
- Pin action versions to a full SHA or major version tag (e.g., `actions/checkout@v4`) — never use `@main`
- Use `npm ci` instead of `npm install` in pipelines for reproducible, lockfile-enforced installs
- Cache dependencies keyed on the lockfile hash so cache invalidates automatically when dependencies change
- Scope secrets to the minimum required environments and branches — avoid global org-level secrets for app-specific values
- Use OIDC federation for cloud authentication (AWS, GCP, Azure) instead of storing long-lived access keys as secrets
- Add a manual approval gate (`environment` with protection rules) before deploying to production
- Run security scans (Trivy, Semgrep, npm audit) in parallel with tests — not sequentially — to minimize pipeline time
- Use matrix builds to test across multiple runtime versions and operating systems

## Common Mistakes
- Hardcoding secrets or API keys directly in workflow YAML — always use the platform secret store
- Using `@latest` or `@master` for third-party actions — introduces supply chain risk; pin to a version tag or SHA
- Running all jobs sequentially when many can be parallelized — dramatically increases pipeline duration
- Not caching dependencies — causes repeated multi-minute installs on every run
- Forgetting to restrict deployment jobs with `if: github.ref == 'refs/heads/main'` — leads to accidental deployments from feature branches
- Checking in `.env` files or using `env:` blocks for secrets in YAML — secrets must come from the secret store
- Not setting `permissions:` on jobs — using overly broad default `GITHUB_TOKEN` permissions

## Tips & Tricks
- Use `workflow_dispatch` trigger with input parameters to enable manual pipeline runs with custom options (e.g., target environment)
- Add `concurrency:` group settings to cancel in-progress runs when a new commit is pushed to the same branch
- Use `paths:` filter on push triggers to skip CI for documentation-only changes
- Store reusable workflow logic in `.github/workflows/reusable-*.yml` and call with `uses: ./.github/workflows/reusable-build.yml`
- Use GitHub Actions `::group::` and `::endgroup::` log commands to collapse verbose step output in the UI
- For monorepos, use path filters on `on.push.paths` to run only the pipeline for the changed service
- Set `timeout-minutes:` on jobs to prevent runaway jobs from consuming minutes quota indefinitely

## Related Skills
- [docker-expert](../docker-expert/SKILL.md)
- [kubernetes-helper](../kubernetes-helper/SKILL.md)
- [monitoring-setup](../monitoring-setup/SKILL.md)
- [security-auditor](../security-auditor/SKILL.md)
