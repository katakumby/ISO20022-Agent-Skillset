---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.8 PartyIdentification272", "7.1.19.8.3 Identification <Id>", "7.1.19.8.3.2 PrivateIdentification <PrvtId>", "7.1.19.8.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>"]
file_pages: [427]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.8.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 427 to 427.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 427

```text
Definition: Unique and unambiguous identification of a person, for example a passport.
PrivateIdentification <PrvtId> contains the following PersonIdentification18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  427
     BirthDate <BirthDt> [1..1] Date 427
     ProvinceOfBirth <PrvcOfBirth> [0..1] Text 427
     CityOfBirth <CityOfBirth> [1..1] Text 428
     CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 428
   Other <Othr> [0..*]  428
     Identification <Id> [1..1] Text 428
     SchemeName <SchmeNm> [0..1]  428
{Or       Code <Cd> [1..1] CodeSet 429
Or}       Proprietary <Prtry> [1..1] Text 429
     Issuer <Issr> [0..1] Text 429
7.1.19.8.3.2.1  DateAndPlaceOfBirth <DtAndPlcOfBirth>
Presence: [0..1]
Definition: Date and place of birth of a person.
DateAndPlaceOfBirth <DtAndPlcOfBirth> contains the following DateAndPlaceOfBirth1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BirthDate <BirthDt> [1..1] Date 427
   ProvinceOfBirth <PrvcOfBirth> [0..1] Text 427
   CityOfBirth <CityOfBirth> [1..1] Text 428
   CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 428
7.1.19.8.3.2.1.1  BirthDate <BirthDt>
Presence: [1..1]
Definition: Date on which a person is born.
Datatype: "ISODate" on page 550
7.1.19.8.3.2.1.2  ProvinceOfBirth <PrvcOfBirth>
Presence: [0..1]
Definition: Province where a person was born.
Datatype: "Max35Text" on page 557
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 427 March 2026
```

