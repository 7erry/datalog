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

## Discovery data in MongoDB (Atlas)

The `server/` app stores editable discovery questions in Atlas under the database name **`datalog`** (configurable via `DB_NAME`).

### Collections

- **`discovery_topics`** — one document per topic (`slug`, `title`, `companionHtml`, `sourceMarkdown`, timestamps)
- **`discovery_questions`** — questions for a topic (`topicSlug`, `order`, `question`, `description`, `customerResponse`, timestamps)

`description` is internal or seller-facing context for the question. `customerResponse` holds what the customer said (captured during discovery). Together they form the basis for a future **RAG** pipeline; see `GET /api/discovery/rag-context?topicSlug=...` for concatenated text chunks.

### Setup

1. Create (or reuse) an Atlas cluster and user. Add your IP (or `0.0.0.0/0` for development only) under **Network Access**.
2. Copy `server/.env.example` to `server/.env` and set `MONGODB_URI` (do not commit `.env`). If a connection string was ever shared in plain text, **rotate the password**.
3. Install and run the API:

```bash
cd server
npm install
npm run seed    # imports **/*.discovery.md into MongoDB
npm start       # serves static site + API + admin UI
```

4. Open **http://localhost:3000/discovery-admin.html** to add, edit, or delete questions and to fill in descriptions and customer responses.

### API (summary)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/health` | Liveness |
| GET | `/api/discovery/topics` | List topics |
| GET | `/api/discovery/questions?topicSlug=` | List questions for a topic (slug may include `/`) |
| POST | `/api/discovery/questions` | Create question (`topicSlug`, `question`, optional `description`, `customerResponse`) |
| PATCH | `/api/discovery/questions/:id` | Update fields |
| DELETE | `/api/discovery/questions/:id` | Remove question |
| GET | `/api/discovery/rag-context?topicSlug=` | Text chunks for future RAG indexing |

## Local Notes

- Static site content (no mandatory root build step)
- Some subprojects (for example `my-weather-app/`) have their own Node toolchain

## License

Apache-2.0 (see `LICENSE`)
