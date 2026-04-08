# Discovery: Aggregation pipeline visualizer

**Companion:** `aggregations.html`

## Opening minute (discovery call)

Good to connect. Today is really about **how your team reasons about data transformations**—the aggregation pipeline is where MongoDB shines for analytics-style workloads without shipping everything to another system. This walkthrough is visual on purpose: most pain shows up when pipelines get long, opaque, and hard to review. I want to make **stages, costs, and outcomes** feel tangible. To aim this usefully: are you mostly fighting **slow dashboards**, **ETL-style pipelines**, or **ad hoc analyst queries**?

## Why current approaches fall short (without a competitive move)

Without a shared discipline, pipelines grow as **copy-paste stages** in code and one-off jobs nobody profiles. The “solution” becomes exporting everything to a warehouse or lake—**higher latency, more sync failure modes**, and two places to secure. Reviews rarely connect **stage cost** to user-visible SLAs, so regressions ship quietly.

## Cost of inaction

Cost of inaction is **surprise Atlas bills**, brittle dashboards, and analytics debt that blocks product bets. Incidents trace back to “**someone changed a $match**” with no explain plan culture. You pay twice: engineering time firefighting and **duplicate pipelines** that diverge from operational truth.

## Ten open-ended questions (pain points & buying process)

1. Describe the slowest or most fragile aggregation you run today—what does it do, and who depends on it?
2. How do developers today discover whether a pipeline is “expensive”—profiling, explain plans, or mainly production incidents?
3. What’s your review process for pipeline changes before they hit production, and where do bottlenecks appear?
4. Are you trying to keep analytics on MongoDB, or is there pressure to move everything to a warehouse or lakehouse?
5. What service-level expectations do stakeholders have for dashboard refresh and ad hoc queries?
6. Who funds tooling and training for pipeline work—central platform, individual product teams, or data engineering?
7. What would trigger a formal evaluation of MongoDB vs another store for these workloads?
8. How do you prioritize fixes when product wants new metrics but ops is seeing rising load?
9. What does procurement look like for database capacity or adjacent BI tools—annual cycle, on-demand, or project-based?
10. If you could change one thing about how your org builds aggregations, what would it be?
