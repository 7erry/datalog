# Discovery: MongoDB Atlas security — defense in depth

**Companion:** `security.html`

## Opening minute (discovery call)

Thanks—security conversations should start with **threat model and boundaries**, not a feature list. Atlas bundles a lot—**identity, network isolation, encryption, auditing**—but the win is when it maps cleanly to **your controls and your regulators’ questions**. What assessment is coming—**SOC2-style**, **highly regulated industry**, or **enterprise security review**?

## Why current approaches fall short (without a competitive move)

Checklist security without **threat modeling** buys tools but not outcomes—misconfigured networks, over-privileged users, and **audit theater**. Non-competitive is “we enabled the toggle.”

## Cost of inaction

Cost of inaction is **breach risk, failed assessments, and delayed launches** while exceptions pile up. Customers ask hard questions you can’t answer crisply; **renewals soften** when trust wavers.

## Ten open-ended questions (pain points & buying process)

1. What threats are you most worried about—credential theft, insider risk, lateral movement, data exfiltration?
2. How do you segment database access today—network, IAM, app-layer—and where are the weak joins?
3. What compliance frameworks apply, and which controls are audit findings waiting to happen?
4. Who runs security review for new databases—central security, cloud team, federated champions?
5. What evidence artifacts do you need—architecture diagrams, config exports, pen test scopes?
6. How does procurement engage security—mandatory questionnaires, red team requirements?
7. What would block Atlas adoption even if engineering loves it?
8. How do you handle key management, logging retention, and third-party access?
9. What timeline is tied to certification, customer contract, or board risk reporting?
10. What would “we can defend this in an audit” look like as an exit criterion?
