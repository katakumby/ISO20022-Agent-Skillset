---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.3 Party Identification", "3.1.3.1 PartyIdentification272", "3.1.3.1.3 Identification <Id>", "3.1.3.1.3.2 PrivateIdentification <PrvtId>", "3.1.3.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>", "3.1.3.1.3.2.1.3 CityOfBirth <CityOfBirth>"]
file_pages: [40]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.3.1.3.2.1.3 CityOfBirth <CityOfBirth>

Source: [src-000011](../../../../../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf). Locator: one-based file pages 40 to 40.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
3.1.3.1.3.2.1.3  CityOfBirth <CityOfBirth>
Presence: [1..1]
Definition: City where a person was born.
Datatype: "Max35Text" on page 57
3.1.3.1.3.2.1.4  CountryOfBirth <CtryOfBirth>
Presence: [1..1]
Definition: Country where a person was born.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 51
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
3.1.3.1.3.2.2  Other <Othr>
Presence: [0..*]
Definition: Unique identification of a person, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericPersonIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 40
   SchemeName <SchmeNm> [0..1]  40
{Or     Code <Cd> [1..1] CodeSet 41
Or}     Proprietary <Prtry> [1..1] Text 41
   Issuer <Issr> [0..1] Text 41
3.1.3.1.3.2.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max256Text" on page 56
3.1.3.1.3.2.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 40 March 2024
```

