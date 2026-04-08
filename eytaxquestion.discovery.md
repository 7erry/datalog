# Discovery: SQL blobs vs MongoDB — tax questionnaires

**Companion:** `eytaxquestion.html`

## Opening minute (discovery call)

Good to meet. The heart of this is **questionnaire and form data** that doesn’t fit cleanly into rectangular SQL without awkward JSON blobs and painful evolution. MongoDB’s document model tends to win when **schema changes often** and you need **nested, versioned answers** without migrations every sprint. Is the pain mostly **developer velocity**, **reporting**, or **compliance and audit**?

## Why current approaches fall short (without a competitive move)

Relational models force **JSON blobs, sparse columns, or EAV** that fight evolving questionnaires. Non-competitive is “we’ll migrate later” while every season adds **DDL stress and brittle reports**.

## Cost of inaction

You ship late on regulatory or client changes; analytics teams spend sprints **unpicking blobs**. Audit risk rises when **lineage and validation** are manual. Technical debt becomes a **business constraint** on entering new markets or segments.

## Ten open-ended questions (pain points & buying process)

1. How do questionnaires vary across jurisdictions, clients, or years—and who owns those changes?
2. What happens today when the business asks for a new question mid-season?
3. How do you report and reconcile answers for auditors or regulators?
4. Where do developers spend time fighting the relational model for this domain?
5. What systems consume this data downstream—warehouses, PDFs, case management?
6. Who would sponsor a move or dual-write strategy—business, engineering, or risk?
7. What migration constraints exist—freeze windows, legacy apps, batch jobs?
8. How do you handle PII, encryption, and retention for questionnaire payloads?
9. What does procurement prefer for new database capacity—capital project or OpEx?
10. What would “safe evolution” look like if schemas changed monthly instead of annually?
