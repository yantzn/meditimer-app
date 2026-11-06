# Security and privacy rules

Threat model: [docs/security-threat-model.md](../../docs/security-threat-model.md). Do not claim a technical control exists until it is implemented and tested.

- Every family/child/event query must enforce server-side least-privilege membership, not rely on client-side filters or user-supplied IDs.
- Cross-family reads, writes and membership escalation must be **denied by default** and tested under the Firebase emulator before sync is released.
- Authn and entitlement are different: payment does not imply access to somebody else's records. Family access cannot be granted by client-generated role assertions.
- Treat child names, symptoms, timestamps and medication details as sensitive. Do not log them, upload real traces, embed in analytics, share crash payloads or commit sample screenshots containing real data.
- Distinguish client config (Firebase web/API key) from privileged credentials. Never commit service account JSON, signing keys, tokens, keystores, certificates, .env with secrets or access refresh tokens.
- Review secure local storage, encryption and backup behavior for selected implementation. Do not assume SQLite/OS backup provides required at-rest protection.
- Preserve records and audit history through offline retries and conflicts; use immutable IDs, idempotent operations and explicit sync statuses.
- Validate security rules with emulator tests for anonymous request, valid family member, unauthorized family, revoked member, and forged membership.
- Do not embed admin SDKs or secrets in mobile clients. Review any offline cache exposure on logout, device transfer and family exit.
- Pin/version dependencies; scrutinize dependency updates, GitHub Action permissions and untrusted PR inputs. CI token permissions must be read-only unless necessary.
- Security review must return file/line, attack scenario, severity, tests and residual risk; it cannot establish compliance by itself.
