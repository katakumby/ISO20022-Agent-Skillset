---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.11 InstructionProcessingReason3Choice", "7.1.28.11.2 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [597]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.11.2 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 597 to 597.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 597

```text
Datatype: "Max210Text" on page 668
7.1.28.11.2  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 636
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
7.1.28.12  AffirmationReason2Choice
Definition: Choice of format for the affirmation status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..*]  597
     Code <Cd> [1..1] ± 597
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 597
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 598
7.1.28.12.1  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the UnaffirmedStatus.
Reason <Rsn> contains the following AffirmationReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 597
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 597
7.1.28.12.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a unaffirmed status.
Code <Cd> contains one of the following elements (see "UnaffirmedReason3Choice" on page 594 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 594
Or}   Proprietary <Prtry> [1..1] ± 595
7.1.28.12.1.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 597 February 2025
```

