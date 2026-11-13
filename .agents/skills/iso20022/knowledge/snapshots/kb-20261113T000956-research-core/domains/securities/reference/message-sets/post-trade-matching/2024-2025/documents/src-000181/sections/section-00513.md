---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.5 ProprietaryReason4"]
file_pages: [589]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.5 ProprietaryReason4

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 589 to 589.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 589

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
7.1.28.5  ProprietaryReason4
Definition: Proprietary identification of the reason related to a status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 589
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 589
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
7.1.28.5.1  Reason <Rsn>
Presence: [0..1]
Definition: Proprietary identification of the reason related to a status.
Reason <Rsn> contains the following elements (see "GenericIdentification30" on page 276 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.28.5.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the processed instruction.
Datatype: "Max210Text" on page 668
7.1.28.6  RejectionReason52Choice
Definition: Choice of format for the rejection reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 590
Or}   Proprietary <Prtry> [1..1] ± 592
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 589 February 2025
```

