# Quality gates

## Bootstrap / current reality

Currently `README.md` and repository policy are being prepared, **not the Flutter app**. `repo-policy` runs the Python validation on every PR; `detect-flutter` reports a notice and the separate `flutter-checks` job is *skipped* until `pubspec.yaml` exists. A policy-only PR cannot claim Dart/Flutter tests passed.

Run policy checks locally:
```bash
python3 scripts/validate_quality_policy.py
```

After initializing Flutter in MEDI-2/MEDI-10:
```bash
flutter pub get --enforce-lockfile
dart format --output=none --set-exit-if-changed lib test
flutter analyze --fatal-infos
flutter test --coverage
```

Add `flutter_lints` to dev_dependencies; include committed `pubspec.lock`, `lib/main.dart`, `test/`, and test fixtures. Analysis options are already present.

## Gates by level

| Gate | Applies | Automated | Release condition |
| --- | --- | --- | --- |
| Agent/skill completeness | All PRs | Yes, Python | Must pass |
| Dart formatting and static analysis | After Flutter bootstrap | Yes, CI | Must pass |
| Unit and widget tests | After Flutter bootstrap | Yes, CI | Must pass |
| Native iOS & Android smoke tests | P1 release | Not yet | Manual/CI integration evidence needed |
| Firebase Security Rules emulator tests | P2 release | Not yet | Cross-family denies must pass |
| Sync offline/conflict/revocation tests | P2 release | Not yet | Evidence required |
| AI PR safety & security review | Relevant change | Manual invocation | Critical/High addressed |
| Threat model / SaMD and legal review | Release | External review | Appropriate decision recorded |

## Reviewer severity policy

- **Critical:** unsupported dosing permission; loss/refusal of already-administered facts; cross-family access; silent destructive sync conflict.
- **High:** misleading timer, missing audit/correction history, unsafe role updates, untested rule change, privacy-sensitive logging.
- **Medium / Low:** correctness, accessibility, resilience or maintainability issues with reduced impact.

AI review only flags potential violations; it is not an autonomous pass/fail certification. For review red-team cases see [ai-review-red-team.md](ai-review-red-team.md). Manual AI skill evaluation is not represented as a CI job.

## GitHub settings needed outside the repository

Configure branch protection/ruleset for `main`: require PR, passing `Repository policy`, and (once Flutter exists) `Flutter format, analyze, test`; require human review if available. Do not turn on mandatory Flutter checks before app bootstrap. Review third-party action pinning and Dependabot security updates.

Do not introduce automatic merges or deployment until risk/rollback policies are agreed. Sensitive sample data must never appear in PR traces.
