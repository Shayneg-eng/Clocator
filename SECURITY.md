# Security Policy

## Supported Versions

| Version | Supported          |
|---------|-------------------|
| 1.0.x   | ✅ Yes            |

## Reporting a Vulnerability

If you discover a security vulnerability in Clocator, please **do not** open a public GitHub issue. Instead, please follow responsible disclosure:

### Steps to Report:

1. **Email**: Send a detailed report to shayn@example.com with:
   - Description of the vulnerability
   - Steps to reproduce (if applicable)
   - Potential impact
   - Suggested fix (if you have one)

2. **Do NOT**:
   - Open a public GitHub issue
   - Disclose the vulnerability publicly before we've had time to address it
   - Share the vulnerability in forums or social media

3. **Response Timeline**:
   - We aim to respond within 48 hours
   - We'll work with you to understand and fix the issue
   - We'll coordinate disclosure timing with you

### Security Best Practices

When using Clocator:

1. **Protect your `~/.claude` directory**: This contains your Claude session history and mapping data. Keep it secure.

2. **Git remote URLs**: Clocator uses your Git remote URL as a fingerprint. Be mindful that this URL may be exposed in error messages.

3. **File permissions**: Ensure your synced files have appropriate permissions on all devices.

4. **Symbolic links**: On Windows, creating junctions may require appropriate permissions. Clocator will warn you if it can't create them.

5. **Cloud sync security**: Use a secure cloud sync service with encryption (most modern services do this by default).

## Security Considerations

Clocator is designed to be lightweight and secure:

- ✅ **No external dependencies**: Reduces attack surface
- ✅ **No authentication required**: Works with any Git repository
- ✅ **Open source**: Code can be audited by anyone
- ✅ **Safe file operations**: Validates paths and handles errors gracefully
- ⚠️ **Local file storage**: Relies on your cloud sync service's security

## Updates

Keep Clocator updated to get the latest security fixes:

```bash
pip install --upgrade clocator
```

## Questions?

If you have security-related questions that aren't vulnerabilities, feel free to open a discussion on GitHub.
