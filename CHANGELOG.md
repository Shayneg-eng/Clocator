# Changelog

## 1.0.0 (2026-06-08)

First release.

- `clocator push`, `clocator pull` and `clocator status`
- Projects are matched by git remote URL, and the mapping is stored in `~/.claude/clocator-map.json`
- Links history folders with symlinks on macOS and Linux and with directory junctions on Windows (no admin rights needed)
- Never overwrites a real history folder
- Standard library only

## Ideas for later

- Support remotes other than `origin`
- A `--dry-run` flag
- Merging history when both machines already have their own folder for a project
