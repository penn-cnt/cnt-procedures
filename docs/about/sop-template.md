---
title: "SOP template"
order: 3
---

# SOP template

Copy the block below into a new file in the right theme and section folder (for example `docs/electrophysiology/channel-mapping/my-new-procedure.md`). Delete any section you don't need; keep the order.

````markdown
---
title: "Verb + object, e.g. Exporting EEG from Natus"
stage: "Data Collection"
roles: [data-rc]
order: 99
---

# Verb + object

!!! abstract "What this page tells you"
    One or two sentences: what you will have at the end, and when you need to do this.

## Purpose

Why this exists and what it produces.

## Scope

When this applies and when it doesn't (which studies, which systems, which data types).

## Prerequisites

- Access you need (link to the request page in Operations › Access & Accounts)
- Software, mounts, VPN
- Inputs: where they are and what they look like

## Procedure

1. First action, with the exact command or menu path in `code`.
2. Second action.
    1. Sub-step if truly needed.
3. How you know it worked (the file that should now exist, the message you should see).

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| … | … | … |

## Notes

History, exceptions, who to ask. Link related pages here.
````

The house structure is **Purpose / Scope / Prerequisites / Procedure / Troubleshooting / Notes**. Migrated pages don't follow it yet; reshaping them one section at a time is a good first contribution.
