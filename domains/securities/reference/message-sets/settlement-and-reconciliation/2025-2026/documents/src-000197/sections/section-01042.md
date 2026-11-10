---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information"]
file_pages: [1481]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14 Identification Information

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1481 to 1481.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1481

```text
Definition: Frequency expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.14 Identification Information
35.1.14.1  TransactionTypeAndAdditionalParameters23
Definition: Specifies the conditions under which the order/trade is to be settled.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1481
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1481
   SecuritiesFinancingTransactionType <SctiesFincgTxTp> [1..1] CodeSet 1481
   Payment <Pmt> [1..1] CodeSet 1482
   ModificationType <ModTp> [0..1] ± 1482
   CommonIdentification <CmonId> [0..1] Text 1482
   PoolIdentification <PoolId> [0..1] Text 1482
   NonceIdentification <NonceId> [0..1] Text 1483
35.1.14.1.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction (unique per piece of collateral) as known by the
account owner (or the instructing party managing the account).
Datatype: "Max35Text" on page 2192
35.1.14.1.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction (unique per piece of collateral) as known by the
account servicer.
Datatype: "Max35Text" on page 2192
35.1.14.1.3  SecuritiesFinancingTransactionType <SctiesFincgTxTp>
Presence: [1..1]
Definition: Specifies the type of securities financing transaction, that is, repurchase agreement, reverse
repurchase agreement, securities lending or securities borrowing.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1481 March 2026
```

