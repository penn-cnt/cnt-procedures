#!/usr/bin/env python3
"""Fail the build if obvious PHI, credential, or legacy-source patterns appear in docs/.

FAIL patterns stop the build. WARN patterns are printed for a human to look at
(institutional phone numbers are fine; personal mobiles are not).

Run: uv run python scripts/check_content.py   (also runs in CI and pre-commit)
"""
import re, sys, pathlib

# Words that commonly follow "password" in prose and are not secrets.
PROSE = set("""in the your get see has was that is and manager removed reset prompt field protected
given within when will must should if to of on or for from with you use using via into set setting
which same separate below above again policy arrives expires length masked required change changed
this they them it its a an as at by be been can do does done each every here into may might new
old once only over per plus then there these those through under until upon used very what where
while who why yes yet first last next later before after sent email link page tab click enter type
temporary expired expiry current previous resets pretty fields my_password your_password yourpassword
xxxxxxxx placeholder""".split())

def password_value(line):
    """Return a suspicious password-like value from a line, or None."""
    for m in re.finditer(r"\bpass(?:word|wd|code)\b\s*(?:[:=]|is|for\s+\w+\s*:?)?\s*[\"'*(]*([A-Za-z0-9!@#$%^&*_\-]{5,})", line, re.I):
        v = m.group(1)
        if v.lower() in PROSE: continue
        if re.search(r"\d", v) or not v.isalpha() or (v.islower() and len(v) >= 5): return v
    return None

FAIL = {
 "api key / token":    re.compile(r"\b(api[_\- ]?(?:token|secret|key)|access[_\- ]?key|secret[_\- ]?key|bearer)\b\s*[:=]?\s*[\"']?[A-Za-z0-9\-]{16,}", re.I),
 "door / unlock code": re.compile(r"\b(door|room|unlock|access)\s+code\b\s*[:=]?\s*\**\d{4,}", re.I),
 "url session key":    re.compile(r"[?&](?:_k|token|sig|sv|sp|sas)=[A-Za-z0-9%]{4,}", re.I),
 "sas token":          re.compile(r"\bsv=\d{4}-\d{2}-\d{2}&", re.I),
 "MRN-like":           re.compile(r"\bMRN\s*[:#]?\s*\d{6,}", re.I),
 "DOB":                re.compile(r"\b(DOB|date of birth)\s*[:#]?\s*\d{1,2}/\d{1,2}/\d{2,4}", re.I),
 "SSN":                re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
 "fund / budget code": re.compile(r"\b\d{3}-\d{4}-\d-\d{6}-"),
 "withheld-note leak": re.compile(r'class="attachment-withheld" title="(?!Withheld after PHI review")'),
 "legacy source":      re.compile(r"18mwk3-\d+|click[\s\-]?u[p]|noti[o]n\.(?:so|site|com)|\bnoti[o]n\b", re.I),
 "import residue":     re.compile(r"You do not have access to this Doc", re.I),
}
WARN = {
 "phone number (institutional is fine)": re.compile(r"(?<![\d\-])\(?\d{3}\)?[\s.\-]\d{3}[\s.\-]\d{4}(?![\d\-])"),
 "uuid (dataset ids are fine, tokens are not)": re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I),
}
fails = warns = 0
for p in sorted(pathlib.Path("docs").rglob("*.md")):
    for i, raw in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.replace("\\_", "_").replace("\\-", "-")
        v = password_value(line)
        if v:
            print(f"FAIL {p}:{i}: password in text ({v}): {raw.strip()[:120]}"); fails += 1
        for name, rx in FAIL.items():
            if rx.search(line):
                print(f"FAIL {p}:{i}: {name}: {raw.strip()[:120]}"); fails += 1
        for name, rx in WARN.items():
            if rx.search(line):
                print(f"warn {p}:{i}: {name}: {raw.strip()[:100]}"); warns += 1
print(f"content check: {'OK' if not fails else str(fails) + ' problem(s)'}; {warns} warning(s) to eyeball")
sys.exit(1 if fails else 0)
