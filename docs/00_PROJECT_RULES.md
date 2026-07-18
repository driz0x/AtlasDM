# AtlasDM Engineering Rules

> This document defines the engineering principles, architecture rules, coding philosophy, and development workflow for AtlasDM.
>
> Every contributor (human or AI) MUST read and follow this document before modifying the project.

---

# 1. Project Philosophy

AtlasDM is **not just a download manager**.

AtlasDM is a **modular download platform** designed to support multiple download providers through a unified architecture.

The project prioritizes:

- Maintainability
- Extensibility
- Performance
- Readability
- Testability

over writing code as quickly as possible.

---

# 2. Architecture First

Architecture always comes before implementation.

Never implement a feature without understanding:

- Vision
- Requirements
- Architecture
- Coding Standards

When unsure, stop coding and ask for clarification.

---

# 3. Single Responsibility

Every module must have one responsibility.

Examples:

✓ Download Engine

Responsible for downloading.

NOT:

- UI
- Settings
- Database

---

✓ Queue Manager

Responsible only for queue management.

---

✓ Plugin Manager

Responsible only for provider management.

---

# 4. UI Rules

The UI must NEVER contain business logic.

The UI should only:

- display information
- collect user input
- send commands to services

Bad:

```
Button Click

↓

Download File
```

Good:

```
Button Click

↓

DownloadService.start()

↓

Download Engine
```

---

# 5. Service-Oriented Design

Core functionality should be implemented as services.

Examples:

DownloadService

QueueService

PluginService

HistoryService

SettingsService

NotificationService

Services should communicate through clearly defined interfaces.

---

# 6. Plugin First

Every external provider must be implemented as a plugin.

Never hardcode provider-specific logic into the download engine.

Supported examples:

- HTTP
- GitHub
- Hugging Face
- CivitAI
- Google Drive
- YouTube
- Torrent

Future providers should require minimal changes to the core.

---

# 7. Dependency Direction

Dependencies should always point toward the core.

Correct:

UI

↓

Services

↓

Engine

↓

Provider

Wrong:

Provider

↓

UI

---

# 8. SOLID Principles

AtlasDM follows SOLID principles.

- Single Responsibility

- Open/Closed

- Liskov Substitution

- Interface Segregation

- Dependency Inversion

Whenever possible.

---

# 9. Event Driven

Modules should communicate using events whenever appropriate.

Avoid direct module-to-module dependencies.

Example:

Download Finished

↓

History Updated

↓

Notification Sent

↓

UI Refreshed

without tightly coupling modules.

---

# 10. File Size

Avoid extremely large source files.

Recommended maximum:

300 lines

Hard limit:

500 lines

If a file grows beyond this limit, consider splitting it.

Exceptions are allowed only with strong justification.

---

# 11. Function Size

Functions should be small.

Recommended:

10–30 lines.

Avoid functions larger than 80 lines.

---

# 12. Naming

Use descriptive names.

Good:

DownloadEngine

PluginManager

HashVerifier

ProviderRegistry

Bad:

Engine

Manager

Data

Utils

Helper2

---

# 13. Type Hints

Every public function must use Python type hints.

Example:

```python
def download(url: str) -> DownloadTask:
    ...
```

---

# 14. Documentation

Every public class must include a docstring.

Every public method must include a docstring.

Complex algorithms should explain WHY rather than WHAT.

---

# 15. Logging

Never use print() in production code.

Use the logging module.

Log levels:

DEBUG

INFO

WARNING

ERROR

CRITICAL

---

# 16. Error Handling

Never silently ignore exceptions.

Bad:

```python
try:
    ...
except:
    pass
```

Good:

```python
try:
    ...
except Exception as exc:
    logger.exception(exc)
```

---

# 17. Security

Never hardcode:

- passwords
- tokens
- API keys

Sensitive information must be stored securely.

---

# 18. Testing

Every new feature should include tests whenever practical.

Bug fixes should include regression tests when applicable.

---

# 19. Performance

The UI must never freeze.

Long-running operations should run in background workers.

Blocking the main UI thread is prohibited.

---

# 20. Git Workflow

Main branch is always stable.

Development happens in:

develop

Feature branches:

feature/<feature-name>

Bug fixes:

fix/<bug-name>

---

# 21. Commit Convention

Examples:

feat:

fix:

docs:

refactor:

perf:

style:

test:

build:

ci:

Examples:

feat: implement download queue

fix: resolve provider timeout

docs: update architecture

---

# 22. AI Collaboration Rules

AI assistants must:

- Read project documentation first.
- Respect architecture decisions.
- Never rewrite unrelated modules.
- Never introduce unnecessary dependencies.
- Keep code modular.
- Explain important architectural changes.

If requirements are unclear,

STOP

and ask for clarification.

---

# 23. Code Review Checklist

Before every commit verify:

☐ Architecture respected

☐ No duplicated logic

☐ Type hints complete

☐ Logging implemented

☐ Exceptions handled

☐ Tests added (if applicable)

☐ Documentation updated

☐ Formatting passed

---

# 24. Project Goal

AtlasDM is intended to become a modern, extensible, cross-platform download platform that developers can extend without modifying the core application.

Every design decision should support this long-term goal.

---

End of Document.