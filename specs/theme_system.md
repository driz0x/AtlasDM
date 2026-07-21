# Theme System Specification

**Milestone:** 1.3  
**Status:** Draft  
**Author:** AtlasDM Development Team

---

# 1. Background

AtlasDM membutuhkan sistem tema yang terpusat agar tampilan aplikasi dapat dikelola secara konsisten. Seluruh gaya antarmuka akan menggunakan Qt Style Sheets (QSS) sehingga perubahan tampilan tidak memerlukan perubahan pada kode UI.

Theme System juga menjadi fondasi untuk seluruh komponen antarmuka yang akan dibangun pada milestone berikutnya seperti Main Window, Sidebar, Toolbar, Status Bar, dan Download Queue.

---

# 2. Goals

Milestone ini bertujuan untuk:

- Menambahkan Theme Manager.
- Mendukung Dark Theme.
- Mendukung Light Theme.
- Memuat theme saat aplikasi dijalankan.
- Mengganti theme melalui API.
- Menggunakan file QSS sebagai stylesheet.

---

# 3. Non Goals

Milestone ini tidak mencakup:

- Theme Marketplace
- Download theme dari internet
- Plugin theme
- Theme editor
- Theme animation

---

# 4. Functional Requirements

### FR-1

Application shall load the configured theme during startup.

### FR-2

Application shall provide a default theme.

### FR-3

Application shall allow switching between available themes.

### FR-4

Theme shall be loaded from QSS files.

### FR-5

Theme shall be applied to the entire application.

---

# 5. Non-Functional Requirements

- Theme loading should be fast.
- Theme implementation should be platform independent.
- Adding a new theme should require minimal code changes.
- Theme files should be organized consistently.

---

# 6. Architecture

The Theme System consists of:

- ThemeManager
- Theme resources
- QSS files
- ConfigManager integration

ThemeManager is responsible for loading, applying, and switching themes.

---

# 7. Folder Structure

src/
└── atlasdm/
    ├── themes/
    │   └── manager.py
    │
    └── resources/
        └── themes/
            ├── dark/
            │   └── theme.qss
            │
            └── light/
                └── theme.qss

---

# 8. Public API

ThemeManager should provide:

- load()
- apply(name)
- current_theme()
- available_themes()

---

# 9. Future Extension

Future milestones may introduce:

- Custom themes
- Plugin themes
- Icon themes
- Dynamic theme reload

---

# 10. Acceptance Criteria

This milestone is complete when:

- ThemeManager is implemented.
- Dark Theme is available.
- Light Theme is available.
- Application starts using the configured theme.
- Theme can be switched through the ThemeManager API.