# Discovery: MongoDB Atlas advanced deployments

**Companion:** `atlas.html`

## Opening minute (discovery call)

Good to meet. When people say “we’re on Atlas,” the next question is almost always **how**—regions, tiers, networking, backup, and how you’ll grow without a forklift. This session is meant to translate **advanced deployment patterns** into decisions you can defend with security and finance. I’ll connect the knobs to outcomes: availability, blast radius, and operational load. What’s the trigger for this review—**a launch**, **compliance**, or **cost and scale pressure**?

## Why current approaches fall short (without a competitive move)

“We’re on Atlas” without an **advanced deployment design** usually means defaults that were fine at MVP: single region assumptions, loose network boundaries, backup policies nobody tests, and **tier upgrades as panic therapy**. Non-competitive isn’t laziness—it’s **no explicit trade space** between blast radius, cost, and agility.

## Cost of inaction

The bill and the incident queue rise together: **noisy neighbors inside the org**, slow failovers, and audits that surface missing evidence. Launches slip because **change windows** become mandatory once risk is discovered late. You pay for **emergency scaling and consulting** that planning would have avoided.

## Ten open-ended questions (pain points & buying process)

1. How is Atlas deployed today—regions, cluster tiers, peering/VPC—and what worries you about that layout?
2. What availability story are you accountable for internally—RPO/RTO, multi-region, maintenance windows?
3. Where have you felt pain: cost surprises, slow queries, backup/restore drills, or change management?
4. Who approves architecture changes—enterprise architecture, security, FinOps—and what do they ask for?
5. How do you handle non-prod environments relative to prod—parity, cost caps, or separate contracts?
6. Is Atlas part of a broader MongoDB or cloud negotiation, and when does that renew?
7. What would trigger a competitive evaluation or a “should we stay” review?
8. How do you fund growth—reserved capacity, autoscaling, or manual upgrades per app?
9. What documentation or runbooks do auditors or SRE expect you to produce?
10. If you could redesign the deployment from scratch with no legacy constraints, what would you change first?
