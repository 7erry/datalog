# Discovery: MongoDB multi-tenancy strategies

**Companion:** `multitenancy.html`

## Opening minute (discovery call)

Appreciate you joining. Multi-tenancy is one of those topics that sounds solved until you hit **noisy neighbors, billing fairness, and blast radius**. I’ll walk through common patterns—**database-per-tenant, collection-per-tenant, shared collections**—and what breaks first at scale. Are you **B2B SaaS**, **internal platforms**, or something else?

## Why current approaches fall short (without a competitive move)

Ad hoc tenancy—**shared everything** until a big customer screams—creates **noisy neighbors and audit anxiety**. Non-competitive design postpones isolation decisions until contracts force them.

## Cost of inaction

Cost is **re-architecture under renewal pressure**, unfair cost allocation across BUs, and **security reviews** that fail on paper. Sales deals stall on **data separation** promises engineering can’t cheaply fulfill.

## Ten open-ended questions (pain points & buying process)

1. How do you isolate tenants today—logically, physically, or both—and where have you been burned?
2. What does “fair” mean for noisy neighbors—throttling, dedicated resources, or premium tiers?
3. How do you bill or allocate cost back to tenants or business units?
4. What compliance or data residency rules force certain isolation patterns?
5. How do you onboard and offboard tenants without risking cross-tenant leaks?
6. Who owns the tenancy model—platform team, security, or individual product squads?
7. What scale are you planning for—tenant count, data per tenant, query mix?
8. What buying or contract terms differ between small tenants and strategic accounts?
9. What migration risk exists if you need to split a hot tenant out later?
10. What would your ideal governance model look like for schema and index changes across tenants?
