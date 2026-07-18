# AtlasDM Architecture

---

# High-Level Architecture

                +------------------+
                |       UI         |
                +--------+---------+
                         |
                         |
                +--------v---------+
                | Application Core |
                +--------+---------+
                         |
     ---------------------------------------------
     |          |           |          |          |
     |          |           |          |          |
+----v----+ +---v----+ +----v----+ +---v----+ +---v----+
| Download| | Queue  | | Plugin  | |History | |Settings|
| Engine  | |Manager | |Manager  | |Manager | |Manager |
+----+----+ +---+----+ +----+----+ +---+----+ +---+----+
     |          |           |
     |          |           |
     +----------+-----------+
                |
         +------v------+
         | Provider API|
         +------+------+
                |
      --------------------------
      |        |        |       |
      |        |        |       |
   HTTP     GitHub   HuggingFace CivitAI

---

# Core Components

## UI

Responsible for presentation only.

Contains no download logic.

---

## Application Core

Coordinates every module.

Acts as service layer.

---

## Download Engine

Responsible for:

- start
- stop
- pause
- resume

Downloads should never directly interact with the UI.

---

## Queue Manager

Maintains task queue.

Supports:

- priority

- retry

- scheduling

---

## Plugin Manager

Loads providers dynamically.

No provider is hardcoded.

---

## Provider API

Every provider must implement the same interface.

```
analyze()

download()

supports()

authenticate()
```

---

## History Manager

Stores completed downloads.

---

## Settings Manager

Stores user preferences.

---

# Design Principles

- Modular

- SOLID

- Dependency Injection

- Event Driven

- Testable

- Platform Independent