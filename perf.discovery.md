# Discovery: Interactive benchmark performance analysis

**Companion:** `perf.html`

## Opening minute (discovery call)

Good to meet. Benchmarks are only useful when we agree on **workload shape**—this is about interpreting results, not worshipping a bar chart. I’ll connect metrics to **what your users feel** and what your **infra bill** becomes. What workload are you trying to model—**read-heavy**, **write-heavy**, or **mixed transactional**?

## Why current approaches fall short (without a competitive move)

Benchmarks disconnected from **production query shapes** mislead procurement and architecture. Non-competitive is **hero charts** that ignore tail latency, write amplification, and **realistic concurrency**.

## Cost of inaction

You buy wrong tiers, pick wrong designs, and **reopen decisions** after go-live pain. Teams lose trust in data-driven narratives; **politics fills the void**. Money flows to hardware instead of **fixable patterns**.

## Ten open-ended questions (pain points & buying process)

1. What production profile are you trying to approximate—document size, indexes, concurrency, geographic spread?
2. Who will interpret benchmark results for leadership—engineering only, or also finance and procurement?
3. What decisions hinge on the numbers—vendor pick, instance sizing, contract negotiation?
4. How do you guard against benchmarks that optimize for demos but mislead on real queries?
5. What SLAs or SLOs are you held to externally—latency percentiles, error rates?
6. Have past benchmarks steered you wrong, and what lesson did you take from that?
7. What buying process uses performance proof—formal bake-off, internal architecture review?
8. Who can challenge methodology—DBA, SRE, vendor—and how do you resolve disputes?
9. What timeline do you have to reach a performance-confident decision?
10. What would you need to reproduce these tests internally without vendor help?
