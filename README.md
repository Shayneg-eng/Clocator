Clocator 🗺️

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/shayn/clocator/workflows/Tests/badge.svg)](https://github.com/shayn/clocator/actions)

Seamlessly sync and resume your local Claude Code sessions across multiple devices.

Clocator (Claude Locator) solves a major pain point in the Claude Code developer workflow: hardcoded absolute file paths.

Claude Code indexes your conversational history using rigid, local directories (e.g., /Users/dev/Projects/my-app). When you synchronize your development environment across different machines (like a work iMac and a personal MacBook), this mapping breaks because of differing directory structures.

Clocator acts as an intelligent abstraction layer. It decouples your Claude session history from volatile local folder paths and anchors them to a permanent digital fingerprint: your GitHub/Git Repository URL.

⚡ The Problem vs. The Clocator Solution

❌ WITHOUT CLOCATOR:
Computer A (/Users/dev/project) ──[Syncs claude.json]──> Computer B (/home/ubuntu/code/project)
                                                                 │
                                                    ⚠️ Claude fails to find path!
                                                    ⚠️ Starts blank session.

==========================================================================================

✅ WITH CLOCATOR:
Computer A (/Users/dev/project) ──> Clocator Map (Git Remote URL) ──┐
                                                                   │ (Synced via cloud)
Computer B (/home/ubuntu/code/project) <── Dynamic Path Patching ──┘


By reading your local .git/config and translating paths on the fly at the last millisecond, Clocator tricks Claude Code into thinking you never switched devices.

🛠️ Installation & Setup

Clocator is designed to be lightweight, fast, and dependency-free.

### Quick Start

```bash
pip install clocator
```

For detailed installation options and troubleshooting, see the [Installation Guide](INSTALL.md).

### What's Required

- **Python 3.8 or later**
- **Git** (already on your machine if you're a developer)
- A cloud sync service (Dropbox, iCloud, OneDrive, Syncthing, etc.)


🚀 How It Works

Clocator operates in a simple, two-step lifecycle integrated into your multi-device workflow:

1. On Computer A (Before you leave)

When you've finished coding on your first machine, run:

clocator push


Under the Hood: Clocator looks up the active workspace path in your native claude.json, reads your local git remote URL (e.g., git@github.com:username/repo.git), and maps that unique repository fingerprint to your current Claude Session ID in a lightweight, synced tracking file (clocator-map.json).

2. On Computer B (When you arrive)

After your cloud syncing service (Dropbox, iCloud, OneDrive, etc.) copies your profile over to your second machine, open your project directory and run:

clocator pull


Under the Hood: Clocator checks your current directory's git remote, looks it up in the synced clocator-map.json to find the correct Session ID, and dynamically updates the path keys inside Computer B's local claude.json on the fly.

You can now run claude and pick up exactly where you left off, with full history and context intact!

📖 Command Reference

clocator push

Saves the mapping of the current directory's Git Remote URL to the active Claude Code session ID. Run this right before your files sync.

clocator pull

Detects the Git Remote URL of the current directory, finds the corresponding Claude session, and patches your local claude.json configuration so Claude instantly recognizes your workspace on this machine.

clocator status

Shows the current Git Remote, its mapped Claude session ID, and whether your local path is correctly synchronized in the configuration.

## Documentation

- **[Installation Guide](INSTALL.md)** — Detailed setup instructions for all platforms
- **[Contributing Guide](CONTRIBUTING.md)** — How to contribute to Clocator
- **[Changelog](CHANGELOG.md)** — Version history and updates
- **[Security Policy](SECURITY.md)** — How to report vulnerabilities

## Troubleshooting

Having issues? Check out the [Installation Guide](INSTALL.md#troubleshooting) troubleshooting section.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 

1. Check out the [Contributing Guide](CONTRIBUTING.md)
2. Fork the repository
3. Create a feature branch
4. Submit a pull request

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## 💡 Questions?

- **Issues**: [GitHub Issues](https://github.com/shayn/clocator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/shayn/clocator/discussions)

---

Made with ❤️ for developers who code on multiple devices