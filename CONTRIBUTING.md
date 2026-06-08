# Contributing to Clocator

Thank you for your interest in contributing to Clocator! We welcome bug reports, feature suggestions, and pull requests.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/clocator.git`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Make your changes
5. Test your changes thoroughly
6. Commit with a clear message: `git commit -m "Add your feature description"`
7. Push to your fork: `git push origin feature/your-feature`
8. Open a Pull Request to the main repository

## Development Setup

```bash
# Clone the repository
git clone https://github.com/shayn/clocator.git
cd clocator

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Run the tool
clocator --help
```

## Testing

Before submitting a PR, ensure your changes work:

```bash
# Test the basic commands
python clocator.py push
python clocator.py status
python clocator.py pull

# Test across different scenarios:
# - Different Git remotes
# - Different folder structures
# - Both macOS/Linux and Windows environments
```

## Code Style

- Follow PEP 8 conventions
- Keep functions focused and well-named
- Add comments only when behavior is non-obvious
- No external dependencies (keep it lightweight)

## Reporting Issues

When reporting bugs, please include:

- Your operating system and Python version
- Steps to reproduce the issue
- Expected vs actual behavior
- Any error messages or logs

## Feature Requests

We're open to feature suggestions! Please describe:

- The use case or problem you're solving
- How the feature would work
- Any potential alternatives or trade-offs

## Code of Conduct

Be respectful and constructive in all interactions. We're all here to make this tool better together!

## Questions?

Feel free to open an issue or discussion if you have questions about the codebase.
