# Discovery: MongoDB migration toolkit comparison

**Companion:** `migrations.html`

## Opening minute (discovery call)

Appreciate the time—migrations are where projects live or die, and tool choice is only part of it. I’ll compare approaches on **fidelity, cutover risk, throughput, and validation**—what you can prove before you flip traffic. Are you coming from **relational**, another **document store**, or **a homegrown pipeline**?

## Why current approaches fall short (without a competitive move)

Tool shopping without a **cutover strategy** produces pretty spreadsheets and scary weekends. Non-competitive migrations skip **validation, rollback, and ownership**—then blame the tool.

## Cost of inaction

You risk **data divergence, extended dual-writes, and compliance gaps** during transition. Business loses confidence; engineering burns out on **manual reconciliation**. Late fixes cost more than **front-loading risk controls**.

## Ten open-ended questions (pain points & buying process)

1. What system are you leaving, and what’s the primary driver—cost, scale, developer experience, or sunset?
2. How much downtime or dual-write complexity can the business tolerate?
3. What validation strategy do you trust—row counts, checksums, shadow reads, business sign-off?
4. Who owns cutover planning—app team, DBA, vendor—and how do you govern go/no-go?
5. What regulatory or audit requirements apply to data movement and logging?
6. What tools have you already tried, and where did they fall short?
7. How do you fund migration work—dedicated project, incremental capacity, professional services?
8. What’s the drop-dead date, and what happens if you miss it?
9. Who could veto the approach after weeks of work—security, compliance, app owners?
10. What does “migration complete” mean—technical cutover, decommission, or cost savings realized?
