# File-operation preview

## Scope

- Root directory:
- May read:
- May write:
- Must not access:

## Rules

- Naming format:
- Classification rule:
- Duplicate handling: mark `REVIEW`; do not delete by default.
- Name collision: stop and report; do not overwrite by default.

## Before execution

Produce `operation-plan.csv` with at least:

```text
action,source,target,reason,status,rollback
```

The first pass creates the plan only. After human approval, test on copies; then produce `rollback.csv` and a failure list.
