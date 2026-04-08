# Discovery: MongoDB for payments playbook

**Companion:** `payments.html`

## Opening minute (discovery call)

Appreciate the time—**payments** demands correctness, audit trails, and predictable performance under spikes. MongoDB shows up when teams want **flexible payment objects**, strong **operational models**, and patterns that don’t fight the domain model. I’ll anchor on **idempotency, ledgering concepts, and reconciliation** without pretending compliance is one-size-fits-all. Are you building **new payment flows**, or **replacing a strained legacy store**?

## Why current approaches fall short (without a competitive move)

Payments on generic patterns without **idempotency, traceability, and reconciliation discipline** invite subtle money bugs. Non-competitive is “it works in happy path” without **failure injection** culture.

## Cost of inaction

Inaction shows as **chargebacks, manual fixes, and audit pain**—brand and regulatory exposure. Scaling events become **bet-the-company weekends**. You pay fines, credits, and **engineering halt** while trust recovers slowly.

## Ten open-ended questions (pain points & buying process)

1. Walk me through the payment lifecycle you support—authorization, capture, refunds, disputes—and where data lives today.
2. What correctness failures are unacceptable—dupes, lost updates, inconsistent balances—and have you seen near-misses?
3. How do you handle idempotency keys, out-of-order webhooks, and retries from partners?
4. What regulatory or scheme requirements (PCI, PSD2, regional rules) shape your storage and access model?
5. Who audits payment data flows, and what evidence do they expect?
6. What peak-load or burst scenarios worry you—sales events, payroll, partner batch files?
7. Who owns the database tier for payments—dedicated team or shared platform—and how do changes get approved?
8. What’s the evaluation bar for a new store—latency, HA, backup, encryption, change control?
9. How does procurement engage for payment-adjacent systems—long security reviews, preferred vendors?
10. What would “we’re stable through Black Friday” mean in measurable terms for your team?
