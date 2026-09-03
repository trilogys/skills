# System Design Guide

Use when the task involves non-trivial architecture.

## Start From Constraints

Clarify:

- expected traffic;
- latency;
- consistency needs;
- failure tolerance;
- data volume;
- security;
- operational complexity;
- team familiarity;
- cost.

Do not introduce distributed systems without a concrete need.

## Common Decisions

### Sync vs Queue

Use a queue when work is:

- slow;
- retryable;
- bursty;
- independent of immediate response;
- needs background processing.

Do not use a queue only because it feels "enterprise".

### Cache vs No Cache

Add cache only when there is a measured or predictable read bottleneck.

Always consider:

- invalidation;
- TTL;
- stale data;
- stampede;
- source of truth.

### Database Choice

Prefer existing infrastructure unless requirements clearly justify a new store.

### Microservice vs Monolith

Prefer modular monolith for ordinary product development unless independent scaling, deployment, ownership, or isolation clearly requires service separation.

### Abstraction

Add abstractions after repeated concrete needs become visible.

Avoid speculative layers.

## Architecture Decision Questions

Before adding complexity ask:

1. What exact problem exists?
2. What is the simplest solution?
3. What alternatives exist?
4. What tradeoff are we accepting?
5. What maintenance burden follows?
6. When should this decision be revisited?
