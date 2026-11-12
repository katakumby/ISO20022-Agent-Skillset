---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.8 References69Choice"]
file_pages: [1489]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.8 References69Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1489 to 1489.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1489

```text
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 2192
35.1.14.8  References69Choice
Definition: Choice of reference.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionConfirmationIdentificatio
n <SctiesSttlmTxConfId>
[1..1] ± 1490
Or   IntraPositionMovementConfirmationIdentification
<IntraPosMvmntConfId>
[1..1] Text 1490
Or   SecuritiesBalanceAccountingReportIdentification
<SctiesBalAcctgRptId>
[1..1] Text 1490
Or   SecuritiesBalanceCustodyReportIdentification
<SctiesBalCtdyRptId>
[1..1] Text 1490
Or   IntraPositionMovementPostingReportIdentification
<IntraPosMvmntPstngRptId>
[1..1] Text 1490
Or   SecuritiesFinancingConfirmationIdentification
<SctiesFincgConfId>
[1..1] ± 1491
Or   SecuritiesTransactionPendingReportIdentification
<SctiesTxPdgRptId>
[1..1] Text 1491
Or   SecuritiesTransactionPostingReportIdentification
<SctiesTxPstngRptId>
[1..1] Text 1491
Or   SecuritiesSettlementTransactionAllegementReportIdentifi
cation <SctiesSttlmTxAllgmtRptId>
[1..1] Text 1491
Or   SecuritiesSettlementTransactionAllegementNotificationTr
ansactionIdentification <SctiesSttlmTxAllgmtNtfctnTxId>
[1..1] ± 1491
Or   PortfolioTransferNotificationIdentification
<PrtflTrfNtfctnId>
[1..1] Text 1492
Or   SecuritiesSettlementTransactionGenerationNotificationId
entification <SctiesSttlmTxGnrtnNtfctnId>
[1..1] ± 1492
Or   OtherMessageIdentification <OthrMsgId> [1..1] Text 1492
Or   TotalPortfolioValuationReportIdentification
<TtlPrtflValtnRptId>
[1..1] Text 1492
Or   TripartyCollateralTransactionInstructionProcessingStatus
AdviceIdentification <TrptyCollTxInstrPrcgStsAdvcId>
[1..1] Text 1492
Or   TripartyCollateralStatusAdviceIdentification
<TrptyCollStsAdvcId>
[1..1] Text 1493
Or}   TripartyCollateralAndExposureReportIdentification
<TrptyCollAndXpsrRptId>
[1..1] Text 1493
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1489 March 2026
```

