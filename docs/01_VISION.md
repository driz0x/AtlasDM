# AtlasDM Vision

## Mission

AtlasDM aims to become a universal download platform capable of downloading almost anything from the Internet through a single application.

The project focuses on flexibility, extensibility, and performance rather than simply replacing existing download managers.

---

# Vision

Instead of creating a downloader for a specific service, AtlasDM provides a modular platform where each provider is implemented independently.

This allows support for:

- HTTP / HTTPS
- GitHub Releases
- Hugging Face
- CivitAI
- Google Drive
- Dropbox
- FTP
- SFTP
- YouTube
- Torrent
- Future providers

without changing the download engine.

---

# Core Principles

## Modular

Everything should be modular.

No provider should depend on another provider.

---

## Extensible

Adding a new provider should require creating a new plugin only.

No core engine modifications.

---

## Maintainable

Readable code is preferred over clever code.

Architecture is more important than shortcuts.

---

## Cross Platform

AtlasDM should support:

- Windows
- Linux
- macOS

---

## Performance

Heavy operations should never block the UI.

Background workers should handle downloads.

---

## Open Source

AtlasDM is designed as an open-source project.

Documentation is considered as important as source code.

---

# Long-term Goal

Create a download platform that developers and power users can extend without modifying the core application.