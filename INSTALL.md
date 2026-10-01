# Installing Clocator

## pip

```bash
pip install clocator
```

## pipx

If you'd rather keep command-line tools out of your main Python environment:

```bash
pipx install clocator
```

## From source

```bash
git clone https://github.com/Shayneg-eng/Clocator.git
cd Clocator
pip install -e .
```

## No install

`clocator.py` is a single file with no dependencies, so you can just download it and run it:

```bash
curl -O https://raw.githubusercontent.com/Shayneg-eng/Clocator/main/clocator.py
python clocator.py status
```

## Requirements

- Python 3.8 or newer
- git
- A sync tool that keeps `~/.claude` the same on every machine (Dropbox, iCloud, OneDrive, Syncthing, and so on)

Check that it worked with `clocator --help`.

## Troubleshooting

**`clocator: command not found`**: pip's scripts folder isn't on your PATH. Run `python -m pip show clocator` to find where it installed, or use pipx, which handles PATH for you.

**"Not a git repository"**: run Clocator from inside the project folder. The project also needs a remote named `origin` (`git remote -v` shows what's set).

**"No mapped session found"**: you haven't run `clocator push` for this repo on the other machine yet, or `~/.claude/clocator-map.json` hasn't finished syncing.

**"A physical directory already exists"**: Claude has already created its own history folder for this path on this machine. Clocator won't overwrite it. If you don't need what's in there, delete or rename that folder in `~/.claude/projects/` and run `clocator pull` again.

## Uninstall

```bash
pip uninstall clocator
```

Any links Clocator made in `~/.claude/projects/` stay where they are. Delete them if you don't want them.
