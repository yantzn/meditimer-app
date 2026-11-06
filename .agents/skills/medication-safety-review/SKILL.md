---
name: medication-safety-review
description: Reviews caregiver medication logging and interval displays against MediTimer safety invariants, including already-administered doses, clock changes and mixed medicine histories; use whenever medication or timing changes.
---

# Medication safety review

1. Read `.agents/rules/medication-safety.md`, `AGENTS.md`, and related SRS/AC.
2. Trace registration, correction, calculation and presentation from event -> repository -> ViewModel -> widget/PDF.
3. Explicitly verify D-01, D-02, D-05, D-07 and every negative scenario in the rule. Check other-child context and family sync uncertainty.
4. Inspect any timer for caregiver-entered **positive whole minutes, initially unset**; base on actual administered timestamp, not recordedAt or a hardcoded default.
5. For different names/formulations, never infer same/different ingredient or a medically safe combination. For grouped medicines only show user-declared association.
6. Check that out-of-interval doses remain loggable, with warning/context, and historical versions remain auditable.
7. Specify at least one positive and one negative unit/widget test per changed invariant. Flag unverified clinical/legal assumptions separately.

Format: **[Critical/High/Medium/Low] file:line** + user-facing consequence + required correction + regression test. A review result cannot grant medical clearance.
