# Discovery: Database architecture showdown

**Companion:** `transactional_db.html`

## Opening minute (discovery call)

Thanks—this is a **competitive architecture** pass across several transactional stores, always anchored back to MongoDB’s trade space. It’s useful when your team is comparing **Cockroach, Scylla, Postgres/EDB, Dynamo**, and wants arguments that aren’t Twitter threads. Which competitor is **actually on the table** for your next decision?

## Why current approaches fall short (without a competitive move)

Architecture debates without **workload-grounded criteria** devolve into tribal loyalties—Cockroach vs Dynamo vs Mongo vs Postgres as sports teams. Non-competitive is **comparison without your** latency, consistency, and ops reality.

## Cost of inaction

You pick defaults that **miss multi-region needs** or over-buy complexity. Migrations restart when **hidden requirements** surface late. Budget and morale suffer from **thrash**.

## Ten open-ended questions (pain points & buying process)

1. What problem statement kicked off the comparison—scale, cost, multi-region, developer velocity?
2. Which alternatives are politically acceptable internally, and which are non-starters?
3. How do you weight consistency models vs operational simplicity vs cloud affinity?
4. What workloads must be represented in any comparison—transactions, analytics, search, batch?
5. Who runs the evaluation—architecture council, platform team, individual product—and how do you avoid bias?
6. What artifacts do executives need—TCO, risk register, timeline—before funding a migration?
7. How does procurement influence the short list—existing discounts, strategic vendor relationships?
8. What timeline is driving the decision, and what happens if you defer?
9. Who has veto power based on skills, risk appetite, or sunk cost?
10. What would a credible “we chose MongoDB” narrative need to include for your culture?
