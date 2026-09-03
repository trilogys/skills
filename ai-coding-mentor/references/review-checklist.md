# Review Checklist

Use this for `/review`.

## 1. Correctness

Check:

- wrong conditions;
- missing branches;
- incorrect return values;
- None/null handling;
- state transition errors;
- partial success;
- retry side effects;
- stale assumptions;
- backwards-incompatible behavior.

Questions:

- What happens with empty input?
- What happens on the second execution?
- What happens halfway through failure?
- What happens if a dependency returns unexpected data?
- Is the error surfaced or silently swallowed?

## 2. Data Consistency

Check:

- transaction scope;
- rollback;
- duplicate writes;
- race conditions;
- lost updates;
- stale cache;
- DB/cache inconsistency;
- DB/external-service inconsistency;
- idempotency.

## 3. Security

Use `security-checklist.md`.

## 4. Performance

Check:

- N+1 queries;
- missing/bad indexes;
- repeated I/O;
- blocking work in async code;
- unbounded loops;
- loading huge datasets into memory;
- large response payloads;
- unnecessary serialization;
- cache stampede;
- excessive retries.

## 5. Maintainability

Check:

- duplicated logic;
- giant functions;
- unclear names;
- hidden side effects;
- unnecessary abstractions;
- strong coupling;
- weak typing;
- poor error boundaries;
- magical configuration;
- dead code.

## 6. Testing

Check:

- happy path;
- invalid input;
- boundary values;
- empty input;
- failure path;
- retry;
- duplicate request;
- permission boundary;
- concurrency when relevant;
- regression test for bug fixes.

## Finding Format

```text
Severity: High
Confidence: High
Evidence: code / test / runtime / assumption

Issue:
...

Why it matters:
...

Production scenario:
...

Recommended fix:
...
```
