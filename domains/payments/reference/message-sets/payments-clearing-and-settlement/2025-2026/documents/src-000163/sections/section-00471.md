---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.11 RemittanceInformation <RmtInf>"]
file_pages: [645, 646, 647, 648]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.11 RemittanceInformation <RmtInf>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 645 to 648.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 645

```text
CreditTransferMandate <CdtTrfMndt> contains the following elements (see
"CreditTransferMandateData1" on page 1169 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 1169
   Type <Tp> [0..1] ± 1169
   DateOfSignature <DtOfSgntr> [0..1] Date 1170
   DateOfVerification <DtOfVrfctn> [0..1] DateTime 1170
   ElectronicSignature <ElctrncSgntr> [0..1] Binary 1170
   FirstPaymentDate <FrstPmtDt> [0..1] Date 1170
   FinalPaymentDate <FnlPmtDt> [0..1] Date 1170
   Frequency <Frqcy> [0..1] ± 1171
   Reason <Rsn> [0..1]  1171
{Or     Code <Cd> [1..1] CodeSet 1171
Or}     Proprietary <Prtry> [1..1] Text 1171
5.4.3.21.11  RemittanceInformation <RmtInf>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
645 March 2026
```

## File page 646

```text
RemittanceInformation <RmtInf> contains the following RemittanceInformation26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 649
   Structured <Strd> [0..*]  649
     ReferredDocumentInformation <RfrdDocInf> [0..*]  653
       Type <Tp> [0..1]  655
         CodeOrProprietary <CdOrPrtry> [1..1]  655
{Or           Code <Cd> [1..1] CodeSet 655
Or}           Proprietary <Prtry> [1..1] Text 655
         Issuer <Issr> [0..1] Text 655
       Number <Nb> [0..1] Text 656
       RelatedDate <RltdDt> [0..1]  656
         Type <Tp> [1..1]  656
{Or           Code <Cd> [1..1] CodeSet 656
Or}           Proprietary <Prtry> [1..1] Text 656
         Date <Dt> [1..1] Date 656
       LineDetails <LineDtls> [0..*]  657
         Identification <Id> [1..*]  657
           Type <Tp> [0..1]  658
             CodeOrProprietary <CdOrPrtry> [1..1]  658
{Or               Code <Cd> [1..1] CodeSet 658
Or}               Proprietary <Prtry> [1..1] Text 658
             Issuer <Issr> [0..1] Text 659
           Number <Nb> [0..1] Text 659
           RelatedDate <RltdDt> [0..1] Date 659
         Description <Desc> [0..1] Text 659
         Amount <Amt> [0..1]  C27 659
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  660
             Type <Tp> [1..1]  660
{Or               Code <Cd> [1..1] CodeSet 661
Or}               Proprietary <Prtry> [1..1] Text 661
             Amount <Amt> [1..1] Amount C2, C11 661
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
646 March 2026
```

## File page 647

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  661
             Amount <Amt> [1..1] Amount C2, C11 661
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 662
             Reason <Rsn> [0..1] Text 662
             AdditionalInformation <AddtlInf> [0..1] Text 662
     ReferredDocumentAmount <RfrdDocAmt> [0..1]  C27 662
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  663
         Type <Tp> [1..1]  663
{Or           Code <Cd> [1..1] CodeSet 664
Or}           Proprietary <Prtry> [1..1] Text 664
         Amount <Amt> [1..1] Amount C2, C11 664
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  664
         Amount <Amt> [1..1] Amount C2, C11 664
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 665
         Reason <Rsn> [0..1] Text 665
         AdditionalInformation <AddtlInf> [0..1] Text 665
     CreditorReferenceInformation <CdtrRefInf> [0..1]  665
       Type <Tp> [0..1]  666
         CodeOrProprietary <CdOrPrtry> [1..1]  666
{Or           Code <Cd> [1..1] CodeSet 666
Or}           Proprietary <Prtry> [1..1] Text 666
         Issuer <Issr> [0..1] Text 667
       Reference <Ref> [0..1] Text 667
     Invoicer <Invcr> [0..1] ± 667
     Invoicee <Invcee> [0..1] ± 668
     TaxRemittance <TaxRmt> [0..1]  669
       Creditor <Cdtr> [0..1] ± 671
       Debtor <Dbtr> [0..1] ± 671
       UltimateDebtor <UltmtDbtr> [0..1] ± 671
       AdministrationZone <AdmstnZone> [0..1] Text 672
       ReferenceNumber <RefNb> [0..1] Text 672
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
647 March 2026
```

## File page 648

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
         AdditionalInformation <AddtlInf> [0..1] Text 680
     GarnishmentRemittance <GrnshmtRmt> [0..1]  680
       Type <Tp> [1..1]  681
         CodeOrProprietary <CdOrPrtry> [1..1]  681
{Or           Code <Cd> [1..1] CodeSet 682
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
648 March 2026
```

