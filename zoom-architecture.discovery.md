# Discovery: MongoDB — Zoom reference architecture

**Companion:** `zoom-architecture.html`

## Opening minute (discovery call)

Appreciate the time—this is a **real-world scale pattern** conversation modeled after how demanding collaboration platforms think about **global distribution, resilience, and data locality**. We’ll use it to translate **architecture diagrams** into questions you can ask about your own system. Are you chasing **multi-region active-active**, or **strong consistency with DR**?

## Why current approaches fall short (without a competitive move)

Global real-time products copied from **diagrams without your constraints** still fail on **client behavior, data locality, and cost**. Non-competitive is pattern tourism without **translation to your SLOs**.

## Cost of inaction

Inaction leaves you **under-invested in resilience** until a regional outage teaches expensive lessons. You scale **complexity before clarity**, paying for **cross-region traffic and coordination** you might have designed differently with an explicit trade study.

## Ten open-ended questions (pain points & buying process)

1. What user journeys are most sensitive to latency and partition behavior in your product?
2. How do you think about data locality—regulations, performance, or cost?
3. What’s your current multi-region story—active-active, primary/DR, messy in-between?
4. Where have you felt pain—failovers, split-brain fears, replication lag, client behavior?
5. Who owns global architecture decisions—platform, SRE, product—and how do trade-offs get negotiated?
6. What incidents changed how you think about resilience and investment?
7. What spend guardrails exist for multi-region redundancy and cross-region traffic?
8. What compliance or sovereignty constraints dictate region topology?
9. What buying or staffing decisions would this architecture review unlock or block?
10. What would you borrow from a Zoom-scale pattern vs explicitly reject for your scale?
