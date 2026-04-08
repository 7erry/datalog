# Discovery: PostgreSQL vs MongoDB transactions (infographic)

**Companion:** `pgmdb.html`

## Opening minute (discovery call)

Good to meet—this one zooms in on **transactions**: what guarantees mean in practice, how failures surface, and how app patterns differ. Useful when your architects want a **shared mental model** without a week of reading. Are you deciding **greenfield**, or **defending a Mongo choice** to a Postgres-centric org?

## Why current approaches fall short (without a competitive move)

Transaction semantics misunderstood across teams cause **subtle bugs**—retries, isolation surprises, and “it worked in dev.” Non-competitive is **assumption mismatch** between app authors and DBAs.

## Cost of inaction

You ship defects that look like app logic but are **concurrency stories**; incidents erode trust in the datastore choice. Education gaps slow **architecture sign-off** and multiply review cycles.

## Ten open-ended questions (pain points & buying process)

1. What transactional scenarios matter most—multi-document ACID, idempotent workflows, sagas?
2. Where has confusion about isolation or retries caused bugs or outages?
3. Who needs to align on semantics—backend, mobile, payments, data engineering?
4. What proof would satisfy a skeptical architect—docs, tests, failure injection?
5. Are standards bodies or internal architecture councils dictating a preferred database?
6. How do you educate teams at scale—guilds, linters, code review checklists?
7. What procurement or vendor relationships bias the technical default?
8. What incidents in memory involved “we thought transactions worked like X”?
9. What’s the decision deadline—platform mandate, migration wave, audit?
10. What would shared vocabulary buy you in terms of faster delivery or fewer defects?
