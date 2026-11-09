# ADR-0016: Language-neutral SQL contract

- Status: accepted
- Date: 2026-10-28
- Scope: project-specific

## Context

The durable-state foundation is intended for use by multiple projects, which
may use different programming languages and runtime platforms. Choosing one
driver or ORM as the foundation would couple consumers to that ecosystem and
would not address SQLite host differences.

## Decision

Keep the normative foundation language-neutral: SQL artifacts, migration
conventions, and observable behavioral requirements are the shared interface.
Do not require a particular driver, ORM, migration-runner implementation, or
application language.

Python's standard-library SQLite driver may be used for repository tests, but
is not a consumer dependency. Future language-specific adapters must be
separately justified, scoped, and tested against this contract.

## Alternatives considered

1. **One language-specific package:** rejected because it narrows adoption and
   makes the package API, rather than the data contract, the shared source.
2. **Only prose documentation:** rejected because reference SQL and executable
   checks make the contract more concrete without requiring a runtime package.
3. **One central SQLite database for all projects:** rejected because it
   couples data ownership, security boundaries, availability, and offboarding.

## Consequences

- Consumers implement the same contract with their runtime's supported
  database APIs.
- Platform-specific differences remain explicit in consumer ADRs.
- A future adapter may duplicate some small integration logic, but cannot
  silently redefine the schema or migration semantics.
