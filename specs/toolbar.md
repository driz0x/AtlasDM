# Toolbar Specification

## Background

The Toolbar provides quick access to the primary actions of AtlasDM. It serves as the main command area where users initiate and control download-related operations.

This milestone focuses only on establishing the visual structure of the Toolbar. No application logic or download functionality shall be implemented.

---

## Goals

- Create a reusable Toolbar component.
- Integrate the Toolbar into the Main Window.
- Display the primary application actions.
- Preserve compatibility with the existing Theme System.

---

## Non Goals

The following features are explicitly out of scope for this milestone:

- Download creation
- Clipboard integration
- URL validation
- Download control logic
- Queue management
- Signal-slot connections
- Event handling
- Icons
- Keyboard shortcuts

---

## Functional Requirements

### FR-1

The application shall display a Toolbar at the top of the Main Window.

### FR-2

The Toolbar shall contain the following actions:

- New Download
- Paste URL
- Start
- Pause
- Stop

### FR-3

The Toolbar shall remain visible while the application is running.

### FR-4

Toolbar actions shall be displayed in the order defined above.

### FR-5

The existing Theme System shall continue to apply correctly.

---

## Design Constraints

- Use Qt's native `QToolBar`.
- Use `QAction` for toolbar actions.
- Keep the implementation reusable.
- Keep MainWindow responsible only for composing the UI.
- Do not implement business logic.
- Do not implement signal-slot connections.
- Do not implement icons.

---

## Acceptance Criteria

- Toolbar is visible.
- Toolbar is positioned at the top of the window.
- All required actions are displayed.
- Existing Sidebar remains functional.
- Existing Main Layout remains unchanged.
- Theme is applied correctly.