---
template: false
document_kind: "business-flow"
title: "Customer-payment cover reimbursement — supplied example"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.009.001.13"]
message_families: ["pacs.009"]
source_locations: [{"source_id": "src-000162", "locator": "P2028–P2147; P2148–P2199"}]
flow_id: "flow-src-000162-example-14"
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-aaaajpjt", "participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-ccccjpjt", "participant-src-000162-example-def-electronics-46588bb"]
participants: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-aaaajpjt", "participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-ccccjpjt", "participant-src-000162-example-def-electronics-46588bb"]
issue_ids: ["issue-000059"]
limitations: ["This flow is the supplied historical example, not an invented scenario.", "Only source-defined outcomes and alternatives apply; the example does not separately specify formal preconditions or universal service rules."]
source_editions: ["March 2026"]
---

# Customer-payment cover reimbursement

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and source-defined conditions

**P2029** This example covers two FinancialInstitutionCreditTransfer messages. The first FinancialInstitutionCreditTransfer message is sent by BBBB Bank to CCCC Bank. The second FinancialInstitutionCreditTransfer message is sent by CCCCJPJT to AAAAJPJT.

**P2032** Under business example 1 of the FIToFICustomerCreditTransfer, BBBB Bank, New York (BBBBUS33) sent an FIToFICustomerCreditTransfer message to AAAA Bank (AAAAGB2L) using the cover method as BBBB Bank does not have a JPY account relationship with AAAA Bank. BBBB Bank uses CCCC Bank, Tokyo as its correspondent. AAAA Bank uses AAAA Bank, Tokyo (AAAAJPJT) as its JPY correspondent.  Immediately after sending the FIToFICustomerCreditTransfer to AAAA Bank, BBBB Bank sends its correspondent CCCC Bank a FinancialInstitutionCreditTransfer message to cover the customer payment.

**P2034** FinancialInstitutionCreditTransfer from BBBB Bank to CCCC Bank:

**P2150** On receipt of the instruction of BBBB Bank, CCCC Bank forwards the FinancialInstitutionCreditTransfer to the creditor agent AAAAJPJT. CCCC Bank holds multiple accounts with AAAAJPJT, and specifies that account 3451571 has to be used for reimbursement.

**P2152** FinancialInstitutionCreditTransfer from CCCCJPJT to AAAAJPJT:


## Ordered message exchanges

| Step | Message | Sender / initiator | Receiver | Source evidence |
| --- | --- | --- | --- | --- |
| 14 | [pacs.009.001.13](../examples/example-14-pacs.009.001.13.md) | [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | [CCCCJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccjpjt.md) | P2036–P2147; T41 |
| 15 | [pacs.009.001.13](../examples/example-15-pacs.009.001.13.md) | [CCCCJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccjpjt.md) | [AAAAJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaajpjt.md) | P2154–P2199; T42 |


## Participant roles and outcomes

| Participant | Instance fields / scope |
| --- | --- |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | Cdtr, CdtrAgt, DbtrAgt, InstdAgt, InstgAgt |
| [AAAAJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaajpjt.md) | CdtrAgt, InstdAgt, InstdRmbrsmntAgt |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-875623a.md) | Dbtr, InitgPty |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | Agt, Dbtr, DbtrAgt, InstgAgt |
| [CCCCJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccjpjt.md) | InstdAgt, InstgAgt, InstgRmbrsmntAgt |
| [DEF Electronics](../../../../../../../shared/reference/participants/participant-src-000162-example-def-electronics-46588bb.md) | Cdtr |


The narrative above supplies the responsible parties, accounting actions, decisions, charges and stated results. Message-instance participant fields retain their full paths; an institution may hold different functional roles in different relationships. No missing response, failure or formal postcondition is invented. These examples contain tables and XML instances rather than a separate reference diagram; the general process diagrams remain in [the source diagram index](../diagrams/clearing/index.md).

[Preserved source differences](../examples/source-discrepancies.md)
