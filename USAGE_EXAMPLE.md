# Real-World Usage Example: Day-to-Day Workflow

This guide shows exactly how developers use Clocator in their daily work across multiple devices.

## Scenario: A Developer with a Work MacBook and Personal Linux Laptop

**Setting**: Alex is a developer who works on an AI project on both their MacBook at the office and a Linux laptop at home. They sync everything via Dropbox and use Claude Code for AI assistance on both machines.

---

## Step 1: Install on Computer A (MacBook - Office)

### 1a. Download and Install

Alex opens the terminal and installs Clocator globally:

```bash
pip install clocator
```

Or if they prefer pipx (isolated):

```bash
pipx install clocator
```

### 1b. Verify Installation

```bash
$ clocator --help

usage: clocator [-h] {push, pull, status}

Seamlessly sync and resume Claude Code sessions across devices...
```

✅ Installed! They're ready to use it.

---

## Step 2: Start Working on Computer A (MacBook)

### 2a. Navigate to Their Project

```bash
cd ~/Projects/my-ai-startup
```

The project structure looks like:

```
~/Projects/my-ai-startup/
├── .git
├── src/
├── README.md
└── ... (their code)
```

### 2b. Start a Claude Code Session

Alex opens Claude Code and starts working on their project:

```bash
claude
```

They ask Claude AI questions about their code, get help with debugging, discuss architecture, etc. Claude Code creates a conversation history and stores it in:

```
~/.claude/projects/Users-alex-Projects-my-ai-startup/
```

(This folder name is Claude's internal encoding of the path)

### 2c. Before Leaving the Office: Run `clocator push`

Before syncing files to Dropbox, Alex runs:

```bash
$ clocator push

ℹ Directory: /Users/alex/Projects/my-ai-startup
ℹ Fingerprint (Git Remote): https://github.com/alex/my-ai-startup.git
ℹ Claude Key: Users-alex-Projects-my-ai-startup
✔ Push Successful! Mapped this project to Clocator registry.
ℹ Ready to sync. Run `clocator pull` on your destination machine once synced.
```

**What just happened:**
- Clocator read the git remote URL from `.git/config`
- It created a mapping file at `~/.claude/clocator-map.json`:
  ```json
  {
    "https://github.com/alex/my-ai-startup.git": "Users-alex-Projects-my-ai-startup"
  }
  ```
- This file travels with their `.claude` folder in Dropbox

### 2d. Verify the Mapping

Alex can check the status:

```bash
$ clocator status

--- Clocator Status ---
Current Path:     /Users/alex/Projects/my-ai-startup
Git Remote URL:   https://github.com/alex/my-ai-startup.git
Local Claude Key: Users-alex-Projects-my-ai-startup
Mapped Key:       Users-alex-Projects-my-ai-startup
Sync Status:      Matched (No linking needed)
```

Perfect! Everything is registered.

---

## Step 3: Files Sync Overnight

Alex's Dropbox (or iCloud, OneDrive, Syncthing) automatically syncs:

- `~/.claude/` folder (including session histories)
- `~/Projects/my-ai-startup/` folder (their code)

Both appear on their Linux laptop at home, but in a different location because Linux has a different directory structure:

```
# On MacBook (what synced)
~/.claude/projects/Users-alex-Projects-my-ai-startup/

# On Linux (same synced folder, different path)
~/.claude/projects/Users-alex-Projects-my-ai-startup/  ← Same folder
```

BUT the project code is at a different path:

```
# On MacBook
~/Projects/my-ai-startup/

# On Linux (different path!)
~/code/projects/my-ai-startup/
```

❌ **Without Clocator**, Claude Code would look for the session at the old path and fail.

✅ **With Clocator**, it automatically fixes this.

---

## Step 4: Arrive Home and Use Computer B (Linux)

### 4a. Install Clocator on Linux (if not already installed)

```bash
pip install clocator
```

### 4b. Navigate to the Project (Different Path!)

Alex opens their Linux laptop and goes to their project:

```bash
cd ~/code/projects/my-ai-startup
```

The project is at a completely different path than the MacBook!

### 4c. Run `clocator pull`

This is the magic moment:

```bash
$ clocator pull

ℹ Local Directory: /home/alex/code/projects/my-ai-startup
ℹ Local Claude Key: home-alex-code-projects-my-ai-startup
ℹ Synced Claude Key: Users-alex-Projects-my-ai-startup
✔ Linked: home-alex-code-projects-my-ai-startup ➔ Users-alex-Projects-my-ai-startup
✔ Pull Successful! Your Claude session history is now linked and synchronized.
ℹ Go ahead and run `claude` to resume your multi-device conversational stream!
```

**What just happened:**
1. Clocator read the git remote URL from the Linux `.git/config`
2. It looked up `https://github.com/alex/my-ai-startup.git` in the synced map
3. It found: "this maps to `Users-alex-Projects-my-ai-startup`"
4. It created a symbolic link (junction on Windows):
   ```
   ~/.claude/projects/home-alex-code-projects-my-ai-startup/
           ↓ (symlink points to)
   ~/.claude/projects/Users-alex-Projects-my-ai-startup/
   ```

Now both paths point to the **same** session history!

### 4d. Open Claude Code and Resume Work

```bash
$ claude
```

Claude Code opens and... **all their conversation history is there!** 

Alex can see:
- ✅ All the questions they asked on their MacBook
- ✅ All the Claude AI responses
- ✅ The entire context from the day before
- ✅ Everything works seamlessly as if they never switched machines

### 4e. Verify Everything Works

```bash
$ clocator status

--- Clocator Status ---
Current Path:     /home/alex/code/projects/my-ai-startup
Git Remote URL:   https://github.com/alex/my-ai-startup.git
Local Claude Key: home-alex-code-projects-my-ai-startup
Mapped Key:       Users-alex-Projects-my-ai-startup
Sync Status:      Linked successfully ➔ Users-alex-Projects-my-ai-startup
```

Everything is working perfectly!

---

## Step 5: Continue Work on Computer B

Alex starts coding and asking Claude new questions. The conversation continues seamlessly:

**In Claude Code:**
```
Claude: "Based on our earlier discussion about the embedding bias issue..."
```

Claude remembers everything! No context loss, no broken paths, no starting over.

---

## Step 6: Back to Computer A? Same Process!

When Alex returns to the office with their MacBook:

### 6a. Files sync again

Dropbox syncs the new session data from the Linux machine.

### 6b. The mapping already exists

`clocator-map.json` still has:
```json
{
  "https://github.com/alex/my-ai-startup.git": "Users-alex-Projects-my-ai-startup"
}
```

### 6c. Run `clocator pull` again (optional, but recommended)

```bash
$ clocator pull

ℹ Local Directory: /Users/alex/Projects/my-ai-startup
ℹ Local Claude Key: Users-alex-Projects-my-ai-startup
ℹ Synced Claude Key: Users-alex-Projects-my-ai-startup
✔ Paths match perfectly! No patching or linking required on this machine.
```

✅ All conversation history is there, waiting to continue.

---

## Real-World Benefits

### Before Clocator

```
Day 1 - MacBook:     Claude session created
        [Work for 8 hours, accumulate context]
        ❌ Sync files to Dropbox
        
Day 2 - Linux laptop: Dropbox syncs
        ❌ Claude Code looks for session at: /home/alex/code/...
        ❌ Not found! Starts BLANK session
        ❌ Lose all context from yesterday
        ❌ Have to re-explain everything to Claude
        ❌ Wasted time getting back to the same point
```

### With Clocator

```
Day 1 - MacBook:     Claude session created
        [Work for 8 hours, accumulate context]
        ✅ Run: clocator push
        ✅ Sync files to Dropbox
        
Day 2 - Linux laptop: Dropbox syncs
        ✅ Run: clocator pull (2 seconds)
        ✅ All context is restored automatically
        ✅ Claude remembers yesterday's conversation
        ✅ Continue working immediately
        ✅ No context loss, no re-explaining
```

---

## Multiple Projects?

Clocator handles multiple projects automatically!

**Day 1:**
```bash
cd ~/Projects/project-alpha
clocator push    # Maps GitHub URL → session

cd ~/Projects/project-beta
clocator push    # Maps different GitHub URL → different session
```

The mapping file stores both:
```json
{
  "https://github.com/alex/project-alpha.git": "Users-alex-Projects-project-alpha",
  "https://github.com/alex/project-beta.git": "Users-alex-Projects-project-beta"
}
```

**Day 2 (Different machine):**
```bash
cd ~/code/alpha
clocator pull    # Finds alpha session automatically

cd ~/code/beta
clocator pull    # Finds beta session automatically
```

Each project keeps its own conversation history. Perfect!

---

## When You Change Jobs?

Old projects stay in the map but are harmless:

```bash
cd ~/new-startup
clocator push    # Adds NEW project to map

# Old projects in the map? They just sit there unused.
# If you ever need them again, they're still there!
```

---

## The Three Commands Summarized

| Command | When | What It Does |
|---------|------|-------------|
| **`clocator push`** | Before syncing files | Registers the current project's Git URL → Session ID |
| **`clocator pull`** | After opening on new machine | Links the new path to the synced session |
| **`clocator status`** | Anytime | Shows what's mapped and if everything is linked |

---

## Installation Summary

### For Users Getting Clocator

```bash
# Step 1: Install
pip install clocator

# Step 2: Before you leave Computer A
cd ~/your/project
clocator push

# Step 3: After sync, on Computer B
cd ~/your/project  (possibly different path)
clocator pull

# Step 4: Open Claude and continue!
claude
```

That's it! 3 commands, seamless multi-device workflow.

---

## Common Real-World Scenarios

### Scenario A: Daily Office-to-Home Switch
```
Monday morning (Office):  clocator push
Monday evening (Home):    clocator pull → Resume
Tuesday morning (Office): clocator pull → Resume
```

### Scenario B: Traveling with Multiple Devices
```
Day 1 (Work laptop):  clocator push
Day 2 (Personal laptop): clocator pull → Continue
Day 3 (iPad with SSH): clocator pull → Continue
Day 4 (Back to work): clocator pull → Everything synced
```

### Scenario C: Team Collaboration
```
You: clocator push
      (Git history with your questions to Claude)
      ↓ (Same git repo)
Team member clones: clocator pull
                    (Maps to YOUR session history)
                    Sees all your Claude conversations!
```

---

## TL;DR

**Download:**
```bash
pip install clocator
```

**Use:**
```bash
# Before syncing
clocator push

# After syncing on new machine
clocator pull

# Verify it worked
clocator status

# Open Claude Code
claude
```

**Result:** Seamless conversation history across all your devices. Period. 🚀
