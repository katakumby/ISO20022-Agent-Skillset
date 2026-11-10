---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.2 Structured <Strd>", "7.4.2.40.30.2.6 TaxRemittance <TaxRmt>"]
file_pages: [965, 966]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.2.6 TaxRemittance <TaxRmt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 965 to 966.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 965

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
7.4.2.40.30.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
965 March 2026
```

## File page 966

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 967
   Debtor <Dbtr> [0..1] ± 967
   UltimateDebtor <UltmtDbtr> [0..1] ± 967
   AdministrationZone <AdmstnZone> [0..1] Text 968
   ReferenceNumber <RefNb> [0..1] Text 968
   Method <Mtd> [0..1] Text 968
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C9 968
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C9 969
   Date <Dt> [0..1] Date 969
   SequenceNumber <SeqNb> [0..1] Quantity 969
   Record <Rcrd> [0..*]  969
     Type <Tp> [0..1] Text 970
     Category <Ctgy> [0..1] Text 970
     CategoryDetails <CtgyDtls> [0..1] Text 970
     DebtorStatus <DbtrSts> [0..1] Text 971
     CertificateIdentification <CertId> [0..1] Text 971
     FormsCode <FrmsCd> [0..1] Text 971
     Period <Prd> [0..1]  971
       Year <Yr> [0..1] Year 971
       Type <Tp> [0..1] CodeSet 971
       FromToDate <FrToDt> [0..1] ± 972
     TaxAmount <TaxAmt> [0..1]  973
       Rate <Rate> [0..1] Rate 973
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 973
       TotalAmount <TtlAmt> [0..1] Amount C2, C9 973
       Details <Dtls> [0..*]  974
         Period <Prd> [0..1]  974
           Year <Yr> [0..1] Year 974
           Type <Tp> [0..1] CodeSet 975
           FromToDate <FrToDt> [0..1] ± 975
         Amount <Amt> [1..1] Amount C2, C9 976
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
966 March 2026
```

