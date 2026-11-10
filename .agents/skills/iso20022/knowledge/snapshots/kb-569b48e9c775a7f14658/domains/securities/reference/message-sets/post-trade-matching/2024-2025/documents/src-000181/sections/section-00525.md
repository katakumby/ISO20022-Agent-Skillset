---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.14 InstructionProcessingReason4Choice", "7.1.28.14.2 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [603]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.14.2 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 603 to 603.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 603

```text
Datatype: "Max210Text" on page 668
7.1.28.14.2  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 636
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
7.1.28.15  CancellationReason39Choice
Definition: Choice of format for the cancellation processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 603
Or}   Reason <Rsn> [1..*]  603
     Code <Cd> [1..1]  604
{Or       Code <Cd> [1..1] CodeSet 604
Or}       Proprietary <Prtry> [1..1] ± 604
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 604
7.1.28.15.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 636
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
7.1.28.15.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the CancellationPending Status.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 603 February 2025
```

