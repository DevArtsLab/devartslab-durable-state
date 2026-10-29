# SQLite portability and operations contract

This contract defines the shared baseline for consumers. It is intentionally
not an ORM API or a runtime-specific implementation.

## Compatibility target

- Use SQLite SQL and documented SQLite behavior.
- Use core features available in the SQLite version required by the consumer.
- Do not require loadable extensions, custom collations, or user-defined SQL
  functions in the shared baseline.
- Treat provider compatibility as a separate check. A Cloudflare consumer must
  verify the current D1 or Durable Object SQLite documentation and its
  configured runtime; native SQLite passing is not proof of provider parity.
- Record any feature outside the baseline in the consuming project's
  architecture docs and ADRs.

The baseline does not promise identical locking, concurrency, backup, size,
transaction, or availability behavior across SQLite hosts.

## Schema conventions

- Store timestamps as UTC ISO 8601 text with an explicit `Z` suffix unless a
  consumer records a different representation and conversion contract.
- Make required values `NOT NULL`; define primary keys explicitly.
- Define foreign keys and enable/enforce them using the consumer runtime's
  documented mechanism.
- Add indexes from observed query patterns rather than speculatively.
- Use explicit constraints (`UNIQUE`, `CHECK`, and foreign keys) for invariants
  that must hold regardless of which application path writes a row.
- Avoid ambiguous affinity-dependent values; document the representation of
  booleans, decimals, and enumerated states.
- Do not store credentials or secrets in application tables.

## Migration format and lifecycle

### Naming

Use immutable, lexically sortable names:

```text
NNNN_short_description.sql
```

For example: `0002_create_evidence_items.sql`.

The four-digit sequence is unique within one consuming project. Each consumer
owns its migration sequence and migration files; do not apply this repository's
sequence as a shared global schema.

### Ledger

The first reference migration creates `schema_migrations` with:

| Column | Meaning |
| --- | --- |
| `version` | Unique migration sequence, such as `0001` |
| `name` | Human-readable migration name |
| `checksum` | Digest of the exact migration file bytes |
| `applied_at` | UTC ISO 8601 application time, written by the runner |

The ledger is a reference contract. A runtime adapter may add metadata if
needed, but it must preserve these meanings.

### Runner behavior

A consumer migration runner should:

1. Discover files in lexical order and validate their names.
2. Read the migration ledger before applying later migrations.
3. Apply each unapplied migration once, then record its version, name,
   checksum, and timestamp.
4. Use a transaction or platform-supported atomic batch for the schema change
   and ledger entry when the storage platform supports it.
5. Halt if an applied migration's checksum changed, an applied migration is
   absent from the source set, or versions are duplicated.
6. Report failures clearly and leave the database in a state that can be
   inspected and safely retried according to that platform's transaction
   guarantees.

Do not silently edit or delete a migration that has been applied outside a
developer's disposable database. Correct released schema through a new
migration. Destructive migrations require a documented backup, rollout, and
recovery plan.

## Query safety

- Bind all runtime values through the database driver's parameter mechanism.
- Never interpolate user-controlled values into SQL.
- Identifiers (table or column names) cannot generally be bound as values;
  select them from a closed, application-controlled allowlist.
- Keep authorization decisions in the application boundary; a database file
  or binding does not by itself establish user authorization.

## Transactions and concurrency

- Keep transactions short and avoid holding them across network or user
  interaction.
- Define retry behavior only after checking the target platform's locking and
  transaction semantics.
- Do not assume one native SQLite connection strategy works unchanged on D1
  or Durable Objects.
- For an agent or workflow, persist intent and state transitions before
  external side effects, following the DevArts Lab Foundation's durable-state
  principles.

## Backup, restore, and integrity

- Select a backup method supported by the actual SQLite host; copying a live
  database file may not capture a consistent state.
- Encrypt backups when they contain sensitive application data and restrict
  access to the minimum necessary.
- Document backup frequency, retention, recovery owner, and recovery-point
  objective in the consuming project.
- Test restore into an isolated environment before relying on the backup.
- After restore, run the platform-supported integrity check, inspect the
  migration ledger, and exercise an application-level read path.
- Use the host's supported export/restore mechanisms for managed SQLite
  services; do not assume local file operations are available remotely.

## Consumer checklist

- [ ] Choose local SQLite, D1, or Durable Object SQLite based on the workload
      and the DevArts Lab Foundation's current defaults.
- [ ] Verify current host compatibility, limits, transactions, and backup
      documentation.
- [ ] Keep the database and migration history isolated to the consuming
      project or tenant boundary.
- [ ] Add project-specific schema and migration tests.
- [ ] Document retention, backup, restore, and destructive migration behavior.
- [ ] Keep runtime secrets outside the database and source repository.
