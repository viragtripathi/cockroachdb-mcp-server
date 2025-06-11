# Changelog

All notable changes to this project will be documented in this file.

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
