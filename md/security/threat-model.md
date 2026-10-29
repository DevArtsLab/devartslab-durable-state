# Threat model

## Scope

This repository contains SQL conventions, reference migrations, documentation,
and a local test harness. It does not receive consumer data or run a hosted
database service.

Consuming applications must extend this baseline with their own assets, data
classification, trust boundaries, attackers, platform controls, and recovery
requirements. See the [DevArts Lab Foundation threat model](https://github.com/DevArtsLab/devartslab-foundation/blob/master/md/security/LAB-THREAT-MODEL.md).

## Assets and boundaries

| Asset | Boundary |
| --- | --- |
| Consumer database records | Owned and controlled by each consuming application |
| Schema and migration history | Reviewed and versioned in the consumer repository |
| Backup copies | Consumer-selected storage and access policy |
| SQL reference artifacts | This public repository and its release workflow |

## Threats and baseline controls

| Threat | Baseline control |
| --- | --- |
| SQL injection in a consumer | Require parameter binding for values; allowlist identifiers |
| Malicious or mistaken migration | Review changes, test on a fresh database, preserve immutable history, require backup plans for destructive changes |
| Migration history tampering | Record and compare checksums; halt on changed or missing applied migrations |
| Data loss or corrupt restore | Consumer documents and exercises platform-supported backup and restore checks |
| Cross-project data exposure | Each consumer owns its own store; no shared database is provided |
| Secret or personal data committed to this repository | Keep consumer records out of this repository; review changes and ignore local database artifacts |
| Platform compatibility assumption | Require consumers to verify host documentation and add provider-level tests |

## Residual risks

- The contract cannot enforce how a consumer implements its own runner,
  authorization, backup, or retention policy.
- Local SQLite tests cannot prove managed-host transaction semantics,
  availability, security, or backup behavior.
- A malicious migration may still pass syntax checks; code review and
  environment-specific controls remain necessary.
