---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>"]
file_pages: [684, 685, 686, 687]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15 RemittanceInformation <RmtInf>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 684 to 687.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 684

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
4.4.2.14.18.2.15  RemittanceInformation <RmtInf>
Presence: [0..1]
Definition: Structured information that enables the matching, that is reconciliation, of a payment with the
items that the payment is intended to settle, such as commercial invoices in an account receivable
system.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
684 March 2026
```

## File page 685

```text
RemittanceInformation <RmtInf> contains the following RemittanceInformation26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 688
   Structured <Strd> [0..*]  688
     ReferredDocumentInformation <RfrdDocInf> [0..*]  692
       Type <Tp> [0..1]  694
         CodeOrProprietary <CdOrPrtry> [1..1]  694
{Or           Code <Cd> [1..1] CodeSet 694
Or}           Proprietary <Prtry> [1..1] Text 694
         Issuer <Issr> [0..1] Text 694
       Number <Nb> [0..1] Text 695
       RelatedDate <RltdDt> [0..1]  695
         Type <Tp> [1..1]  695
{Or           Code <Cd> [1..1] CodeSet 695
Or}           Proprietary <Prtry> [1..1] Text 695
         Date <Dt> [1..1] Date 695
       LineDetails <LineDtls> [0..*]  696
         Identification <Id> [1..*]  696
           Type <Tp> [0..1]  697
             CodeOrProprietary <CdOrPrtry> [1..1]  697
{Or               Code <Cd> [1..1] CodeSet 697
Or}               Proprietary <Prtry> [1..1] Text 697
             Issuer <Issr> [0..1] Text 698
           Number <Nb> [0..1] Text 698
           RelatedDate <RltdDt> [0..1] Date 698
         Description <Desc> [0..1] Text 698
         Amount <Amt> [0..1]  C26 698
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  699
             Type <Tp> [1..1]  699
{Or               Code <Cd> [1..1] CodeSet 700
Or}               Proprietary <Prtry> [1..1] Text 700
             Amount <Amt> [1..1] Amount C2, C6 700
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
685 March 2026
```

## File page 686

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  700
             Amount <Amt> [1..1] Amount C2, C6 700
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 701
             Reason <Rsn> [0..1] Text 701
             AdditionalInformation <AddtlInf> [0..1] Text 701
     ReferredDocumentAmount <RfrdDocAmt> [0..1]  C26 701
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  702
         Type <Tp> [1..1]  702
{Or           Code <Cd> [1..1] CodeSet 703
Or}           Proprietary <Prtry> [1..1] Text 703
         Amount <Amt> [1..1] Amount C2, C6 703
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  703
         Amount <Amt> [1..1] Amount C2, C6 703
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 704
         Reason <Rsn> [0..1] Text 704
         AdditionalInformation <AddtlInf> [0..1] Text 704
     CreditorReferenceInformation <CdtrRefInf> [0..1]  704
       Type <Tp> [0..1]  705
         CodeOrProprietary <CdOrPrtry> [1..1]  705
{Or           Code <Cd> [1..1] CodeSet 705
Or}           Proprietary <Prtry> [1..1] Text 705
         Issuer <Issr> [0..1] Text 706
       Reference <Ref> [0..1] Text 706
     Invoicer <Invcr> [0..1] ± 706
     Invoicee <Invcee> [0..1] ± 707
     TaxRemittance <TaxRmt> [0..1]  708
       Creditor <Cdtr> [0..1] ± 710
       Debtor <Dbtr> [0..1] ± 710
       UltimateDebtor <UltmtDbtr> [0..1] ± 710
       AdministrationZone <AdmstnZone> [0..1] Text 711
       ReferenceNumber <RefNb> [0..1] Text 711
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
686 March 2026
```

## File page 687

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
         AdditionalInformation <AddtlInf> [0..1] Text 719
     GarnishmentRemittance <GrnshmtRmt> [0..1]  719
       Type <Tp> [1..1]  720
         CodeOrProprietary <CdOrPrtry> [1..1]  720
{Or           Code <Cd> [1..1] CodeSet 721
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
687 March 2026
```

