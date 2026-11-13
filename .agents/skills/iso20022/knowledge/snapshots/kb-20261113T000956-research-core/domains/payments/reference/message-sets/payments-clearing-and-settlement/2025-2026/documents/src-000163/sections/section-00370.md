---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.30 RemittanceInformation <RmtInf>", "4.4.3.27.23.30.2 Structured <Strd>", "4.4.3.27.23.30.2.6 TaxRemittance <TaxRmt>"]
file_pages: [512, 513]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.30.2.6 TaxRemittance <TaxRmt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 512 to 513.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 512

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
4.4.3.27.23.30.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
512 March 2026
```

## File page 513

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 514
   Debtor <Dbtr> [0..1] ± 514
   UltimateDebtor <UltmtDbtr> [0..1] ± 514
   AdministrationZone <AdmstnZone> [0..1] Text 515
   ReferenceNumber <RefNb> [0..1] Text 515
   Method <Mtd> [0..1] Text 515
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 515
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 516
   Date <Dt> [0..1] Date 516
   SequenceNumber <SeqNb> [0..1] Quantity 516
   Record <Rcrd> [0..*]  516
     Type <Tp> [0..1] Text 517
     Category <Ctgy> [0..1] Text 517
     CategoryDetails <CtgyDtls> [0..1] Text 517
     DebtorStatus <DbtrSts> [0..1] Text 518
     CertificateIdentification <CertId> [0..1] Text 518
     FormsCode <FrmsCd> [0..1] Text 518
     Period <Prd> [0..1]  518
       Year <Yr> [0..1] Year 518
       Type <Tp> [0..1] CodeSet 518
       FromToDate <FrToDt> [0..1] ± 519
     TaxAmount <TaxAmt> [0..1]  520
       Rate <Rate> [0..1] Rate 520
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 520
       TotalAmount <TtlAmt> [0..1] Amount C2, C12 520
       Details <Dtls> [0..*]  521
         Period <Prd> [0..1]  521
           Year <Yr> [0..1] Year 521
           Type <Tp> [0..1] CodeSet 522
           FromToDate <FrToDt> [0..1] ± 522
         Amount <Amt> [1..1] Amount C2, C12 523
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
513 March 2026
```

