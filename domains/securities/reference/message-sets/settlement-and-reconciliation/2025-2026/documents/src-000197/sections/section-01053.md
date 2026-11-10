---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.8 References69Choice", "35.1.14.8.11 PortfolioTransferNotificationIdentification <PrtflTrfNtfctnId>"]
file_pages: [1492]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.8.11 PortfolioTransferNotificationIdentification <PrtflTrfNtfctnId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1492 to 1492.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1492

```text
SecuritiesSettlementTransactionAllegementNotificationTransactionIdentification
<SctiesSttlmTxAllgmtNtfctnTxId> contains the following elements (see
"SettlementTypeAndIdentification18" on page 1501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 1501
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1501
   Payment <Pmt> [1..1] CodeSet 1501
35.1.14.8.11  PortfolioTransferNotificationIdentification <PrtflTrfNtfctnId>
Presence: [1..1]
Definition: Identification of the portfolio transfer.
Datatype: "Max35Text" on page 2192
35.1.14.8.12  SecuritiesSettlementTransactionGenerationNotificationIdentification
<SctiesSttlmTxGnrtnNtfctnId>
Presence: [1..1]
Definition: Unambiguous identification of the notification message to be cancelled.
SecuritiesSettlementTransactionGenerationNotificationIdentification
<SctiesSttlmTxGnrtnNtfctnId> contains the following elements (see
"SettlementTypeAndIdentification18" on page 1501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 1501
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1501
   Payment <Pmt> [1..1] CodeSet 1501
35.1.14.8.13  OtherMessageIdentification <OthrMsgId>
Presence: [1..1]
Definition: Unambiguous identification of the message to be cancelled.
Datatype: "Max35Text" on page 2192
35.1.14.8.14  TotalPortfolioValuationReportIdentification <TtlPrtflValtnRptId>
Presence: [1..1]
Definition: Unique identification of the report.
Datatype: "Max35Text" on page 2192
35.1.14.8.15  TripartyCollateralTransactionInstructionProcessingStatusAdviceIdentification
<TrptyCollTxInstrPrcgStsAdvcId>
Presence: [1..1]
Definition: Unambiguous identification of the triparty collateral transaction instruction status advice to be
cancelled.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1492 March 2026
```

