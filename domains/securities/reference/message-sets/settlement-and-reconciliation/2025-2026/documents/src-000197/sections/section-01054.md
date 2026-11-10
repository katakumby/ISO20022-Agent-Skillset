---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.8 References69Choice", "35.1.14.8.16 TripartyCollateralStatusAdviceIdentification <TrptyCollStsAdvcId>"]
file_pages: [1493]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.8.16 TripartyCollateralStatusAdviceIdentification <TrptyCollStsAdvcId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1493 to 1493.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1493

```text
Datatype: "Max35Text" on page 2192
35.1.14.8.16  TripartyCollateralStatusAdviceIdentification <TrptyCollStsAdvcId>
Presence: [1..1]
Definition: Unambiguous identification of the triparty collateral status advice to be cancelled.
Datatype: "Max35Text" on page 2192
35.1.14.8.17  TripartyCollateralAndExposureReportIdentification <TrptyCollAndXpsrRptId>
Presence: [1..1]
Definition: Unambiguous identification of the triparty collateral and exposure report to be cancelled.
Datatype: "Max35Text" on page 2192
35.1.14.9  TransactionIdentifications33
Definition: Unique identifier of a document, message or transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1493
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1494
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1494
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1494
   OtherIdentification <OthrId> [0..1] Text 1494
Constraints
• AccountOwnerTransactionIdentificationRule
If AccountOwnerTransactionIdentification is NONREF then at least one of the other references must
be present.
On Condition
    /AccountOwnerTransactionIdentification is equal to value 'NONREF'
Following Must be True
    /AccountServicerTransactionIdentification Must be present
 Or    /MarketInfrastructureTransactionIdentification Must be present
 Or    /ProcessorTransactionIdentification Must be present
 Or    /OtherIdentification Must be present
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, then the
AccountOwnerTransactionIdentification must be NONREF.
35.1.14.9.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1493 March 2026
```

