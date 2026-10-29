# INDEX.md - devartslab-durable-state

> Repository map. Update when files or folders are added, removed, or
> substantially rewritten.
>
> **Last updated:** 2026-10-28

## Top-level

| Path | What it is |
| --- | --- |
| `README.md` | Project purpose, scope, and validation entry point |
| `AGENTS.md` | Agent workflow and safety boundaries |
| `INDEX.md` | This repository map |
| `LICENSE` | MIT License |
| `SECURITY.md` | Vulnerability reporting guidance |
| `Makefile` | Short validation command |
| `migrations/` | Reference SQL migration ledger |
| `tests/` | Dependency-free checks for SQL artifacts |
| `md/architecture/` | Storage architecture and portability contract |
| `md/adr/` | Instantiated Foundation decision and project decisions |
| `md/security/` | Repository-specific threat model |
| `.agents/signal/context.md` | Durable project context for repository-aware agents |
| `.github/workflows/` | Continuous validation |

## Architecture

| File | What it covers |
| --- | --- |
| `md/architecture/architecture.md` | Purpose, boundaries, consumers, and integration model |
| `md/architecture/sqlite-contract.md` | Portable SQL, migration, and operational requirements |
| `md/adr/ADR-0003-storage-selection.md` | Adoption of Foundation D3 for SQLite scope |
| `md/adr/ADR-0016-language-neutral-sql-contract.md` | Language-neutral project-specific decision |
| `md/security/threat-model.md` | Data-layer threats and baseline controls |

## SQL and tests

| File | What it covers |
| --- | --- |
| `migrations/0001_create_schema_migrations.sql` | First migration: migration history table |
| `tests/test_migrations.py` | Applies and checks the reference SQL using `sqlite3` |
