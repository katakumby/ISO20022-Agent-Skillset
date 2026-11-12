---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.11 RemittanceInformation <RmtInf>", "3.4.3.7.12.11.2 Structured <Strd>", "3.4.3.7.12.11.2.6 TaxRemittance <TaxRmt>"]
file_pages: [239, 240]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.11.2.6 TaxRemittance <TaxRmt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 239 to 240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 239

```text
Invoicee <Invcee> contains the following elements (see "PartyIdentification272" on page 554 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 555
   PostalAddress <PstlAdr> [0..1] ± 556
   Identification <Id> [0..1]  556
{Or     OrganisationIdentification <OrgId> [1..1]  557
       AnyBIC <AnyBIC> [0..1] IdentifierSet C3 558
       LEI <LEI> [0..1] IdentifierSet 558
       Other <Othr> [0..*]  558
         Identification <Id> [1..1] Text 559
         SchemeName <SchmeNm> [0..1]  559
{Or           Code <Cd> [1..1] CodeSet 559
Or}           Proprietary <Prtry> [1..1] Text 559
         Issuer <Issr> [0..1] Text 559
Or}     PrivateIdentification <PrvtId> [1..1]  559
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  560
         BirthDate <BirthDt> [1..1] Date 560
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 560
         CityOfBirth <CityOfBirth> [1..1] Text 561
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C18 561
       Other <Othr> [0..*]  561
         Identification <Id> [1..1] Text 561
         SchemeName <SchmeNm> [0..1]  561
{Or           Code <Cd> [1..1] CodeSet 562
Or}           Proprietary <Prtry> [1..1] Text 562
         Issuer <Issr> [0..1] Text 562
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C18 562
   ContactDetails <CtctDtls> [0..1] ± 562
3.4.3.7.12.11.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 239 March 2026
```

## File page 240

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 241
   Debtor <Dbtr> [0..1] ± 241
   UltimateDebtor <UltmtDbtr> [0..1] ± 241
   AdministrationZone <AdmstnZone> [0..1] Text 242
   ReferenceNumber <RefNb> [0..1] Text 242
   Method <Mtd> [0..1] Text 242
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C8 242
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C8 243
   Date <Dt> [0..1] Date 243
   SequenceNumber <SeqNb> [0..1] Quantity 243
   Record <Rcrd> [0..*]  243
     Type <Tp> [0..1] Text 244
     Category <Ctgy> [0..1] Text 244
     CategoryDetails <CtgyDtls> [0..1] Text 244
     DebtorStatus <DbtrSts> [0..1] Text 245
     CertificateIdentification <CertId> [0..1] Text 245
     FormsCode <FrmsCd> [0..1] Text 245
     Period <Prd> [0..1]  245
       Year <Yr> [0..1] Year 245
       Type <Tp> [0..1] CodeSet 245
       FromToDate <FrToDt> [0..1] ± 246
     TaxAmount <TaxAmt> [0..1]  247
       Rate <Rate> [0..1] Rate 247
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 247
       TotalAmount <TtlAmt> [0..1] Amount C2, C8 247
       Details <Dtls> [0..*]  248
         Period <Prd> [0..1]  248
           Year <Yr> [0..1] Year 248
           Type <Tp> [0..1] CodeSet 249
           FromToDate <FrToDt> [0..1] ± 249
         Amount <Amt> [1..1] Amount C2, C8 250
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 240 March 2026
```

