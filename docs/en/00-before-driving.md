<!-- lang: en | status: synced | source_revision: v0.1.0 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 00 | Before You Drive: A Safe First Run

[简体中文](../zh-CN/00-before-driving.md) · [Home](../../README.en.md)

## Remember this

Do not begin by asking an agent to automate everything. Put copies in a recoverable practice folder, ask for a read-only inventory and a plan, and authorize one small change only after you understand it.

## Why this matters

A chatbot usually gives you an answer. An agent may read files, execute commands, and leave persistent changes. That is useful, but vague instructions can become real disorder. Your first lesson is therefore scope, permissions, and inspection—not a “perfect prompt.”

You do not need to program. You do need to identify where the material is, what result you want, and how you will know it is correct.

## Try it: a ten-minute read-only exercise

1. Create a folder named `agent-practice` and place three non-sensitive document copies inside. Never use your only copy.
2. Open that folder in Codex and keep the default sandbox and approval settings.
3. Send this task:

```text
Inspect the current folder in read-only mode. Do not create, delete, move, or modify files.
List each file, its type, and its likely purpose. Flag duplicates, inconsistent names, and missing context.
Finish with an organization plan and identify every step that would modify a file. Do not execute the plan yet.
```

4. Compare the inventory with File Explorer.
5. Authorize one low-risk action, such as creating `inventory.md`; do not move originals.
6. Open the result and check its content and encoding yourself.

## Mistakes I have made

- Saying “organize this” without defining a classification rule.
- Practicing in Downloads, a raw-data folder, or the root of a synchronized drive.
- Treating “completed” as proof without opening the file.
- Disabling the sandbox to solve every permission problem.

## A normal result

- The inventory matches the folder and originals are unchanged.
- Recommendations are clearly separated from actions.
- The new inventory file is present and readable.
- Out-of-scope access triggers an approval request or a clear limitation.

## Checklist

- [ ] I used copies or synthetic material.
- [ ] My first request explicitly said read-only and no modification.
- [ ] I compared the inventory with the real folder.
- [ ] I reviewed the plan before an edit.
- [ ] I opened and inspected the result.
- [ ] I know how to remove or revert the practice output.

## What you can do now

You have completed the basic agent loop: define scope, constrain permissions, inspect the plan, allow a small action, and verify the result. Every later workflow is an extension of this loop.

## Sources and verification

- [OpenAI Docs: Codex best practices](https://learn.chatgpt.com/guides/best-practices)
- [OpenAI Docs: Windows app and sandbox](https://learn.chatgpt.com/docs/windows/windows-app)
- Last verified: 2026-09-22

[Next: Know your agent](01-know-your-agent.md)
