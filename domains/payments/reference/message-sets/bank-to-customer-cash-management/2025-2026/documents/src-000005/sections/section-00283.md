---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.15 RemittanceInformation <RmtInf>"]
file_pages: [426, 427, 428, 429]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.15 RemittanceInformation <RmtInf>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 426 to 429.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 426

```text
Address <Adr> contains the following elements (see "PostalAddress27" on page 875 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  875
{Or     Code <Cd> [1..1] CodeSet 876
Or}     Proprietary <Prtry> [1..1] ± 876
   CareOf <CareOf> [0..1] Text 876
   Department <Dept> [0..1] Text 876
   SubDepartment <SubDept> [0..1] Text 877
   StreetName <StrtNm> [0..1] Text 877
   BuildingNumber <BldgNb> [0..1] Text 877
   BuildingName <BldgNm> [0..1] Text 877
   Floor <Flr> [0..1] Text 877
   UnitNumber <UnitNb> [0..1] Text 877
   PostBox <PstBx> [0..1] Text 877
   Room <Room> [0..1] Text 877
   PostCode <PstCd> [0..1] Text 878
   TownName <TwnNm> [0..1] Text 878
   TownLocationName <TwnLctnNm> [0..1] Text 878
   DistrictName <DstrctNm> [0..1] Text 878
   CountrySubDivision <CtrySubDvsn> [0..1] Text 878
   Country <Ctry> [0..1] CodeSet C4 878
   AddressLine <AdrLine> [0..7] Text 878
3.4.2.15.18.2.15  RemittanceInformation <RmtInf>
Presence: [0..1]
Definition: Structured information that enables the matching, that is reconciliation, of a payment with the
items that the payment is intended to settle, such as commercial invoices in an account receivable
system.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
426 March 2026
```

## File page 427

```text
RemittanceInformation <RmtInf> contains the following RemittanceInformation26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 430
   Structured <Strd> [0..*]  430
     ReferredDocumentInformation <RfrdDocInf> [0..*]  434
       Type <Tp> [0..1]  436
         CodeOrProprietary <CdOrPrtry> [1..1]  436
{Or           Code <Cd> [1..1] CodeSet 436
Or}           Proprietary <Prtry> [1..1] Text 436
         Issuer <Issr> [0..1] Text 436
       Number <Nb> [0..1] Text 437
       RelatedDate <RltdDt> [0..1]  437
         Type <Tp> [1..1]  437
{Or           Code <Cd> [1..1] CodeSet 437
Or}           Proprietary <Prtry> [1..1] Text 437
         Date <Dt> [1..1] Date 437
       LineDetails <LineDtls> [0..*]  438
         Identification <Id> [1..*]  438
           Type <Tp> [0..1]  439
             CodeOrProprietary <CdOrPrtry> [1..1]  439
{Or               Code <Cd> [1..1] CodeSet 439
Or}               Proprietary <Prtry> [1..1] Text 439
             Issuer <Issr> [0..1] Text 440
           Number <Nb> [0..1] Text 440
           RelatedDate <RltdDt> [0..1] Date 440
         Description <Desc> [0..1] Text 440
         Amount <Amt> [0..1]  C27 440
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  441
             Type <Tp> [1..1]  441
{Or               Code <Cd> [1..1] CodeSet 442
Or}               Proprietary <Prtry> [1..1] Text 442
             Amount <Amt> [1..1] Amount C2, C6 442
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
427 March 2026
```

## File page 428

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  442
             Amount <Amt> [1..1] Amount C2, C6 442
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 443
             Reason <Rsn> [0..1] Text 443
             AdditionalInformation <AddtlInf> [0..1] Text 443
     ReferredDocumentAmount <RfrdDocAmt> [0..1]  C27 443
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  444
         Type <Tp> [1..1]  444
{Or           Code <Cd> [1..1] CodeSet 445
Or}           Proprietary <Prtry> [1..1] Text 445
         Amount <Amt> [1..1] Amount C2, C6 445
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  445
         Amount <Amt> [1..1] Amount C2, C6 445
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 446
         Reason <Rsn> [0..1] Text 446
         AdditionalInformation <AddtlInf> [0..1] Text 446
     CreditorReferenceInformation <CdtrRefInf> [0..1]  446
       Type <Tp> [0..1]  447
         CodeOrProprietary <CdOrPrtry> [1..1]  447
{Or           Code <Cd> [1..1] CodeSet 447
Or}           Proprietary <Prtry> [1..1] Text 447
         Issuer <Issr> [0..1] Text 448
       Reference <Ref> [0..1] Text 448
     Invoicer <Invcr> [0..1] ± 448
     Invoicee <Invcee> [0..1] ± 449
     TaxRemittance <TaxRmt> [0..1]  450
       Creditor <Cdtr> [0..1] ± 452
       Debtor <Dbtr> [0..1] ± 452
       UltimateDebtor <UltmtDbtr> [0..1] ± 452
       AdministrationZone <AdmstnZone> [0..1] Text 453
       ReferenceNumber <RefNb> [0..1] Text 453
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
428 March 2026
```

## File page 429

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
         AdditionalInformation <AddtlInf> [0..1] Text 461
     GarnishmentRemittance <GrnshmtRmt> [0..1]  461
       Type <Tp> [1..1]  462
         CodeOrProprietary <CdOrPrtry> [1..1]  462
{Or           Code <Cd> [1..1] CodeSet 463
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
429 March 2026
```

