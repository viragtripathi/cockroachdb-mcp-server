# 📘 API Reference: `cockroachdb-mcp-server`

This document describes the full HTTP API surface of the CockroachDB MCP Server implementation.

---

## 🧠 Overview

All endpoints follow RESTful conventions and are aligned with the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction).

- Base URL: `http://localhost:8081` (by default)
- Content-Type: `application/json`
- Auth: Optional (token-based support planned)

---

## 🔄 `/healthz`

Check server health and readiness.

### Request

```http
GET /healthz
````

### Response

```json
{ "status": "ok" }
```

---

## 📦 `/contexts`

The main endpoint for creating, listing, retrieving, updating, and deleting contexts.

---

### `POST /contexts` — Create a Context

Create a new MCP-compatible context.

#### Request Body

```json
{
  "context_name": "summarizer",
  "context_version": "1.0.0",
  "body": {
    "inputs": ["text"],
    "outputs": ["summary"],
    "description": "Summarize any block of text."
  }
}
```

#### Example

```bash
curl -X POST http://localhost:8081/contexts \
  -H "Content-Type: application/json" \
  -d @context.json
```

#### Response

```json
{
  "status": "created",
  "context_name": "summarizer"
}
```

---

### `GET /contexts` — List Contexts

Returns all registered contexts (minimal metadata).

```bash
curl http://localhost:8081/contexts
```

```json
{
  "contexts": [
    {
      "id": "abc123-uuid",
      "context_name": "summarizer",
      "context_version": "1.0.0",
      "created_at": "2025-06-11T15:30:00Z"
    }
  ]
}
```

---

### `GET /contexts/{id}` — Get by ID

Retrieve full context metadata and body.

```bash
curl http://localhost:8081/contexts/abc123-uuid
```

---

### `PUT /contexts/{id}` — Replace a Context

Submit full replacement for the context (same shape as POST). Partial updates not supported.

---

### `DELETE /contexts/{id}` — Remove a Context

```bash
curl -X DELETE http://localhost:8081/contexts/abc123-uuid
```

---

## 🐛 `/debug/*` — Demo + Diagnostics

> ⚠️ These endpoints are **only available** when the server is started with:
>
> ```bash
> export MCP_DEMO_MODE=true
> cockroachdb-mcp-server serve --demo-mode
> ```

---

### `GET /debug/info`

Returns basic CockroachDB metadata.

```bash
curl http://localhost:8081/debug/info
```

```json
{
  "database": "defaultdb",
  "version": "CockroachDB CCL v25.2.1 ..."
}
```

---

### `GET /debug/tables`

Lists public user-defined tables in the connected CRDB instance.

```bash
curl http://localhost:8081/debug/tables
```

```json
{
  "tables": ["mcp_contexts"]
}
```

---

### `POST /debug/sql`

Execute a **read-only SELECT** SQL statement.

#### Request

```json
{
  "query": "SELECT version()"
}
```

#### Example

```bash
curl -X POST http://localhost:8081/debug/sql \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT version()"}'
```

#### Response

```json
[
  { "version": "CockroachDB CCL v25.2.1 ..." }
]
```

❌ Any non-SELECT query will be rejected.

---

## 🧪 Swagger + OpenAPI

Interactive documentation is auto-generated and available at:

* [Swagger UI](http://localhost:8081/docs)
* [ReDoc](http://localhost:8081/redoc)
* [OpenAPI JSON](http://localhost:8081/openapi.json)

---

## 🔐 Future Enhancements

Planned API extensions:

* `/run` — trigger LLM evaluation
* `/evaluate` — scoring and comparison
* `/deploy` — push to model runtime

Stay tuned.

---