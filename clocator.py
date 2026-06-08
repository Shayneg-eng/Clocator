#!/usr/bin/env python3
"""
Clocator (Claude Locator) - Multi-device sync utility for Claude Code sessions.
Translates absolute file paths mapped in Claude Code sessions using Git remote URLs.
"""

import argparse
import io
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows and all platforms
if sys.stdout.encoding and 'utf' not in sys.stdout.encoding.lower():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if sys.stderr.encoding and 'utf' not in sys.stderr.encoding.lower():
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# --- ANSI Terminal Color Formatting ---
def color_text(text: str, color_code: str) -> str:
    """Formats text with ANSI color codes if the stdout supports it."""
    if sys.stdout.isatty():
        return f"\033[{color_code}m{text}\033[0m"
    return text

def info(msg: str):
    print(f"{color_text('ℹ', '34')} {msg}")

def success(msg: str):
    print(f"{color_text('✔', '32')} {msg}")

def warning(msg: str):
    print(f"{color_text('⚠', '33')} {color_text(msg, '33')}")

def error(msg: str, exit_code: int = 1):
    print(f"{color_text('✖', '31;1')} {color_text(msg, '31')}", file=sys.stderr)
    if exit_code is not None:
        sys.exit(exit_code)

# --- Global Paths & Directory Discovery ---
HOME_DIR = Path.home()
CLAUDE_DIR = HOME_DIR / ".claude"
PROJECTS_DIR = CLAUDE_DIR / "projects"
MAP_FILE_NAME = "clocator-map.json"
MAP_FILE_PATH = CLAUDE_DIR / MAP_FILE_NAME

# --- Git Helper Utilities ---
def get_git_remote() -> str:
    """Retrieves the remote origin URL of the current git repository."""
    try:
        # Run git command to get the remote URL
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        url = result.stdout.strip()
        if not url:
            error("Git remote 'origin' is empty. Please set a remote URL to fingerprint this project.")
        return url
    except subprocess.CalledProcessError:
        error("Not a git repository (or git is not installed). Clocator requires a git repository to work.")
    except FileNotFoundError:
        error("Git executable not found. Please install git.")

# --- Claude Code Path Encoder ---
def encode_path(absolute_path: Path) -> str:
    """
    Replicates Claude Code's internal project directory mapping format.
    Every non-alphanumeric character in the absolute path is replaced with a single dash (-).
    E.g., /Users/dev/my-project -> -Users-dev-my-project
    """
    path_str = str(absolute_path.resolve())
    # Replace non-alphanumeric characters with a dash
    encoded = "".join([c if c.isalnum() else "-" for c in path_str])
    return encoded

# --- Map Persistence Layer ---
def load_map() -> dict:
    """Loads the Clocator translation map from the synced Claude directory."""
    if not MAP_FILE_PATH.exists():
        return {}
    try:
        with open(MAP_FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        warning(f"Failed to read {MAP_FILE_NAME} ({e}). Creating a fresh map.")
        return {}

def save_map(mapping: dict):
    """Saves the Clocator translation map safely to disk."""
    try:
        CLAUDE_DIR.mkdir(parents=True, exist_ok=True)
        with open(MAP_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(mapping, f, indent=2)
    except Exception as e:
        error(f"Failed to write to {MAP_FILE_PATH}: {e}")

# --- Platform-Agnostic Directory Linking ---
def create_directory_link(link_path: Path, target_path: Path):
    """
    Creates a symbolic link (or junction on Windows) from link_path pointing to target_path.
    If a real directory exists at link_path, it will warn the user instead of overwriting.
    """
    if link_path.exists() or link_path.is_symlink():
        # Check if it already points to the correct location
        if link_path.is_symlink() and os.readlink(str(link_path)) == str(target_path):
            return
        
        # If it's a junction or symlink but wrong, remove it to update
        if link_path.is_symlink():
            link_path.unlink()
        elif os.name == 'nt' and link_path.is_dir():
            # Check if it's a Windows junction using attributes
            try:
                # Try unlinking or rmdir to clear the directory link
                os.rmdir(link_path)
            except OSError:
                warning(f"A physical directory already exists at: {link_path}.\nSkipping automatic link creation.")
                return
        else:
            warning(f"A physical directory already exists at: {link_path}.\nSkipping link creation to avoid wiping your data.")
            return

    try:
        if os.name == 'nt':
            # Windows native fallback: try directory junction which doesn't require administrator privileges
            subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(link_path), str(target_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True
            )
        else:
            # macOS / Linux standard symbolic link
            os.symlink(target_path, link_path)
        success(f"Linked: {link_path.name} ➔ {target_path.name}")
    except Exception as e:
        error(f"Failed to create system link from {link_path} to {target_path}.\nError details: {e}")

# --- CLI Command Implementations ---
def handle_push(args):
    """Binds the active Git remote to the current absolute path fingerprint."""
    if not CLAUDE_DIR.exists():
        warning("Global Claude configuration directory (~/.claude) does not exist yet.")
        info("We highly recommend starting a quick Claude session (`claude`) here first to let it configure.")
    
    current_cwd = Path.cwd()
    git_remote = get_git_remote()
    encoded_folder = encode_path(current_cwd)
    
    info(f"Directory: {current_cwd}")
    info(f"Fingerprint (Git Remote): {git_remote}")
    info(f"Claude Key: {encoded_folder}")
    
    # Check if a session history folder actually exists for this workspace
    session_dir = PROJECTS_DIR / encoded_folder
    if not session_dir.exists():
        warning(f"No existing Claude session history folder found at {session_dir}")
        info("Don't worry! Running `claude` once in this directory will automatically populate this.")
    
    # Update and save the mapping
    mapping = load_map()
    mapping[git_remote] = encoded_folder
    save_map(mapping)
    
    success("Push Successful! Mapped this project to Clocator registry.")
    info("Ready to sync. Run `clocator pull` on your destination machine once synced.")

def handle_pull(args):
    """Finds the original mapped folder from the registry and links the local folder to it."""
    current_cwd = Path.cwd()
    git_remote = get_git_remote()
    local_encoded_folder = encode_path(current_cwd)
    
    mapping = load_map()
    
    if git_remote not in mapping:
        error(
            f"No mapped session found for remote URL:\n  {git_remote}\n\n"
            f"Please run `clocator push` on the host machine containing your conversational history first."
        )
    
    synced_encoded_folder = mapping[git_remote]
    
    info(f"Local Directory: {current_cwd}")
    info(f"Local Claude Key: {local_encoded_folder}")
    info(f"Synced Claude Key: {synced_encoded_folder}")
    
    # Create projects directory if it does not exist
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    
    synced_folder_path = PROJECTS_DIR / synced_encoded_folder
    local_folder_path = PROJECTS_DIR / local_encoded_folder
    
    if not synced_folder_path.exists():
        error(
            f"Expected synced session folder not found at: {synced_folder_path}\n"
            f"Make sure your file synchronization client (Syncthing, Dropbox, iCloud) has finished syncing your ~/.claude directory."
        )
        
    if local_encoded_folder == synced_encoded_folder:
        success("Paths match perfectly! No patching or linking required on this machine.")
        return

    # Perform path linking intervention
    create_directory_link(local_folder_path, synced_folder_path)
    success("Pull Successful! Your Claude session history is now linked and synchronized.")
    info("Go ahead and run `claude` to resume your multi-device conversational stream!")

def handle_status(args):
    """Displays the registration status of the current workspace."""
    current_cwd = Path.cwd()
    git_remote = get_git_remote()
    local_encoded = encode_path(current_cwd)
    mapping = load_map()
    
    print(f"\n--- {color_text('Clocator Status', '1;35')} ---")
    print(f"Current Path:     {current_cwd}")
    print(f"Git Remote URL:   {git_remote}")
    print(f"Local Claude Key: {local_encoded}")
    
    if git_remote in mapping:
        synced_encoded = mapping[git_remote]
        print(f"Mapped Key:       {color_text(synced_encoded, '32')}")
        
        local_path = PROJECTS_DIR / local_encoded
        if local_encoded == synced_encoded:
            print(f"Sync Status:      {color_text('Matched (No linking needed)', '32')}")
        elif local_path.is_symlink():
            target = os.readlink(str(local_path))
            print(f"Sync Status:      {color_text('Linked successfully', '32')} ➔ {Path(target).name}")
        elif local_path.exists():
            print(f"Sync Status:      {color_text('Both folders exist independently', '33')} (Conflict possible)")
        else:
            print(f"Sync Status:      {color_text('Not Linked (Run clocator pull to sync)', '33')}")
    else:
        print(f"Sync Status:      {color_text('Unregistered (Run clocator push to map)', '31')}")
    print()

# --- Command Line Interface Definition ---
def main():
    parser = argparse.ArgumentParser(
        description="Seamlessly sync and resume Claude Code sessions across devices using Git remotes as fingerprints.",
        epilog="Designed with love for developers syncing via Dropbox, iCloud, Syncthing, or Resilio Sync."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available actions")

    # Command: Push
    subparsers.add_parser(
        "push", 
        help="Map current directory's Git remote to the active Claude session"
    )
    
    # Command: Pull
    subparsers.add_parser(
        "pull", 
        help="Apply dynamic path patches so Claude session history is active on this machine"
    )
    
    # Command: Status
    subparsers.add_parser(
        "status", 
        help="Show Clocator registration details for the current repository"
    )

    args = parser.parse_args()

    if args.command == "push":
        handle_push(args)
    elif args.command == "pull":
        handle_pull(args)
    elif args.command == "status":
        handle_status(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()