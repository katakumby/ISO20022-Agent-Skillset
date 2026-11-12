---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.8 Party Identification", "7.1.8.2 PartyIdentification272", "7.1.8.2.1 Name <Nm>"]
file_pages: [155]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.8.2.1 Name <Nm>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 155 to 155.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 155

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 155
   PostalAddress <PstlAdr> [0..1] ± 156
   Identification <Id> [0..1]  156
{Or     OrganisationIdentification <OrgId> [1..1]  157
       AnyBIC <AnyBIC> [0..1] IdentifierSet C3 158
       LEI <LEI> [0..1] IdentifierSet 158
       Other <Othr> [0..*]  158
         Identification <Id> [1..1] Text 159
         SchemeName <SchmeNm> [0..1]  159
{Or           Code <Cd> [1..1] CodeSet 159
Or}           Proprietary <Prtry> [1..1] Text 159
         Issuer <Issr> [0..1] Text 159
Or}     PrivateIdentification <PrvtId> [1..1]  159
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  160
         BirthDate <BirthDt> [1..1] Date 160
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 160
         CityOfBirth <CityOfBirth> [1..1] Text 161
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C7 161
       Other <Othr> [0..*]  161
         Identification <Id> [1..1] Text 161
         SchemeName <SchmeNm> [0..1]  161
{Or           Code <Cd> [1..1] CodeSet 162
Or}           Proprietary <Prtry> [1..1] Text 162
         Issuer <Issr> [0..1] Text 162
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C7 162
   ContactDetails <CtctDtls> [0..1] ± 162
7.1.8.2.1  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 182
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 155 August 2026
```

