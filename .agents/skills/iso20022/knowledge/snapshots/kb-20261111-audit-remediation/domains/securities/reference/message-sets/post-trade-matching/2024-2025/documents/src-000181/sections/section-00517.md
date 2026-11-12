---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.8 MatchingStatus27Choice"]
file_pages: [594]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.8 MatchingStatus27Choice

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 594 to 594.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 594

```text
7.1.28.8  MatchingStatus27Choice
Definition: Choice of format for the matching status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 594
Or}   Proprietary <Prtry> [1..1] ± 594
7.1.28.8.1  Code <Cd>
Presence: [1..1]
Definition: Provides the matching status of the instruction.
Datatype: "MatchingStatus1Code" on page 635
CodeName Name Definition
MACH Matched Instruction has been matched.
NMAT Unmatched Instruction has not been matched.
7.1.28.8.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the matching status of the instruction.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.28.9  UnaffirmedReason3Choice
Definition: Choice of format for the unaffirmed reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 594
Or}   Proprietary <Prtry> [1..1] ± 595
7.1.28.9.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has an unaffirmed status.
Datatype: "UnaffirmedReason1Code" on page 657
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 594 February 2025
```

