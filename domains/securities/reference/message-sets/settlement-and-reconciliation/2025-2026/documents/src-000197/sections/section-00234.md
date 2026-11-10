---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.7.15 TransactionDetails <TxDtls>", "9.4.7.15.23 TransactionAdditionalDetails <TxAddtlDtls>"]
file_pages: [348, 349]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.7.15.23 TransactionAdditionalDetails <TxAddtlDtls>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 348 to 349.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 348

```text
9.4.7.15.23  TransactionAdditionalDetails <TxAddtlDtls>
Presence: [0..1]
Definition: Provides additional details on the transaction which cannot be included within the structured
fields of the message.
Datatype: "Max350Text" on page 2192
9.4.7.15.24  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C40 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
9.4.7.16  StatusAndReason <StsAndRsn>
Presence: [0..*]
Definition: Status and reason for the transaction.
Impacted by: C26 "PendingToFailingRule", C39 "SettlementStatusAndMatchedRule"
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 348 March 2026
```

## File page 349

```text
StatusAndReason <StsAndRsn> contains one of the following Status43Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Proprietary <Prtry> [1..1] ± 350
Or   MatchingStatus <MtchgSts> [1..1] ± 350
Or   InferredMatchingStatus <IfrrdMtchgSts> [1..1] ± 350
Or   SettlementStatus <SttlmSts> [1..1] ± C27 351
Or}   InstructionProcessingStatus <InstrPrcgSts> [1..1]  351
{Or     PendingProcessing <PdgPrcg> [1..1]  352
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 353
Or}       Reason <Rsn> [1..*]  353
         Code <Cd> [1..1]  353
{Or           Code <Cd> [1..1] CodeSet 354
Or}           Proprietary <Prtry> [1..1] ± 355
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 355
Or     CancellationRequested <CxlReqd> [1..1] ± C4 355
Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 356
Or     Cancelled <Canc> [1..1] ± 356
Or     Generated <Gnrtd> [1..1]  356
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 357
Or}       Reason <Rsn> [1..*] ± 357
Or     Repair <Rpr> [1..1] ± 357
Or     PendingCancellation <PdgCxl> [1..1]  357
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 358
Or}       Reason <Rsn> [1..*]  358
         Code <Cd> [1..1]  358
{Or           Code <Cd> [1..1] CodeSet 359
Or}           Proprietary <Prtry> [1..1] ± 359
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 359
Or}     ModificationRequested <ModReqd> [1..1] ± C4 360
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 349 March 2026
```

