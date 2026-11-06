## Jira and scope

- Work item: MEDI-___
- Purpose / user impact:
- Scope and non-scope:
- Affected SRS requirement IDs:

## Implementation and verification

- [ ] Changes match Jira acceptance criteria and current Confluence SRS
- [ ] No unreviewed medical/safety claim or interval calculation
- [ ] No cross-family data exposure, silent overwrite or lost recording
- [ ] iOS and Android behavior considered
- [ ] Unit/widget/integration tests added or justified
- [ ] Dart format/analyze/test results provided **if Flutter exists**
- [ ] Any skipped checks listed with reason (not marked passed)
- [ ] No secrets or real child/medication records added

### Commands and evidence

```text
<exact commands executed and results; write "not run" where appropriate>
```

## AI / self review

- [ ] Read AGENTS.md and related .agents/rules/ files
- [ ] Run /flutter-code-review for Flutter changes
- [ ] Run /medication-safety-review for medication/time changes
- [ ] Run /security-review for sync/auth/storage/telemetry changes
- [ ] Run /test-design for regression gaps
- [ ] Include actual findings with severity, file:line, reproduction and status
- [ ] Critical/High findings addressed and reverified

## Deployment / rollback and unresolved risks

- Data migration or persistence impact:
- Offline and sync behavior:
- Residual risks and open questions:
- Follow-up ticket (if needed):
