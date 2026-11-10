---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.1 StatusAndReason <StsAndRsn>", "9.4.6.1.5 InstructionProcessingStatus <InstrPrcgSts>", "9.4.6.1.5.5 Generated <Gnrtd>", "9.4.6.1.5.5.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [301]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.1.5.5.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 301 to 301.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 301

```text
Generated <Gnrtd> contains one of the following GeneratedStatus7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 301
Or}   Reason <Rsn> [1..*] ± 301
9.4.6.1.5.5.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
9.4.6.1.5.5.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the generated status.
Reason <Rsn> contains the following elements (see "GeneratedReason5" on page 1953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1954
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1954
9.4.6.1.5.6  Repair <Rpr>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer but is in repair.
Repair <Rpr> contains one of the following elements (see "RepairStatus12Choice" on page 2010 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2011
Or}   Reason <Rsn> [1..*]  2011
     Code <Cd> [1..1]  2011
{Or       Code <Cd> [1..1] CodeSet 2011
Or}       Proprietary <Prtry> [1..1] ± 2013
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2013
9.4.6.1.5.7  PendingCancellation <PdgCxl>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 301 March 2026
```

