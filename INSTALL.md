# Installation Guide

Choose the installation method that works best for your workflow.

## Option 1: Install with pip (Recommended)

The easiest way to install Clocator globally:

```bash
pip install clocator
```

Then use the `clocator` command from anywhere in your terminal.

## Option 2: Install from source

If you want the latest development version:

```bash
# Clone the repository
git clone https://github.com/shayn/clocator.git
cd clocator

# Install in development mode
pip install -e .
```

## Option 3: Install with pipx (Isolated environment)

For isolated global command-line apps without affecting your Python environment:

```bash
pipx install clocator
```

This is recommended if you use many CLI tools and want to keep them isolated.

## Option 4: Use as a standalone script

If you prefer not to install anything:

```bash
# Download clocator.py
wget https://raw.githubusercontent.com/shayn/clocator/main/clocator.py

# Run it with Python
python clocator.py push
python clocator.py pull
python clocator.py status
```

## Requirements

- **Python 3.8 or later**
- **Git** (already installed on most development machines)
- A cloud sync service (Dropbox, iCloud, OneDrive, Syncthing, Resilio Sync, etc.)

## Verifying Installation

After installing, verify it works:

```bash
clocator --help
```

You should see the help message with available commands.

## Uninstallation

### If you installed with pip:
```bash
pip uninstall clocator
```

### If you installed with pipx:
```bash
pipx uninstall clocator
```

### If you used the standalone script:
Simply delete the `clocator.py` file.

## Troubleshooting

### "clocator: command not found"

Make sure the installation completed successfully:

```bash
pip install --force-reinstall clocator
```

### "Not a git repository" error

Clocator requires your working directory to be inside a Git repository:

```bash
git init
git remote add origin https://github.com/your-username/your-repo.git
```

### Windows permission issues

If you get permission errors on Windows, ensure Python is installed for your user:

```bash
python --version
pip --version
```

Or use `pipx` which handles permissions more gracefully:

```bash
pipx install clocator
```

## Getting Started

Once installed, see the [README](README.md) for usage instructions:

```bash
clocator push   # Before syncing your files
clocator pull   # After syncing on a new machine
clocator status # Check synchronization status
```
