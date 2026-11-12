---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.7.16 StatusAndReason <StsAndRsn>", "9.4.7.16.5 InstructionProcessingStatus <InstrPrcgSts>", "9.4.7.16.5.1 PendingProcessing <PdgPrcg>", "9.4.7.16.5.1.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [353]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.7.16.5.1.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 353 to 353.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 353

```text
PendingProcessing <PdgPrcg> contains one of the following PendingProcessingStatus20Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 353
Or}   Reason <Rsn> [1..*]  353
     Code <Cd> [1..1]  353
{Or       Code <Cd> [1..1] CodeSet 354
Or}       Proprietary <Prtry> [1..1] ± 355
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 355
9.4.7.16.5.1.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
9.4.7.16.5.1.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending processing status.
Reason <Rsn> contains the following PendingProcessingReason17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  353
{Or     Code <Cd> [1..1] CodeSet 354
Or}     Proprietary <Prtry> [1..1] ± 355
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 355
9.4.7.16.5.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Code <Cd> contains one of the following PendingProcessingReason19Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 354
Or}   Proprietary <Prtry> [1..1] ± 355
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 353 March 2026
```

