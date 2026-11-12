---
template: false
document_kind: "business-flow"
title: "Credit-transfer return after cancellation consent — supplied example"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.004.001.15"]
message_families: ["pacs.004"]
source_locations: [{"source_id": "src-000162", "locator": "P836–P899; P900–P966"}]
flow_id: "flow-src-000162-example-03"
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-bbbbie2d", "participant-src-000162-example-ccccie2d", "participant-src-000162-example-seed-inc-0785746"]
participants: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-bbbbie2d", "participant-src-000162-example-ccccie2d", "participant-src-000162-example-seed-inc-0785746"]
issue_ids: ["issue-000059"]
limitations: ["This flow is the supplied historical example, not an invented scenario.", "Only source-defined outcomes and alternatives apply; the example does not separately specify formal preconditions or universal service rules."]
source_editions: ["March 2026"]
---

# Credit-transfer return after cancellation consent

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and source-defined conditions

**P837** This example covers two PaymentReturn messages. The first PaymentReturn message is sent by CCCC Bank to BBBB Bank. The second PaymentReturn message is sent by BBBB Bank to AAAA Bank.

**P840** On receipt of an FIToFIPaymentCancellationRequest message from BBBB Bank, CCCC Bank checks with Seed Inc. whether it is willing to return the credited funds. Seed Inc. accepts to return the amount credited onto its account (EUR 74850) without requesting compensation. CCCC Bank sends a PaymentReturn message to BBBB Bank.

**P842** PaymentReturn from CCCC Bank to BBBB Bank:

**P902** On receipt of the payment return message from CCCC Bank, BBBB Bank deducts processing charges for the return message, credits the account of AAAA Bank and forwards the payment return message to AAAA Bank.

**P904** PaymentReturn from BBBB Bank to AAAA Bank:


## Ordered message exchanges

| Step | Message | Sender / initiator | Receiver | Source evidence |
| --- | --- | --- | --- | --- |
| 3 | [pacs.004.001.15](../examples/example-03-pacs.004.001.15.md) | [CCCCIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccie2d.md) | [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | P844–P899; T30 |
| 4 | [pacs.004.001.15](../examples/example-04-pacs.004.001.15.md) | [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | P906–P966; T31 |


## Participant roles and outcomes

| Participant | Instance fields / scope |
| --- | --- |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | Cdtr, CdtrAgt, DbtrAgt, InstdAgt, InstgAgt |
| [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | Agt, InstdAgt, InstgAgt |
| [CCCCIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccie2d.md) | Agt, CdtrAgt, InstdAgt, InstgAgt |
| [Seed Inc.](../../../../../../../shared/reference/participants/participant-src-000162-example-seed-inc-0785746.md) | Orgtr |


The narrative above supplies the responsible parties, accounting actions, decisions, charges and stated results. Message-instance participant fields retain their full paths; an institution may hold different functional roles in different relationships. No missing response, failure or formal postcondition is invented. These examples contain tables and XML instances rather than a separate reference diagram; the general process diagrams remain in [the source diagram index](../diagrams/clearing/index.md).

[Preserved source differences](../examples/source-discrepancies.md)
