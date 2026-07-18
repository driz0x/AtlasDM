# Milestone 1.2 — Core Infrastructure

Version: 1.0

Sprint: 1

Status: Planned

---

# Objective

Implement the Core Infrastructure for AtlasDM based on the specification defined in:

specs/core_infrastructure.md

This milestone establishes the shared infrastructure that will be used by all future application modules.

No UI features should be implemented.

---

# References

Before implementing this milestone, read the following documents in order:

1. README.md
2. docs/00_PROJECT_RULES.md
3. docs/01_VISION.md
4. docs/02_REQUIREMENTS.md
5. docs/03_USE_CASES.md
6. docs/04_ARCHITECTURE.md
7. docs/99_AI_DEVELOPER_GUIDE.md
8. developer/SPRINT_01.md
9. specs/core_infrastructure.md

---

# Scope

Implement only the following modules:

src/atlasdm/core/

- constants.py
- paths.py
- config.py
- logger.py
- resources.py

---

# Deliverables

The milestone must provide:

✓ Application constants

✓ Path management

✓ Configuration manager

✓ Logger factory

✓ Resource manager

No additional functionality.

---

# Public API

The implementation must follow the public API defined in:

specs/core_infrastructure.md

Do not rename public classes or methods.

Do not introduce undocumented APIs.

---

# Responsibilities

## constants.py

Contains immutable application constants.

No functions.

No classes.

No business logic.

---

## paths.py

Implement:

PathManager

Responsibilities:

- resolve application directories
- expose Path objects
- create missing directories when appropriate

No module outside PathManager should manually construct application paths.

---

## config.py

Implement:

ConfigManager

Responsibilities:

- load configuration
- save configuration
- get values
- set values
- reset defaults

Persistence may remain minimal for this milestone.

---

## logger.py

Implement:

get_logger(name)

Responsibilities:

- return configured Logger instances
- centralize logging configuration
- avoid duplicate handlers

---

## resources.py

Implement:

ResourceManager

Responsibilities:

- resolve icons
- resolve images
- resolve stylesheets

Only path resolution is required.

Loading resources is out of scope.

---

# Out of Scope

Do NOT implement:

- Download Engine
- Queue Manager
- Theme Loader
- Sidebar
- Pages
- Network Communication
- Provider System
- Database
- Plugin Loader

---

# Allowed Files

The implementation may modify:

src/atlasdm/core/

tests/

pyproject.toml (only if absolutely necessary)

No other modules should be modified.

---

# Acceptance Criteria

The milestone is complete when:

- Every module exists.
- Public API matches the specification.
- Imports work correctly.
- No circular dependencies.
- Type hints are complete.
- Public classes contain docstrings.
- Ruff reports no critical issues.

---

# Definition of Done

The milestone is finished only if:

- Architecture follows project rules.
- Code is modular.
- No duplicated logic.
- No unnecessary dependencies.
- Project still launches successfully.
- Core infrastructure can be reused by future modules.

---

# Commit Convention

Recommended commit message:

feat(core): implement core infrastructure

---

# Deliverable Report

After implementation, provide:

## Summary

Brief description of the implementation.

---

## Files Created

List every new file.

---

## Files Modified

List every modified file.

---

## Design Decisions

Explain any architectural decisions made during implementation.

---

## Risks

Describe any known limitations.

---

## Next Recommended Milestone

Recommend the next logical milestone.

---

End of Document