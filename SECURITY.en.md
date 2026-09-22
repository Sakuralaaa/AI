# Security

[简体中文](SECURITY.md)

## Never commit

- API keys, OAuth tokens, cookies, passwords, recovery codes, or authentication files.
- Unauthorized student, patient, interview, customer, or company data.
- Full logs or screenshots containing personal paths, accounts, IP addresses, or internal domains.

## Recommended practice

- Use placeholders such as `YOUR_API_KEY` and `https://example.invalid/v1`.
- Inventory an unfamiliar folder in read-only mode first. Preview batch renames, moves, or deletions and keep a recovery map.
- Keep sandboxing and approvals on by default; grant the minimum access required to trusted projects.
- Review the source, permissions, and network behavior of MCP servers, skills, plugins, and install scripts.
- Keep sensitive data in a controlled environment. Redact and obtain authorization before uploading it.

## If a secret leaks

Do not paste it into a public issue. Revoke or rotate it immediately, remove the public material, and inspect Git history. Deleting the current file does not invalidate a secret already present in history.

## Report a repository issue

This repository contains documentation and examples only. If an example accidentally contains sensitive information, use GitHub private vulnerability reporting and include the path and impact.
