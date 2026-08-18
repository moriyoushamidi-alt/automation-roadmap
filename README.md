# Automation Roadmap

A hands-on portfolio built while working through a 24-week roadmap to become an automation specialist. The centerpiece is a production-minded lead intake pipeline built with n8n, FastAPI, and PostgreSQL.

## What this project does

**Lead Intake** receives leads from an external source, validates them against business rules, rejects duplicates, and stores valid records in a database. Every rejected record is written to a structured error log with a correlation ID, so no lead ever fails silently.

The point isn't that it moves data from A to B. The point is that it keeps working when things go wrong — bad input, duplicate submissions, network failures, unauthorized requests.

## Architecture

```
HTTP request
    ↓
Webhook (header authentication)
    ↓
Code node (generates correlation ID)
    ↓
Remove Duplicates (idempotency)
    ↓
HTTP Request → FastAPI service (business logic)
    ↓
IF (routes on validation result)
    ├── valid   → PostgreSQL: leads
    └── invalid → PostgreSQL: error_logs
```

Three independent layers, each doing one job:

- **n8n** orchestrates — connects services, routes data, handles retries
- **FastAPI** decides — business rules live here, in testable Python
- **PostgreSQL** guarantees — constraints enforce data integrity regardless of what the application layer does
![Lead Intake workflow](lead-intake.png)

## Tech stack

| Tool | Role |
|---|---|
| n8n | Workflow orchestration |
| FastAPI | Business logic service |
| PostgreSQL | Data layer |
| Docker | Container infrastructure |
| pytest | Automated testing |

## Key features

**Authentication on the webhook.** Requests without a valid `Authorization` header are rejected before the workflow runs.

**Idempotency at two layers.** The workflow deduplicates on email address, and the database enforces a `UNIQUE` constraint on the same column. If the workflow layer is bypassed or breaks, the database still refuses duplicate records.

**Structured error logging.** Rejected leads are written to `error_logs` with a correlation ID, severity level, flow name, failure reason, and the complete original payload stored as JSONB — queryable after the fact.

**Correlation IDs.** Every record gets a unique traceable identifier at the point of entry, making it possible to follow a single record through the entire pipeline.

**Error handling that surfaces failures.** Nodes are configured with retry-on-fail and a dedicated error output path. A separate error workflow catches failures at the workflow level. Nothing dies silently.

**Automated tests.** The validation service ships with pytest coverage for both success and failure paths — 4 tests running in under half a second.

## Database schema

```sql
CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    city TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE error_logs (
    id SERIAL PRIMARY KEY,
    correlation_id TEXT NOT NULL,
    level TEXT NOT NULL,
    flow_name TEXT NOT NULL,
    message TEXT NOT NULL,
    received_data JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## Project structure

```
main.py                    FastAPI validation service
test_main.py               pytest suite
Lead Intake.json           Main pipeline workflow
Error Handler.json         Workflow-level error notification
Webhook Practice.json      Webhook and expression exercises
Practice1.json             HTTP error handling exercises
*.py                       Python fundamentals exercises
```

## Running locally

**Start the infrastructure:**

```bash
docker start postgres
docker start n8n
```

Or, on a fresh machine:

```bash
docker run -d --name postgres \
  -e POSTGRES_PASSWORD=<your-password> \
  -e POSTGRES_DB=automation \
  -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres:16

docker run -d --name n8n -p 5678:5678 \
  -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n

docker network create automation-net
docker network connect automation-net postgres
docker network connect automation-net n8n
```

**Start the validation service:**

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install fastapi uvicorn pytest httpx
uvicorn main:app --reload
```

Interactive API docs are then available at `http://127.0.0.1:8000/docs`.

**Run the tests:**

```bash
pytest
```

## Testing the pipeline

```bash
# Valid lead — stored in leads table
curl.exe -H "Authorization: Bearer <token>" \
  "http://localhost:5678/webhook-test/lead-intake?name=Ali&email=ali@example.com&city=Tehran"

# Invalid email — logged to error_logs
curl.exe -H "Authorization: Bearer <token>" \
  "http://localhost:5678/webhook-test/lead-intake?name=Ali&email=broken&city=Tehran"

# No auth header — rejected at the webhook
curl.exe "http://localhost:5678/webhook-test/lead-intake?name=Ali&email=ali@example.com"
```

## Roadmap progress

| Phase | Focus | Status |
|---|---|---|
| 1 | Python fundamentals, files, JSON, APIs, Git | Complete |
| 2 | n8n workflows, error handling, idempotency, credentials | Complete |
| 3 | PostgreSQL, custom API service, automated testing | Complete |
| 4 | Browser automation, monitoring, health checks | Next |
| 5 | CRM MVP | Planned |
| 6 | Lightweight ERP module | Planned |

## Notes

Credentials and tokens are never committed. n8n credentials are stored in n8n's encrypted credential store and referenced by ID in exported workflows — the exports contain no secrets.
