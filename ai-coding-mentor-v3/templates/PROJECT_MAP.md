# PROJECT MAP

> Keep this concise. Update only when architecture materially changes.

## Project Purpose

Describe the system in 2–5 sentences.

## Entry Points

| Entry | File / Module | Purpose |
|---|---|---|
| Example: HTTP API | `app/main.py` | FastAPI application entry |

## Architecture

```text
Client
 ↓
API
 ↓
Service
 ↓
Repository
 ↓
Database
```

Replace with the real architecture.

## Core Modules

| Module | Path | Responsibility |
|---|---|---|
|  |  |  |

## Data Stores

| Store | Usage | Source of Truth? |
|---|---|---|
|  |  |  |

## External Services

| Service | Purpose | Failure Impact |
|---|---|---|
|  |  |  |

## Authentication / Authorization

Describe where identity and permission checks occur.

## Background Jobs

| Job | Trigger | Implementation |
|---|---|---|
|  |  |  |

## Important Call Chains

### Example

```text
POST /users
 ↓
UserRouter
 ↓
UserService.create()
 ↓
UserRepository.create()
 ↓
PostgreSQL
```

## Risk Hotspots

- 

## Notes

-
