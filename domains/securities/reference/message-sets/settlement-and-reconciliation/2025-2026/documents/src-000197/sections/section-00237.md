---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.7.16 StatusAndReason <StsAndRsn>", "9.4.7.16.5 InstructionProcessingStatus <InstrPrcgSts>", "9.4.7.16.5.1 PendingProcessing <PdgPrcg>"]
file_pages: [352]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.7.16.5.1 PendingProcessing <PdgPrcg>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 352 to 352.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 352

```text
InstructionProcessingStatus <InstrPrcgSts> contains one of the following
InstructionProcessingStatus61Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingProcessing <PdgPrcg> [1..1]  352
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 353
Or}     Reason <Rsn> [1..*]  353
       Code <Cd> [1..1]  353
{Or         Code <Cd> [1..1] CodeSet 354
Or}         Proprietary <Prtry> [1..1] ± 355
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 355
Or   CancellationRequested <CxlReqd> [1..1] ± C4 355
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 356
Or   Cancelled <Canc> [1..1] ± 356
Or   Generated <Gnrtd> [1..1]  356
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 357
Or}     Reason <Rsn> [1..*] ± 357
Or   Repair <Rpr> [1..1] ± 357
Or   PendingCancellation <PdgCxl> [1..1]  357
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 358
Or}     Reason <Rsn> [1..*]  358
       Code <Cd> [1..1]  358
{Or         Code <Cd> [1..1] CodeSet 359
Or}         Proprietary <Prtry> [1..1] ± 359
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 359
Or}   ModificationRequested <ModReqd> [1..1] ± C4 360
9.4.7.16.5.1  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer, but processing of the instruction
is pending.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 352 March 2026
```

