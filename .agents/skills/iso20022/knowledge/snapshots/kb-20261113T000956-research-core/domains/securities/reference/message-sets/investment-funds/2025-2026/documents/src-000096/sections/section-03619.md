---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.30 AdditiononalInformation13", "66.1.28.30.6 Status <Sts>", "66.1.28.30.6.2 Proprietary <Prtry>"]
file_pages: [4869]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.30.6.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4869 to 4869.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4869

```text
CodeName Name Definition
ACTV Active Status of the restriction is active.
INAC Inactive Status of the restriction is inactive.
66.1.28.30.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Status of the restriction expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.28.30.7  Period <Prd>
Presence: [0..1]
Definition: Period of the restriction.
Period <Prd> contains the following elements (see "DateTimePeriod2" on page 4465 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 4466
   ToDateTime <ToDtTm> [0..1] DateTime 4466
66.1.28.31  CancellationReason32Choice
Definition: Choice of format for the cancellation reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] Text 4869
Or}   Proprietary <Prtry> [1..1] ± 4869
66.1.28.31.1  Code <Cd>
Presence: [1..1]
Definition: Cancellation reason expressed as a code.
Datatype: "Max35Text" on page 5403
66.1.28.31.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cancellation reason expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4869 May 2026
```

