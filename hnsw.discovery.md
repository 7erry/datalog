# Discovery: HNSW visualizer

**Companion:** `hnsw.html`

## Opening minute (discovery call)

Appreciate you joining. If vectors are new to your team, **HNSW** is the algorithm behind a lot of fast approximate search—this is about **building intuition**, not proving math. I want you to leave understanding **accuracy vs speed tradeoffs** and why tuning matters. Is this for **education**, or are you **choosing an index strategy** for production?

## Why current approaches fall short (without a competitive move)

Treating vector indexes as magic black boxes leads to **mystery latency** and tuning by rumor. Non-competitive is skipping intuition on **accuracy vs speed** tradeoffs until production users feel it.

## Cost of inaction

You pick parameters that **don’t match recall needs**, overspend on hardware, or oscillate between “too slow” and “wrong answers.” ML and platform teams argue without **shared vocabulary**, delaying releases.

## Ten open-ended questions (pain points & buying process)

1. What decisions are you trying to make after understanding HNSW—index params, hardware sizing, vendor choice?
2. How does your team learn new retrieval tech today—courses, vendors, hiring?
3. What quality bar must vector search meet before you ship to users?
4. Who will tune and monitor indexes in production, and what tooling do they expect?
5. What risks worry you about approximate search—wrong results, drift, adversarial queries?
6. How do you connect educational assets to your internal standards and review gates?
7. Is there budget for experimentation—load testing, labeling, human eval?
8. What stakeholders need a non-mathematical explanation before they approve vector search?
9. How does this initiative tie to a broader AI or search roadmap?
10. What would “we’re confident in our index strategy” look like as an exit criterion?
