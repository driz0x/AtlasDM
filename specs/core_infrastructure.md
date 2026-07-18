# Core Infrastructure Specification

Version: 1.0

Status: Draft

Sprint: 1

Milestone: 1.2

---

# Purpose

This document specifies the design of AtlasDM's Core Infrastructure.

The Core Infrastructure provides shared services used throughout the application.

It contains no download logic, UI logic, or provider-specific implementation.

Its responsibility is to provide reusable infrastructure for higher-level modules.

---

# Objectives

The Core Infrastructure must provide:

- Centralized application constants
- Unified path management
- Configuration management
- Logging services
- Resource management

Every component must be reusable and independent.

---

# Architecture

```
Application
      │
      ▼
 Core Infrastructure
      │
 ┌────┼────┐
 │    │    │
 ▼    ▼    ▼
Config Logger Resources
      │
      ▼
   PathManager
```

All modules depend on the Core Infrastructure.

The Core Infrastructure depends only on the Python standard library and approved third-party libraries.

---

# Directory Structure

```
src/
└── atlasdm/
    └── core/
        ├── __init__.py
        ├── config.py
        ├── constants.py
        ├── logger.py
        ├── paths.py
        └── resources.py
```

---

# Module Specifications

## constants.py

### Responsibility

Contains application-wide constants.

No business logic.

No file access.

No imports from other project modules.

---

### Public API

```python
APP_NAME

APP_VERSION

ORGANIZATION_NAME

ORGANIZATION_DOMAIN
```

Example:

```python
APP_NAME = "AtlasDM"
```

---

## paths.py

### Responsibility

Centralize every filesystem path.

No module may manually construct application directories.

---

### Public Class

```python
class PathManager
```

---

### Public Properties

```python
project_root

assets_dir

config_dir

logs_dir

cache_dir

plugins_dir

downloads_dir
```

Each property returns a `pathlib.Path`.

---

### Rules

Never use:

```python
Path("logs")
```

inside another module.

Always use:

```python
PathManager.logs_dir
```

---

## config.py

### Responsibility

Application configuration management.

---

### Public Class

```python
ConfigManager
```

---

### Public Methods

```python
load()

save()

get(key)

set(key, value)

reset()
```

---

### Initial Implementation

Configuration may remain in memory.

Persistent storage will be implemented in a future milestone.

---

## logger.py

### Responsibility

Provide centralized logging.

---

### Public Function

```python
get_logger(name)
```

Returns:

```python
logging.Logger
```

---

### Rules

Modules must never call:

```python
logging.getLogger(...)
```

directly.

Always use:

```python
get_logger(...)
```

---

## resources.py

### Responsibility

Locate application resources.

---

### Public Class

```python
ResourceManager
```

---

### Public Methods

```python
icon(name)

image(name)

stylesheet(name)
```

Each method returns a `Path`.

---

# Dependency Rules

```
constants

↓

paths

↓

resources

↓

config

↓

logger
```

Dependencies must never point upward.

Forbidden:

```
logger

↓

config

↓

logger
```

(circular dependency)

---

# Coding Rules

Every public class requires:

- Type hints
- Docstrings

Private attributes should begin with:

```python
_
```

Example:

```python
self._config
```

---

# Error Handling

Raise meaningful exceptions.

Do not silently ignore errors.

Forbidden:

```python
except:
    pass
```

---

# Thread Safety

Core Infrastructure should avoid mutable global state whenever practical.

Shared resources should be encapsulated behind classes or controlled access points.

---

# Testing Requirements

Each module should eventually include unit tests.

Example:

```
tests/

test_paths.py

test_config.py

test_logger.py

test_resources.py
```

---

# Future Extensions

Future milestones may extend the infrastructure with:

- JSON configuration backend
- TOML configuration backend
- Application cache
- Localization
- Resource packs
- Plugin discovery
- Theme loader

without breaking the public API.

---

# Out of Scope

The following are NOT part of this milestone:

- Download Engine
- Queue Manager
- Provider SDK
- Network communication
- Database
- Theme implementation
- Browser integration
- REST API

---

# Acceptance Criteria

The milestone is complete when:

- All modules exist.
- Public APIs match this specification.
- Code follows project rules.
- No circular dependencies exist.
- Unit tests can be added without redesigning the modules.
- No UI components depend on the Core Infrastructure implementation details.

---

# Definition of Done

- Architecture matches this specification.
- Public APIs are documented.
- Type hints are complete.
- Docstrings are present.
- Ruff reports no critical issues.
- Project launches successfully after integration.

---

End of Document.