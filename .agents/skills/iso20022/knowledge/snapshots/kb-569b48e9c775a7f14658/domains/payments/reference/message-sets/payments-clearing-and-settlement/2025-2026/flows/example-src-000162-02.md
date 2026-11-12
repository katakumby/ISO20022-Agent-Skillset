---
template: false
document_kind: "business-flow"
title: "Direct-debit collection — supplied example"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.003.001.12"]
message_families: ["pacs.003"]
source_locations: [{"source_id": "src-000162", "locator": "P732–P835"}]
flow_id: "flow-src-000162-example-02"
participant_ids: ["participant-src-000162-example-aaaaus29", "participant-src-000162-example-ababus23", "participant-src-000162-example-bbbbus39", "participant-src-000162-example-jones-4dbd8f5", "participant-src-000162-example-virgay-6e3f97e"]
participants: ["participant-src-000162-example-aaaaus29", "participant-src-000162-example-ababus23", "participant-src-000162-example-bbbbus39", "participant-src-000162-example-jones-4dbd8f5", "participant-src-000162-example-virgay-6e3f97e"]
issue_ids: ["issue-000059"]
limitations: ["This flow is the supplied historical example, not an invented scenario.", "Only source-defined outcomes and alternatives apply; the example does not separately specify formal preconditions or universal service rules."]
source_editions: ["March 2026"]
---

# Direct-debit collection

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and source-defined conditions

**P734** On 28 June 2015, following the receipt of a CustomerDirectDebitInitiation message from its customer Virgay, AAAAUS29 in its turn sends an FIToFICustomerDirectDebit message to ABABUS23, the common correspondent for AAAAUS29 and BBBBUS39, the agent of debtor Jones.

**P735** AAAAUS29 instructs ABABUS23, under Service Level CTRV - 356, to collect USD 1025 from account 123456, owned by Jones, the debtor, and serviced by BBBBUS39. The mandate related information is also provided: the mandate reference is VIRGAY123 and the mandate was signed by Jones on 13 July 2008. The last collection is due to take place on 13 July 2015. The payment is for life insurance. The requested collection date is 13 July 20102 and charges related to the handling of the instruction are shared between the creditor and the debtor.

**P736** The CustomerDirectDebitInitiation instruction sent by Virgay to AAAAUS29 is documented in the business example section of the CustomerDirectDebitInitiation message in the Payments Initiation Message Reference Guide.

**P738** FIToFICustomerDirectDebit from AAAAUS29 to ABABUS23:


## Ordered message exchanges

| Step | Message | Sender / initiator | Receiver | Source evidence |
| --- | --- | --- | --- | --- |
| 2 | [pacs.003.001.12](../examples/example-02-pacs.003.001.12.md) | [AAAAUS29](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaaus29.md) | [ABABUS23](../../../../../../../shared/reference/participants/participant-src-000162-example-ababus23.md) | P740–P835; T29 |


## Participant roles and outcomes

| Participant | Instance fields / scope |
| --- | --- |
| [AAAAUS29](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaaus29.md) | CdtrAgt, InstdAgt, InstgAgt |
| [ABABUS23](../../../../../../../shared/reference/participants/participant-src-000162-example-ababus23.md) | Agt, InstdAgt, InstgAgt |
| [BBBBUS39](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus39.md) | Agt, DbtrAgt, InstgAgt |
| [Jones](../../../../../../../shared/reference/participants/participant-src-000162-example-jones-4dbd8f5.md) | Dbtr |
| [Virgay](../../../../../../../shared/reference/participants/participant-src-000162-example-virgay-6e3f97e.md) | Cdtr |


The narrative above supplies the responsible parties, accounting actions, decisions, charges and stated results. Message-instance participant fields retain their full paths; an institution may hold different functional roles in different relationships. No missing response, failure or formal postcondition is invented. These examples contain tables and XML instances rather than a separate reference diagram; the general process diagrams remain in [the source diagram index](../diagrams/clearing/index.md).

[Preserved source differences](../examples/source-discrepancies.md)
