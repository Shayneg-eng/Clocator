# Security

Clocator only works with files inside `~/.claude`. It reads your git remote URL, writes `~/.claude/clocator-map.json`, and creates links inside `~/.claude/projects/`. It makes no network requests.

Keep in mind that `~/.claude` holds your full Claude Code conversation history, so whatever you use to sync it can see that history. Pick a sync service you'd trust with your code.

If you find a security problem, please report it privately through GitHub's [private vulnerability reporting](https://github.com/Shayneg-eng/Clocator/security/advisories/new) instead of opening a public issue.
