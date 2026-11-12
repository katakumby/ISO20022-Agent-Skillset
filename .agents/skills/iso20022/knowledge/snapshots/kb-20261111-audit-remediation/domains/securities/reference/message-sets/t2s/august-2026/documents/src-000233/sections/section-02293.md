---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.8 PartyIdentification272", "82.1.20.8.3 Identification <Id>", "82.1.20.8.3.2 PrivateIdentification <PrvtId>", "82.1.20.8.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>", "82.1.20.8.3.2.1.3 CityOfBirth <CityOfBirth>"]
file_pages: [3074]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.8.3.2.1.3 CityOfBirth <CityOfBirth>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3074 to 3074.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3074

```text
82.1.20.8.3.2.1.3  CityOfBirth <CityOfBirth>
Presence: [1..1]
Definition: City where a person was born.
Datatype: "Max35Text" on page 3328
82.1.20.8.3.2.1.4  CountryOfBirth <CtryOfBirth>
Presence: [1..1]
Definition: Country where a person was born.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
82.1.20.8.3.2.2  Other <Othr>
Presence: [0..*]
Definition: Unique identification of a person, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericPersonIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 3074
   SchemeName <SchmeNm> [0..1]  3074
{Or     Code <Cd> [1..1] CodeSet 3075
Or}     Proprietary <Prtry> [1..1] Text 3075
   Issuer <Issr> [0..1] Text 3075
82.1.20.8.3.2.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max256Text" on page 3327
82.1.20.8.3.2.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3074 August 2026
```

