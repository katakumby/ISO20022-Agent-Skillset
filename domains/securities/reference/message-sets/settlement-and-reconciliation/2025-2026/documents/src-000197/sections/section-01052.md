---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.8 References69Choice", "35.1.14.8.6 SecuritiesFinancingConfirmationIdentification <SctiesFincgConfId>"]
file_pages: [1491]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.8.6 SecuritiesFinancingConfirmationIdentification <SctiesFincgConfId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1491 to 1491.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1491

```text
Datatype: "Max35Text" on page 2192
35.1.14.8.6  SecuritiesFinancingConfirmationIdentification <SctiesFincgConfId>
Presence: [1..1]
Definition: Unambiguous identification of the confirmation to be cancelled.
SecuritiesFinancingConfirmationIdentification <SctiesFincgConfId> contains the following
elements (see "SettlementTypeAndIdentification18" on page 1501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 1501
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1501
   Payment <Pmt> [1..1] CodeSet 1501
35.1.14.8.7  SecuritiesTransactionPendingReportIdentification <SctiesTxPdgRptId>
Presence: [1..1]
Definition: Unambiguous identification of the report message to be cancelled.
Datatype: "Max35Text" on page 2192
35.1.14.8.8  SecuritiesTransactionPostingReportIdentification <SctiesTxPstngRptId>
Presence: [1..1]
Definition: Unambiguous identification of the report message to be cancelled.
Datatype: "Max35Text" on page 2192
35.1.14.8.9  SecuritiesSettlementTransactionAllegementReportIdentification
<SctiesSttlmTxAllgmtRptId>
Presence: [1..1]
Definition: Unambiguous identification of the report to be cancelled.
Datatype: "Max35Text" on page 2192
35.1.14.8.10  SecuritiesSettlementTransactionAllegementNotificationTransactionIdentification
<SctiesSttlmTxAllgmtNtfctnTxId>
Presence: [1..1]
Definition: Unambiguous identification of the allegement notification to be cancelled as known by the
account servicer.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1491 March 2026
```

