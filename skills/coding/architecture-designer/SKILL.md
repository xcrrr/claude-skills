---
name: architecture-designer
description: "Use this skill when designing system architecture, making technology stack decisions, evaluating trade-offs between architectural patterns, or writing Architecture Decision Records (ADRs). Trigger phrases: 'design a system for', 'what architecture should I use', 'monolith vs microservices', 'how should I structure this'. Not for implementation-level code design or UI/UX design."
version: 1.0.0
author: community
tags: [coding, architecture, system-design, patterns, microservices]
license: MIT
---

# Architecture Designer

## Overview
The Architecture Designer skill guides the creation of well-structured, scalable, and maintainable software systems. It covers selecting the right architectural pattern for the problem (monolith, microservices, event-driven, layered/hexagonal), conducting trade-off analysis using established frameworks, writing Architecture Decision Records (ADRs) to document decisions, and reasoning about scalability, reliability, and operational complexity. Good architecture serves the current and anticipated needs of the system without over-engineering for hypothetical future scale.

## When to Use
- Starting a new system or service and choosing the overall structure
- Evaluating whether to split a monolith into microservices
- Designing the data flow between components (sync vs. async, events vs. REST)
- Making technology choices with lasting consequences (messaging, database type, framework)
- Documenting architectural decisions for team alignment and future reference

## When NOT to Use
- Implementation-level code structure within a single service (use refactorer skill)
- Database schema design for a single service (use sql-expert skill)
- API endpoint design (use api-designer skill)
- Infrastructure and DevOps decisions (deployment, networking, cloud IAM)

## Quick Reference
| Pattern | Best For | Trade-off |
|---------|----------|-----------|
| Monolith | Small teams, early product, CRUD-heavy | Simple to develop; harder to scale independently |
| Microservices | Large teams, independent scaling, different tech stacks | Complex operations; network overhead; distributed tracing needed |
| Modular Monolith | Growing team, future microservice migration | Best of both worlds at moderate scale |
| Event-Driven | Async workflows, decoupled producers/consumers | Eventual consistency; harder to debug; ordering issues |
| Layered (N-tier) | Standard CRUD apps with clear separation | Can create rigid coupling between layers |
| Hexagonal (Ports & Adapters) | Testable, domain-first design; framework-agnostic core | More boilerplate; learning curve |
| CQRS | Read-heavy systems where reads/writes have different models | Complexity; sync challenges between command and query sides |
| Saga | Distributed transactions across services | Complex compensation logic; eventual consistency |

## Instructions

1. **Gather requirements**
   - **Functional**: What does the system do? Core use cases, user types, integrations.
   - **Non-functional**: Expected load (requests/sec, users), latency targets (p99 < 200ms?), availability (99.9%?), data volume, compliance requirements.
   - **Constraints**: Team size, existing infrastructure, budget, deployment environment, time to market.

2. **Identify the key architectural drivers**
   - Which non-functional requirements most constrain the design? (Scale? Latency? Consistency? Compliance?)
   - What are the riskiest unknowns? Spike those first.
   - Apply the "It Depends" rule — the right architecture depends on specific context, not on trends.

3. **Choose the primary architectural style**
   - **Start with a monolith** unless you have a clear, proven need for microservices (independent scaling of components, truly independent teams, different runtime requirements).
   - **Modular monolith** is often the right middle ground — enforce module boundaries inside one deployable unit.
   - **Microservices** only when the organizational and operational maturity exists to support them.
   - **Event-driven** when you need to decouple producers and consumers or process async workflows.

4. **Design the component diagram**
   - Identify major components: client, API gateway, services, data stores, external integrations.
   - Define communication patterns: synchronous (REST/gRPC) for request-response; asynchronous (message queue/event bus) for fire-and-forget and fan-out.
   - Assign data ownership: each component owns its data; never share a database between services.

5. **Address cross-cutting concerns**
   - **Authentication/Authorization**: Who authenticates? (API Gateway, each service?) JWT vs. session.
   - **Observability**: Structured logging, distributed tracing (OpenTelemetry), metrics (Prometheus).
   - **Resilience**: Circuit breakers, retries with exponential backoff, bulkheads, timeouts.
   - **Data consistency**: Strong (single DB) vs. eventual (events). Choose based on business requirements.

6. **Analyze trade-offs explicitly**
   - For each major decision, list pros, cons, and alternatives considered.
   - Use a simple scoring matrix if the team is divided.
   - Document the decision in an ADR.

7. **Write an Architecture Decision Record (ADR)**
   Use the template below for every significant architectural decision.

8. **Plan for evolution**
   - What would need to change as the system grows 10x? 100x?
   - How hard would it be to swap a component (e.g., change the database)?
   - Can the architecture absorb new requirements without a full rewrite?

## ADR Template

```markdown
# ADR-001: [Short Decision Title]

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-XXX

## Context
[Describe the situation, problem, or question that forced a decision.
Include relevant constraints and goals.]

## Decision
[State the decision clearly and concisely.
"We will use X because Y."]

## Alternatives Considered
| Option | Pros | Cons |
|--------|------|------|
| Option A | ... | ... |
| Option B | ... | ... |
| Option C | ... | ... |

## Consequences
**Positive:**
- ...

**Negative:**
- ...

**Risks:**
- ...

## References
- [Link to relevant RFC, blog post, or prior art]
```

## Examples

### Example 1: Design a social media feed system

**Input:** "Design the architecture for a social media feed — users post content, follow each other, and see a personalized feed of posts from followed users. Target: 10M users, 1M daily active, 100K peak requests/sec."

**Output:**

**Key Drivers:**
- Scale: 100K rps at peak — must horizontally scale reads
- Read >> Write: feed reads outnumber posts ~50:1 — optimize for reads
- Latency: feed load < 200ms p99
- Eventual consistency acceptable: a 1–2 second delay in feed is fine

**Architecture: Hybrid Fan-out**

```
┌──────────────┐     ┌─────────────┐     ┌─────────────────┐
│   Client     │────▶│ API Gateway │────▶│  Post Service   │
│  (Web/Mobile)│     │  (Auth, TLS)│     │  (Write path)   │
└──────────────┘     └─────────────┘     └────────┬────────┘
                                                  │ publishes
                                         ┌────────▼────────┐
                                         │  Message Queue  │
                                         │  (Kafka/SQS)    │
                                         └────────┬────────┘
                                                  │ consumes
                                         ┌────────▼────────┐
                                         │  Feed Fanout    │
                                         │    Worker       │
                                         └────────┬────────┘
                           ┌─────────────┐        │ writes to
                           │  Feed Cache │◀───────┘
                           │  (Redis)    │       per-user inbox
                           └────────┬────┘
                                    │
┌──────────────┐     ┌─────────────▼─┐
│   Client     │────▶│ Feed Service  │ (Read path — hits cache first)
└──────────────┘     └───────────────┘
```

**Key Decisions:**

**Posts DB:** PostgreSQL (for ACID, relational queries). Shard by `user_id`.

**Feed fanout strategy:**
- *Fan-out on write* (push): when a user posts, push to followers' Redis inboxes. Fast reads; expensive writes for celebrity accounts.
- *Fan-out on read* (pull): compute feed on request. Slow reads; simple writes.
- **Decision**: Hybrid — push to regular followers' inboxes; pull celebrity posts at read time.

**Feed Cache:** Redis sorted set per user, scored by timestamp. Store last 200 posts.

**Scalability path:**
- Add read replicas for Post DB as read traffic grows
- Kafka partitioning by `user_id` ensures ordered events per user
- Redis Cluster for horizontal cache scaling

**ADR for Feed Strategy:**
```markdown
# ADR-001: Feed Fanout Strategy

**Date:** 2024-01-15
**Status:** Accepted

## Context
Feed reads vastly outnumber writes. We need feed load < 200ms.
Celebrity accounts (>100K followers) make fan-out on write expensive.

## Decision
Use hybrid fanout: fan-out on write for users with <10K followers;
fan-out on read for celebrity accounts, merged at read time.

## Alternatives Considered
| Option | Pros | Cons |
|--------|------|------|
| Fan-out on write only | Fast reads | Celebrity posts spike write load |
| Fan-out on read only | Simple writes | Slow feed loads for followed-many accounts |
| Hybrid (chosen) | Balances read speed and write cost | More complex implementation |

## Consequences
Positive: p99 feed load < 200ms; write path scales independently.
Negative: Two code paths to maintain; requires follower count metadata.
```

---

### Example 2: Design a payment processing service

**Input:** "Design a payment processing microservice that handles charges, refunds, and webhooks from Stripe."

**Output:**

**Key Drivers:**
- Correctness over performance — a missed payment or double charge is a business-critical failure
- Idempotency — retries must not cause duplicate charges
- Auditability — every state transition must be logged
- Compliance — PCI-DSS scope must be minimized

**Architecture: Event-Sourced Saga**

```
┌──────────────┐     ┌──────────────────┐     ┌────────────────┐
│ Order Service│────▶│ Payment Service  │────▶│  Stripe API    │
│              │     │                  │◀────│  (external)    │
└──────────────┘     │  - Idempotency   │     └────────────────┘
                     │  - State machine │
                     │  - Audit log     │     ┌────────────────┐
                     └────────┬─────────┘     │ Webhook Handler│
                              │ events        │  (Stripe →us)  │
                     ┌────────▼─────────┐     └────────┬───────┘
                     │  Payment Events  │              │
                     │  DB (append-only)│◀─────────────┘
                     └──────────────────┘
```

**Idempotency pattern:**
```python
# Every charge request includes an idempotency key
def charge(order_id: str, amount_cents: int, idempotency_key: str):
    existing = db.payments.find_by_idempotency_key(idempotency_key)
    if existing:
        return existing  # Return cached result, don't re-charge

    result = stripe.charge.create(
        amount=amount_cents,
        idempotency_key=idempotency_key
    )
    db.payments.create(
        order_id=order_id,
        stripe_charge_id=result.id,
        idempotency_key=idempotency_key,
        status='succeeded'
    )
    return result
```

**Payment state machine:**
```
PENDING → PROCESSING → SUCCEEDED
                     ↘ FAILED
SUCCEEDED → REFUND_PENDING → REFUNDED
```

**Webhook handling (idempotent):**
```python
@app.route('/webhooks/stripe', methods=['POST'])
def stripe_webhook():
    event = stripe.Webhook.construct_event(
        request.data,
        request.headers['Stripe-Signature'],
        WEBHOOK_SECRET  # Verify authenticity
    )
    # Idempotent: process only if not already handled
    if not db.webhook_events.exists(event.id):
        handle_event(event)
        db.webhook_events.mark_processed(event.id)
    return '', 200
```

## Best Practices
- Match the architecture to the team, not to the trend — a two-person startup doesn't need Kubernetes and 20 microservices
- Data consistency requirements drive architecture more than anything else: identify them early
- Design for the failure case — every network call can fail; every service can be slow
- Make services independently deployable from day one if you're doing microservices
- Keep the operational burden in scope — microservices are operationally expensive

## Common Mistakes
- Jumping to microservices before the domain is well understood (premature decomposition)
- Sharing a database between services (creates tight coupling at the data layer)
- Ignoring operations: who deploys, monitors, and debugs this in production?
- Building for 100x current scale on day one (over-engineering adds real cost and complexity now)
- Not writing ADRs — future team members have no context for past decisions

## Tips & Tricks
- Draw the architecture on a whiteboard first; validate with the team before writing code
- "You must be this tall to use microservices" — start with a modular monolith; extract services when team/scaling pain is concrete
- Use the C4 model (Context → Container → Component → Code) for layered architecture diagrams
- Martin Fowler's "Strangler Fig" pattern is the safest way to migrate a monolith incrementally
- Treat ADRs as living documents — update them when decisions are revisited

## Related Skills
- [api-designer](../api-designer/SKILL.md)
- [sql-expert](../sql-expert/SKILL.md)
- [security-auditor](../security-auditor/SKILL.md)
- [refactorer](../refactorer/SKILL.md)
