# File-organization example

[简体中文](README.md)

This example demonstrates “map first, execute later.” `manifest-before.csv` describes a fictional directory, and `rename-plan.csv` is a plan awaiting human review.

Exercise:

1. Ask the agent to read the manifest without touching real files.
2. Review collisions, unknown items, and possible duplicates.
3. Resolve every `REVIEW` row manually.
4. Generate a new plan for your own temporary copy; never execute the sample paths directly.
5. After real execution, generate `rollback.csv` with source and target reversed for recovery.
