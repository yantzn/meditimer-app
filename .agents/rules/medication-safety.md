# Medication safety invariants — MUST review

This project is a **log** for caregivers and clinicians, not a clinical decision support or prescription engine.

## P0/P1 critical acceptance

- D-01: `before dose: check history` and `dose already administered: record fact` are distinct user flows. A dose already given must be recordable even if the configured interval has not elapsed; show an explicit warning and permit factual recording with context. Never lose the event.
- D-07: `intervalMinutes` is caregiver entered, **integer > 0**, per medication preset; default is **unset**. Do not infer from drug name/age/weight. No timer when unset.
- `referenceTime = most recent actual administeredAt + intervalMinutes` for the configured preset. Display the **elapsed-time reference**, not a medication authorization. Example: 01:30 + 330 min = 07:00, including midnight rollover.
- D-02: P1: check same-preset timing and show all-medication history; do **not** assume medicines with different names have different active ingredients. P2: explicitly caregiver-associated related-medication groups, no automatic ingredient/interaction claims.
- D-05: reject labels such as `投薬可能`, `投与して安全`, `脱水なし`, `併用してよい` and any equivalent unqualified claim.
- Corrections must preserve immutable factual event versions, original timestamp, author and correction reason; deleted history must remain auditable.
- Uncertain or unsynced family history cannot be presented as complete.

## Mandatory negative scenarios

1. Interval unset or 0: no countdown / validation failure.
2. Dose at 01:30 + 5h30m: reference 07:00, not 05:15 or 06:00.
3. Dose at 20:00 + 7h15m: next-day 03:15.
4. Backdated dose with shorter-than-configured elapsed time: warning + factual record still saved.
5. Different medicines not linked: no equivalence/safety assertion, all recent history still visible.
6. Offline second caregiver: outdated state clearly marked, not falsely synchronized.
7. Clock change, DST/timezone change, rapid double-tap and record correction: stable audit and recomputed display.

Severity: false medication authorization, suppressed factual history, cross-child mix-up or undetected overwritten administration => **Critical**. Missing exception coverage, misleading clock, incomplete audit or misleading related-drug grouping => at least **High**, adjust with evidence.

Never substitute AI interpretation for medical or legal review.
