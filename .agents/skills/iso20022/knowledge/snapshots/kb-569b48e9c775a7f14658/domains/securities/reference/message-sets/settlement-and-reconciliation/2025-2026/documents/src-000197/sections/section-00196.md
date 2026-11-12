---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.1 StatusAndReason <StsAndRsn>", "9.4.6.1.5 InstructionProcessingStatus <InstrPrcgSts>", "9.4.6.1.5.1 PendingProcessing <PdgPrcg>"]
file_pages: [296]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.1.5.1 PendingProcessing <PdgPrcg>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 296 to 296.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 296

```text
InstructionProcessingStatus <InstrPrcgSts> contains one of the following
InstructionProcessingStatus61Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingProcessing <PdgPrcg> [1..1]  296
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 297
Or}     Reason <Rsn> [1..*]  297
       Code <Cd> [1..1]  297
{Or         Code <Cd> [1..1] CodeSet 298
Or}         Proprietary <Prtry> [1..1] ± 299
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 299
Or   CancellationRequested <CxlReqd> [1..1] ± C4 299
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 300
Or   Cancelled <Canc> [1..1] ± 300
Or   Generated <Gnrtd> [1..1]  300
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 301
Or}     Reason <Rsn> [1..*] ± 301
Or   Repair <Rpr> [1..1] ± 301
Or   PendingCancellation <PdgCxl> [1..1]  301
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 302
Or}     Reason <Rsn> [1..*]  302
       Code <Cd> [1..1]  302
{Or         Code <Cd> [1..1] CodeSet 303
Or}         Proprietary <Prtry> [1..1] ± 303
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 303
Or}   ModificationRequested <ModReqd> [1..1] ± C4 304
9.4.6.1.5.1  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer, but processing of the instruction
is pending.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 296 March 2026
```

