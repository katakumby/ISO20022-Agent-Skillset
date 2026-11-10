---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.3 Party Identification", "3.1.3.1 PartyIdentification272", "3.1.3.1.3 Identification <Id>", "3.1.3.1.3.2 PrivateIdentification <PrvtId>", "3.1.3.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>"]
file_pages: [39]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.3.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>

Source: [src-000011](../../../../../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf). Locator: one-based file pages 39 to 39.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 39

```text
Definition: Unique and unambiguous identification of a person, for example a passport.
PrivateIdentification <PrvtId> contains the following PersonIdentification18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  39
     BirthDate <BirthDt> [1..1] Date 39
     ProvinceOfBirth <PrvcOfBirth> [0..1] Text 39
     CityOfBirth <CityOfBirth> [1..1] Text 40
     CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 40
   Other <Othr> [0..*]  40
     Identification <Id> [1..1] Text 40
     SchemeName <SchmeNm> [0..1]  40
{Or       Code <Cd> [1..1] CodeSet 41
Or}       Proprietary <Prtry> [1..1] Text 41
     Issuer <Issr> [0..1] Text 41
3.1.3.1.3.2.1  DateAndPlaceOfBirth <DtAndPlcOfBirth>
Presence: [0..1]
Definition: Date and place of birth of a person.
DateAndPlaceOfBirth <DtAndPlcOfBirth> contains the following DateAndPlaceOfBirth1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BirthDate <BirthDt> [1..1] Date 39
   ProvinceOfBirth <PrvcOfBirth> [0..1] Text 39
   CityOfBirth <CityOfBirth> [1..1] Text 40
   CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 40
3.1.3.1.3.2.1.1  BirthDate <BirthDt>
Presence: [1..1]
Definition: Date on which a person is born.
Datatype: "ISODate" on page 53
3.1.3.1.3.2.1.2  ProvinceOfBirth <PrvcOfBirth>
Presence: [0..1]
Definition: Province where a person was born.
Datatype: "Max35Text" on page 57
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 39 March 2024
```

