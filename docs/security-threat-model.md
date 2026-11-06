# Security threat model (P0 draft)

Scope: sensitive child profile, medication, symptoms, caregiver identity, offline cache and (P2) synchronized family history. This is a preliminary engineering threat model, **not** a compliance audit.

| Asset / boundary | Attacker scenario | Required mitigation | Verification |
| --- | --- | --- | --- |
| Family-scoped records | Authenticated family A reads/writes family B paths | Server-side family membership/least privilege; deny-by-default | Emulator negative tests for read/list/write |
| Invitations | Forged invite, stolen or replayed token | Expiring/one-use invite design, securely validated grants, revocation | Invite abuse / rejoin tests |
| Membership | Revoked caregiver keeps sync access | Authorization checks on every read/write; refresh/expunge cached access as designed | Post-revocation emulator tests |
| Offline device | Lost/shared device leaks child record | Evaluate local encryption, device lock, logout cache, key storage and backups | Threat review on both OSs |
| Event sync | Concurrent writes erase a dose | Immutable event IDs, audited corrections, idempotent retries, observable conflicts | Two-device offline-reconnect tests |
| App logs/analytics | Names/meds exposed via crash/logs | Data-minimized telemetry and redaction; no raw sensitive values | Code review and synthetic trace check |
| CI/repository | Commit leaks secrets or actions abused | No secrets in code, least privilege workflow permissions, dependency maintenance | Scanning and PR review |
| Billing | Non-paying member accesses protected storage or paying member sees other family | Separate entitlement and family ACL; server rules always enforce membership | Entitlement vs authorization tests |

## Non-negotiable rules

The application is *not* a diagnosis or drug-interaction engine. Avoid unvalidated clinical language. Do not place real child data in tests/fixtures or external AI prompts. Firestore rules must be tested in the emulator before P2 can pass. All denial tests must fail to access another family's data.

## Pending P0 decisions

Authentication provider, invite validation protocol, membership revocation latency, offline storage encryption/backup, analytics and crash telemetry providers, data retention/deletion policy, realistic SLO and incident response. Mark each as undecided until a review assigns an owner.
