# Discovery: MongoDB plan visualizer

**Companion:** `planvisualizer.html`

## Opening minute (discovery call)

Thanks—if you’re tuning MongoDB, the **plan** is the truth: which indexes win, where sorts hurt, and what the database actually does. This is about making explain output **legible** so developers stop guessing. Is your pain mostly **slow finds**, **aggregations**, or **unstable plans after data growth**?

## Why current approaches fall short (without a competitive move)

When explain plans are **wall-of-text**, developers guess at indexes and ship **collscans** under feature pressure. Non-competitive tuning is **whack-a-mole** in prod.

## Cost of inaction

Cost shows as **latency regressions**, oversized clusters, and frustrated teams that won’t touch queries. Knowledge stays siloed with **senior engineers** instead of spreading as a habit.

## Ten open-ended questions (pain points & buying process)

1. Which queries are on your “most wanted” list for optimization, and who feels the pain?
2. How do developers learn indexing today—pairing with DBAs, docs, trial and error?
3. What’s your process when a deploy regresses performance—rollback, hotfix, or flag?
4. Who approves index builds in production—change windows, risk reviews?
5. How do you balance index count vs write amplification as schemas evolve?
6. Are you trying to reduce MongoDB spend by tuning rather than scaling hardware?
7. What tooling budget exists for observability and query analysis?
8. What training would make your squads self-sufficient at reading plans?
9. What SLAs tie directly to specific queries—checkout, search, dashboards?
10. What would “we trust our query reviews” look like as a team habit?
