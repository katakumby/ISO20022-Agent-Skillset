---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.58 AdditionalParameters33", "35.1.16.58.2 PreviousPartialConfirmationIdentification <PrvsPrtlConfId>"]
file_pages: [1596]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.58.2 PreviousPartialConfirmationIdentification <PrvsPrtlConfId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1596 to 1596.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1596

```text
Definition: Specifies partial settlement information.
Datatype: "PartialSettlement2Code" on page 2089
CodeName Name Definition
PAIN PartialSettlement Confirmation is for partial settlement.
Part of the transaction remains
unsettled.
PARC PartiallyConfirmed Confirmation is for partial settlement. No
additional settlement will take place.
35.1.16.58.2  PreviousPartialConfirmationIdentification <PrvsPrtlConfId>
Presence: [0..1]
Definition: Identification of the confirmation previously sent to confirm the partial settlement of a
transaction.
Datatype: "Max35Text" on page 2192
35.1.16.58.3  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 2192
35.1.16.58.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
35.1.16.58.5  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 2192
35.1.16.58.6  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 2192
35.1.16.58.7  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1596 March 2026
```

