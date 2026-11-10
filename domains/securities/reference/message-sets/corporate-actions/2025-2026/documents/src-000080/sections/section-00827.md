---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.17 Party Identification", "16.1.17.7 PartyIdentification120Choice"]
file_pages: [1045]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.17.7 PartyIdentification120Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1045 to 1045.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1045

```text
PrivateIdentification <PrvtId> contains the following elements (see "PersonIdentification13" on
page 1052 for details)
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
16.1.17.7  PartyIdentification120Choice
Definition: Choice between different formats for the identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
16.1.17.7.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C1 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 1244
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1045 February 2026
```

