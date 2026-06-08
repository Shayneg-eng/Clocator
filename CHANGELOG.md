# Changelog

All notable changes to Clocator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-06-08

### Added

- Initial release of Clocator
- `clocator push` command to map Git repositories to Claude Code sessions
- `clocator pull` command to apply path patches across different machines
- `clocator status` command to display synchronization status
- Cross-platform support (Windows, macOS, Linux)
- Automatic Windows junction creation for path linking
- UTF-8 encoding support for emoji output on all platforms
- Git remote URL fingerprinting for stable cross-device mapping
- Colored terminal output with helpful status indicators

### Features

- Seamless multi-device workflow for Claude Code sessions
- No external dependencies (pure Python stdlib)
- Smart path encoding that matches Claude Code's internal format
- Safe symlink/junction creation with conflict detection
- Persistent mapping storage in `~/.claude/clocator-map.json`
- Works with any cloud sync service (Dropbox, iCloud, OneDrive, Syncthing, etc.)

---

## [Unreleased]

### Planned

- Support for multiple Git remotes
- Dry-run mode for previewing changes
- Manual path mapping editing
- Configuration file support
- Better error recovery and validation
- Shell completion scripts (bash, zsh, PowerShell)
