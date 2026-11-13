---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 camt.008.001.11 CancelTransactionV11", "7.4 Message Building Blocks", "7.4.4 CancellationReason <CxlRsn>", "7.4.4.2 Reason <Rsn>"]
file_pages: [362]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.008.001.11"]
---

# 7.4.4.2 Reason <Rsn>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 362 to 362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 362

```text
Originator <Orgtr> contains the following elements (see "PartyIdentification272" on page 823 for
details)
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
7.4.4.2  Reason <Rsn>
Presence: [0..1]
Definition: Specifies the reason for the cancellation.
Approved by the Payments SEG on 04 February 2025 camt.008.001.11 CancelTransactionV11
Cash Management - Maintenance 2024 - 2025 362 February 2025
```

