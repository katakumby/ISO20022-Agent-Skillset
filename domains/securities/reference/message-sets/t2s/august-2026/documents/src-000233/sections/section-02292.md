---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.8 PartyIdentification272", "82.1.20.8.3 Identification <Id>", "82.1.20.8.3.2 PrivateIdentification <PrvtId>", "82.1.20.8.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>"]
file_pages: [3073]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.8.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3073 to 3073.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3073

```text
Definition: Unique and unambiguous identification of a person, for example a passport.
PrivateIdentification <PrvtId> contains the following PersonIdentification18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  3073
     BirthDate <BirthDt> [1..1] Date 3073
     ProvinceOfBirth <PrvcOfBirth> [0..1] Text 3073
     CityOfBirth <CityOfBirth> [1..1] Text 3074
     CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 3074
   Other <Othr> [0..*]  3074
     Identification <Id> [1..1] Text 3074
     SchemeName <SchmeNm> [0..1]  3074
{Or       Code <Cd> [1..1] CodeSet 3075
Or}       Proprietary <Prtry> [1..1] Text 3075
     Issuer <Issr> [0..1] Text 3075
82.1.20.8.3.2.1  DateAndPlaceOfBirth <DtAndPlcOfBirth>
Presence: [0..1]
Definition: Date and place of birth of a person.
DateAndPlaceOfBirth <DtAndPlcOfBirth> contains the following DateAndPlaceOfBirth1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BirthDate <BirthDt> [1..1] Date 3073
   ProvinceOfBirth <PrvcOfBirth> [0..1] Text 3073
   CityOfBirth <CityOfBirth> [1..1] Text 3074
   CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 3074
82.1.20.8.3.2.1.1  BirthDate <BirthDt>
Presence: [1..1]
Definition: Date on which a person is born.
Datatype: "ISODate" on page 3319
82.1.20.8.3.2.1.2  ProvinceOfBirth <PrvcOfBirth>
Presence: [0..1]
Definition: Province where a person was born.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3073 August 2026
```

