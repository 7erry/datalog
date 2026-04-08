# Discovery: Elasticsearch vs MongoDB search

**Companion:** `elastic_mongo.html`

## Opening minute (discovery call)

Appreciate the time. This is a **search consolidation** conversation: Elasticsearch is powerful, but many teams are paying for **sync complexity, dual stacks, and operational overhead**. I’ll compare honestly—where Atlas Search is strong, where you’d still pair tools, and how to think about **migration risk**. Are you trying to **replace Elasticsearch**, or **narrow what it has to do**?

## Why current approaches fall short (without a competitive move)

Dual-stack Elasticsearch + document DB is powerful until **sync becomes the product**: mapping drift, reindex pain, and two on-call domains. Non-competitive is accepting **operational coupling** without measuring toil or failure blast radius.

## Cost of inaction

Cost of inaction is **headcount and incident load** maintaining pipelines that could narrow. TCO debates ignore **engineering time** until hiring can’t keep up. Search relevance work fragments across teams with **different tooling and standards**.

## Ten open-ended questions (pain points & buying process)

1. What search and analytics workloads run on Elasticsearch today, and which are business-critical?
2. Where does the Elasticsearch stack hurt—cost, ops, mapping drift, or relevance tuning?
3. How do you keep MongoDB and search indices consistent, and what breaks when you don’t?
4. Who owns Elasticsearch operations, and is that skill depth a risk for the org?
5. What are your SLAs for search availability and query latency?
6. What migration risks worry you most—relevance parity, query language, or ingest pipelines?
7. How do you evaluate TCO—including people time, not just license and nodes?
8. What procurement relationship do you have with Elastic or cloud marketplace equivalents?
9. Who would need to approve a consolidation plan—search team, data platform, finance?
10. What would a phased approach look like that de-risks cutover?
