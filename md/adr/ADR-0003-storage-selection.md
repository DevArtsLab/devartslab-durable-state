# ADR-0003: Storage selection

- Status: accepted
- Date: 2026-10-28
- Foundation decision: D3 storage selection
- Scope: this repository and its reference SQL artifacts

## Context

The DevArts Lab Foundation defines the lab-wide storage defaults: D1 for
relational and reporting data, Durable Object SQLite for per-entity state, R2
for files and artifacts, and KV for read-heavy configuration. This repository
needs to define the SQLite-specific SQL and migration contract without
establishing a central database.

## Decision

Adopt Foundation D3. This repository documents portable SQLite schema and
migration conventions and provides reference SQL. It does not host data or
select the storage product for a consuming application.

Consumers choose the concrete store based on their deployment and workload.
For DevArts Lab production systems, use the Foundation's current D3 default
unless the consumer's architecture records a justified deviation.

## Consequences

- Schema and migration files can be reviewed and tested without binding the
  contract to one application language.
- Every project remains responsible for its own data, runtime integration,
  limits, security, and recovery.
- Native SQLite tests do not establish parity with D1 or Durable Object
  SQLite; consumers must verify host-specific behavior.
- This repository will not introduce a shared credential or application-data
  database.

## Sources

- [DevArts Lab Foundation, MEGA-PLAN: D3 Storage selection](https://github.com/DevArtsLab/devartslab-foundation/blob/master/md/MEGA-PLAN.md)
- [DevArts Lab Foundation, PRE-DEVELOPMENT: ADR-0003](https://github.com/DevArtsLab/devartslab-foundation/blob/master/md/PRE-DEVELOPMENT.md)
