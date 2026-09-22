<!-- lang: en | status: synced | source_revision: v0.1.0 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 05 | Learn to Drive: Workspace, Task, Plan, and Review

[简体中文](../zh-CN/05-learn-to-drive.md) · [Home](../../README.en.md)

## Remember this

A reliable task states the goal, material, output, constraints, and definition of done. Plan difficult work, execute in small reversible steps, and inspect every stage.

## Build a clean workspace

Keep one task in one directory:

```text
project/
├─ input/       # original material, preferably read-only
├─ work/        # intermediate artifacts
├─ output/      # deliverables
├─ README.md    # stable purpose and structure
└─ HANDOFF.md   # current state and next action
```

Do not use Desktop, Downloads, or your entire document library as a workspace. Separating inputs and outputs reduces accidental overwrites.

## State the destination

Use the [task brief](../../templates/en/task-brief.md):

```text
Goal: Turn three interview summaries into briefing material.
Context: The audience did not attend the interviews.
Inputs: Three redacted documents under input/.
Outputs: output/summary.md and output/briefing-outline.md.
Constraints: Do not edit input; do not invent participant views; use no external sources.
Done when: Every theme has a source pointer and conflicting views are listed separately.
```

It takes longer than “summarize this,” but prevents repeated repair.

## When to plan first

Use Plan mode or request investigation without edits when the task spans files, touches important data, includes irreversible operations, or remains unclear to you. Ask the agent to identify knowns, unknowns, files affected, staged outputs, dependencies, risks, recovery, and decisions that belong to you.

A small, reversible, well-scoped task does not need a ceremonial long plan.

## Rules during execution

1. **Inventory first.** Confirm files, formats, and counts.
2. **Make one sample.** Validate one item before a batch.
3. **Work in batches.** Leave readable intermediate results.
4. **Keep originals.** Write to a new output unless overwrite is explicitly approved.
5. **Report evidence.** Name actual files, checks performed, and items not verified.

## Give a project memory

- `README.md`: stable purpose, layout, and goals.
- `AGENTS.md`: durable operating agreements such as protecting raw data and defining verification.
- `HANDOFF.md`: completed work, unresolved questions, and the next action.
- Current prompt: requirements unique to this task.

OpenAI documentation describes layered `AGENTS.md` discovery from global to project and deeper directories, with more specific guidance taking precedence. Keep instructions short and accurate.

## Mistakes I have made

- Mixing five goals into one prompt and finishing none of them well.
- Specifying presentation without specifying evidence or acceptance.
- Asking the agent to judge correctness without a calculable or comparable standard.
- Putting a temporary request into permanent AGENTS.md guidance.

## Checklist

- [ ] The workspace contains only relevant material.
- [ ] Inputs and outputs are separated.
- [ ] The brief defines goal, inputs, outputs, constraints, and done.
- [ ] I reviewed a plan or preview before risky actions.
- [ ] The final report lists real artifacts and unverified items.
- [ ] I can revert through version history, backup, or a recovery map.

## Sources and verification

- [OpenAI Docs: Best practices](https://learn.chatgpt.com/guides/best-practices)
- [OpenAI Docs: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- Last verified: 2026-09-22

[Previous](04-routing-and-proxy.md) · [Next: Everyday workflows](06-daily-workflows.md)
