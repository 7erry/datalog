# Discovery: Oracle → MongoDB developer deep dive

**Companion:** `oracle_mongo.html`

## Opening minute (discovery call)

Thanks—this is a **relational-to-document** shift conversation, and the hard part is rarely syntax; it’s **transactions, reporting, stored procedures, and organizational habit**. I’ll focus on a sane migration path: what to modernize first, what to emulate temporarily, and how to **de-risk cutover**. What Oracle footprint are we talking about—**OLTP apps**, **batch/reporting**, or **mixed**?

## Why current approaches fall short (without a competitive move)

Staying on Oracle for familiarity avoids **rethinking workflows**—but licensing and agility penalties compound. Non-competitive is incremental SQL tweaks when the domain is **document-shaped** or change-heavy.

## Cost of inaction

Cost of inaction is **renewal leverage against you**, slower feature delivery, and talent scarcity. Migrations deferred become **bigger-bang risk** with more integrations and reporting entanglements.

## Ten open-ended questions (pain points & buying process)

1. Which Oracle workloads hurt most—licensing cost, agility, scale limits, or staffing?
2. What app patterns are deeply Oracle-specific—PL/SQL, triggers, complex joins, batch jobs?
3. Who depends on existing reports and BI flows, and how fixed are those contracts?
4. How do you stage migration—strangler, big bang, dual-write—and what’s your bias?
5. What skills does your team have today—Oracle DBAs, Java/.NET, cloud-native—and where are the gaps?
6. Who sponsors the business case—IT savings, speed to market, risk reduction?
7. What procurement dynamics affect Oracle renewals vs MongoDB adoption timing?
8. What validation will finance or audit require before decommissioning Oracle for a domain?
9. Who could block progress—data owners, app owners, integration partners?
10. What does a twelve-month roadmap look like if leadership says “go”?
