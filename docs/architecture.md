# Architecture principles (draft — MEDI-2 PoC pending)

Status: **proposed**, not yet implemented. Required products: iOS and Android. No permanent application backend is required if the managed cloud solution is viable.

## Logical boundaries

```text
Flutter UI / ViewModels
           |
      Domain models
 (events, clocks, validation)
           |
       Repositories
       /         \
local SQLite    Sync adapter (P2 candidate Firestore)
  (P1)           + Auth / membership / security rules
```

- P1 is offline-first: logging, history, event correction, timer and PDF must work without network.
- P2 synchronization is an eventual-consistency feature; records are local-first and marked queued/sent/acknowledged/conflicted/stale as appropriate. The protocol and exact statuses are subject to PoC.
- Keep event IDs stable and changes auditable; distinguish administration time from save time and sync time. Prefer append-only fact/audit event semantics over silent overwrite.
- P2 caregiver sharing must work across iOS and Android and prevent cross-family access via server-side authorization.
- Subscription entitlement and family membership are separate; billing does not confer data access rights.
- No medical recommendation algorithm; only caregiver-configured elapsed-time display and factual records.

## Evaluation gates

- Flutter/Dart + Drift/SQLite + Firebase Authentication/Firestore Blaze are proposed, not accepted technology commitments.
- Verify device persistence, migration, restored app state, clock abstraction, cross-platform SDK behavior, security rules in emulator, sync cost and quota behavior before adopting.
- State management and dependency injection package choice must be an explicit, documented P0 decision.
- Phase labels P0–P3 refer to roadmap, not fixed delivery dates.

Reference: [Flutter official architecture guidance](https://docs.flutter.dev/app-architecture/recommendations). Use as strong guidance, adapting to MediTimer's actual complexity.
