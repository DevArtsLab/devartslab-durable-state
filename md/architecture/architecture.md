# Architecture

## Purpose

Provide a small, language-neutral foundation for durable relational state:
portable SQLite schema conventions, migration history, and operational
contracts that multiple DevArts Lab projects can adopt without sharing their
data.

The normative implementation artifacts are SQL files and the documented
behavioral contract. Language-specific adapters may be added later only when
there is a demonstrated consumer need.

## System boundary

This repository is a specification and reference-artifact repository. It does
not run a database server, host application data, provide authentication, or
connect applications to one another.

```text
Project A ── its SQLite-compatible store ── Project A's schema and data
Project B ── its SQLite-compatible store ── Project B's schema and data
                         │
                         └── both may adopt this repository's contract
```

Consumers own their database instance, schema, retention policy, access
controls, backup destination, and recovery process. A shared convention is not
a shared database.

## Foundation relationship

The [DevArts Lab Foundation](https://github.com/DevArtsLab/devartslab-foundation)
is the authority for lab-wide platform strategy and architectural decisions.
Its D3 storage default is D1 for relational/reporting data and Durable Object
SQLite for per-entity state, with R2 for files and KV only for read-heavy
configuration. This repository adopts the SQLite-compatible schema and
migration concerns; it does not redefine the platform selection.

Each consumer still records its actual storage choice and platform-specific
constraints in its own architecture documents and ADRs. For example, a local
single-user tool may use a local SQLite file, while a Cloudflare production
service follows the Foundation's D1 or Durable Object model.

## Design principles

1. **Isolation by project:** never centralize unrelated project or client
   records in one shared database.
2. **Portable SQL first:** keep the shared contract independent of a client
   programming language and avoid requiring optional SQLite extensions.
3. **Explicit migration history:** version schema changes, detect changed
   migration files, and never silently rewrite an applied migration.
4. **Safe boundaries:** bind data values, authorize operations in the
   application, and treat migrations as reviewed code.
5. **Recoverability:** backups are useful only when restore and integrity
   checks are exercised.
6. **Platform-aware adoption:** SQLite compatibility does not imply identical
   operational semantics across native SQLite, D1, and Durable Objects.

## Initial artifacts

- `migrations/0001_create_schema_migrations.sql` defines the reference
  migration ledger.
- `md/architecture/sqlite-contract.md` defines migration and portability
  behavior.
- `tests/` verifies that the reference SQL applies to a fresh SQLite database.

There is deliberately no shared domain schema. A consumer's domain entities
belong in that consumer's repository and database.

## Open implementation boundary

No runtime migration runner is included in this initial version. A future
adapter may implement the contract in a consumer's language, but it must:

- provide parameterized operations for runtime values;
- apply each migration with platform-appropriate atomicity;
- compare applied checksums with repository migration files;
- stop on unknown, missing, or modified migration history; and
- expose a clear backup and restore procedure.
