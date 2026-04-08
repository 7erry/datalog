# Discovery: MongoDB time series collections

**Companion:** `timeseries.html`

## Opening minute (discovery call)

Good to meet—**time series** workloads have their own physics: ingestion rate, retention, downsampling, and query patterns. MongoDB time series collections are aimed at **keeping hot data efficient** without bolting on a separate TSDB for every use case. What domain is this—**metrics**, **IoT**, **financial ticks**, or something else?

## Why current approaches fall short (without a competitive move)

General collections for **high-cardinality telemetry** explode storage and index cost; bolting on yet another TSDB duplicates pipelines. Non-competitive is **no deliberate time-series model**.

## Cost of inaction

Dashboards lag; **retention policies** become manual nightmares. Incidents lack **granular history** because hot paths weren’t designed for ingest volume. You pay for **storage and compute** that a purpose-built pattern would trim.

## Ten open-ended questions (pain points & buying process)

1. What volume and cardinality are you ingesting—points per second, unique series, retention horizons?
2. Where does your current TS stack hurt—cost, query latency, ops, or modeling rigidity?
3. Who queries the data—humans, dashboards, ML pipelines—and what latency do they need?
4. How do you handle late-arriving data, backfills, and corrections?
5. What compliance requirements apply to telemetry—PII, retention, access logging?
6. Are you trying to retire a dedicated TSDB, or coexist during a transition?
7. Who owns the budget line for metrics storage—platform, SRE, product?
8. What proof would you need to trust MongoDB for your hottest telemetry path?
9. What buying process applies if this expands Atlas footprint significantly?
10. What would a migration cutover look like without blinding your operators?
