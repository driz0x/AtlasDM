# AtlasDM Development Workflow

Version: 1.0

Status: Active

---

# Purpose

This document defines the official development workflow for AtlasDM.

Every feature, bug fix, refactor, and enhancement must follow this workflow.

The purpose is to ensure consistency, maintainability, and high engineering quality throughout the project.

---

# Project Philosophy

AtlasDM follows a documentation-first development approach.

Every implementation begins with documentation before any code is written.

The implementation should follow the documentation—not the other way around.

---

# Development Lifecycle

Every feature follows the same lifecycle.

```
Idea
    │
    ▼
Documentation
    │
    ▼
Specification
    │
    ▼
Architecture Review
    │
    ▼
Implementation
    │
    ▼
Code Review
    │
    ▼
Testing
    │
    ▼
Merge
    │
    ▼
Release
```

---

# Repository Structure

```
docs/
```

Project knowledge.

Examples:

- Vision
- Requirements
- Architecture
- Project Rules

---

```
developer/
```

Development planning.

Examples:

- Sprint plans
- Milestone plans
- Workflow

---

```
specs/
```

Technical feature specifications.

Every major feature must have its own specification.

---

```
review/
```

Architecture and implementation reviews.

Every completed milestone should produce a review document.

---

```
src/
```

Application source code.

---

```
tests/
```

Unit tests and integration tests.

---

# Feature Development Workflow

Every new feature must follow these steps.

## Step 1

Identify the feature.

---

## Step 2

Update documentation if required.

Affected documents may include:

- Vision
- Requirements
- Architecture

---

## Step 3

Create a Feature Specification.

Location:

```
specs/
```

Example:

```
download_engine.md
```

---

## Step 4

Create a Milestone document.

Location:

```
developer/
```

Example:

```
MILESTONE_02_01.md
```

---

## Step 5

Architecture Review.

The specification must be reviewed before implementation begins.

---

## Step 6

Implementation.

Only implement the documented scope.

Avoid adding undocumented features.

---

## Step 7

Run quality checks.

Minimum requirements:

- Project launches successfully
- No broken imports
- Ruff passes
- Existing functionality still works

---

## Step 8

Architecture Review.

Review:

- Design
- Structure
- Maintainability
- Readability
- Public APIs
- Technical debt

Create:

```
review/
REVIEW_xx_xx.md
```

---

## Step 9

Commit.

Use Conventional Commits.

Examples:

```
feat(core): implement path manager

fix(logger): prevent duplicate handlers

refactor(config): simplify configuration loading

docs(specs): update download engine specification
```

---

## Step 10

Merge into develop.

Never merge directly into main.

---

# Branch Strategy

```
main
```

Production-ready code.

---

```
develop
```

Active development.

---

```
feature/*
```

Optional feature branches.

Examples:

```
feature/theme-system

feature/download-engine

feature/plugin-loader
```

---

# Release Strategy

Milestones are developed on:

```
develop
```

Stable milestones may be tagged.

Example:

```
v0.1.0-m1
```

Official releases are merged into:

```
main
```

---

# Coding Standards

Every module should:

- Follow SOLID principles
- Be modular
- Use type hints
- Include docstrings for public classes and functions
- Avoid duplicated logic

---

# Dependency Rules

Lower-level modules must never depend on higher-level modules.

Example:

```
UI

↓

Services

↓

Core
```

Never:

```
Core

↓

UI
```

---

# Documentation Rules

Documentation is considered part of the source code.

Whenever implementation changes affect documentation, the documentation must be updated in the same milestone.

---

# Review Rules

Every milestone should answer the following questions:

- Does the implementation follow the specification?
- Is the architecture still clean?
- Are there unnecessary dependencies?
- Can the module be reused?
- Is the public API intuitive?
- Is technical debt introduced?

---

# Commit Rules

Commit frequently.

Each commit should represent a single logical change.

Avoid combining unrelated changes into one commit.

---

# Pull Request Checklist

Before merging, verify:

- Documentation updated
- Specification updated (if required)
- Code reviewed
- Ruff passes
- Application launches successfully
- No circular dependencies
- No dead code

---

# Definition of Done

A milestone is complete when:

- Implementation matches the specification.
- Architecture review is completed.
- Review document is created.
- Code quality checks pass.
- Changes are committed.
- The project remains stable.

---

# AI Development Policy

AI is used as an engineering assistant.

Responsibilities:

Software Architect

- Design architecture
- Review implementations
- Maintain engineering standards

Developer AI

- Implement approved specifications
- Follow project rules
- Do not introduce undocumented behavior

Project Maintainer

- Review final decisions
- Manage Git
- Integrate changes
- Approve releases

---

# Source of Truth

When conflicts occur, the following priority applies:

1. Feature Specification (`specs/`)
2. Milestone Document (`developer/`)
3. Project Rules (`docs/`)
4. Source Code (`src/`)

The source code should always reflect the approved documentation.

---

End of Document.