# Changelog

All notable changes to this project will be documented in this file.

## [v0.2.0] - 2025-06-12

### ✨ Added
- `/debug/info`, `/debug/tables`, `/debug/sql` demo endpoints (gated via `--demo-mode` or `MCP_DEMO_MODE`)
- `docs/api.md` with full HTTP API reference
- GitHub Actions CI badge and deployment workflows
- `mkdocs.yml` and Pages-ready docs site
- CLI options: `--demo-mode`, `--log-level`
- ASCII banner on startup

### 🛠 Changed
- Merged `app/` into `cockroachdb_mcp_server/` for cleaner structure
- All SQLAlchemy connections now resolve correct dialect (CockroachDB vs PostgreSQL)
- Improved error handling and schema initialization

### 🧪 Fixed
- Incorrect usage of `uvicorn.run(..., env=...)` removed
- Redirects and validation issues in `/debug/sql` fixed
- Typo in health check route (`/healtz` → `/healthz`)

---

## [v0.1.0] - 2025-06-11

### Added
- Initial public release of `cockroachdb-mcp-server`
- FastAPI server implementing MCP spec
- REST endpoints for context CRUD (`/contexts`)
- SQLAlchemy integration with CockroachDB
- Automatic dialect fix for `cockroachdb://` and `postgresql://` prefixes
- CLI entrypoint via `cockroachdb-mcp-server serve`
- Schema bootstrap via `--init-schema` or `MCP_AUTO_INIT_SCHEMA`
- ASCII banner (`--banner`) and version info (`--version`)
- Structured logging (`--log-level`)

### Known Limitations
- No `/run`, `/deploy`, or `/evaluate` endpoints yet
- No auth or rate limiting (coming in future versions)
