---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.18 Person Identification", "16.1.18.1 PersonIdentification13", "16.1.18.1.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>"]
file_pages: [1053]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.18.1.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1053 to 1053.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1053

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  1053
     BirthDate <BirthDt> [1..1] Date 1053
     ProvinceOfBirth <PrvcOfBirth> [0..1] Text 1053
     CityOfBirth <CityOfBirth> [1..1] Text 1053
     CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 1054
   Other <Othr> [0..*]  1054
     Identification <Id> [1..1] Text 1054
     SchemeName <SchmeNm> [0..1]  1054
{Or       Code <Cd> [1..1] CodeSet 1055
Or}       Proprietary <Prtry> [1..1] Text 1055
     Issuer <Issr> [0..1] Text 1055
16.1.18.1.1  DateAndPlaceOfBirth <DtAndPlcOfBirth>
Presence: [0..1]
Definition: Date and place of birth of a person.
DateAndPlaceOfBirth <DtAndPlcOfBirth> contains the following DateAndPlaceOfBirth1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BirthDate <BirthDt> [1..1] Date 1053
   ProvinceOfBirth <PrvcOfBirth> [0..1] Text 1053
   CityOfBirth <CityOfBirth> [1..1] Text 1053
   CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 1054
16.1.18.1.1.1  BirthDate <BirthDt>
Presence: [1..1]
Definition: Date on which a person is born.
Datatype: "ISODate" on page 1243
16.1.18.1.1.2  ProvinceOfBirth <PrvcOfBirth>
Presence: [0..1]
Definition: Province where a person was born.
Datatype: "Max35Text" on page 1251
16.1.18.1.1.3  CityOfBirth <CityOfBirth>
Presence: [1..1]
Definition: City where a person was born.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1053 February 2026
```

