# Agent instructions

## Purpose and boundaries

- This repository defines language-neutral SQLite conventions and SQL
  artifacts for DevArts Lab projects.
- Keep the data layer project-owned: never introduce a shared cross-project
  database or shared credential store.
- The [DevArts Lab Foundation](https://github.com/DevArtsLab/devartslab-foundation)
  owns lab-wide architectural decisions. This repository implements and
  explains the SQLite-specific contract; do not copy the Foundation's
  architectural corpus here.
- SQL and behavioral contracts are the product. Python is only the current
  test harness; do not make a Python runtime library a consumer requirement.

## Working rules

- Prefer SQLite features with broad support and document any feature outside
  the portability baseline.
- Bind values as parameters; never build SQL by interpolating user-controlled
  values.
- Keep domain tables and user data out of this repository.
- A migration is immutable after release. Add a new migration to correct a
  released schema change; do not rewrite history.
- Do not add a platform-specific runtime dependency without a documented
  requirement and an ADR.
- Keep references to vendor/platform behavior linked to current authoritative
  documentation and dated when they are version-sensitive.

## Validation

Run the standard-library suite:

```sh
python3 -m unittest discover -s tests -v
```

For SQL or migration changes, verify the migration applies to a fresh SQLite
database, the ledger records it, and the tests cover relevant constraints.

## Safety

- Never add credentials, database files, production data, or personal data.
- Review migrations for destructive operations and document required backup
  and recovery steps.
- Do not stage, commit, push, or change remote settings unless the user
  explicitly requests that operation.
