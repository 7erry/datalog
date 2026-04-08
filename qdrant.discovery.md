# Discovery: Atlas Search vs Qdrant

**Companion:** `qdrant.html`

## Opening minute (discovery call)

Appreciate the time—**Qdrant** is a strong specialized vector store; the strategic question is whether you need that separation or you can meet SLAs **inside Atlas**. I’ll compare on **ops, filtering, hybrid workflows, and how your app already stores data**. Is your vector workload **pure similarity**, or **heavy metadata filtering + hybrid search**?

## Why current approaches fall short (without a competitive move)

Specialist vector stores shine until **data gravity** pulls you into sync jobs, duplicate access policies, and **two on-call domains**. Non-competitive is choosing tech without **workflow ownership**.

## Cost of inaction

Inaction on consolidation leaks **time-to-ship** on every feature touching metadata + vectors. Security reviews duplicate; **cost forecasting** splits across products. You may overpay for separation you don’t strategically need.

## Ten open-ended questions (pain points & buying process)

1. What retrieval patterns dominate—pure kNN, filtered search, hybrid text+vector?
2. Where does Qdrant shine for you today, and where does it create drag?
3. How many services must stay in sync if vectors live outside the primary database?
4. Who operates the vector tier on-call, and what headcount is allocated?
5. What latency and recall targets does product expect under peak load?
6. How do you evaluate cost—infra, egress, engineering time, vendor support?
7. What security requirements apply to vector payloads and audit logs?
8. Who decides build vs buy for AI infrastructure—platform, ML team, CTO office?
9. What timeline are you on—experiment, pilot, production hardening?
10. What would consolidation need to prove before you’d retire a specialized store?
