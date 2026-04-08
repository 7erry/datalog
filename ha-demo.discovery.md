# Discovery: MongoDB high availability demo

**Companion:** `ha-demo.html`

## Opening minute (discovery call)

Thanks—this one is visceral: **what happens when nodes fail, regions misbehave, and clients keep writing**. HA isn’t a checkbox; it’s behavior under failure plus **your app’s retry and idempotency story**. I’ll walk through the mechanics in a way your **DBAs and app teams** can share vocabulary. Are you designing for **single-region HA**, or **real multi-region** expectations?

## Why current approaches fall short (without a competitive move)

HA slides without app behavior teach the wrong lesson: **failover mechanics** look fine while retries stampede or idempotency breaks. Non-competitive is infra confidence without **client and workflow design**.

## Cost of inaction

Inaction yields **false security**—drills pass until a real partial outage corrupts data or duplicates money movement. Customers experience **longer outages** than the database’s story promised. Postmortems blame “the driver” instead of **end-to-end contracts**.

## Ten open-ended questions (pain points & buying process)

1. Describe your last significant database-impacting incident—what failed and how users felt it.
2. What RPO/RTO targets do you advertise internally vs what you can actually demonstrate?
3. How do application retries and idempotency keys behave under partial failures today?
4. Who is accountable for failover drills—SRE, DBA, vendor—and how often do you run them?
5. What tradeoffs are you willing to make between cost and redundancy?
6. What compliance or contractual language references availability or disaster recovery?
7. Are you evaluating changes to topology soon—new regions, sharding, tier upgrades?
8. Who approves infrastructure spend tied to HA improvements?
9. What proof would leadership need before signing off on a multi-region design?
10. What worries you more—MongoDB’s mechanics, or application behavior under chaos?
