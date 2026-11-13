---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.7 MatchingReason6Choice", "7.1.28.7.1 Reason <Rsn>"]
file_pages: [593]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.7.1 Reason <Rsn>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 593 to 593.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 593

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..*]  593
     Code <Cd> [1..1] ± 593
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 593
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 593
7.1.28.7.1  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the UnmatchStatus.
Reason <Rsn> contains the following UnmatchedReason23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 593
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 593
7.1.28.7.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has an unmatched status.
Code <Cd> contains one of the following elements (see "UnmatchedReason32Choice" on page 582 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 582
Or}   Proprietary <Prtry> [1..1] ± 585
7.1.28.7.1.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the reason in narrative form.
Datatype: "Max210Text" on page 668
7.1.28.7.2  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 636
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 593 February 2025
```

