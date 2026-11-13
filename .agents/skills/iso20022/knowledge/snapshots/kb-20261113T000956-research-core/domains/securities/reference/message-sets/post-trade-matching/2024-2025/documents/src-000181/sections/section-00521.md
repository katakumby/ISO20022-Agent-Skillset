---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.12 AffirmationReason2Choice", "7.1.28.12.2 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [598]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.12.2 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 598 to 598.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 598

```text
Definition: Provides additional information about the reason in narrative form.
Datatype: "Max210Text" on page 668
7.1.28.12.2  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 636
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
7.1.28.13  MatchingReason5Choice
Definition: Choice of format for the matching processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..*]  598
     Code <Cd> [1..1]  598
{Or       Code <Cd> [1..1] CodeSet 599
Or}       Proprietary <Prtry> [1..1] ± 599
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 599
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 599
7.1.28.13.1  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the MatchedAlleged Status.
Reason <Rsn> contains the following AllegementMatchingReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  598
{Or     Code <Cd> [1..1] CodeSet 599
Or}     Proprietary <Prtry> [1..1] ± 599
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 599
7.1.28.13.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has been alleged.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 598 February 2025
```

