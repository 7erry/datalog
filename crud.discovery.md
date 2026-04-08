# Discovery: MongoDB CRUD operations guide

**Companion:** `crud.html`

## Opening minute (discovery call)

Thanks for making time. Sometimes CRUD sounds basic, but it’s where **data modeling, indexing, and application patterns** either stay healthy or quietly rot. I want to align on how your team does **inserts, updates, deletes, and reads** at scale—especially idempotency, schema flexibility, and performance pitfalls. Are we talking **greenfield API design**, or **tuning an app that’s already loud in production**?

## Why current approaches fall short (without a competitive move)

When CRUD is “obvious,” teams skip **schema discipline, index strategy, and idempotency**—then blame the database. Non-competitive patterns include unbounded documents, **silent partial updates**, and deletes that orphan related data. Reviews focus on features, not **data shape**.

## Cost of inaction

You get **incident debt**: duplicate keys, hot shards, and migrations that freeze releases. Customer-visible symptoms—timeouts, inconsistent reads—trigger **expensive war rooms**. Paying down the model later costs more than shaping it early, especially under **compliance or multi-team** ownership.

## Ten open-ended questions (pain points & buying process)

1. Walk me through your hottest read and write paths—what documents look like and who owns the schema.
2. Where do you see contention—locks, retries, duplicate keys, or unbounded growth in documents?
3. How do you handle schema evolution across services that share the same database?
4. What’s your testing story for data migrations and backward compatibility?
5. Who is accountable when queries regress—app teams, DBAs, or a platform group?
6. Are you standardizing on MongoDB org-wide, or is this team still proving the model?
7. What training or guardrails do developers need before you’d trust broad CRUD changes?
8. How does buying work for support tiers, consulting, or Atlas features tied to reliability?
9. What incidents in the past year traced back to “simple” CRUD assumptions?
10. What would a healthy CRUD baseline look like for your team—linting, reviews, or automated checks?
