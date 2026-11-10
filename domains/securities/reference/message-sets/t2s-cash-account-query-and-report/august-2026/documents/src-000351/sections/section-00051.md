---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.3 Organisation <Org>", "3.4.3.1 FullLegalName <FullLglNm>"]
file_pages: [58]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.3.1 FullLegalName <FullLglNm>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 58 to 58.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 58

```text
Organisation <Org> contains the following Organisation42 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FullLegalName <FullLglNm> [1..1] Text 58
   TradingName <TradgNm> [0..1] Text 58
   CountryOfOperation <CtryOfOpr> [1..1] CodeSet C7 59
   RegistrationDate <RegnDt> [0..1] Date 59
   OperationalAddress <OprlAdr> [0..1] ± 59
   BusinessAddress <BizAdr> [0..1] ± 60
   LegalAddress <LglAdr> [1..1] ± 61
   BillingAddress <BllgAdr> [0..1] ± 62
   OrganisationIdentification <OrgId> [1..1]  63
     AnyBIC <AnyBIC> [0..1] IdentifierSet C3 64
     LEI <LEI> [0..1] IdentifierSet 64
     Other <Othr> [0..*]  64
       Identification <Id> [1..1] Text 65
       SchemeName <SchmeNm> [0..1]  65
{Or         Code <Cd> [1..1] CodeSet 65
Or}         Proprietary <Prtry> [1..1] Text 65
       Issuer <Issr> [0..1] Text 65
   RepresentativeOfficer <RprtvOffcr> [0..*] ± 65
   TreasuryManager <TrsrMgr> [0..1] ± 66
   MainMandateHolder <MainMndtHldr> [0..*] ± 67
   Sender <Sndr> [0..*] ± 68
   LegalRepresentative <LglRprtv> [0..*] ± 69
3.4.3.1  FullLegalName <FullLglNm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 183
3.4.3.2  TradingName <TradgNm>
Presence: [0..1]
Definition: Name used by a business for commercial purposes, although its registered legal name, used
for contracts and other formal situations, may be another.
Datatype: "Max350Text" on page 183
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 58 August 2026
```

