---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.3 Organisation <Org>", "3.4.3.12 MainMandateHolder <MainMndtHldr>"]
file_pages: [67]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.3.12 MainMandateHolder <MainMndtHldr>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 67 to 67.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 67

```text
TreasuryManager <TrsrMgr> contains the following elements (see "PartyIdentification274" on
page 148 for details)
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
3.4.3.12  MainMandateHolder <MainMndtHldr>
Presence: [0..*]
Definition: Person that has the mandate to delegate authority, to assign mandates to other individuals
(mandate holders) to perform specific bank operations on the account.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 67 August 2026
```

