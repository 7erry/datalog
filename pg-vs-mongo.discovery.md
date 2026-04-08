# Discovery: Postgres and MongoDB at humongous scale

**Companion:** `pg-vs-mongo.html`

## Opening minute (discovery call)

Appreciate you joining. This is the honest **Postgres vs MongoDB at serious scale** conversation—join storms, MVCC behavior, connection economics, and when document modeling reduces pressure. I’m not here to declare a religion; I’m here to align on **where each engine earns its keep**. What failure mode are you seeing today—**latency tail**, **write bottlenecks**, or **operational complexity**?

## Why current approaches fall short (without a competitive move)

Postgres at huge scale without honest tradeoffs leads to **connection storms, MVCC pain, and ORM-generated join monsters**—then MongoDB is dismissed because “we’re a Postgres shop.” Non-competitive is **identity over fit**.

## Cost of inaction

Cost is **expensive vertical scaling**, specialized DBAs stretched thin, and features delayed by **schema migration fear**. Opportunity cost grows when document or scale-out models would **reduce blast radius** for specific workloads.

## Ten open-ended questions (pain points & buying process)

1. What workload traits push Postgres hardest for you—wide tables, heavy writes, connection churn, big JSON?
2. Where has scaling Postgres created organizational drag—specialists, tuning rituals, hardware spend?
3. Are you considering MongoDB for net-new workloads, migration, or hybrid coexistence?
4. Who advocates for Postgres vs document stores internally, and what evidence would shift the debate?
5. How do you handle reporting and analytics when OLTP is under stress?
6. What buying constraints apply—existing EA with a cloud vendor, enterprise Postgres support contracts?
7. What timeline and triggers would cause you to act—renewal, incident, new product bet?
8. Who signs off on polyglot persistence vs standardization mandates?
9. What risks worry you about splitting data across two operational systems?
10. What does a fair comparison look like in your environment—same team, same SLA, same data?
