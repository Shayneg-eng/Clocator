# Contributing

Bug reports and pull requests are welcome.

If something breaks, open an issue with your OS, Python version, which sync tool you use, and the output of `clocator status` from both machines if you can. Path handling is where almost every bug in this kind of tool comes from, so the exact paths help a lot.

For code changes:

```bash
git clone https://github.com/Shayneg-eng/Clocator.git
cd Clocator
pip install -e .
```

A couple of ground rules:

- Keep it standard-library only. Being a single file with no dependencies is a big part of why it's easy to trust with your `~/.claude` folder.
- Never delete or overwrite a real directory in `~/.claude/projects/`. Clocator should only ever create or replace links.
- If you touch the linking code, test on Windows (junctions) and on macOS or Linux (symlinks), since they behave differently.
