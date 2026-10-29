# DevArts Lab Durable State

Language-neutral SQLite conventions for applications that need durable,
portable relational state.

This repository defines SQL artifacts and behavioral contracts that projects
can implement with their own language and runtime. It is not a shared database
service, an ORM, or a cross-project data store. Each application owns and
isolates its database and domain schema.

## What this provides

- A conservative SQLite portability contract for schemas and migrations.
- A standard migration ledger and migration naming convention.
- Operational guidance for transactions, backups, restore checks, and safe
  queries.
- Executable checks for the SQL artifacts, using Python's standard-library
  SQLite driver only as a test harness.

## What this does not provide

- A central database or shared authentication store.
- Application-specific tables or data.
- A language-specific database client, ORM, migration runner, or package.
- A promise that every SQLite feature is supported by every SQLite-based
  platform.

## Start here

1. Read [the architecture contract](md/architecture/architecture.md).
2. Read [the SQLite portability contract](md/architecture/sqlite-contract.md).
3. Use the migration ledger in `migrations/` as the template for a project's
   own migration history.
4. Record platform-specific choices in the consuming project's ADRs and verify
   them against that platform's current documentation.

For DevArts Lab projects, this repository complements rather than replaces
the [DevArts Lab Foundation](https://github.com/DevArtsLab/devartslab-foundation).
The Foundation remains the source for lab-wide architecture and platform
decisions; this repository operationalizes the SQLite portion of its storage
guidance.

## Validate

The test harness uses Python's standard library (the CI workflow currently
tests on Python 3.12); the SQL contract itself does not depend on Python.

```sh
python3 -m unittest discover -s tests -v
```

## Status

Initial contract and reference migration. No runtime adapters are published.
See [INDEX.md](INDEX.md) for the repository map.
