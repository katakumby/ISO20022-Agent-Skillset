---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.60 ProcessingPosition7Choice", "35.1.16.60.2 Proprietary <Prtry>"]
file_pages: [1599]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.60.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1599 to 1599.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1599

```text
35.1.16.60.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Processing position expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.61  AutomaticBorrowing7Choice
Definition: Choice of format for the automatic borrowing information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1599
Or}   Proprietary <Prtry> [1..1] ± 1599
35.1.16.61.1  Code <Cd>
Presence: [1..1]
Definition: Condition for automatic borrowing expressed as an ISO 20022 code.
Datatype: "AutoBorrowing2Code" on page 2046
CodeName Name Definition
LAMI LastResort Only last resort borrowing should be
considered to make settlement occur.
NBOR NoAutomatic No automatic borrowing should take
place.
YBOR Automatic Automatic borrowing should take place.
RTRN Return Return of stocks should take place.
35.1.16.61.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Condition for automatic borrowing expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1599 March 2026
```

