---
name: security-review
description: Reviews child-health data security, cross-family Firestore authorization, credentials, logging, offline retention and CI supply chain; use for sync/auth/storage/PR security changes.
---

# Security review

1. Read `AGENTS.md`, `.agents/rules/security.md`, `docs/security-threat-model.md` and the Jira issue.
2. Map identities, family membership, child ownership, trust boundaries, local cache and Firestore document paths touched by the change.
3. Attempt malicious scenarios: anonymous read; user A reads/writes user B's family; forged role; revoked member still writes; unauthenticated invite; child moved between families; stale offline cache; duplicate sync.
4. Inspect data exposure in logs, crash reporting, screenshots, telemetry, backups and network calls. Check keys and tokens are not committed.
5. For Security Rules, require Firebase Emulator positive **and negative** tests. Do not treat mobile UI checks as authorization.
6. Check GitHub Actions token scope, untrusted input usage, dependencies, lockfiles and secret-scanning process.
7. Document exploits, file:line and test evidence; mark untested assumptions explicitly. Critical unauthorized data access is a release blocker.

Output: findings with Critical/High/Medium/Low, attack preconditions, evidence, affected scope, concrete remediation and regression test; then residual risks and checks actually executed.
