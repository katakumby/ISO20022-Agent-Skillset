---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.35 RemittanceInformation <RmtInf>", "3.4.2.35.2 Structured <Strd>", "3.4.2.35.2.6 TaxRemittance <TaxRmt>"]
file_pages: [227, 228]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.35.2.6 TaxRemittance <TaxRmt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 227 to 228.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 227

```text
Invoicee <Invcee> contains the following elements (see "PartyIdentification272" on page 1193 for
details)
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
3.4.2.35.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
227 March 2026
```

## File page 228

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 229
   Debtor <Dbtr> [0..1] ± 229
   UltimateDebtor <UltmtDbtr> [0..1] ± 229
   AdministrationZone <AdmstnZone> [0..1] Text 230
   ReferenceNumber <RefNb> [0..1] Text 230
   Method <Mtd> [0..1] Text 230
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C11 230
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C11 231
   Date <Dt> [0..1] Date 231
   SequenceNumber <SeqNb> [0..1] Quantity 231
   Record <Rcrd> [0..*]  231
     Type <Tp> [0..1] Text 232
     Category <Ctgy> [0..1] Text 232
     CategoryDetails <CtgyDtls> [0..1] Text 232
     DebtorStatus <DbtrSts> [0..1] Text 233
     CertificateIdentification <CertId> [0..1] Text 233
     FormsCode <FrmsCd> [0..1] Text 233
     Period <Prd> [0..1]  233
       Year <Yr> [0..1] Year 233
       Type <Tp> [0..1] CodeSet 233
       FromToDate <FrToDt> [0..1] ± 234
     TaxAmount <TaxAmt> [0..1]  235
       Rate <Rate> [0..1] Rate 235
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C11 235
       TotalAmount <TtlAmt> [0..1] Amount C2, C11 235
       Details <Dtls> [0..*]  236
         Period <Prd> [0..1]  236
           Year <Yr> [0..1] Year 236
           Type <Tp> [0..1] CodeSet 237
           FromToDate <FrToDt> [0..1] ± 237
         Amount <Amt> [1..1] Amount C2, C11 238
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
228 March 2026
```

