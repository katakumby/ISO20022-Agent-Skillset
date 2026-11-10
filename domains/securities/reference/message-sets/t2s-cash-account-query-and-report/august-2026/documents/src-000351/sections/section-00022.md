---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.4 Organisation <Org>", "2.4.4.14 LegalRepresentative <LglRprtv>"]
file_pages: [25]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.4.14 LegalRepresentative <LglRprtv>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 25 to 25.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 25

```text
Sender <Sndr> contains the following elements (see "PartyIdentification274" on page 148 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 149
   PostalAddress <PstlAdr> [0..1] ± 149
   Identification <Id> [0..1]  150
     DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  151
       BirthDate <BirthDt> [1..1] Date 151
       ProvinceOfBirth <PrvcOfBirth> [0..1] Text 151
       CityOfBirth <CityOfBirth> [1..1] Text 151
       CountryOfBirth <CtryOfBirth> [1..1] CodeSet C7 152
     Other <Othr> [0..*]  152
       Identification <Id> [1..1] Text 152
       SchemeName <SchmeNm> [0..1]  152
{Or         Code <Cd> [1..1] CodeSet 153
Or}         Proprietary <Prtry> [1..1] Text 153
       Issuer <Issr> [0..1] Text 153
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C7 153
   ContactDetails <CtctDtls> [0..1] ± 153
2.4.4.14  LegalRepresentative <LglRprtv>
Presence: [0..*]
Definition: Person that is officially and legally mandated to represent the organisation. Depending on
legislation, the legal representative(s) might for instance be assigned by the Board, identified in the by-
laws of the organisation, be publicly announced in the official journal of a country, etc.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 25 August 2026
```

