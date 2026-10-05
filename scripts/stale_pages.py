#!/usr/bin/env python3
"""List procedures by last change (from git), oldest first; pages untouched for a year are marked stale.

Same data as _reports/stale.json in the built site. Nothing is kept by hand: git knows who last
changed a page and when.
"""
import os, sys, datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hooks"))
import yaml, wiki  # noqa: E402

root = os.path.join(os.path.dirname(__file__), "..")
config = yaml.safe_load(open(os.path.join(root, "mkdocs.yml")).read().replace("!!python/name:", ""))
config["docs_dir"] = os.path.join(root, "docs")
today = datetime.date.today()
hist = wiki.git_history(root)
rows = []
for n in wiki._procedures(config):
    date, author, commits = hist.get(os.path.join("docs", n["id"]), ("", "", 0))
    age = (today - datetime.date.fromisoformat(date)).days if date else None
    rows.append((date or "0000-00-00", author or "-", commits, age, n["id"]))
rows.sort()
stale = 0
for date, author, commits, age, path in rows:
    flag = "STALE" if age is None or age > 365 else "     "
    stale += flag.strip() == "STALE"
    print(f"{flag} {date:>10}  {commits:>3} change(s)  {author:<18} {path}")
print(f"\n{len(rows)} procedure(s); {stale} not changed in a year")
