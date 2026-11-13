---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.11 RemittanceInformation <RmtInf>", "2.4.3.18.11.2 Structured <Strd>", "2.4.3.18.11.2.6 TaxRemittance <TaxRmt>"]
file_pages: [99, 100]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.11.2.6 TaxRemittance <TaxRmt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 99 to 100.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 99

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
2.4.3.18.11.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
99 March 2026
```

## File page 100

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 101
   Debtor <Dbtr> [0..1] ± 101
   UltimateDebtor <UltmtDbtr> [0..1] ± 101
   AdministrationZone <AdmstnZone> [0..1] Text 102
   ReferenceNumber <RefNb> [0..1] Text 102
   Method <Mtd> [0..1] Text 102
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C8 102
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C8 103
   Date <Dt> [0..1] Date 103
   SequenceNumber <SeqNb> [0..1] Quantity 103
   Record <Rcrd> [0..*]  103
     Type <Tp> [0..1] Text 104
     Category <Ctgy> [0..1] Text 104
     CategoryDetails <CtgyDtls> [0..1] Text 104
     DebtorStatus <DbtrSts> [0..1] Text 105
     CertificateIdentification <CertId> [0..1] Text 105
     FormsCode <FrmsCd> [0..1] Text 105
     Period <Prd> [0..1]  105
       Year <Yr> [0..1] Year 105
       Type <Tp> [0..1] CodeSet 105
       FromToDate <FrToDt> [0..1] ± 106
     TaxAmount <TaxAmt> [0..1]  107
       Rate <Rate> [0..1] Rate 107
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 107
       TotalAmount <TtlAmt> [0..1] Amount C2, C8 107
       Details <Dtls> [0..*]  108
         Period <Prd> [0..1]  108
           Year <Yr> [0..1] Year 108
           Type <Tp> [0..1] CodeSet 109
           FromToDate <FrToDt> [0..1] ± 109
         Amount <Amt> [1..1] Amount C2, C8 110
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
100 March 2026
```

