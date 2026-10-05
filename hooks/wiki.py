"""MkDocs hooks for the CNT procedures manual.

A page carries only what cannot be derived: title, stage, roles, scope, and
optionally order (and audit while the 2026 audit is being worked through).
Everything else comes from the folder it sits in or from git.

on_config         builds the navigation from the docs/ tree (no hand-maintained nav)
on_page_markdown  injects tags (stage + roles), the scope banner, and the landing-page counts
on_post_build     writes map/graph.json (pages x theme/stage/roles/scope) for the map page
                  and _reports/stale.json (every procedure's last change from git; stale = untouched for a year)

Pure Python + PyYAML (already a MkDocs dependency); no extra plugins needed.
"""
import os, re, json, datetime, subprocess, yaml
from mkdocs.plugins import event_priority

FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)

def front_matter(path):
    try:
        text = open(path, encoding="utf-8").read(20000)
    except OSError:
        return {}
    m = FM.match(text)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}

def title_of(path, fallback):
    fm = front_matter(path)
    if fm.get("title"):
        return str(fm["title"])
    try:
        for line in open(path, encoding="utf-8"):
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        pass
    return fallback

def sort_key(path):
    fm = front_matter(path)
    return (int(fm.get("order", 9999)), title_of(path, os.path.basename(path)).lower())

def pages_in(dirpath, docs_dir):
    files = [f for f in os.listdir(dirpath) if f.endswith(".md") and f != "index.md"]
    files.sort(key=lambda f: sort_key(os.path.join(dirpath, f)))
    return [{title_of(os.path.join(dirpath, f), f): os.path.relpath(os.path.join(dirpath, f), docs_dir)} for f in files]

def section_order_hint(theme_index):
    """The theme index lists its sections in a table; use that row order."""
    hint = {}
    if not os.path.exists(theme_index):
        return hint
    for i, m in enumerate(re.finditer(r"\]\(([a-z0-9\-]+)/index\.md\)", open(theme_index, encoding="utf-8").read())):
        hint.setdefault(m.group(1), i)
    return hint

def theme_nav(theme_dir, docs_dir, title):
    items = [os.path.relpath(os.path.join(theme_dir, "index.md"), docs_dir)]
    sections = [d for d in sorted(os.listdir(theme_dir)) if os.path.isdir(os.path.join(theme_dir, d))]
    order_hint = section_order_hint(os.path.join(theme_dir, "index.md"))
    sections.sort(key=lambda d: (order_hint.get(d, 9999), d))
    for d in sections:
        sdir = os.path.join(theme_dir, d)
        idx = os.path.join(sdir, "index.md")
        stitle = title_of(idx, d) if os.path.exists(idx) else d.replace("-", " ").title()
        entries = ([os.path.relpath(idx, docs_dir)] if os.path.exists(idx) else []) + pages_in(sdir, docs_dir)
        items.append({stitle: entries})
    return {title: items}

def on_config(config):
    docs = config["docs_dir"]
    themes = config["extra"]["wiki"]["themes"]
    nav = [{"Home": "index.md"}]
    lm = os.path.join(docs, "lab-manual")
    if os.path.isdir(lm):
        nav.append({"Lab Manual": pages_in(lm, docs)})
    for t in themes:
        tdir = os.path.join(docs, t["dir"])
        if os.path.isdir(tdir):
            nav.append(theme_nav(tdir, docs, t["title"]))
    if os.path.exists(os.path.join(docs, "map", "index.md")):
        nav.append({"Map": "map/index.md"})
    if os.path.exists(os.path.join(docs, "tags.md")):
        nav.append({"Tags": "tags.md"})
    about = os.path.join(docs, "about")
    if os.path.isdir(about):
        nav.append({"About this wiki": pages_in(about, docs)})
    config["nav"] = nav
    return config

# ------------------------------------------------------------------ derived page facts
def _theme_dirs(config):
    return {t["dir"]: t["title"] for t in config["extra"]["wiki"]["themes"]}

def _roles(config):
    path = os.path.join(os.path.dirname(config["docs_dir"]), "roles.json")
    return json.load(open(path)) if os.path.exists(path) else {}

def _procedures(config):
    """Every procedure page: a .md that is not an index, inside a theme folder, with a stage."""
    docs = config["docs_dir"]
    themes = _theme_dirs(config)
    nodes = []
    for tdir, ttitle in themes.items():
        root = os.path.join(docs, tdir)
        if not os.path.isdir(root):
            continue
        for dirpath, _, files in os.walk(root):
            for f in files:
                if not f.endswith(".md") or f == "index.md":
                    continue
                p = os.path.join(dirpath, f)
                fm = front_matter(p)
                if not fm.get("stage"):
                    continue
                rel = os.path.relpath(p, docs)
                sidx = os.path.join(dirpath, "index.md")
                section = title_of(sidx, os.path.basename(dirpath)) if dirpath != root and os.path.exists(sidx) else ""
                nodes.append({
                    "id": rel, "title": str(fm.get("title") or title_of(p, f)),
                    "url": re.sub(r"\.md$", "/", rel),
                    "theme": ttitle, "section": section, "stage": str(fm["stage"]),
                    "roles": list(fm.get("roles") or []), "scope": fm.get("scope", ""), "audit": fm.get("audit", ""),
                })
    return nodes

# ------------------------------------------------------------------ per-page markdown
SCOPE_BANNERS = {
    "clinical-coverage": ("note", "Clinical coverage only",
        "This is participant-facing work done by the CNT clinical research coordinators. NeuroBridge members need it "
        "only when covering a clinical duty. Trainees and analysts can skip it."),
    "shared": ("info", "Shared infrastructure",
        "This describes a CNT or Penn system the lab depends on but does not run. Read it to understand the pipeline; "
        "ask the data research coordinator before acting on it."),
    "reference": ("abstract", "Background reading",
        "Read once for orientation. It is not a procedure you will be asked to perform."),
    "flagged": ("warning", "Flagged in the audit",
        "The October 2026 audit recommends retiring or merging this page (see `AUDIT.md` in the repository). "
        "Treat its content as unconfirmed until the lab decides."),
}
AUDIT_NOTE = {
    "merge": ("warning", "Flagged for merging",
        "The October 2026 audit recommends merging this page with a sibling (see `AUDIT.md`). The content stands until then."),
    "retire": ("warning", "Flagged for retirement",
        "The October 2026 audit recommends retiring this page (see `AUDIT.md`). Treat its content as unconfirmed."),
}

def _banner(kind, title, text):
    return f'!!! {kind} "{title}"\n    {text}\n\n'

@event_priority(50)   # before the Material tags plugin reads page.meta["tags"]
def on_page_markdown(markdown, page, config, files):
    meta = page.meta or {}

    # tags = stage + role labels, so the Tags page needs no hand-written list
    if meta.get("stage") and "tags" not in meta:
        roles = _roles(config)
        meta["tags"] = [str(meta["stage"])] + [roles[r][0] if r in roles else r for r in (meta.get("roles") or [])]

    scope = meta.get("scope")
    banners = ""
    if scope in SCOPE_BANNERS:
        banners += _banner(*SCOPE_BANNERS[scope])
    if scope != "flagged" and meta.get("audit") in AUDIT_NOTE:
        banners += _banner(*AUDIT_NOTE[meta["audit"]])
    if banners:
        lines = markdown.split("\n", 1)
        if lines[0].startswith("# "):
            markdown = lines[0] + "\n\n" + banners + (lines[1] if len(lines) > 1 else "")
        else:
            markdown = banners + markdown

    if page.file.src_path != "index.md" or "%%" not in markdown:
        return markdown
    nodes = _procedures(config)
    docs = config["docs_dir"]
    manual = len([f for f in os.listdir(os.path.join(docs, "lab-manual")) if f.endswith(".md")]) if os.path.isdir(os.path.join(docs, "lab-manual")) else 0
    def repl(m):
        key = m.group(1)
        if key == "PAGES": return str(len(nodes))
        if key == "MANUAL": return str(manual)
        if key.startswith("T:"): return str(sum(1 for n in nodes if n["theme"] == key[2:]))
        if key.startswith("S:"): return str(sum(1 for n in nodes if n["stage"] == key[2:]))
        return m.group(0)
    return re.sub(r"%%([^%]+)%%", repl, markdown)

# ------------------------------------------------------------------ graph + reports
def git_history(repo_root, docs_rel="docs"):
    """{path relative to repo: (last_date, last_author, number_of_commits)} from git, or {} if no git."""
    try:
        out = subprocess.run(["git", "log", "--format=%x01%cs%x09%an", "--name-only", "--", docs_rel],
                             cwd=repo_root, capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {}
    hist, date, author = {}, None, None
    for line in out.splitlines():
        if line.startswith("\x01"):
            date, author = line[1:].split("\t", 1)
        elif line.strip():
            d = hist.setdefault(line.strip(), [date, author, 0])
            d[2] += 1
    return {k: tuple(v) for k, v in hist.items()}

def on_post_build(config):
    docs = config["docs_dir"]
    repo = os.path.dirname(docs)
    nodes = _procedures(config)
    scopes = {"core": "Core: our people do this", "shared": "Shared infrastructure", "reference": "Background reading",
              "clinical-coverage": "Clinical coverage only", "flagged": "Flagged: retire or merge"}
    out = {"generated": datetime.date.today().isoformat(), "themes": list(_theme_dirs(config).values()),
           "stages": config["extra"]["wiki"]["stages"], "roles": _roles(config), "nodes": nodes,
           "scopes": scopes if any(n.get("scope") for n in nodes) else {}}
    os.makedirs(os.path.join(config["site_dir"], "map"), exist_ok=True)
    json.dump(out, open(os.path.join(config["site_dir"], "map", "graph.json"), "w"), indent=0)

    # review report, from git: every procedure with its last change; stale = untouched for a year
    today = datetime.date.today()
    hist = git_history(repo)
    report = []
    for n in nodes:
        rel = os.path.join(os.path.basename(docs), n["id"])
        date, author, commits = hist.get(rel, (None, None, 0))
        try:
            age = (today - datetime.date.fromisoformat(date)).days if date else None
        except ValueError:
            age = None
        report.append({"page": n["id"], "title": n["title"], "last_changed": date or "", "last_author": author or "",
                       "commits": commits, "stale": age is None or age > 365})
    report.sort(key=lambda r: r["last_changed"])
    stale = [r for r in report if r["stale"]]
    os.makedirs(os.path.join(config["site_dir"], "_reports"), exist_ok=True)
    json.dump({"generated": today.isoformat(), "stale_count": len(stale), "pages": report},
              open(os.path.join(config["site_dir"], "_reports", "stale.json"), "w"), indent=1)
