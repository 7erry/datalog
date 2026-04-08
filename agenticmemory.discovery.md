# Discovery: Agentic memory on MongoDB

**Companion:** `agenticmemory.html`

## Opening minute (discovery call)

Thanks for making time. I’m glad we’re digging into **agentic memory**—the layer that lets agents remember context, retrieve what matters, and stay coherent across sessions. A lot of teams are stuck between bolting on a vector DB and keeping operational data in one place; MongoDB is increasingly the place teams unify that story. In the next bit I’ll walk through how we think about **memory patterns**—short-term vs long-term, retrieval, and governance—so it’s not just “embeddings in a bucket.” Before I go deep: what’s driving this for you right now—**a specific agent product**, or **platform standards** your teams have to follow?

## Why current approaches fall short (without a competitive move)

The usual “non-competitive” pattern is **memory scattered** across caches, blob stores, ad hoc vector indexes, and application tables nobody owns end-to-end. Nothing enforces a consistent lifecycle for **PII, retention, or eval hooks**, so every agent feature becomes a custom integration. Teams optimize demos, not **governed retrieval**—and production surprises follow.

## Cost of inaction

Inaction compounds into **rework tax**: each new use case rebuilds the same plumbing while latency and quality drift under real traffic. You risk **trust incidents** (wrong recall, leaked context) and slower GTM because security and legal can’t sign off on a system that wasn’t designed as a platform. Budget leaks into **duplicate stores, ETL, and on-call** for glue that should be standardized.

## Ten open-ended questions (pain points & buying process)

1. Walk me through how an agent session works today—from first user message to what gets stored and what gets thrown away.
2. Where does memory break down for you: retrieval quality, latency, cost, privacy, or consistency across channels?
3. Who owns the memory layer today—application teams, a platform group, ML, or security—and where do decisions get stuck?
4. What would “bad memory” look like in production for your users or your brand, and have you seen early warning signs already?
5. How do you handle PII, retention, and the right to be forgotten when memory spans multiple systems?
6. What evaluation criteria will you use to decide this architecture is “good enough”—offline benchmarks, online metrics, or compliance gates?
7. What other vendors or internal platforms are in the evaluation set, and what would make MongoDB the default vs a specialist vector store?
8. Who has to sign off on a production design—security, legal, architecture review—and what artifacts do they expect to see?
9. What’s your target timeline from pilot to production, and what milestones are tied to budget or headcount?
10. If we solved memory perfectly, what downstream problem would still remain—observability, cost controls, or governance workflows?
