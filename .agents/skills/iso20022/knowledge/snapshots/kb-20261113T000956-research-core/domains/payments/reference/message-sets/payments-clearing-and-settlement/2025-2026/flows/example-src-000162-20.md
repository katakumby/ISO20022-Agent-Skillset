---
template: false
document_kind: "business-flow"
title: "Missing-status request — supplied example"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.028.001.07"]
message_families: ["pacs.028"]
source_locations: [{"source_id": "src-000162", "locator": "P2506–P2615"}]
flow_id: "flow-src-000162-example-20"
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-def-electronics-bf4c618"]
participants: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-def-electronics-bf4c618"]
issue_ids: ["issue-000059"]
limitations: ["This flow is the supplied historical example, not an invented scenario.", "Only source-defined outcomes and alternatives apply; the example does not separately specify formal preconditions or universal service rules."]
source_editions: ["March 2026"]
---

# Missing-status request

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and source-defined conditions

**P2508** This example relates to the instruction message in section 7.6.1, a FIToFICustomerCreditTransfer message sent by BBBBUS33 to AAAAGB2L. No FIToFIPaymentStatusReport message was received yet, but BBBBUS33 wants to know the status of the instruction. BBBBUS33 therefore sends a FIToFIPaymentStatusRequest message to request a FIToFIPaymentStatusReport.

**P2510** The FIToFIPaymentStatusRequest message, from Bank BBBBUS33 to Bank AAAAGB2L:


## Ordered message exchanges

| Step | Message | Sender / initiator | Receiver | Source evidence |
| --- | --- | --- | --- | --- |
| 20 | [pacs.028.001.07](../examples/example-20-pacs.028.001.07.md) | [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | P2514–P2615; T47 |


## Participant roles and outcomes

| Participant | Instance fields / scope |
| --- | --- |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | Cdtr, CdtrAgt, DbtrAgt, InstdAgt, InstgAgt |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-875623a.md) | Dbtr, InitgPty |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | Agt, Dbtr, DbtrAgt, InstgAgt |
| [DEF Electronics](../../../../../../../shared/reference/participants/participant-src-000162-example-def-electronics-bf4c618.md) | Cdtr |


The narrative above supplies the responsible parties, accounting actions, decisions, charges and stated results. Message-instance participant fields retain their full paths; an institution may hold different functional roles in different relationships. No missing response, failure or formal postcondition is invented. These examples contain tables and XML instances rather than a separate reference diagram; the general process diagrams remain in [the source diagram index](../diagrams/clearing/index.md).

[Preserved source differences](../examples/source-discrepancies.md)
