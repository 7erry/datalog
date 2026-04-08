# Discovery: Atlas vs Cosmos DB vs DocumentDB

**Companion:** `cosmosdb_documentdb.html`

## Opening minute (discovery call)

Good to connect—this is the **“imitation game”** conversation: document APIs that look familiar but differ in **consistency, operations, and what you’re actually buying**. I’ll keep it practical: migration friction, pricing dynamics, and where teams get surprised after the POC. What prompted the eval—**Azure affinity**, **DocumentDB in the path**, or **MongoDB compatibility** as a requirement?

## Why current approaches fall short (without a competitive move)

Teams stay on **compatibility surfaces** that behave subtly differently—**RU math surprises**, unexpected limits, and operational models that don’t match how MongoDB drivers and tools were built. Non-competitive is tolerating **ongoing translation tax** between docs, support, and reality.

## Cost of inaction

Cost is **slower delivery** (workarounds in app code), **higher true TCO** once throughput grows, and **migration fear** that hardens into permanent friction. Strategic bets wait because nobody wants to replatform—while competitors ship on **predictable semantics** and richer ecosystem support.

## Ten open-ended questions (pain points & buying process)

1. What workload are you running today—read/write mix, transactions, aggregations—and on which API or service?
2. Where has compatibility or behavior differed from what your developers expected?
3. What operational tasks consume the most time—tuning RU/s, backups, networking, or upgrades?
4. How do costs trend as you grow—predictable, or full of surprises—and who gets the bill?
5. Who is championing stay-on-Azure vs best-fit database, and how is that tension managed?
6. What does a migration need to prove—functional parity, performance, cost, or risk reduction?
7. What security and compliance requirements constrain data location and encryption models?
8. What’s your decision timeline, and what milestones are tied to contracts or product launches?
9. Who has veto power—procurement, enterprise architecture, FinOps—and what do they need to see?
10. If you moved to Atlas, what would “success after six months” sound like in a retrospective?
