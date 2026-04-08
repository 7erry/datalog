# Discovery: MongoDB Atlas at scale — runbook

**Companion:** `mongoatscale.html`

## Opening minute (discovery call)

Good to meet. “At scale” usually means **a mix of performance, cost discipline, and operational readiness**—not one knob. This runbook style is meant to turn patterns into **checklists your team can run**. What’s the symptom driving this—**latency**, **cost**, **incident frequency**, or **prep for a major event**?

## Why current approaches fall short (without a competitive move)

At-scale runbooks don’t appear by accident; without them, teams **react to metrics** instead of preventing drift. Non-competitive scale means **heroic individuals** holding production together.

## Cost of inaction

Incidents, **unplanned spend**, and launch slips become normal. Leaders hear “we need more hardware” without a **prioritized reliability roadmap**. Talent attrition rises when **on-call is chaos**.

## Ten open-ended questions (pain points & buying process)

1. What metrics tell you MongoDB is “at scale” for your org—QPS, data size, shard count, monthly spend?
2. Where do you feel the system creaking—hot shards, disk IO, connection storms, query patterns?
3. How do you balance reliability investments vs feature delivery when both compete for the same engineers?
4. Who approves spend changes—reserved instances, tier bumps, consulting engagements?
5. What events are you preparing for—product launch, seasonal traffic, M&A data integration?
6. How mature are your runbooks and on-call playbooks for MongoDB-specific failure modes?
7. What would a third-party or partner need to prove before you’d trust their recommendations?
8. How do you prioritize technical debt discovered during reviews?
9. What internal scorecards does leadership use to judge platform health?
10. What does success look like ninety days after implementing runbook improvements?
