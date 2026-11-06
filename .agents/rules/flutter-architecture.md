# Flutter architecture — project rule

Source: https://docs.flutter.dev/app-architecture/recommendations

- Separate presentation (widgets/screens and ViewModels) from data (repositories/services). Keep widgets declarative and free of database or medicine business logic.
- Use unidirectional data flow and explicit state transitions. Favor immutable models, dependency injection and repository abstractions for local/remote data.
- Keep domain-specific interval calculation, event reconciliation and time handling in independently testable pure code; never depend on `DateTime.now()` directly inside logic—inject a clock.
- Store `occurredAt` (actual event time) separately from `recordedAt`, preserve timezone context, handle day rollover and time correction.
- Keep app features isolated (`lib/features/<feature>/{data,domain,presentation}` is a suggested layout; exact structure is approved in P0). Prefer simple structure over premature layers.
- Make async work cancellation/error/reporting explicit. Never silently swallow database or sync errors.
- Reject UI code that substitutes mock state for persisted data after P1 implementation.
- Design for iOS and Android: accessibility, large tap targets, screen-reader labels, dark/night mode, offline screens, local PDF export.
- Per service/repository/ViewModel: unit tests; per screen: widget tests; per critical flow: integration tests. Verify crashes and data durability, not only happy paths.
- State management, dependency injection, navigation and persistence packages are architecture decisions to be recorded in a Jira/Confluence ADR after PoC, not chosen implicitly by AI.
