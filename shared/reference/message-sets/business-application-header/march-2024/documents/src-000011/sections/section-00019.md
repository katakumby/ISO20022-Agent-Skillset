---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["2 head.001.001.04 BusinessApplicationHeaderV04", "2.4 Message Building Blocks", "2.4.14 Related <Rltd>", "2.4.14.3 To <To>", "2.4.14.3.2 FinancialInstitutionIdentification <FIId>"]
file_pages: [21]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.04"]
---

# 2.4.14.3.2 FinancialInstitutionIdentification <FIId>

Source: [src-000011](../../../../../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf). Locator: one-based file pages 21 to 21.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification272" on
page 33 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 34
   PostalAddress <PstlAdr> [0..1] ± 35
   Identification <Id> [0..1]  35
{Or     OrganisationIdentification <OrgId> [1..1]  36
       AnyBIC <AnyBIC> [0..1] IdentifierSet C1 37
       LEI <LEI> [0..1] IdentifierSet 37
       Other <Othr> [0..*]  37
         Identification <Id> [1..1] Text 38
         SchemeName <SchmeNm> [0..1]  38
{Or           Code <Cd> [1..1] CodeSet 38
Or}           Proprietary <Prtry> [1..1] Text 38
         Issuer <Issr> [0..1] Text 38
Or}     PrivateIdentification <PrvtId> [1..1]  38
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  39
         BirthDate <BirthDt> [1..1] Date 39
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 39
         CityOfBirth <CityOfBirth> [1..1] Text 40
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C3 40
       Other <Othr> [0..*]  40
         Identification <Id> [1..1] Text 40
         SchemeName <SchmeNm> [0..1]  40
{Or           Code <Cd> [1..1] CodeSet 41
Or}           Proprietary <Prtry> [1..1] Text 41
         Issuer <Issr> [0..1] Text 41
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C3 41
   ContactDetails <CtctDtls> [0..1] ± 41
2.4.14.3.2  FinancialInstitutionIdentification <FIId>
Presence: [1..1]
Definition: Identification of a financial institution.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 21 March 2024
```

