---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.24 Identification32", "35.1.14.24.9 MasterIdentification <MstrId>"]
file_pages: [1509, 1510]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.24.9 MasterIdentification <MstrId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1509 to 1510.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1509

```text
35.1.14.24.9  MasterIdentification <MstrId>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 2192
35.1.14.24.10  BasketIdentification <BsktId>
Presence: [0..1]
Definition: Identification of a basket trade.
Datatype: "Max35Text" on page 2192
35.1.14.24.11  IndexIdentification <IndxId>
Presence: [0..1]
Definition: Reference identifying an index trade.
Datatype: "Max35Text" on page 2192
35.1.14.24.12  ListIdentification <ListId>
Presence: [0..1]
Definition: Unique identifier for a list, as assigned by the trading party. The identifier must be unique
within a single trading day.
Datatype: "Max35Text" on page 2192
35.1.14.24.13  ProgramIdentification <PrgmId>
Presence: [0..1]
Definition: Program reference which identifies a program trade.
Datatype: "Max35Text" on page 2192
35.1.14.24.14  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 2192
35.1.14.24.15  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 2192
35.1.14.25  TransactionTypeAndAdditionalParameters22
Definition: Specifies the conditions under which the order/trade is to be settled.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1509 March 2026
```

## File page 1510

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1511
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1511
   SecuritiesFinancingTransactionType <SctiesFincgTxTp> [1..1] CodeSet 1511
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1512
   Payment <Pmt> [1..1] CodeSet 1512
   CommonIdentification <CmonId> [0..1] Text 1512
   PoolIdentification <PoolId> [0..1] Text 1512
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1512
   NonceIdentification <NonceId> [0..1] Text 1513
Constraints
• TwoLegTransactionOpeningClosingRule
For transactions settling in two legs (Securities Financing), the opening/initiation and closing/return
information of the transaction is provided by sending the below combination of
SecuritiesMovementType codes and SecuritiesFinancingTransactionType codes:
Repo Opening
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: Repo (REPU)
Repo Closing
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: Repo (REPU)
Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: ReverseRepo (RVPO)
Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: ReverseRepo (RVPO)
Securities Lending Initiation
SecuritiesMovementType: Delivery (DELI)
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1510 March 2026
```

