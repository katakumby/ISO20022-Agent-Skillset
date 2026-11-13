---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.36 ModificationProcessingStatus9Choice"]
file_pages: [3175]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.36 ModificationProcessingStatus9Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3175 to 3175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3175

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.36  ModificationProcessingStatus9Choice
Definition: Choice of modification processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3175
Or}   Proprietary <Prtry> [1..1] ± 3175
82.1.30.36.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of a modification request.
Datatype: "ModificationProcessingStatus1Code" on page 3264
CodeName Name Definition
PACK Accepted Modification request has been
acknowledged for further processing by
the account servicer.
REJT Rejected Modification has been rejected for further
processing.
MODC Completed Modification has been completed.
DEND Denied Modification will not be executed.
MODP Pending Modification is pending. It is not known
at this time whether modified can be
executed.
REPR InRepair Modification request is in repair.
82.1.30.36.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of a modification request.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3175 August 2026
```

