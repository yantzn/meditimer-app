---
name: test-design
description: Creates verification plans, boundary-condition and negative tests for Flutter, medication timing, offline durability, family sync and Firestore authorization; use when implementing acceptance criteria or reviewing test coverage.
---

# Test design

1. Convert Jira acceptance criteria into Given / When / Then tests; include requirements and evidence links.
2. Partition by unit (pure time calculations, domain decisions), repository (transactions/persistence), widget (user messaging), integration (cross-device sync and OS parity), and security emulator (Firestore authorization).
3. Include negative cases from `.agents/rules/medication-safety.md` and `.agents/rules/security.md`.
4. Time: 01:30+330min=07:00; 20:00+435min=next-day03:15; unset/0/negative interval; date boundaries; clock/timezone changes; retroactive corrections and multiple children.
5. Offline/sync: create on two devices, disconnect/reconnect, duplicated send, two concurrent events, correction/undo, member revocation, stale sync indicator, data retention.
6. Security: authorized family member succeeds; unauthenticated, unrelated family and revoked family members fail (use Firebase emulator, never production credentials).
7. Deliver a test matrix with test ID, intent, fixture, command, expected evidence, what remains manual. **Do not claim a test passed without running it.**
