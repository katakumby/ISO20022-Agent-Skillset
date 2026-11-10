---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.1 Financial Institution Identification", "3.1.1.3 GenericFinancialIdentification1", "3.1.1.3.1 Identification <Id>"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.1.3.1 Identification <Id>

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
3.1.1.3.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max35Text" on page 57
3.1.1.3.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
FinancialIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 32
Or}   Proprietary <Prtry> [1..1] Text 32
3.1.1.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalFinancialInstitutionIdentification1Code" on page 52
3.1.1.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 57
3.1.1.3.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 57
3.1.2 Identification Information
3.1.2.1  GenericIdentification30
Definition: Information related to an identification, for example, party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 33
   Issuer <Issr> [1..1] Text 33
   SchemeName <SchmeNm> [0..1] Text 33
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 32 March 2024
```

