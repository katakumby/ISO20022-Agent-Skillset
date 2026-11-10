---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.11 InstructionProcessingReason3Choice"]
file_pages: [596]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.11 InstructionProcessingReason3Choice

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 596 to 596.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 596

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.28.11  InstructionProcessingReason3Choice
Definition: Choice of format for the instruction processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..*]  596
     Code <Cd> [1..1] ± 596
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 596
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 597
7.1.28.11.1  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the RejectedStatus.
Reason <Rsn> contains the following RejectionReason67 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 596
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 596
7.1.28.11.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected status.
Code <Cd> contains one of the following elements (see "RejectionReason52Choice" on page 589 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 590
Or}   Proprietary <Prtry> [1..1] ± 592
7.1.28.11.1.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the reason in narrative form.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 596 February 2025
```

