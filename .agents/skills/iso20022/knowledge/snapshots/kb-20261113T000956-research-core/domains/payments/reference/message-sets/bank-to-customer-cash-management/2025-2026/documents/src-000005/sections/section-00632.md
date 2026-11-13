---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.16 Party Identification", "6.1.16.1 PartyIdentification272", "6.1.16.1.3 Identification <Id>", "6.1.16.1.3.2 PrivateIdentification <PrvtId>", "6.1.16.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>"]
file_pages: [865]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.16.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 865 to 865.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 865

```text
Definition: Unique and unambiguous identification of a person, for example a passport.
PrivateIdentification <PrvtId> contains the following PersonIdentification18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  865
     BirthDate <BirthDt> [1..1] Date 865
     ProvinceOfBirth <PrvcOfBirth> [0..1] Text 865
     CityOfBirth <CityOfBirth> [1..1] Text 866
     CountryOfBirth <CtryOfBirth> [1..1] CodeSet C4 866
   Other <Othr> [0..*]  866
     Identification <Id> [1..1] Text 866
     SchemeName <SchmeNm> [0..1]  866
{Or       Code <Cd> [1..1] CodeSet 867
Or}       Proprietary <Prtry> [1..1] Text 867
     Issuer <Issr> [0..1] Text 867
6.1.16.1.3.2.1  DateAndPlaceOfBirth <DtAndPlcOfBirth>
Presence: [0..1]
Definition: Date and place of birth of a person.
DateAndPlaceOfBirth <DtAndPlcOfBirth> contains the following DateAndPlaceOfBirth1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BirthDate <BirthDt> [1..1] Date 865
   ProvinceOfBirth <PrvcOfBirth> [0..1] Text 865
   CityOfBirth <CityOfBirth> [1..1] Text 866
   CountryOfBirth <CtryOfBirth> [1..1] CodeSet C4 866
6.1.16.1.3.2.1.1  BirthDate <BirthDt>
Presence: [1..1]
Definition: Date on which a person is born.
Datatype: "ISODate" on page 908
6.1.16.1.3.2.1.2  ProvinceOfBirth <PrvcOfBirth>
Presence: [0..1]
Definition: Province where a person was born.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
865 March 2026
```

