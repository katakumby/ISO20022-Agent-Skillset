---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.2 CancellationReport <CxlRpt>", "15.4.2.2.1 RegulatoryData <RgltryData>", "15.4.2.2.1.2 Invoicee <Invcee>"]
file_pages: [335]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.2.1.2 Invoicee <Invcee>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 335 to 335.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 335

```text
Invoicer <Invcr> contains the following elements (see "PartyIdentification272" on page 3068 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 3068
   PostalAddress <PstlAdr> [0..1] ± 3069
   Identification <Id> [0..1]  3069
{Or     OrganisationIdentification <OrgId> [1..1]  3070
       AnyBIC <AnyBIC> [0..1] IdentifierSet C2 3071
       LEI <LEI> [0..1] IdentifierSet 3071
       Other <Othr> [0..*]  3071
         Identification <Id> [1..1] Text 3072
         SchemeName <SchmeNm> [0..1]  3072
{Or           Code <Cd> [1..1] CodeSet 3072
Or}           Proprietary <Prtry> [1..1] Text 3072
         Issuer <Issr> [0..1] Text 3072
Or}     PrivateIdentification <PrvtId> [1..1]  3072
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  3073
         BirthDate <BirthDt> [1..1] Date 3073
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 3073
         CityOfBirth <CityOfBirth> [1..1] Text 3074
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 3074
       Other <Othr> [0..*]  3074
         Identification <Id> [1..1] Text 3074
         SchemeName <SchmeNm> [0..1]  3074
{Or           Code <Cd> [1..1] CodeSet 3075
Or}           Proprietary <Prtry> [1..1] Text 3075
         Issuer <Issr> [0..1] Text 3075
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C3 3075
   ContactDetails <CtctDtls> [0..1] ± 3075
15.4.2.2.1.2  Invoicee <Invcee>
Presence: [1..1]
Definition: Identification of the party to whom an invoice is issued, when it is different from the debtor or
ultimate debtor.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 335 August 2026
```

