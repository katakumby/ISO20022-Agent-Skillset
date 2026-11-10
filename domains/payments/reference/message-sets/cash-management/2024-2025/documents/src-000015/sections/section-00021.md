---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2.2.6 AccountServicer <AcctSvcr>"]
file_pages: [40]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.2.6 AccountServicer <AcctSvcr>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 40 to 40.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification272" on
page 823 for details)
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
2.4.2.2.2.2.6  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Servicer of the account which is being queried.
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 40 February 2025
```

