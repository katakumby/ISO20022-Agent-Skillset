---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.2 Structured <Strd>", "4.4.3.8.9.11.2.6 TaxRemittance <TaxRmt>"]
file_pages: [370, 371]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.2.6 TaxRemittance <TaxRmt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 370 to 371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 370

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
4.4.3.8.9.11.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 370 March 2026
```

## File page 371

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 372
   Debtor <Dbtr> [0..1] ± 372
   UltimateDebtor <UltmtDbtr> [0..1] ± 372
   AdministrationZone <AdmstnZone> [0..1] Text 373
   ReferenceNumber <RefNb> [0..1] Text 373
   Method <Mtd> [0..1] Text 373
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C9 373
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C9 374
   Date <Dt> [0..1] Date 374
   SequenceNumber <SeqNb> [0..1] Quantity 374
   Record <Rcrd> [0..*]  374
     Type <Tp> [0..1] Text 375
     Category <Ctgy> [0..1] Text 375
     CategoryDetails <CtgyDtls> [0..1] Text 375
     DebtorStatus <DbtrSts> [0..1] Text 376
     CertificateIdentification <CertId> [0..1] Text 376
     FormsCode <FrmsCd> [0..1] Text 376
     Period <Prd> [0..1]  376
       Year <Yr> [0..1] Year 376
       Type <Tp> [0..1] CodeSet 376
       FromToDate <FrToDt> [0..1] ± 377
     TaxAmount <TaxAmt> [0..1]  378
       Rate <Rate> [0..1] Rate 378
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 378
       TotalAmount <TtlAmt> [0..1] Amount C2, C9 378
       Details <Dtls> [0..*]  379
         Period <Prd> [0..1]  379
           Year <Yr> [0..1] Year 379
           Type <Tp> [0..1] CodeSet 380
           FromToDate <FrToDt> [0..1] ± 380
         Amount <Amt> [1..1] Amount C2, C9 381
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 371 March 2026
```

