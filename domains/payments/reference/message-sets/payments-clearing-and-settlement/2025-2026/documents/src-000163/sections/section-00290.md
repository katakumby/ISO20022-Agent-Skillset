---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.11 RemittanceInformation <RmtInf>", "4.4.3.27.11.2 Structured <Strd>", "4.4.3.27.11.2.6 TaxRemittance <TaxRmt>"]
file_pages: [415, 416]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.11.2.6 TaxRemittance <TaxRmt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 415 to 416.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 415

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
4.4.3.27.11.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
415 March 2026
```

## File page 416

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 417
   Debtor <Dbtr> [0..1] ± 417
   UltimateDebtor <UltmtDbtr> [0..1] ± 417
   AdministrationZone <AdmstnZone> [0..1] Text 418
   ReferenceNumber <RefNb> [0..1] Text 418
   Method <Mtd> [0..1] Text 418
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 418
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 419
   Date <Dt> [0..1] Date 419
   SequenceNumber <SeqNb> [0..1] Quantity 419
   Record <Rcrd> [0..*]  419
     Type <Tp> [0..1] Text 420
     Category <Ctgy> [0..1] Text 420
     CategoryDetails <CtgyDtls> [0..1] Text 420
     DebtorStatus <DbtrSts> [0..1] Text 421
     CertificateIdentification <CertId> [0..1] Text 421
     FormsCode <FrmsCd> [0..1] Text 421
     Period <Prd> [0..1]  421
       Year <Yr> [0..1] Year 421
       Type <Tp> [0..1] CodeSet 421
       FromToDate <FrToDt> [0..1] ± 422
     TaxAmount <TaxAmt> [0..1]  423
       Rate <Rate> [0..1] Rate 423
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 423
       TotalAmount <TtlAmt> [0..1] Amount C2, C12 423
       Details <Dtls> [0..*]  424
         Period <Prd> [0..1]  424
           Year <Yr> [0..1] Year 424
           Type <Tp> [0..1] CodeSet 425
           FromToDate <FrToDt> [0..1] ± 425
         Amount <Amt> [1..1] Amount C2, C12 426
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
416 March 2026
```

