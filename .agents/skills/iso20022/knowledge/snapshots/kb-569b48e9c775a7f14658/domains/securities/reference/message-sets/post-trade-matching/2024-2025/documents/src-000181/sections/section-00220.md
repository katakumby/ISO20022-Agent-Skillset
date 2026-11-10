---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.16 Frequency"]
file_pages: [274]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.16 Frequency

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 274 to 274.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 274

```text
OriginalAndCurrentFace <OrgnlAndCurFace> contains the following elements (see
"OriginalAndCurrentQuantities1" on page 519 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FaceAmount <FaceAmt> [1..1] Amount 519
   AmortisedValue <AmtsdVal> [1..1] Amount 519
7.1.16 Frequency
7.1.16.1  Frequency25Choice
Definition: Choice of format for a frequency, for example, the frequency of delivery of a statement.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 274
Or}   Proprietary <Prtry> [1..1] ± 274
7.1.16.1.1  Code <Cd>
Presence: [1..1]
Definition: Frequency expressed as an ISO 20022 code.
Datatype: "EventFrequency4Code" on page 625
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
ADHO Adhoc Event takes place as necessary.
MNTH Monthly Event takes place every month or once a
month.
DAIL Daily Event takes place every day.
INDA IntraDay Event takes place several times a day.
WEEK Weekly Event takes place once a week.
7.1.16.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Frequency expressed as a proprietary code.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 274 February 2025
```

