# MediTimer repository instructions for GitHub Copilot

**Primary source of truth is [AGENTS.md](../AGENTS.md).** Read it, the matching `.agents/rules/*.md` and the Jira MEDI issue before changing code. Never replace explicit requirements with generic medication advice.

- Flutter implementation: follow `.agents/rules/flutter-architecture.md`.
- Medication, time, presets, UI claims: follow `.agents/rules/medication-safety.md`; the app records facts and **does not authorize dosing**.
- Authentication, offline cache, Firestore, logging: follow `.agents/rules/security.md`.
- Use the four review skills under `.agents/skills/` when evaluating a PR.
- Include reproduction, severity, test gaps, commands and actual results in reviews. Do not assume automated AI code review runs just because instructions are present.
- Prefer smallest change meeting the Jira AC and keep Critical/High findings unmerged.
