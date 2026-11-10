---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "2.4.2.15.18.2.15.2 Structured <Strd>", "2.4.2.15.18.2.15.2.6 TaxRemittance <TaxRmt>"]
file_pages: [190, 191]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.15.2.6 TaxRemittance <TaxRmt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 190 to 191.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 190

```text
Invoicee <Invcee> contains the following elements (see "PartyIdentification272" on page 859 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 860
   PostalAddress <PstlAdr> [0..1] ± 861
   Identification <Id> [0..1]  861
{Or     OrganisationIdentification <OrgId> [1..1]  862
       AnyBIC <AnyBIC> [0..1] IdentifierSet C2 863
       LEI <LEI> [0..1] IdentifierSet 863
       Other <Othr> [0..*]  863
         Identification <Id> [1..1] Text 864
         SchemeName <SchmeNm> [0..1]  864
{Or           Code <Cd> [1..1] CodeSet 864
Or}           Proprietary <Prtry> [1..1] Text 864
         Issuer <Issr> [0..1] Text 864
Or}     PrivateIdentification <PrvtId> [1..1]  864
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  865
         BirthDate <BirthDt> [1..1] Date 865
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 865
         CityOfBirth <CityOfBirth> [1..1] Text 866
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C4 866
       Other <Othr> [0..*]  866
         Identification <Id> [1..1] Text 866
         SchemeName <SchmeNm> [0..1]  866
{Or           Code <Cd> [1..1] CodeSet 867
Or}           Proprietary <Prtry> [1..1] Text 867
         Issuer <Issr> [0..1] Text 867
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C4 867
   ContactDetails <CtctDtls> [0..1] ± 867
2.4.2.15.18.2.15.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
190 March 2026
```

## File page 191

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 192
   Debtor <Dbtr> [0..1] ± 192
   UltimateDebtor <UltmtDbtr> [0..1] ± 192
   AdministrationZone <AdmstnZone> [0..1] Text 193
   ReferenceNumber <RefNb> [0..1] Text 193
   Method <Mtd> [0..1] Text 193
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 193
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 194
   Date <Dt> [0..1] Date 194
   SequenceNumber <SeqNb> [0..1] Quantity 194
   Record <Rcrd> [0..*]  194
     Type <Tp> [0..1] Text 195
     Category <Ctgy> [0..1] Text 195
     CategoryDetails <CtgyDtls> [0..1] Text 195
     DebtorStatus <DbtrSts> [0..1] Text 196
     CertificateIdentification <CertId> [0..1] Text 196
     FormsCode <FrmsCd> [0..1] Text 196
     Period <Prd> [0..1]  196
       Year <Yr> [0..1] Year 196
       Type <Tp> [0..1] CodeSet 196
       FromToDate <FrToDt> [0..1] ± 197
     TaxAmount <TaxAmt> [0..1]  198
       Rate <Rate> [0..1] Rate 198
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 198
       TotalAmount <TtlAmt> [0..1] Amount C2, C6 198
       Details <Dtls> [0..*]  199
         Period <Prd> [0..1]  199
           Year <Yr> [0..1] Year 199
           Type <Tp> [0..1] CodeSet 200
           FromToDate <FrToDt> [0..1] ± 200
         Amount <Amt> [1..1] Amount C2, C6 201
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
191 March 2026
```

