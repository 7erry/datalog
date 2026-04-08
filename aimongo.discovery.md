# Discovery: Architecting intelligence — Atlas Vector Search

**Companion:** `aimongo.html`

## Opening minute (discovery call)

Appreciate you carving this out. We’re here because **vector search** stopped being a science experiment—it’s part of how products ship search, recommendations, and RAG. The real design question is whether you want **another specialized stack** or a path where vectors live next to the documents and metadata you already trust. I’ll keep this grounded in **architecture choices**: indexing, hybrid search, latency, and who operates it. What’s your north star—**time to first good retrieval**, or **long-term TCO and fewer moving parts**?

## Why current approaches fall short (without a competitive move)

Teams avoiding a deliberate vector strategy default to **yet another database** plus nightly sync jobs and fuzzy ownership. Hybrid search (text + vector + metadata filters) gets bolted on inconsistently, so relevance tuning lives in **notebooks, not production**. Non-competitive here means **integration spaghetti**, not “we picked the wrong algorithm once.”

## Cost of inaction

You stall on **time-to-production** while competitors ship retrieval that matches their domain. TCO climbs from **egress, duplicated data, and specialist headcount**; security reviews multiply because vectors and source documents live in different trust boundaries. The org learns the same HNSW lesson **six times** across squads.

## Ten open-ended questions (pain points & buying process)

1. What user-facing workflows require vectors today, and what’s on the roadmap for the next two quarters?
2. Where are you feeling friction—index build times, relevance, hybrid ranking, filtering, or operational runbooks?
3. How many systems currently touch “search + vectors,” and who keeps them in sync?
4. What latency and availability targets do product and SRE agree on for retrieval paths?
5. How do you measure quality today—human eval, click metrics, offline recall tests—and who owns that loop?
6. What security or data-residency constraints apply to embeddings and source documents?
7. Who are the economic buyers vs technical champions, and what would they need to see to expand usage?
8. Is this purchase tied to a broader cloud or data platform renewal, or a standalone initiative?
9. What does your pilot-to-production path look like—who gates go-live?
10. What would make you say “we’re glad we didn’t add another specialized database” six months from now?
