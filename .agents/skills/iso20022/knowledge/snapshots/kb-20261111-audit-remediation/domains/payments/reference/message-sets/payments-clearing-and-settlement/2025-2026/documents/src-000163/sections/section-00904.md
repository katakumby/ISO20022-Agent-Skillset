---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.12 Party Identification", "10.1.12.1 PartyIdentification272", "10.1.12.1.3 Identification <Id>", "10.1.12.1.3.2 PrivateIdentification <PrvtId>", "10.1.12.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>"]
file_pages: [1199]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.12.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1199 to 1199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1199

```text
Definition: Unique and unambiguous identification of a person, for example a passport.
PrivateIdentification <PrvtId> contains the following PersonIdentification18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  1199
     BirthDate <BirthDt> [1..1] Date 1199
     ProvinceOfBirth <PrvcOfBirth> [0..1] Text 1199
     CityOfBirth <CityOfBirth> [1..1] Text 1200
     CountryOfBirth <CtryOfBirth> [1..1] CodeSet C10 1200
   Other <Othr> [0..*]  1200
     Identification <Id> [1..1] Text 1200
     SchemeName <SchmeNm> [0..1]  1200
{Or       Code <Cd> [1..1] CodeSet 1201
Or}       Proprietary <Prtry> [1..1] Text 1201
     Issuer <Issr> [0..1] Text 1201
10.1.12.1.3.2.1  DateAndPlaceOfBirth <DtAndPlcOfBirth>
Presence: [0..1]
Definition: Date and place of birth of a person.
DateAndPlaceOfBirth <DtAndPlcOfBirth> contains the following DateAndPlaceOfBirth1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BirthDate <BirthDt> [1..1] Date 1199
   ProvinceOfBirth <PrvcOfBirth> [0..1] Text 1199
   CityOfBirth <CityOfBirth> [1..1] Text 1200
   CountryOfBirth <CtryOfBirth> [1..1] CodeSet C10 1200
10.1.12.1.3.2.1.1  BirthDate <BirthDt>
Presence: [1..1]
Definition: Date on which a person is born.
Datatype: "ISODate" on page 1239
10.1.12.1.3.2.1.2  ProvinceOfBirth <PrvcOfBirth>
Presence: [0..1]
Definition: Province where a person was born.
Datatype: "Max35Text" on page 1246
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1199 March 2026
```

