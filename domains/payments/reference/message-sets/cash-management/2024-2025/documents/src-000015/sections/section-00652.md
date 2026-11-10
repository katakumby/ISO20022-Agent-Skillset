---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.12 Party Identification", "37.1.12.1 PartyIdentification272", "37.1.12.1.3 Identification <Id>", "37.1.12.1.3.2 PrivateIdentification <PrvtId>", "37.1.12.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>"]
file_pages: [829]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.12.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 829 to 829.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 829

```text
Definition: Unique and unambiguous identification of a person, for example a passport.
PrivateIdentification <PrvtId> contains the following PersonIdentification18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  829
     BirthDate <BirthDt> [1..1] Date 829
     ProvinceOfBirth <PrvcOfBirth> [0..1] Text 829
     CityOfBirth <CityOfBirth> [1..1] Text 830
     CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 830
   Other <Othr> [0..*]  830
     Identification <Id> [1..1] Text 830
     SchemeName <SchmeNm> [0..1]  830
{Or       Code <Cd> [1..1] CodeSet 831
Or}       Proprietary <Prtry> [1..1] Text 831
     Issuer <Issr> [0..1] Text 831
37.1.12.1.3.2.1  DateAndPlaceOfBirth <DtAndPlcOfBirth>
Presence: [0..1]
Definition: Date and place of birth of a person.
DateAndPlaceOfBirth <DtAndPlcOfBirth> contains the following DateAndPlaceOfBirth1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BirthDate <BirthDt> [1..1] Date 829
   ProvinceOfBirth <PrvcOfBirth> [0..1] Text 829
   CityOfBirth <CityOfBirth> [1..1] Text 830
   CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 830
37.1.12.1.3.2.1.1  BirthDate <BirthDt>
Presence: [1..1]
Definition: Date on which a person is born.
Datatype: "ISODate" on page 883
37.1.12.1.3.2.1.2  ProvinceOfBirth <PrvcOfBirth>
Presence: [0..1]
Definition: Province where a person was born.
Datatype: "Max35Text" on page 889
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 829 February 2025
```

