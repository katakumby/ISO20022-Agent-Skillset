---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.4 Organisation <Org>", "2.4.4.1 FullLegalName <FullLglNm>"]
file_pages: [14]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.4.1 FullLegalName <FullLglNm>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 14 to 14.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 14

```text
Organisation <Org> contains the following Organisation42 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FullLegalName <FullLglNm> [1..1] Text 14
   TradingName <TradgNm> [0..1] Text 14
   CountryOfOperation <CtryOfOpr> [1..1] CodeSet C4 15
   RegistrationDate <RegnDt> [0..1] Date 15
   OperationalAddress <OprlAdr> [0..1] ± 15
   BusinessAddress <BizAdr> [0..1] ± 16
   LegalAddress <LglAdr> [1..1] ± 17
   BillingAddress <BllgAdr> [0..1] ± 18
   OrganisationIdentification <OrgId> [1..1]  19
     AnyBIC <AnyBIC> [0..1] IdentifierSet C2 20
     LEI <LEI> [0..1] IdentifierSet 20
     Other <Othr> [0..*]  20
       Identification <Id> [1..1] Text 21
       SchemeName <SchmeNm> [0..1]  21
{Or         Code <Cd> [1..1] CodeSet 21
Or}         Proprietary <Prtry> [1..1] Text 21
       Issuer <Issr> [0..1] Text 21
   RepresentativeOfficer <RprtvOffcr> [0..*] ± 21
   TreasuryManager <TrsrMgr> [0..1] ± 22
   MainMandateHolder <MainMndtHldr> [0..*] ± 23
   Sender <Sndr> [0..*] ± 24
   LegalRepresentative <LglRprtv> [0..*] ± 25
2.4.4.1  FullLegalName <FullLglNm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 183
2.4.4.2  TradingName <TradgNm>
Presence: [0..1]
Definition: Name used by a business for commercial purposes, although its registered legal name, used
for contracts and other formal situations, may be another.
Datatype: "Max350Text" on page 183
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 14 August 2026
```

