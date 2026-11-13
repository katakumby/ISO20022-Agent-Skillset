---
template: false
document_kind: "business-flow"
title: "Financial-institution direct debit — supplied example"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.010.001.06"]
message_families: ["pacs.010"]
source_locations: [{"source_id": "src-000162", "locator": "P2418–P2503"}]
flow_id: "flow-src-000162-example-19"
participant_ids: ["participant-src-000162-example-mmmmbebb", "participant-src-000162-example-nnnndeff", "participant-src-000162-example-ooooatww", "participant-src-000162-example-ppppdkkk", "participant-src-000162-example-qqqqfrpp"]
participants: ["participant-src-000162-example-mmmmbebb", "participant-src-000162-example-nnnndeff", "participant-src-000162-example-ooooatww", "participant-src-000162-example-ppppdkkk", "participant-src-000162-example-qqqqfrpp"]
issue_ids: ["issue-000059"]
limitations: ["This flow is the supplied historical example, not an invented scenario.", "Only source-defined outcomes and alternatives apply; the example does not separately specify formal preconditions or universal service rules."]
source_editions: ["March 2026"]
---

# Financial-institution direct debit

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and source-defined conditions

**P2420** Bank MMMM instructs Bank NNNN to debit the account of Bank PPPP for 2500 EUR and Bank OOOO for 5000 EUR in favour of its account at Bank QQQQ with value date 21 November 2015.

**P2422** The FinancialInstitutionDirectDebit message, from Bank MMMMBEBB to Bank NNNNDEFF:


## Ordered message exchanges

| Step | Message | Sender / initiator | Receiver | Source evidence |
| --- | --- | --- | --- | --- |
| 19 | [pacs.010.001.06](../examples/example-19-pacs.010.001.06.md) | [MMMMBEBB](../../../../../../../shared/reference/participants/participant-src-000162-example-mmmmbebb.md) | [NNNNDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-nnnndeff.md) | P2425–P2503; T46 |


## Participant roles and outcomes

| Participant | Instance fields / scope |
| --- | --- |
| [MMMMBEBB](../../../../../../../shared/reference/participants/participant-src-000162-example-mmmmbebb.md) | Cdtr, InstgAgt |
| [NNNNDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-nnnndeff.md) | DbtrAgt, InstdAgt |
| [OOOOATWW](../../../../../../../shared/reference/participants/participant-src-000162-example-ooooatww.md) | Dbtr |
| [PPPPDKKK](../../../../../../../shared/reference/participants/participant-src-000162-example-ppppdkkk.md) | Dbtr |
| [QQQQFRPP](../../../../../../../shared/reference/participants/participant-src-000162-example-qqqqfrpp.md) | CdtrAgt |


The narrative above supplies the responsible parties, accounting actions, decisions, charges and stated results. Message-instance participant fields retain their full paths; an institution may hold different functional roles in different relationships. No missing response, failure or formal postcondition is invented. These examples contain tables and XML instances rather than a separate reference diagram; the general process diagrams remain in [the source diagram index](../diagrams/clearing/index.md).

[Preserved source differences](../examples/source-discrepancies.md)
