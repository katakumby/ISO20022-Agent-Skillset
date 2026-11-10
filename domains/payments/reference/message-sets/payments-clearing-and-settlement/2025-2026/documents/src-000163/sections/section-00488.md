---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.11 RemittanceInformation <RmtInf>", "5.4.3.21.11.2 Structured <Strd>", "5.4.3.21.11.2.6 TaxRemittance <TaxRmt>"]
file_pages: [669, 670]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.11.2.6 TaxRemittance <TaxRmt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 669 to 670.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 669

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
5.4.3.21.11.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
669 March 2026
```

## File page 670

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 671
   Debtor <Dbtr> [0..1] ± 671
   UltimateDebtor <UltmtDbtr> [0..1] ± 671
   AdministrationZone <AdmstnZone> [0..1] Text 672
   ReferenceNumber <RefNb> [0..1] Text 672
   Method <Mtd> [0..1] Text 672
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C11 672
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C11 673
   Date <Dt> [0..1] Date 673
   SequenceNumber <SeqNb> [0..1] Quantity 673
   Record <Rcrd> [0..*]  673
     Type <Tp> [0..1] Text 674
     Category <Ctgy> [0..1] Text 674
     CategoryDetails <CtgyDtls> [0..1] Text 674
     DebtorStatus <DbtrSts> [0..1] Text 675
     CertificateIdentification <CertId> [0..1] Text 675
     FormsCode <FrmsCd> [0..1] Text 675
     Period <Prd> [0..1]  675
       Year <Yr> [0..1] Year 675
       Type <Tp> [0..1] CodeSet 675
       FromToDate <FrToDt> [0..1] ± 676
     TaxAmount <TaxAmt> [0..1]  677
       Rate <Rate> [0..1] Rate 677
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C11 677
       TotalAmount <TtlAmt> [0..1] Amount C2, C11 677
       Details <Dtls> [0..*]  678
         Period <Prd> [0..1]  678
           Year <Yr> [0..1] Year 678
           Type <Tp> [0..1] CodeSet 679
           FromToDate <FrToDt> [0..1] ± 679
         Amount <Amt> [1..1] Amount C2, C11 680
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
670 March 2026
```

