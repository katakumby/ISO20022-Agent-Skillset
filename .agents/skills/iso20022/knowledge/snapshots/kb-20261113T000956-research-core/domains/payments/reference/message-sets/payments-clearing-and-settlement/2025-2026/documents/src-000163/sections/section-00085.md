---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.12 UltimateDebtor <UltmtDbtr>", "2.4.3.18.12.2 Agent <Agt>"]
file_pages: [118]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.12.2 Agent <Agt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 118 to 118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 118

```text
Party <Pty> contains the following elements (see "PartyIdentification272" on page 1193 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 1194
   PostalAddress <PstlAdr> [0..1] ± 1195
   Identification <Id> [0..1]  1195
{Or     OrganisationIdentification <OrgId> [1..1]  1196
       AnyBIC <AnyBIC> [0..1] IdentifierSet C4 1197
       LEI <LEI> [0..1] IdentifierSet 1197
       Other <Othr> [0..*]  1197
         Identification <Id> [1..1] Text 1198
         SchemeName <SchmeNm> [0..1]  1198
{Or           Code <Cd> [1..1] CodeSet 1198
Or}           Proprietary <Prtry> [1..1] Text 1198
         Issuer <Issr> [0..1] Text 1198
Or}     PrivateIdentification <PrvtId> [1..1]  1198
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  1199
         BirthDate <BirthDt> [1..1] Date 1199
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 1199
         CityOfBirth <CityOfBirth> [1..1] Text 1200
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C10 1200
       Other <Othr> [0..*]  1200
         Identification <Id> [1..1] Text 1200
         SchemeName <SchmeNm> [0..1]  1200
{Or           Code <Cd> [1..1] CodeSet 1201
Or}           Proprietary <Prtry> [1..1] Text 1201
         Issuer <Issr> [0..1] Text 1201
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C10 1201
   ContactDetails <CtctDtls> [0..1] ± 1201
2.4.3.18.12.2  Agent <Agt>
Presence: [1..1]
Definition: Identification of a financial institution.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
118 March 2026
```

