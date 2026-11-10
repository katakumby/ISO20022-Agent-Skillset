---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.13 MatchingReason5Choice", "7.1.28.13.1 Reason <Rsn>", "7.1.28.13.1.1 Code <Cd>", "7.1.28.13.1.1.1 Code <Cd>"]
file_pages: [599]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.13.1.1.1 Code <Cd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 599 to 599.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 599

```text
Code <Cd> contains one of the following AllegementReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 599
Or}   Proprietary <Prtry> [1..1] ± 599
7.1.28.13.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has been alleged.
Datatype: "AllegementReason1Code" on page 614
CodeName Name Definition
ALG1 AllegementReceived Allegement has been received and no
match could be found.
7.1.28.13.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has been alleged.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.28.13.1.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the reason in narrative form.
Datatype: "Max210Text" on page 668
7.1.28.13.2  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 636
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
7.1.28.14  InstructionProcessingReason4Choice
Definition: Choice of format for the instruction processing status.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 599 February 2025
```

