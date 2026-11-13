---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.18 Person Identification", "16.1.18.1 PersonIdentification13", "16.1.18.1.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>", "16.1.18.1.1.4 CountryOfBirth <CtryOfBirth>"]
file_pages: [1054]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.18.1.1.4 CountryOfBirth <CtryOfBirth>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1054 to 1054.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1054

```text
Datatype: "Max35Text" on page 1251
16.1.18.1.1.4  CountryOfBirth <CtryOfBirth>
Presence: [1..1]
Definition: Country where a person was born.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
16.1.18.1.2  Other <Othr>
Presence: [0..*]
Definition: Unique identification of a person, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericPersonIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1054
   SchemeName <SchmeNm> [0..1]  1054
{Or     Code <Cd> [1..1] CodeSet 1055
Or}     Proprietary <Prtry> [1..1] Text 1055
   Issuer <Issr> [0..1] Text 1055
16.1.18.1.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max35Text" on page 1251
16.1.18.1.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
PersonIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1055
Or}   Proprietary <Prtry> [1..1] Text 1055
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1054 February 2026
```

