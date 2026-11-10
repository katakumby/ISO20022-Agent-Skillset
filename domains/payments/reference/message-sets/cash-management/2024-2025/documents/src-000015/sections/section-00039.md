---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.7 Servicer <Svcr>"]
file_pages: [69]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.7 Servicer <Svcr>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 69 to 69.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 69

```text
Owner <Ownr> contains the following elements (see "PartyIdentification272" on page 823 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 824
   PostalAddress <PstlAdr> [0..1] ± 825
   Identification <Id> [0..1]  825
{Or     OrganisationIdentification <OrgId> [1..1]  826
       AnyBIC <AnyBIC> [0..1] IdentifierSet C2 827
       LEI <LEI> [0..1] IdentifierSet 827
       Other <Othr> [0..*]  827
         Identification <Id> [1..1] Text 828
         SchemeName <SchmeNm> [0..1]  828
{Or           Code <Cd> [1..1] CodeSet 828
Or}           Proprietary <Prtry> [1..1] Text 828
         Issuer <Issr> [0..1] Text 828
Or}     PrivateIdentification <PrvtId> [1..1]  828
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  829
         BirthDate <BirthDt> [1..1] Date 829
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 829
         CityOfBirth <CityOfBirth> [1..1] Text 830
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 830
       Other <Othr> [0..*]  830
         Identification <Id> [1..1] Text 830
         SchemeName <SchmeNm> [0..1]  830
{Or           Code <Cd> [1..1] CodeSet 831
Or}           Proprietary <Prtry> [1..1] Text 831
         Issuer <Issr> [0..1] Text 831
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C3 831
   ContactDetails <CtctDtls> [0..1] ± 831
3.4.2.1.2.1.7  Servicer <Svcr>
Presence: [0..1]
Definition: Servicer of the account which is being queried.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 69 February 2025
```

