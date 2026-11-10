---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "3.4.2.15.18.2.15.2 Structured <Strd>", "3.4.2.15.18.2.15.2.6 TaxRemittance <TaxRmt>"]
file_pages: [450, 451]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.15.2.6 TaxRemittance <TaxRmt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 450 to 451.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 450

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
3.4.2.15.18.2.15.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
450 March 2026
```

## File page 451

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 452
   Debtor <Dbtr> [0..1] ± 452
   UltimateDebtor <UltmtDbtr> [0..1] ± 452
   AdministrationZone <AdmstnZone> [0..1] Text 453
   ReferenceNumber <RefNb> [0..1] Text 453
   Method <Mtd> [0..1] Text 453
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 453
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 454
   Date <Dt> [0..1] Date 454
   SequenceNumber <SeqNb> [0..1] Quantity 454
   Record <Rcrd> [0..*]  454
     Type <Tp> [0..1] Text 455
     Category <Ctgy> [0..1] Text 455
     CategoryDetails <CtgyDtls> [0..1] Text 455
     DebtorStatus <DbtrSts> [0..1] Text 456
     CertificateIdentification <CertId> [0..1] Text 456
     FormsCode <FrmsCd> [0..1] Text 456
     Period <Prd> [0..1]  456
       Year <Yr> [0..1] Year 456
       Type <Tp> [0..1] CodeSet 456
       FromToDate <FrToDt> [0..1] ± 457
     TaxAmount <TaxAmt> [0..1]  458
       Rate <Rate> [0..1] Rate 458
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 458
       TotalAmount <TtlAmt> [0..1] Amount C2, C6 458
       Details <Dtls> [0..*]  459
         Period <Prd> [0..1]  459
           Year <Yr> [0..1] Year 459
           Type <Tp> [0..1] CodeSet 460
           FromToDate <FrToDt> [0..1] ± 460
         Amount <Amt> [1..1] Amount C2, C6 461
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
451 March 2026
```

