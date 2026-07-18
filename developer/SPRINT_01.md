# Sprint 01 — Application Skeleton

Version: 1.0

Status: Planned

---

# Sprint Goal

Build the initial AtlasDM desktop application skeleton.

This sprint focuses on establishing the project foundation without implementing any download functionality.

At the end of this sprint, AtlasDM should launch successfully and provide the basic application structure required for future development.

---

# Objective

Create a clean, modular desktop application using PySide6 with a scalable architecture.

The application should provide:

- Main Window
- Navigation Sidebar
- Empty Pages
- Theme System
- Configuration Loader
- Logging System

No download engine or provider implementation is included in this sprint.

---

# Scope

Included:

- Project initialization
- Application entry point
- Main window
- Sidebar navigation
- Page management
- Theme loading
- Logging
- Configuration system
- Folder structure

Not Included:

- Download Engine
- Queue Manager
- Provider System
- aria2 Integration
- Database
- Plugin Loader
- Browser Extension

---

# Deliverables

The following components must exist after Sprint 01.

## Application

- Application launches
- Window opens successfully
- Proper application title
- Application icon (placeholder allowed)

---

## Navigation

Sidebar contains:

- Dashboard
- Downloads
- History
- Plugins
- Settings

Navigation switches pages correctly.

---

## Pages

Create placeholder pages for:

DashboardPage

DownloadsPage

HistoryPage

PluginsPage

SettingsPage

Each page should display only its title.

---

## Theme

Implement a basic theme system.

Requirements:

- External stylesheet
- Easily replaceable
- Applied during startup

Dark theme is preferred.

---

## Configuration

Create configuration manager.

Responsibilities:

- Load configuration
- Save configuration
- Default settings

Example settings:

- Download directory
- Theme
- Concurrent downloads

---

## Logging

Create centralized logging.

Requirements:

- Console logging
- File logging

Log file:

logs/application.log

---

# Suggested Folder Structure

```
src/

app/
    application.py

core/
    config.py
    logger.py

ui/
    main_window.py

pages/
    dashboard.py
    downloads.py
    history.py
    plugins.py
    settings.py

widgets/

resources/

styles/

services/
```

Folder names may evolve if justified by architecture.

---

# Acceptance Criteria

Sprint is considered complete when:

- Application starts without errors.
- Sidebar navigation works.
- Every page can be opened.
- Logging writes to file.
- Configuration file is created automatically.
- No download functionality exists.
- Project follows architecture rules.

---

# Definition of Done

The sprint is complete only if:

- Code follows `00_PROJECT_RULES.md`
- Architecture remains modular
- Type hints are used
- Public classes contain docstrings
- Ruff reports no critical issues
- No placeholder TODOs remain without explanation

---

# Files Expected

Likely new files include:

- app/application.py
- ui/main_window.py
- core/config.py
- core/logger.py

and page modules.

Additional helper modules may be created if justified.

---

# Out of Scope

The following must NOT be implemented:

- Download tasks
- Network requests
- Provider plugins
- Queue logic
- Database
- Authentication
- API

---

# Risks

Avoid putting business logic inside UI components.

Avoid hardcoding navigation.

Avoid creating monolithic classes.

---

# Notes for AI Developers

Before writing code:

1. Read project documentation.
2. Follow the architecture.
3. Implement only the requested scope.
4. Keep modules small.
5. Explain any architectural deviation.

---

# Completion Checklist

- [ ] Application launches
- [ ] Main window created
- [ ] Sidebar navigation works
- [ ] Placeholder pages exist
- [ ] Theme system implemented
- [ ] Configuration system implemented
- [ ] Logging implemented
- [ ] Documentation updated
- [ ] Code reviewed

---

End of Sprint 01