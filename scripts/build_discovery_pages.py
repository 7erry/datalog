#!/usr/bin/env python3
"""
Regenerate *.discovery.md (insert status-quo + cost sections) and *.discovery.html
from the same content. Run from repo root: .venv/bin/python scripts/build_discovery_pages.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
MARKER = "## Why current approaches fall short (without a competitive move)"
QUESTION_HEADER = "## Ten open-ended questions (pain points & buying process)"

# (slug, why_markdown, cost_markdown) — slug matches path relative to ROOT without `.discovery.md`
TOPICS: list[tuple[str, str, str]] = [
    (
        "agenticmemory",
        "The usual “non-competitive” pattern is **memory scattered** across caches, blob stores, ad hoc vector indexes, and application tables nobody owns end-to-end. Nothing enforces a consistent lifecycle for **PII, retention, or eval hooks**, so every agent feature becomes a custom integration. Teams optimize demos, not **governed retrieval**—and production surprises follow.",
        "Inaction compounds into **rework tax**: each new use case rebuilds the same plumbing while latency and quality drift under real traffic. You risk **trust incidents** (wrong recall, leaked context) and slower GTM because security and legal can’t sign off on a system that wasn’t designed as a platform. Budget leaks into **duplicate stores, ETL, and on-call** for glue that should be standardized.",
    ),
    (
        "aggregations",
        "Without a shared discipline, pipelines grow as **copy-paste stages** in code and one-off jobs nobody profiles. The “solution” becomes exporting everything to a warehouse or lake—**higher latency, more sync failure modes**, and two places to secure. Reviews rarely connect **stage cost** to user-visible SLAs, so regressions ship quietly.",
        "Cost of inaction is **surprise Atlas bills**, brittle dashboards, and analytics debt that blocks product bets. Incidents trace back to “**someone changed a $match**” with no explain plan culture. You pay twice: engineering time firefighting and **duplicate pipelines** that diverge from operational truth.",
    ),
    (
        "aimongo",
        "Teams avoiding a deliberate vector strategy default to **yet another database** plus nightly sync jobs and fuzzy ownership. Hybrid search (text + vector + metadata filters) gets bolted on inconsistently, so relevance tuning lives in **notebooks, not production**. Non-competitive here means **integration spaghetti**, not “we picked the wrong algorithm once.”",
        "You stall on **time-to-production** while competitors ship retrieval that matches their domain. TCO climbs from **egress, duplicated data, and specialist headcount**; security reviews multiply because vectors and source documents live in different trust boundaries. The org learns the same HNSW lesson **six times** across squads.",
    ),
    (
        "aisearch",
        "Status quo is often **three products pretending to be one**: search, LLM gateway, and content connectors stitched with scripts. Procurement buys “AI search” but operations inherit **opaque relevance**, weak governance, and unpredictable metering. Non-competitive evaluations compare slide decks instead of **your corpus, your compliance, your latency SLOs**.",
        "Inaction shows up as **pilot purgatory**: promising demos that can’t pass enterprise gates or survive cost at scale. Support and internal users churn when answers are confident but wrong. You burn quarters reconciling **logging, access control, and data residency** across vendors that weren’t chosen as a system.",
    ),
    (
        "atlas",
        "“We’re on Atlas” without an **advanced deployment design** usually means defaults that were fine at MVP: single region assumptions, loose network boundaries, backup policies nobody tests, and **tier upgrades as panic therapy**. Non-competitive isn’t laziness—it’s **no explicit trade space** between blast radius, cost, and agility.",
        "The bill and the incident queue rise together: **noisy neighbors inside the org**, slow failovers, and audits that surface missing evidence. Launches slip because **change windows** become mandatory once risk is discovered late. You pay for **emergency scaling and consulting** that planning would have avoided.",
    ),
    (
        "caveats",
        "Ignoring scale caveats, teams accept **vendor fairy tales** tuned to toy datasets. Filtering + high churn + hybrid queries expose **memory cliffs and tail latency** that averages hide. Non-competitive here is **benchmark theater** instead of workload-faithful testing.",
        "Cost of inaction is **production surprises after commit**: re-index storms, recall collapses, and re-architecture under deadline. Finance sees **unplanned spend**; product sees **rolled-back features**. You lose credibility with leadership when the POC hero metrics don’t survive **real metadata and write rates**.",
    ),
    (
        "changelog",
        "When enablement content is a **static PDF graveyard**, teams work from outdated narratives and repeat the same objections in deals. Non-competitive is **no single source of truth** for what changed, why it matters, and who should read it—so customer-facing folks improvise.",
        "Deals slow over **fear of being wrong**; solution engineers rebuild collateral instead of selling. New hires ramp on **myths**. You absorb hidden cost in **reworked RFP answers, repeated workshops, and lost expansion** because buyers don’t trust your story is current.",
    ),
    (
        "clusterreview",
        "Without periodic health discipline, clusters drift: **indexes nobody dares drop**, zombie connections, backup policies never restored, and metrics nobody ties to **customer pain**. Non-competitive operations mean **tribal knowledge** and heroics—not a prioritized risk backlog.",
        "Inaction converts to **preventable incidents**, overtime, and renewals negotiated from weakness because reliability stories are thin. Performance regressions become **“MongoDB is slow”** narratives instead of fixable design issues. You pay for **fire drills** that a structured review would have flagged as yellow weeks earlier.",
    ),
    (
        "cosmosdb_documentdb",
        "Teams stay on **compatibility surfaces** that behave subtly differently—**RU math surprises**, unexpected limits, and operational models that don’t match how MongoDB drivers and tools were built. Non-competitive is tolerating **ongoing translation tax** between docs, support, and reality.",
        "Cost is **slower delivery** (workarounds in app code), **higher true TCO** once throughput grows, and **migration fear** that hardens into permanent friction. Strategic bets wait because nobody wants to replatform—while competitors ship on **predictable semantics** and richer ecosystem support.",
    ),
    (
        "crud",
        "When CRUD is “obvious,” teams skip **schema discipline, index strategy, and idempotency**—then blame the database. Non-competitive patterns include unbounded documents, **silent partial updates**, and deletes that orphan related data. Reviews focus on features, not **data shape**.",
        "You get **incident debt**: duplicate keys, hot shards, and migrations that freeze releases. Customer-visible symptoms—timeouts, inconsistent reads—trigger **expensive war rooms**. Paying down the model later costs more than shaping it early, especially under **compliance or multi-team** ownership.",
    ),
    (
        "cts",
        "AI ops initiatives fail when they’re **dashboards without workflow**: alerts still route to humans with no context, and automation lacks **guardrails**. Non-competitive is buying “AIOps” as branding while runbooks stay static and data stays siloed.",
        "Inaction preserves **toil and MTTR** that executives thought they funded away. Skepticism grows after a flashy POC can’t pass **change control**. You waste budget on tools that don’t connect to **tickets, CMDB, and actionable remediation**—so value never reaches the incident bridge.",
    ),
    (
        "ddp",
        "The fragmented default is **best-of-breed sprawl**: OLTP here, search there, vectors elsewhere, glue everywhere. Each team optimizes locally; **nobody owns the integration tax**. Non-competitive means accepting **sync lag and dual security models** as “just how it is.”",
        "Cost of inaction is **velocity cliffs**: every new feature crosses three teams and three on-call rotations. Incidents become **multi-system mysteries**; FinOps can’t allocate spend cleanly. You compete against orgs that ship **one data plane** with coherent observability and access policy.",
    ),
    (
        "ddp_old",
        "Older narratives still shape decisions: teams **standardize on stories** instead of current capabilities, or dismiss consolidation as marketing. Non-competitive is **static mental models**—architecture reviews cite slides from two years ago.",
        "You mis-scope pilots (**missing features you didn’t know existed**) or over-build (**replicating platform value in-house**). Strategy meetings debate ghosts while **renewal clocks** tick. Education debt turns into **wrong RFPs and delayed migrations**.",
    ),
    (
        "demo",
        "Short demos without discovery become **feature bingo**: impressive clicks, weak linkage to **your** constraints. Non-competitive selling skips **success criteria**, so the meeting ends without a shared next step or owner.",
        "You burn cycles repeating demos for **spectators who can’t buy**, while champions lack artifacts to **navigate security and procurement**. Deals stall not on tech but on **missing proof packaged for your process**.",
    ),
    (
        "demo2",
        "Big-picture demos without grounding invite **“cool, but not us”** reactions—too abstract to map to workloads and stakeholders. Non-competitive is enthusiasm without **criteria, timeline, or sponsor**.",
        "Cost is **lost momentum**: execs nod, engineers shrug, and nothing hits the roadmap. Competitors anchor a **concrete POC** while you’re still aligning on vocabulary. Expansion revenue waits on **a narrative tied to measurable outcomes**.",
    ),
    (
        "ea-architecture",
        "Enterprise Advanced matters when teams **under-buy controls**—then try to bolt audit, encryption, and ops rigor on late. Non-competitive is treating EA as a SKU checkbox instead of **mapping to control frameworks and ownership**.",
        "Inaction surfaces as **audit findings, delayed go-lives, and expensive exceptions**. Legal and security become **serial revisitors** because architecture evidence was never assembled. You pay for **rush implementations** and reworked designs under scrutiny.",
    ),
    (
        "elastic_mongo",
        "Dual-stack Elasticsearch + document DB is powerful until **sync becomes the product**: mapping drift, reindex pain, and two on-call domains. Non-competitive is accepting **operational coupling** without measuring toil or failure blast radius.",
        "Cost of inaction is **headcount and incident load** maintaining pipelines that could narrow. TCO debates ignore **engineering time** until hiring can’t keep up. Search relevance work fragments across teams with **different tooling and standards**.",
    ),
    (
        "eytaxquestion",
        "Relational models force **JSON blobs, sparse columns, or EAV** that fight evolving questionnaires. Non-competitive is “we’ll migrate later” while every season adds **DDL stress and brittle reports**.",
        "You ship late on regulatory or client changes; analytics teams spend sprints **unpicking blobs**. Audit risk rises when **lineage and validation** are manual. Technical debt becomes a **business constraint** on entering new markets or segments.",
    ),
    (
        "ha-demo",
        "HA slides without app behavior teach the wrong lesson: **failover mechanics** look fine while retries stampede or idempotency breaks. Non-competitive is infra confidence without **client and workflow design**.",
        "Inaction yields **false security**—drills pass until a real partial outage corrupts data or duplicates money movement. Customers experience **longer outages** than the database’s story promised. Postmortems blame “the driver” instead of **end-to-end contracts**.",
    ),
    (
        "hnsw",
        "Treating vector indexes as magic black boxes leads to **mystery latency** and tuning by rumor. Non-competitive is skipping intuition on **accuracy vs speed** tradeoffs until production users feel it.",
        "You pick parameters that **don’t match recall needs**, overspend on hardware, or oscillate between “too slow” and “wrong answers.” ML and platform teams argue without **shared vocabulary**, delaying releases.",
    ),
    (
        "home",
        "Without a hub, people **bookmark random PDFs** and contradict each other in customer meetings. Non-competitive enablement is **navigation by memory** instead of curated paths.",
        "Ramp time stretches; **inconsistent messaging** erodes trust. You reinvent explainers per deal instead of **scaling learning**. Strategic initiatives lack a **single entry point** tied to outcomes.",
    ),
    (
        "matrix",
        "Decisions made by **loudest voice** or vendor affinity recycle old debates. Non-competitive is no explicit **criteria, weighting, or evidence**—so choices don’t stick and teams reopen them under stress.",
        "Cost of inaction is **re-litigation**, stalled migrations, and architecture churn. You pay for **duplicate POCs** and political damage when teams feel ignored. Execution slows because nobody documented **why** a decision was made.",
    ),
    (
        "migrations",
        "Tool shopping without a **cutover strategy** produces pretty spreadsheets and scary weekends. Non-competitive migrations skip **validation, rollback, and ownership**—then blame the tool.",
        "You risk **data divergence, extended dual-writes, and compliance gaps** during transition. Business loses confidence; engineering burns out on **manual reconciliation**. Late fixes cost more than **front-loading risk controls**.",
    ),
    (
        "mongoatscale",
        "At-scale runbooks don’t appear by accident; without them, teams **react to metrics** instead of preventing drift. Non-competitive scale means **heroic individuals** holding production together.",
        "Incidents, **unplanned spend**, and launch slips become normal. Leaders hear “we need more hardware” without a **prioritized reliability roadmap**. Talent attrition rises when **on-call is chaos**.",
    ),
    (
        "mongoatscalev2",
        "Command-center thinking fails if signals don’t drive **weekly prioritization**—dashboards become wallpaper. Non-competitive ops confuses **visibility with control**.",
        "You still miss **cross-team hotspots**; executives get noise without decisions. Cost shows up as **repeated outages** and late capacity work. Platform teams drown in **tickets that should be patterns**.",
    ),
    (
        "multitenancy",
        "Ad hoc tenancy—**shared everything** until a big customer screams—creates **noisy neighbors and audit anxiety**. Non-competitive design postpones isolation decisions until contracts force them.",
        "Cost is **re-architecture under renewal pressure**, unfair cost allocation across BUs, and **security reviews** that fail on paper. Sales deals stall on **data separation** promises engineering can’t cheaply fulfill.",
    ),
    (
        "my-weather-app/index",
        "Sandbox apps without intent become **toy demos** that don’t connect to **integration, auth, or delivery** reality. Non-competitive learning stops at UI polish.",
        "Teams celebrate a prototype that **doesn’t prove** database fit, API patterns, or security gates—then stall moving to prod. Stakeholders withhold budget because **risk wasn’t addressed**, only aesthetics.",
    ),
    (
        "oracle_mongo",
        "Staying on Oracle for familiarity avoids **rethinking workflows**—but licensing and agility penalties compound. Non-competitive is incremental SQL tweaks when the domain is **document-shaped** or change-heavy.",
        "Cost of inaction is **renewal leverage against you**, slower feature delivery, and talent scarcity. Migrations deferred become **bigger-bang risk** with more integrations and reporting entanglements.",
    ),
    (
        "payments",
        "Payments on generic patterns without **idempotency, traceability, and reconciliation discipline** invite subtle money bugs. Non-competitive is “it works in happy path” without **failure injection** culture.",
        "Inaction shows as **chargebacks, manual fixes, and audit pain**—brand and regulatory exposure. Scaling events become **bet-the-company weekends**. You pay fines, credits, and **engineering halt** while trust recovers slowly.",
    ),
    (
        "perf",
        "Benchmarks disconnected from **production query shapes** mislead procurement and architecture. Non-competitive is **hero charts** that ignore tail latency, write amplification, and **realistic concurrency**.",
        "You buy wrong tiers, pick wrong designs, and **reopen decisions** after go-live pain. Teams lose trust in data-driven narratives; **politics fills the void**. Money flows to hardware instead of **fixable patterns**.",
    ),
    (
        "performance_visualization",
        "Numbers without narrative fail in **exec rooms**—stakeholders don’t see why latency ties to revenue or cost. Non-competitive is spreadsheets nobody reads.",
        "Decisions default to **gut and vendor noise**; good engineering work doesn’t get funded. You repeat the same debates quarterly because **the story wasn’t visualized and archived**.",
    ),
    (
        "pg-vs-mongo",
        "Postgres at huge scale without honest tradeoffs leads to **connection storms, MVCC pain, and ORM-generated join monsters**—then MongoDB is dismissed because “we’re a Postgres shop.” Non-competitive is **identity over fit**.",
        "Cost is **expensive vertical scaling**, specialized DBAs stretched thin, and features delayed by **schema migration fear**. Opportunity cost grows when document or scale-out models would **reduce blast radius** for specific workloads.",
    ),
    (
        "pgmdb",
        "Transaction semantics misunderstood across teams cause **subtle bugs**—retries, isolation surprises, and “it worked in dev.” Non-competitive is **assumption mismatch** between app authors and DBAs.",
        "You ship defects that look like app logic but are **concurrency stories**; incidents erode trust in the datastore choice. Education gaps slow **architecture sign-off** and multiply review cycles.",
    ),
    (
        "planvisualizer",
        "When explain plans are **wall-of-text**, developers guess at indexes and ship **collscans** under feature pressure. Non-competitive tuning is **whack-a-mole** in prod.",
        "Cost shows as **latency regressions**, oversized clusters, and frustrated teams that won’t touch queries. Knowledge stays siloed with **senior engineers** instead of spreading as a habit.",
    ),
    (
        "qdrant",
        "Specialist vector stores shine until **data gravity** pulls you into sync jobs, duplicate access policies, and **two on-call domains**. Non-competitive is choosing tech without **workflow ownership**.",
        "Inaction on consolidation leaks **time-to-ship** on every feature touching metadata + vectors. Security reviews duplicate; **cost forecasting** splits across products. You may overpay for separation you don’t strategically need.",
    ),
    (
        "readme",
        "A README nobody maintains becomes **misdirection**. Non-competitive onboarding is Slack archaeology instead of **clear scope and usage norms**.",
        "Contributors hesitate; **external sharing** stalls on uncertainty. The library’s value compounds only when **navigation and trust** are explicit—otherwise it’s another static site.",
    ),
    (
        "security",
        "Checklist security without **threat modeling** buys tools but not outcomes—misconfigured networks, over-privileged users, and **audit theater**. Non-competitive is “we enabled the toggle.”",
        "Cost of inaction is **breach risk, failed assessments, and delayed launches** while exceptions pile up. Customers ask hard questions you can’t answer crisply; **renewals soften** when trust wavers.",
    ),
    (
        "speciality",
        "Best-of-breed search + vector stacks often mean **five vendors and four sync paths**—each with its own failure domain. Non-competitive is optimizing components while **system reliability degrades**.",
        "You hemorrhage **engineering time** on glue, spend multiples on **egress and ops**, and struggle to enforce **consistent governance**. Strategic agility drops because every feature crosses **too many boundaries**.",
    ),
    (
        "timeseries",
        "General collections for **high-cardinality telemetry** explode storage and index cost; bolting on yet another TSDB duplicates pipelines. Non-competitive is **no deliberate time-series model**.",
        "Dashboards lag; **retention policies** become manual nightmares. Incidents lack **granular history** because hot paths weren’t designed for ingest volume. You pay for **storage and compute** that a purpose-built pattern would trim.",
    ),
    (
        "transactional_db",
        "Architecture debates without **workload-grounded criteria** devolve into tribal loyalties—Cockroach vs Dynamo vs Mongo vs Postgres as sports teams. Non-competitive is **comparison without your** latency, consistency, and ops reality.",
        "You pick defaults that **miss multi-region needs** or over-buy complexity. Migrations restart when **hidden requirements** surface late. Budget and morale suffer from **thrash**.",
    ),
    (
        "zoom-architecture",
        "Global real-time products copied from **diagrams without your constraints** still fail on **client behavior, data locality, and cost**. Non-competitive is pattern tourism without **translation to your SLOs**.",
        "Inaction leaves you **under-invested in resilience** until a regional outage teaches expensive lessons. You scale **complexity before clarity**, paying for **cross-region traffic and coordination** you might have designed differently with an explicit trade study.",
    ),
]

INSIGHTS = {slug: {"why": w, "cost": c} for slug, w, c in TOPICS}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | MongoDB Unpacked</title>
    <link rel="icon" type="image/png" href="{assets}mongodb-leaf.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #001E2B;
            --bg-secondary: #002838;
            --bg-card: #003345;
            --text-primary: #fafafa;
            --text-secondary: #b8d8e8;
            --text-muted: #7fa8bc;
            --accent: #00ED64;
            --accent-dim: #00c853;
            --border-subtle: rgba(255, 255, 255, 0.06);
            --warn-bg: rgba(248, 113, 113, 0.08);
            --warn-border: rgba(248, 113, 113, 0.35);
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html {{ scroll-behavior: smooth; }}
        body {{
            font-family: 'Inter', system-ui, sans-serif;
            background: var(--bg-primary);
            color: var(--text-secondary);
            min-height: 100vh;
            line-height: 1.7;
            -webkit-font-smoothing: antialiased;
        }}
        .top-bar {{
            position: sticky;
            top: 0;
            z-index: 50;
            background: rgba(0, 30, 43, 0.85);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border-subtle);
            padding: 0.75rem 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
        }}
        .top-bar a {{
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.875rem;
            font-weight: 500;
            transition: color 0.2s;
        }}
        .top-bar a:hover {{ color: var(--accent); }}
        .top-bar .sep {{ color: var(--text-muted); opacity: 0.35; }}
        .top-bar .doc-name {{
            color: var(--text-primary);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            font-weight: 500;
        }}
        .content {{
            max-width: 52rem;
            margin: 0 auto;
            padding: 2.5rem 1.5rem 5rem;
        }}
        .callout {{
            margin-bottom: 2rem;
            padding: 1rem 1.25rem;
            border-radius: 0.75rem;
            border: 1px solid var(--warn-border);
            background: var(--warn-bg);
        }}
        .callout h2 {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: #fca5a5;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }}
        .callout p {{
            color: var(--text-secondary);
            font-size: 0.9rem;
            line-height: 1.65;
        }}
        .markdown-body h1 {{
            font-size: 2rem;
            font-weight: 800;
            color: var(--text-primary);
            margin-bottom: 0.35rem;
            padding-bottom: 0.65rem;
            border-bottom: 2px solid var(--accent);
        }}
        .markdown-body h2 {{
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-top: 2rem;
            margin-bottom: 0.65rem;
        }}
        .markdown-body h2:first-of-type {{ margin-top: 0.5rem; }}
        .markdown-body p {{
            margin-bottom: 1rem;
            color: var(--text-secondary);
        }}
        .markdown-body strong {{ color: var(--text-primary); font-weight: 600; }}
        .markdown-body ol {{
            margin: 0 0 1.25rem 1.25rem;
            padding-left: 0.5rem;
        }}
        .markdown-body li {{
            margin-bottom: 0.5rem;
            color: var(--text-secondary);
        }}
        .markdown-body hr {{
            border: none;
            border-top: 1px solid var(--border-subtle);
            margin: 2rem 0;
        }}
        .markdown-body a {{ color: var(--accent); }}
    </style>
</head>
<body>
    <div class="top-bar">
        <a href="{home_href}">MongoDB Unpacked</a>
        <span class="sep">/</span>
        <a href="{companion_href}">Interactive companion</a>
        <span class="sep">/</span>
        <span class="doc-name">{md_name}</span>
    </div>
    <div class="content">
        <div class="callout">
            <h2>Why this matters</h2>
            <p>Non-competitive paths—staying on ad hoc tools, fragmented stacks, or “we’ll fix it later” designs—compound as <strong>rework, incidents, and stalled decisions</strong>. The sections below name how status-quo choices fail and what delay actually costs.</p>
        </div>
        <article class="markdown-body">
{body_html}
        </article>
    </div>
</body>
</html>
"""


def companion_and_assets(slug: str) -> tuple[str, str, str]:
    """Return (companion_href, assets_prefix, home_href) for HTML links."""
    if "/" in slug:
        return f"{slug.split('/')[-1]}.html", "../assets/", "../home.html"
    return f"{slug}.html", "assets/", "home.html"


def insert_insights(md_text: str, why: str, cost: str) -> str:
    if MARKER in md_text:
        return md_text
    if QUESTION_HEADER not in md_text:
        raise ValueError("Expected question header in markdown")
    block = (
        f"{MARKER}\n\n{why}\n\n## Cost of inaction\n\n{cost}\n\n"
    )
    return md_text.replace(
        QUESTION_HEADER,
        block + QUESTION_HEADER,
        1,
    )


def title_from_md(md: str) -> str:
    m = re.match(r"^#\s+(.+)$", md, re.MULTILINE)
    return m.group(1).strip() if m else "Discovery"


def main() -> int:
    root = ROOT
    missing = []
    for slug, why, cost in TOPICS:
        if slug not in INSIGHTS:
            missing.append(slug)
    if missing:
        print("Missing insights:", missing, file=sys.stderr)
        return 1

    discovered = list(root.rglob("*.discovery.md"))
    by_slug: dict[str, Path] = {}
    for p in discovered:
        rel = p.relative_to(root)
        key = str(rel).removesuffix(".discovery.md").replace("\\", "/")
        by_slug[key] = p

    for slug in INSIGHTS:
        if slug not in by_slug:
            print(f"WARN: no file for slug {slug}", file=sys.stderr)

    md_ext = markdown.Markdown(extensions=["extra", "sane_lists"])

    for slug, path in sorted(by_slug.items(), key=lambda x: x[0]):
        data = INSIGHTS.get(slug)
        if not data:
            print(f"SKIP (no insights): {path}", file=sys.stderr)
            continue
        text = path.read_text(encoding="utf-8")
        updated = insert_insights(text, data["why"], data["cost"])
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            print("updated MD", path.relative_to(root))

        md_ext.reset()
        body_html = md_ext.convert(updated)
        title = title_from_md(updated)
        companion_href, assets_prefix, home_href = companion_and_assets(slug)
        # e.g. agenticmemory.discovery.md → agenticmemory.discovery.html
        out = path.parent / f"{path.stem}.html"

        html = HTML_TEMPLATE.format(
            title=title.replace("&", "&amp;").replace("<", "&lt;"),
            assets=assets_prefix,
            companion_href=companion_href,
            home_href=home_href,
            md_name=path.name,
            body_html=body_html,
        )
        out.write_text(html, encoding="utf-8")
        print("wrote HTML", out.relative_to(root))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
