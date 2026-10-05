---
title: "Style guide"
order: 2
---

# Style guide

Short, because a style guide nobody reads is worse than none.

**Write for the person doing the task for the first time, at 5 pm, slightly stressed.** Lead with the outcome ("After this you will have a de-identified EDF in `…/deid/`"), then the steps. Put the thing that goes wrong most often in *Troubleshooting*, not in a parenthesis in step 4.

**One task per page.** If a page needs a second H2 that starts with "How to", it is two pages.

**Steps are numbered, imperative, and testable.** "Run `natus2mef …`" not "The natus2mef script can be run". One action per step. Put the exact command, path or menu label in `code`.

**Names are exact.** Server names, folder names, project names and REDCap field names are written the way the system shows them (`cnt-fs`, `/project/eeg_process`, `HUPXXX_channelMapping`). Use `HUPXXX` and `sub-XXX` as placeholders, never a real subject.

**Link, don't repeat.** If another page already explains how to mount cnt-fs, link it. The Lab Manual explains; the themes instruct.

**Prefer plain Markdown.** Admonitions (`!!! note`, `!!! warning`, `!!! danger`) for things that must not be missed; tables for reference data; Mermaid for flows. Avoid HTML except the attachment placeholders.

**Dates are ISO** (`2026-10-04`). People are named by role in procedures ("the regulatory coordinator") and by name only on the Contacts page, so pages survive staff turnover.

**Headings:** the page title is the only H1. Body sections start at H2. Keep to three levels.

**Tone:** direct and friendly. No "please", no "simply", no "just".
