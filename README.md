# Clocator

[![PyPI](https://img.shields.io/pypi/v/clocator.svg)](https://pypi.org/project/clocator/)
[![Tests](https://github.com/Shayneg-eng/Clocator/workflows/Tests/badge.svg)](https://github.com/Shayneg-eng/Clocator/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Pick up your Claude Code conversations on a different computer.

Claude Code stores each project's conversation history under `~/.claude/projects/`, in a folder named after the project's full path. `/Users/me/code/my-app` becomes `-Users-me-code-my-app`. So even if you sync `~/.claude` between two machines, the history doesn't follow you, because on the other machine the project lives at `/home/me/projects/my-app` and Claude looks for a folder that doesn't exist.

Clocator fixes that by keying projects on something that's the same everywhere: the git remote URL.

## How it works

**On the machine you're leaving**, run `clocator push` inside the project. It reads `remote.origin.url` and records which history folder belongs to that remote in `~/.claude/clocator-map.json`.

**On the machine you're switching to**, once your sync tool has copied `~/.claude` over, run `clocator pull` inside the same project. It looks up the remote in the map, finds the original history folder, and creates a link to it under the name Claude expects for this machine's path. That's a symlink on macOS and Linux, and a directory junction on Windows, so you don't need admin rights.

Start `claude` and your history is there. Nothing in Claude's own files gets edited, so to undo it you just delete the link.

```
$ cd ~/projects/my-app
$ clocator pull
ℹ Local Directory: /home/me/projects/my-app
ℹ Local Claude Key: -home-me-projects-my-app
ℹ Synced Claude Key: -Users-me-code-my-app
✔ Linked: -home-me-projects-my-app ➔ -Users-me-code-my-app
✔ Pull Successful! Your Claude session history is now linked and synchronized.
```

If a real folder already exists where the link would go, Clocator leaves it alone and warns you instead of overwriting it.

## Install

```bash
pip install clocator
```

Or `pipx install clocator`, or just download `clocator.py` and run it with Python. It has no dependencies beyond the standard library. You need Python 3.8+, git, and something that syncs `~/.claude` between your machines (Dropbox, iCloud, OneDrive, Syncthing, whatever you already use).

## Commands

| Command | What it does |
|---|---|
| `clocator push` | Record this project's history folder under its git remote |
| `clocator pull` | Link this machine's path to the synced history folder |
| `clocator status` | Show the remote, both folder names, and whether they're linked |

You only need to `push` once per project. After that, `pull` on any new machine (or after you move the project folder) is enough.

## Limitations

- The project needs a remote named `origin`. Two clones of the same repo share one history.
- It only links whole history folders. It doesn't merge conversations from two machines that both have their own history for the same project.

More install options and troubleshooting are in [INSTALL.md](INSTALL.md). Bug reports and pull requests are welcome, see [CONTRIBUTING.md](CONTRIBUTING.md). MIT licensed.
