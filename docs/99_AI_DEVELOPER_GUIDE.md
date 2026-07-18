# AI Developer Guide

> This document defines how AI coding assistants must contribute to the AtlasDM project.
>
> It complements `00_PROJECT_RULES.md` and should be read before generating, modifying, or reviewing any code.

---

# Purpose

AtlasDM is developed with the assistance of AI coding tools.

To keep the project maintainable, every AI assistant must follow the same workflow and engineering standards.

The goal is not to generate code as quickly as possible, but to generate code that is:

- Correct
- Modular
- Maintainable
- Easy to review
- Consistent with the project architecture

---

# Mandatory Reading Order

Before making any changes, read the following documents in this exact order:

1. `README.md`
2. `docs/00_PROJECT_RULES.md`
3. `docs/01_VISION.md`
4. `docs/02_REQUIREMENTS.md`
5. `docs/03_USE_CASES.md`
6. `docs/04_ARCHITECTURE.md`
7. `docs/05_TECH_STACK.md` *(when available)*
8. `docs/06_PLUGIN_SYSTEM.md` *(when available)*
9. The current Sprint specification.

If any required document is missing, ask for clarification instead of making assumptions.

---

# Development Philosophy

AI must never optimize for speed over quality.

When there is a conflict between:

- writing less code
- writing better architecture

always choose better architecture.

---

# Scope Control

Only implement the requested milestone.

Do NOT:

- implement future features
- redesign unrelated modules
- perform large refactors
- rename files without approval
- change project structure without approval

Stay within the requested scope.

---

# No Assumptions

Never invent:

- APIs
- configuration files
- database schema
- provider behavior
- plugin interfaces

If the specification is unclear:

STOP

Explain what information is missing and ask for clarification.

---

# Preserve Architecture

Respect the existing architecture.

UI must never contain business logic.

Providers must never access UI components.

Business logic must never depend on presentation code.

---

# Modularity

Prefer adding new modules instead of increasing complexity inside existing modules.

Large classes should be divided into smaller services.

Avoid "God Objects".

---

# Dependency Rules

Dependencies must always point toward the application core.

Forbidden:

Provider → UI

Allowed:

UI → Services → Engine → Provider

---

# Plugin Rules

Provider-specific logic belongs only inside provider plugins.

Never place provider-specific conditions inside the download engine.

Bad:

```python
if "huggingface" in url:
```

Good:

```python
provider = registry.find_provider(url)
provider.download(...)
```

---

# Coding Style

Generate clean and readable code.

Avoid unnecessary cleverness.

Prefer explicit code over implicit behavior.

Readability is more important than saving a few lines.

---

# Type Hints

All public functions must include type hints.

Example:

```python
def pause(task_id: str) -> None:
    ...
```

---

# Docstrings

Public classes require docstrings.

Public methods require docstrings.

Document WHY the code exists rather than describing obvious syntax.

---

# Logging

Never use:

```python
print(...)
```

Use:

```python
logging
```

Appropriate log levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

---

# Exception Handling

Never ignore exceptions.

Forbidden:

```python
except:
    pass
```

Preferred:

```python
except Exception as exc:
    logger.exception(exc)
```

---

# Performance

Never block the UI thread.

Long-running operations must execute in background workers.

Avoid unnecessary polling.

Prefer asynchronous or event-driven solutions where appropriate.

---

# Testing

Whenever practical:

- add unit tests
- update existing tests
- ensure previous behavior is preserved

Bug fixes should include regression tests when possible.

---

# File Modification Rules

Modify the minimum number of files required.

Avoid unnecessary formatting changes.

Do not reorganize imports or rewrite unrelated code unless explicitly requested.

Keep pull requests easy to review.

---

# Output Format

When completing a task, summarize using the following format:

## Summary

- Objective
- Files Modified
- Important Decisions
- Potential Risks
- Next Recommended Step

---

# If You Cannot Complete the Task

Do not guess.

Instead report:

- what is missing
- why it is required
- possible implementation options

---

# Forbidden Actions

Do NOT:

- rewrite the entire project
- delete files without approval
- replace existing architecture
- introduce heavy dependencies without justification
- add unfinished TODO code as a substitute for implementation
- change coding conventions
- bypass project documentation

---

# Preferred Workflow

1. Read documentation.
2. Understand the requested milestone.
3. Identify affected modules.
4. Explain the implementation plan.
5. Implement the smallest complete solution.
6. Verify consistency.
7. Summarize the changes.

---

# Code Quality Checklist

Before finishing, verify:

- Architecture respected
- SOLID principles preserved
- No duplicated logic
- No unnecessary dependencies
- UI remains independent
- Business logic remains modular
- Type hints complete
- Logging implemented
- Exceptions handled
- Documentation updated
- Tests updated (if applicable)

---

# AI Collaboration

When multiple AI assistants contribute to AtlasDM:

- Preserve previous architectural decisions.
- Do not overwrite another AI's work without reason.
- Explain incompatible changes before applying them.
- Prefer extending existing modules over replacing them.

Consistency across contributions is more important than individual coding preferences.

---

# Engineering Principle

The primary responsibility of an AI contributor is not to generate code.

The primary responsibility is to preserve the long-term quality of the project.

Every implementation should make AtlasDM easier to extend, easier to maintain, and easier to understand.

---

End of Document.