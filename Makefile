# Requires uv (https://docs.astral.sh/uv/). `uv run` creates the environment on first use.
.PHONY: serve build check stale
serve:        ## live preview at http://127.0.0.1:8000
	uv run mkdocs serve
build:        ## strict build into site/
	uv run mkdocs build --strict
check: build  ## build + secret scan (needs gitleaks) + identifier scan
	@command -v gitleaks >/dev/null && gitleaks detect --no-banner --redact || echo "gitleaks not installed — skipping secret scan"
	@uv run python scripts/check_content.py
stale:        ## list pages past their review window
	@uv run python scripts/stale_pages.py
