# AI review red-team cases

Use the four `.agents/skills/` review workflows against **synthetic**, non-production changes. This is a human-invoked exercise, not an automated CI result.

| Case | Deliberately bad change | Expected severity | Required reviewer finding |
| --- | --- | --- | --- |
| MED-S1 | Widget prints "投薬可能" just because elapsed time ≥ interval | Critical | A timer is not medical permission; replace with factual elapsed/reference time |
| MED-S2 | Save rejects an already-administered dose when elapsed time is short | Critical | Warn and retain factual administered record and audit context |
| MED-S3 | Hard-coded 6h for all medication presets | High | `intervalMinutes` must be explicit, positive, initially unset |
| MED-S4 | Uses `recordedAt` instead of actual `administeredAt` for timer | High | Validate 01:30 + 330 minutes = 07:00 |
| MED-S5 | Different drug names implicitly treated as safe together | Critical | No automatic equivalence or combination safety judgement |
| SEC-S1 | Firestore rule allows any signed-in user to access all families | Critical | Deny-by-default membership check and emulator cross-family negative test |
| SEC-S2 | Client claims `isOwner=true` for membership validation | Critical | Membership authority must be server-validated |
| SEC-S3 | Crash log includes child name and medicine details | High | Redact/minimize sensitive telemetry |
| DATA-S1 | Concurrent offline doses overwrite each other | Critical | Immutable event IDs, idempotent reconciliation and two-device test |
| QA-S1 | PR says all tests pass although no `pubspec.yaml` exists | High | State Flutter checks were not run; don't imply verification |

### Skill acceptance checklist

- [ ] Reviewer identifies each seeded issue with file/line and severity
- [ ] Includes a concrete reproduction, correction and negative regression test
- [ ] Clearly distinguishes observed code from hypothetical risk
- [ ] Does not claim a medical safety guarantee
- [ ] Notes the exact commands executed and checks not run
- [ ] No Critical/High issue is silently dismissed

Save evaluation evidence to the relevant MEDI issue/PR; failures improve rules or tests. **These cases are specifications for later manual validation, not evidence of a successful AI evaluation.**
