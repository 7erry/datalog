# datalog

Static HTML demo library for MongoDB solution narratives, architecture explainers, and discovery-call enablement.

## What This Repo Contains

- Interactive demo pages such as `atlas.html`, `payments.html`, and `migrations.html`
- Discovery companion markdown for each page (`*.discovery.md`)
- Discovery companion HTML pages for each page (`*.discovery.html`)
- Mirror/demo content under `misc/` and `readme/`

## Discovery Workflow

For each primary HTML page:

1. Opening-minute discovery script
2. Targeted open-ended discovery questions
3. Why status-quo/non-competitive approaches fail
4. Cost-of-inaction framing
5. Discovery operating framework (pre/during/end/post call guidance)

## Query Redirect Behavior

All non-discovery HTML pages support query-param redirects:

- `?discovery=true` -> sibling `*.discovery.html`
- `?discover=true` -> sibling `*.discovery.html`

Any remaining query params and hash are preserved.

## Scripts

- `scripts/build_discovery_pages.py`
  - Regenerates `*.discovery.html` from `*.discovery.md`
  - Ensures status-quo and cost-of-inaction sections are present
- `scripts/inject_discovery_query_redirect.py`
  - Injects redirect script into non-discovery HTML pages

## Local Notes

- Static site content (no mandatory root build step)
- Some subprojects (for example `my-weather-app/`) have their own Node toolchain

## License

Apache-2.0 (see `LICENSE`)
