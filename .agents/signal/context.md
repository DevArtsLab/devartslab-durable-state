# Project context

- Updated: 2026-10-28
- Repository or folder: DevArtsLab/devartslab-durable-state
- Visibility: public
- Context confidence: verified

## Purpose

Language-neutral SQLite conventions, reference SQL migrations, and operational
contracts for applications that need isolated durable relational state.

## Current state

Initial repository foundation. It defines a migration ledger and SQLite
portability contract, with a Python standard-library test harness. No
language-specific runtime adapter or shared database service is provided.

## Technology and architecture

- SQL artifacts and behavioral contracts are the normative interface.
- Each consuming project owns and isolates its database and domain schema.
- Python `sqlite3` is used only to validate reference SQL in tests.
- DevArts Lab production storage choices remain governed by Foundation D3.

## Key locations

- `md/architecture/architecture.md`: scope and integration boundaries.
- `md/architecture/sqlite-contract.md`: portability, migrations, safe queries,
  transactions, and recovery requirements.
- `migrations/`: reference migration history.
- `tests/`: executable SQL artifact checks.
- `md/adr/`: adopted storage and language-neutrality decisions.

## Verified work and outcomes

- The initial migration creates a checksum-ready `schema_migrations` ledger.
- The contract explicitly distinguishes native SQLite validation from
  provider-specific validation.

## Open work and constraints

- No application runtime migration runner or language adapter is included.
- Consumer projects must verify current platform-specific behavior, including
  transactions, limits, concurrency, and backup/restore.
- The repository does not store or centralize consumer data.

## Sources

- `README.md`
- `md/architecture/architecture.md`
- `md/architecture/sqlite-contract.md`
- `md/adr/ADR-0003-storage-selection.md`
- https://github.com/DevArtsLab/devartslab-foundation
