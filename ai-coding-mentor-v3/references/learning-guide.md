# Learning Guide

The goal is not to teach everything.

Each meaningful task may teach 1–2 things deeply enough to recognize next time. Routine work does not need a forced lesson.

## Good learning target

A good target:

- appeared in the actual task;
- affected correctness, performance, security, or design;
- is reusable in future work;
- can be explained with concrete project code;
- fits the current intervention budget.

Examples include transactions, idempotency, optimistic locking, async blocking, cache invalidation, retry, timeout, pagination, index selectivity, and authorization boundaries.

## Teaching sequence

1. Check the current mentor level and remaining intervention budget.
2. Ask what the user thinks only when useful at that level.
3. Explain the concrete project problem.
4. Explain the concept.
5. Show where it appears in current code.
6. Explain failure without it.
7. Explain how to recognize the pattern next time.
8. Ask one short understanding question.
9. Give one 5–15 minute mini challenge when the user wants practice.

## Avoid

- giant textbook dumps;
- more than two major concepts;
- teaching unrelated syntax;
- pretending explanation equals understanding;
- repeating concepts already mastered;
- delaying authorized delivery for a low-value quiz.

## Knowledge note format

```markdown
# Concept

## Problem
What real problem triggered this?

## Idea
Short explanation.

## In This Project
Where is it used?

## Failure Without It
What breaks?

## Recognition Pattern
What clues should make me think of this next time?

## Ownership
Was the evidence produced by the user, shared work, or AI?
```
