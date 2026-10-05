# CNT Procedures Manual

Standard operating procedures of the Center for Neuroengineering & Therapeutics research teams, as Markdown, built into a website with [MkDocs](https://www.mkdocs.org) + [Material](https://squidfunk.github.io/mkdocs-material/). Maintained by the CNT associate director; anyone on the team can propose a change.

- `docs/` — the content. One folder per theme, one sub-folder per section, one file per procedure. The repository root is also an Obsidian vault.
- `hooks/wiki.py` — builds the navigation from the folders and writes `map/graph.json` and `_reports/stale.json` at build time. No hand-maintained nav.
- `docs/about/` — how to contribute, style guide, SOP template, roles.
- `AUDIT.md` — the October 2026 page-by-page audit: what is stale, what should merge or retire, and the questions to answer.
- `HOSTING.md` — how the website (https://cnt-manual.neurobridge.link) is published from this repository and edited in the browser.
- `MIGRATION-TODO.md` — what still needs a human pass after the import from the previous knowledge base.

## Preview locally

```bash
brew install uv          # once (or: curl -LsSf https://astral.sh/uv/install.sh | sh)
make serve               # http://127.0.0.1:8000 — uv creates .venv and installs MkDocs on first run
```

`make build` runs a strict build (broken links fail it); `make check` also runs the secret scanner if `gitleaks` is installed and the content check (`scripts/check_content.py`), which fails on passwords, keys, identifiers and the like.

## Editing with Obsidian

1. Obsidian → *Open folder as vault* → choose this repository folder.
2. Settings → Community plugins → install **Git** and enable it; set an auto commit-and-sync interval or use *Git: Commit all changes* / *Git: Push*.
3. The vault settings already use Markdown links with relative paths and put attachments in `docs/assets/`.

## Rules

No patient identifiers. No credentials. One procedure per page. See `docs/about/contributing.md`.

## Relationship to the NeuroBridge wiki

The Penn NeuroBridge Lab keeps its own wiki with the subset of these procedures its people run, and links here for everything else. Where a procedure exists in both, this manual is authoritative for the shared CNT systems.
