---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.6 TaxRemittance <TaxRmt>"]
file_pages: [708, 709]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.6 TaxRemittance <TaxRmt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 708 to 709.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 708

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
4.4.2.14.18.2.15.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
708 March 2026
```

## File page 709

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 710
   Debtor <Dbtr> [0..1] ± 710
   UltimateDebtor <UltmtDbtr> [0..1] ± 710
   AdministrationZone <AdmstnZone> [0..1] Text 711
   ReferenceNumber <RefNb> [0..1] Text 711
   Method <Mtd> [0..1] Text 711
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 711
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 712
   Date <Dt> [0..1] Date 712
   SequenceNumber <SeqNb> [0..1] Quantity 712
   Record <Rcrd> [0..*]  712
     Type <Tp> [0..1] Text 713
     Category <Ctgy> [0..1] Text 713
     CategoryDetails <CtgyDtls> [0..1] Text 713
     DebtorStatus <DbtrSts> [0..1] Text 714
     CertificateIdentification <CertId> [0..1] Text 714
     FormsCode <FrmsCd> [0..1] Text 714
     Period <Prd> [0..1]  714
       Year <Yr> [0..1] Year 714
       Type <Tp> [0..1] CodeSet 714
       FromToDate <FrToDt> [0..1] ± 715
     TaxAmount <TaxAmt> [0..1]  716
       Rate <Rate> [0..1] Rate 716
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 716
       TotalAmount <TtlAmt> [0..1] Amount C2, C6 716
       Details <Dtls> [0..*]  717
         Period <Prd> [0..1]  717
           Year <Yr> [0..1] Year 717
           Type <Tp> [0..1] CodeSet 718
           FromToDate <FrToDt> [0..1] ± 718
         Amount <Amt> [1..1] Amount C2, C6 719
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
709 March 2026
```

