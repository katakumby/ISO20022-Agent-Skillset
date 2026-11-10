---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.22 GenericIdentification56", "35.1.14.22.4 Balance <Bal>"]
file_pages: [1506]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.22.4 Balance <Bal>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1506 to 1506.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1506

```text
35.1.14.22.4  Balance <Bal>
Presence: [1..1]
Definition: Value of the balance.
Datatype: "DecimalNumber" on page 2188
35.1.14.23  TransactionIdentifications56
Definition: Unique identifier of a document, message or transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeIdentification <TradId> [0..*] Text 1506
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1506
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1506
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1506
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1507
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1507
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
35.1.14.23.1  TradeIdentification <TradId>
Presence: [0..*]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 2192
35.1.14.23.2  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 2188
35.1.14.23.3  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 2192
35.1.14.23.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1506 March 2026
```

