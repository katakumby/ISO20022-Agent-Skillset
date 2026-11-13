---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.7 Party Identification", "4.1.7.3 PartyIdentification272", "4.1.7.3.3 Identification <Id>", "4.1.7.3.3.2 PrivateIdentification <PrvtId>", "4.1.7.3.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>"]
file_pages: [129]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.7.3.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 129 to 129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 129

```text
Definition: Unique and unambiguous identification of a person, for example a passport.
PrivateIdentification <PrvtId> contains the following PersonIdentification18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  129
     BirthDate <BirthDt> [1..1] Date 129
     ProvinceOfBirth <PrvcOfBirth> [0..1] Text 129
     CityOfBirth <CityOfBirth> [1..1] Text 130
     CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 130
   Other <Othr> [0..*]  130
     Identification <Id> [1..1] Text 130
     SchemeName <SchmeNm> [0..1]  130
{Or       Code <Cd> [1..1] CodeSet 131
Or}       Proprietary <Prtry> [1..1] Text 131
     Issuer <Issr> [0..1] Text 131
4.1.7.3.3.2.1  DateAndPlaceOfBirth <DtAndPlcOfBirth>
Presence: [0..1]
Definition: Date and place of birth of a person.
DateAndPlaceOfBirth <DtAndPlcOfBirth> contains the following DateAndPlaceOfBirth1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BirthDate <BirthDt> [1..1] Date 129
   ProvinceOfBirth <PrvcOfBirth> [0..1] Text 129
   CityOfBirth <CityOfBirth> [1..1] Text 130
   CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 130
4.1.7.3.3.2.1.1  BirthDate <BirthDt>
Presence: [1..1]
Definition: Date on which a person is born.
Datatype: "ISODate" on page 148
4.1.7.3.3.2.1.2  ProvinceOfBirth <PrvcOfBirth>
Presence: [0..1]
Definition: Province where a person was born.
Datatype: "Max35Text" on page 153
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 129 December 2025
```

