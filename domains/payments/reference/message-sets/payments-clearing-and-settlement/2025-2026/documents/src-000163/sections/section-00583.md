---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.47 RemittanceInformation <RmtInf>", "6.4.2.47.1 Unstructured <Ustrd>"]
file_pages: [791, 792, 793, 794]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.47.1 Unstructured <Ustrd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 791 to 794.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 791

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] Text 824
         Issuer <Issr> [0..1] Text 824
       Garnishee <Grnshee> [0..1] ± 824
       GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 825
       ReferenceNumber <RefNb> [0..1] Text 826
       Date <Dt> [0..1] Date 827
       RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 827
       FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 827
       EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 827
     SecuritiesData <SctiesData> [0..*]  827
       UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 828
       Amount <Amt> [0..1] Amount C1, C11 828
     AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 828
6.4.2.47.1  Unstructured <Ustrd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in an
unstructured form.
Datatype: "Max140Text" on page 1244
6.4.2.47.2  Structured <Strd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a
structured form.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
791 March 2026
```

## File page 792

```text
Structured <Strd> contains the following StructuredRemittanceInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferredDocumentInformation <RfrdDocInf> [0..*]  795
     Type <Tp> [0..1]  797
       CodeOrProprietary <CdOrPrtry> [1..1]  797
{Or         Code <Cd> [1..1] CodeSet 797
Or}         Proprietary <Prtry> [1..1] Text 797
       Issuer <Issr> [0..1] Text 797
     Number <Nb> [0..1] Text 798
     RelatedDate <RltdDt> [0..1]  798
       Type <Tp> [1..1]  798
{Or         Code <Cd> [1..1] CodeSet 798
Or}         Proprietary <Prtry> [1..1] Text 798
       Date <Dt> [1..1] Date 798
     LineDetails <LineDtls> [0..*]  799
       Identification <Id> [1..*]  799
         Type <Tp> [0..1]  800
           CodeOrProprietary <CdOrPrtry> [1..1]  800
{Or             Code <Cd> [1..1] CodeSet 800
Or}             Proprietary <Prtry> [1..1] Text 800
           Issuer <Issr> [0..1] Text 801
         Number <Nb> [0..1] Text 801
         RelatedDate <RltdDt> [0..1] Date 801
       Description <Desc> [0..1] Text 801
       Amount <Amt> [0..1]  C39 801
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  802
           Type <Tp> [1..1]  802
{Or             Code <Cd> [1..1] CodeSet 803
Or}             Proprietary <Prtry> [1..1] Text 803
           Amount <Amt> [1..1] Amount C2, C12 803
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  803
           Amount <Amt> [1..1] Amount C2, C12 803
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
792 March 2026
```

## File page 793

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 804
           Reason <Rsn> [0..1] Text 804
           AdditionalInformation <AddtlInf> [0..1] Text 804
   ReferredDocumentAmount <RfrdDocAmt> [0..1]  C39 804
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  805
       Type <Tp> [1..1]  805
{Or         Code <Cd> [1..1] CodeSet 806
Or}         Proprietary <Prtry> [1..1] Text 806
       Amount <Amt> [1..1] Amount C2, C12 806
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  806
       Amount <Amt> [1..1] Amount C2, C12 806
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 807
       Reason <Rsn> [0..1] Text 807
       AdditionalInformation <AddtlInf> [0..1] Text 807
   CreditorReferenceInformation <CdtrRefInf> [0..1]  807
     Type <Tp> [0..1]  808
       CodeOrProprietary <CdOrPrtry> [1..1]  808
{Or         Code <Cd> [1..1] CodeSet 808
Or}         Proprietary <Prtry> [1..1] Text 808
       Issuer <Issr> [0..1] Text 809
     Reference <Ref> [0..1] Text 809
   Invoicer <Invcr> [0..1] ± 809
   Invoicee <Invcee> [0..1] ± 810
   TaxRemittance <TaxRmt> [0..1]  811
     Creditor <Cdtr> [0..1] ± 813
     Debtor <Dbtr> [0..1] ± 813
     UltimateDebtor <UltmtDbtr> [0..1] ± 813
     AdministrationZone <AdmstnZone> [0..1] Text 814
     ReferenceNumber <RefNb> [0..1] Text 814
     Method <Mtd> [0..1] Text 814
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 814
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
793 March 2026
```

## File page 794

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 815
     Date <Dt> [0..1] Date 815
     SequenceNumber <SeqNb> [0..1] Quantity 815
     Record <Rcrd> [0..*]  815
       Type <Tp> [0..1] Text 816
       Category <Ctgy> [0..1] Text 816
       CategoryDetails <CtgyDtls> [0..1] Text 816
       DebtorStatus <DbtrSts> [0..1] Text 817
       CertificateIdentification <CertId> [0..1] Text 817
       FormsCode <FrmsCd> [0..1] Text 817
       Period <Prd> [0..1]  817
         Year <Yr> [0..1] Year 817
         Type <Tp> [0..1] CodeSet 817
         FromToDate <FrToDt> [0..1] ± 818
       TaxAmount <TaxAmt> [0..1]  819
         Rate <Rate> [0..1] Rate 819
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 819
         TotalAmount <TtlAmt> [0..1] Amount C2, C12 819
         Details <Dtls> [0..*]  820
           Period <Prd> [0..1]  820
             Year <Yr> [0..1] Year 820
             Type <Tp> [0..1] CodeSet 821
             FromToDate <FrToDt> [0..1] ± 821
           Amount <Amt> [1..1] Amount C2, C12 822
       AdditionalInformation <AddtlInf> [0..1] Text 822
   GarnishmentRemittance <GrnshmtRmt> [0..1]  822
     Type <Tp> [1..1]  823
       CodeOrProprietary <CdOrPrtry> [1..1]  823
{Or         Code <Cd> [1..1] CodeSet 824
Or}         Proprietary <Prtry> [1..1] Text 824
       Issuer <Issr> [0..1] Text 824
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
794 March 2026
```

