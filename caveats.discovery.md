# Discovery: Scale caveats — vector / Qdrant angles

**Companion:** `caveats.html`

## Opening minute (discovery call)

Thanks for the time. This one is intentionally a **“what actually matters at scale”** lens—not marketing checklists. If you’re comparing **vector engines**, the winning story on a slide often breaks when you look at **memory, indexing, filtering under load, and ops**. I’ll walk through the caveats teams wish they’d known earlier. Are you benchmarking for **a fixed corpus** or **high-churn, high-write** workloads?

## Why current approaches fall short (without a competitive move)

Ignoring scale caveats, teams accept **vendor fairy tales** tuned to toy datasets. Filtering + high churn + hybrid queries expose **memory cliffs and tail latency** that averages hide. Non-competitive here is **benchmark theater** instead of workload-faithful testing.

## Cost of inaction

Cost of inaction is **production surprises after commit**: re-index storms, recall collapses, and re-architecture under deadline. Finance sees **unplanned spend**; product sees **rolled-back features**. You lose credibility with leadership when the POC hero metrics don’t survive **real metadata and write rates**.

## Ten open-ended questions (pain points & buying process)

1. What workload are you modeling for benchmarks, and how representative is it of production?
2. Where have past vector or search projects failed—ops burden, cost at scale, or relevance under load?
3. How sensitive are you to tail latency vs average latency for your use case?
4. What filtering and metadata constraints does your app impose on vector queries?
5. Who will own on-call for the vector tier, and what skill level do they have today?
6. How do you decide between “good enough” relevance and perfect relevance when budgets differ?
7. What procurement steps apply to new infrastructure—security review, legal, vendor onboarding?
8. Are you comparing against an incumbent, and what would it take to displace it politically?
9. What timeline do you have for a decision, and what happens if you delay?
10. What evidence would make your leadership trust a smaller, simpler stack over a best-of-breed specialist?
