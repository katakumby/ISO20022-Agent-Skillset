---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.16 Organisation Identification", "16.1.16.1 OrganisationIdentification29", "16.1.16.1.3 Other <Othr>", "16.1.16.1.3.1 Identification <Id>"]
file_pages: [1033]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.16.1.3.1 Identification <Id>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1033 to 1033.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1033

```text
Other <Othr> contains the following GenericOrganisationIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1033
   SchemeName <SchmeNm> [0..1]  1033
{Or     Code <Cd> [1..1] CodeSet 1033
Or}     Proprietary <Prtry> [1..1] Text 1033
   Issuer <Issr> [0..1] Text 1033
16.1.16.1.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max35Text" on page 1251
16.1.16.1.3.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
OrganisationIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1033
Or}   Proprietary <Prtry> [1..1] Text 1033
16.1.16.1.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalOrganisationIdentification1Code" on page 1210
16.1.16.1.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 1251
16.1.16.1.3.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 1251
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1033 February 2026
```

