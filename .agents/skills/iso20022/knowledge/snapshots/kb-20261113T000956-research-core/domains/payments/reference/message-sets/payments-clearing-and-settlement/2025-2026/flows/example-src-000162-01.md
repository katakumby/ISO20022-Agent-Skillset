---
template: false
document_kind: "business-flow"
title: "Direct-debit rejection — supplied example"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.002.001.16"]
message_families: ["pacs.002"]
source_locations: [{"source_id": "src-000162", "locator": "P650–P731"}]
flow_id: "flow-src-000162-example-01"
participant_ids: ["participant-src-000162-example-aaaaus29", "participant-src-000162-example-ababus23", "participant-src-000162-example-jones-4dbd8f5", "participant-src-000162-example-virgay-6e3f97e"]
participants: ["participant-src-000162-example-aaaaus29", "participant-src-000162-example-ababus23", "participant-src-000162-example-jones-4dbd8f5", "participant-src-000162-example-virgay-6e3f97e"]
issue_ids: ["issue-000059"]
limitations: ["This flow is the supplied historical example, not an invented scenario.", "Only source-defined outcomes and alternatives apply; the example does not separately specify formal preconditions or universal service rules."]
source_editions: ["March 2026"]
---

# Direct-debit rejection

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and source-defined conditions

**P652** On 28 June 2015, ABABUS23 received a FIToFICustomerDirectDebit message from AAAAUS29. On 29 June 2015, ABABUS23 rejects the FIToFICustomerDirectDebit message by sending a FIToFIPaymentStatusReport message to AAAAUS29, referring to the original instruction and indicating the reason for the rejection.

**P654** The FIToFICustomerDirectDebit instruction from AAAAUS29 to ABABUS23 is included in the business example section of the FIToFICustomerDirectDebit message.

**P655** As AAAUS29 has not yet credited the account of its customer, Virgay, in turn, AAAAUS29 will send a CustomerPaymentStatusReport to inform Virgay of the rejection. This example is included in the business example section of the PaymentStatusReport message in the Payments Initiation Message Reference Guide.

**P657** PaymentStatusReport from ABABUS23 to AAAAUS29:


## Ordered message exchanges

| Step | Message | Sender / initiator | Receiver | Source evidence |
| --- | --- | --- | --- | --- |
| 1 | [pacs.002.001.16](../examples/example-01-pacs.002.001.16.md) | [ABABUS23](../../../../../../../shared/reference/participants/participant-src-000162-example-ababus23.md) | [AAAAUS29](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaaus29.md) | P659–P731; T28 |


## Participant roles and outcomes

| Participant | Instance fields / scope |
| --- | --- |
| [AAAAUS29](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaaus29.md) | CdtrAgt, InstdAgt, InstgAgt |
| [ABABUS23](../../../../../../../shared/reference/participants/participant-src-000162-example-ababus23.md) | Agt, InstdAgt, InstgAgt |
| [Jones](../../../../../../../shared/reference/participants/participant-src-000162-example-jones-4dbd8f5.md) | Dbtr |
| [Virgay](../../../../../../../shared/reference/participants/participant-src-000162-example-virgay-6e3f97e.md) | Cdtr |


The narrative above supplies the responsible parties, accounting actions, decisions, charges and stated results. Message-instance participant fields retain their full paths; an institution may hold different functional roles in different relationships. No missing response, failure or formal postcondition is invented. These examples contain tables and XML instances rather than a separate reference diagram; the general process diagrams remain in [the source diagram index](../diagrams/clearing/index.md).

[Preserved source differences](../examples/source-discrepancies.md)
