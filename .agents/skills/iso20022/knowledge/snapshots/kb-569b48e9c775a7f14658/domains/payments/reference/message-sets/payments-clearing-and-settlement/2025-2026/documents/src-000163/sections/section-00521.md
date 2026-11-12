---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.2 Structure"]
file_pages: [703, 704, 705, 706, 707, 708, 709, 710]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.2 Structure

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 703 to 710.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 703

```text
6.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FIToFICstmrCdtTrf> [1..1]  C13,
C14,
C18,
C23,
C31,
C32,
C45,
C50,
C51,
C53
   GroupHeader <GrpHdr> [1..1]  C49 0
     MessageIdentification <MsgId> [1..1] Text 718
     CreationDateTime <CreDtTm> [1..1] DateTime 718
     ExpiryDateTime <XpryDtTm> [0..1] DateTime 718
     BatchBooking <BtchBookg> [0..1] Indicator 718
     NumberOfTransactions <NbOfTxs> [1..1] Text 718
     ControlSum <CtrlSum> [0..1] Quantity 719
     TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt> [0..1] Amount C1, C11 719
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 719
     SettlementInformation <SttlmInf> [1..1]  C22,
C24,
C41,
C42,
C43,
C44,
C47,
C48
719
       SettlementMethod <SttlmMtd> [1..1] CodeSet 721
       SettlementAccount <SttlmAcct> [0..1] ± C17,
C16
722
       ClearingSystem <ClrSys> [0..1]  722
{Or         Code <Cd> [1..1] CodeSet 723
Or}         Proprietary <Prtry> [1..1] Text 723
       InstructingReimbursementAgent <InstgRmbrsmntAgt> [0..1] ± 723
       InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C17,
C16
724
       InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 724
       InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C17,
C16
725
       ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 726
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
703 March 2026
```

## File page 704

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C17,
C16
726
     PaymentTypeInformation <PmtTpInf> [0..1] ± 727
     InstructingAgent <InstgAgt> [0..1] ± 728
     InstructedAgent <InstdAgt> [0..1] ± 729
   CreditTransferTransactionInformation <CdtTrfTxInf> [1..*]  C6, C8,
C19,
C20,
C21,
C25,
C26,
C27,
C28,
C29,
C30,
C33,
C35,
C36,
C37,
C38, C7,
C9, C34,
C54,
C55
0
     PaymentIdentification <PmtId> [1..1] ± C52 739
     PaymentTypeInformation <PmtTpInf> [0..1] ± 740
     InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount C1, C11 740
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 741
     SettlementPriority <SttlmPrty> [0..1] CodeSet 741
     SettlementTimeIndication <SttlmTmIndctn> [0..1]  741
       DebitDateTime <DbtDtTm> [0..1] DateTime 742
       CreditDateTime <CdtDtTm> [0..1] DateTime 742
     SettlementTimeRequest <SttlmTmReq> [0..1] ± 742
     AdditionalDateTime <AddtlDtTm> [0..1]  C3 742
       AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 743
       PoolingAdjustmentDate <PoolgAdjstmntDt> [0..1] Date 743
       ExpiryDateTime <XpryDtTm> [0..1] DateTime 743
     InstructedAmount <InstdAmt> [0..1] Amount C2, C12 743
     ExchangeRate <XchgRate> [0..1] Rate 744
     AgreedRate <AgrdRate> [0..1]  744
       UnitCurrency <UnitCcy> [0..1] CodeSet C2 744
       QuotedCurrency <QtdCcy> [0..1] CodeSet C2 744
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
704 March 2026
```

## File page 705

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       PreAgreedExchangeRate <PreAgrdXchgRate> [1..1] Rate 745
       QuotationDateTime <QtnDtTm> [0..1] DateTime 745
       QuoteIdentification <QtId> [0..1] IdentifierSet 745
       ForeignExchangeAgent <FXAgt> [0..1] ± 745
     ChargeBearer <ChrgBr> [1..1] CodeSet 746
     ChargesInformation <ChrgsInf> [0..*]  746
       Amount <Amt> [1..1] Amount C2, C12 747
       Agent <Agt> [1..1] ± 747
       Type <Tp> [0..1]  748
{Or         Code <Cd> [1..1] CodeSet 748
Or}         Proprietary <Prtry> [1..1] ± 748
     MandateRelatedInformation <MndtRltdInf> [0..1] ± 749
     PaymentSignature <PmtSgntr> [0..1]  749
{Or       ILPV4 <ILPV4> [1..1] Text 750
Or}       Signature <Sgntr> [1..1] Text 750
     PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 750
     PreviousInstructingAgent1Account <PrvsInstgAgt1Acct> [0..1] ± C17,
C16
750
     PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 751
     PreviousInstructingAgent2Account <PrvsInstgAgt2Acct> [0..1] ± C17,
C16
752
     PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 753
     PreviousInstructingAgent3Account <PrvsInstgAgt3Acct> [0..1] ± C17,
C16
753
     InstructingAgent <InstgAgt> [0..1] ± 754
     InstructedAgent <InstdAgt> [0..1] ± 755
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 756
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C17,
C16
757
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 758
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C17,
C16
758
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 759
     IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C17,
C16
760
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
705 March 2026
```

## File page 706

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     UltimateDebtor <UltmtDbtr> [0..1] ± 761
     InitiatingParty <InitgPty> [0..1] ± 762
     Debtor <Dbtr> [1..1] ± 763
     DebtorAccount <DbtrAcct> [0..1] ± C17,
C16
764
     DebtorAgent <DbtrAgt> [1..1] ± 765
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C17,
C16
766
     CreditorAgent <CdtrAgt> [1..1] ± 767
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C17,
C16
767
     Creditor <Cdtr> [1..1] ± 768
     CreditorAccount <CdtrAcct> [0..1] ± C17,
C16
769
     UltimateCreditor <UltmtCdtr> [0..1] ± 770
     InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 771
     InstructionForNextAgent <InstrForNxtAgt> [0..*]  772
       Code <Cd> [0..1] CodeSet 772
       InstructionInformation <InstrInf> [0..1] Text 772
     Purpose <Purp> [0..1] ± 772
     RegulatoryReporting <RgltryRptg> [0..10] ± 773
     Tax <Tax> [0..1]  773
       Creditor <Cdtr> [0..1] ± 775
       Debtor <Dbtr> [0..1] ± 775
       UltimateDebtor <UltmtDbtr> [0..1] ± 775
       AdministrationZone <AdmstnZone> [0..1] Text 776
       ReferenceNumber <RefNb> [0..1] Text 776
       Method <Mtd> [0..1] Text 776
       TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 776
       TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 777
       Date <Dt> [0..1] Date 777
       SequenceNumber <SeqNb> [0..1] Quantity 777
       Record <Rcrd> [0..*]  777
         Type <Tp> [0..1] Text 778
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
706 March 2026
```

## File page 707

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         Category <Ctgy> [0..1] Text 778
         CategoryDetails <CtgyDtls> [0..1] Text 778
         DebtorStatus <DbtrSts> [0..1] Text 779
         CertificateIdentification <CertId> [0..1] Text 779
         FormsCode <FrmsCd> [0..1] Text 779
         Period <Prd> [0..1]  779
           Year <Yr> [0..1] Year 779
           Type <Tp> [0..1] CodeSet 779
           FromToDate <FrToDt> [0..1] ± 780
         TaxAmount <TaxAmt> [0..1]  781
           Rate <Rate> [0..1] Rate 781
           TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 781
           TotalAmount <TtlAmt> [0..1] Amount C2, C12 781
           Details <Dtls> [0..*]  782
             Period <Prd> [0..1]  782
               Year <Yr> [0..1] Year 782
               Type <Tp> [0..1] CodeSet 783
               FromToDate <FrToDt> [0..1] ± 783
             Amount <Amt> [1..1] Amount C2, C12 784
         AdditionalInformation <AddtlInf> [0..1] Text 784
     RelatedRemittanceInformation <RltdRmtInf> [0..10]  784
       RemittanceIdentification <RmtId> [0..1] Text 785
       RemittanceLocationDetails <RmtLctnDtls> [0..*]  785
         Method <Mtd> [1..1] CodeSet 785
         ElectronicAddress <ElctrncAdr> [0..1] Text 786
         PostalAddress <PstlAdr> [0..1]  786
           Name <Nm> [1..1] Text 786
           Address <Adr> [1..1] ± 786
     RemittanceInformation <RmtInf> [0..1]  787
       Unstructured <Ustrd> [0..*] Text 791
       Structured <Strd> [0..*]  791
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
707 March 2026
```

## File page 708

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         ReferredDocumentInformation <RfrdDocInf> [0..*]  795
           Type <Tp> [0..1]  797
             CodeOrProprietary <CdOrPrtry> [1..1]  797
{Or               Code <Cd> [1..1] CodeSet 797
Or}               Proprietary <Prtry> [1..1] Text 797
             Issuer <Issr> [0..1] Text 797
           Number <Nb> [0..1] Text 798
           RelatedDate <RltdDt> [0..1]  798
             Type <Tp> [1..1]  798
{Or               Code <Cd> [1..1] CodeSet 798
Or}               Proprietary <Prtry> [1..1] Text 798
             Date <Dt> [1..1] Date 798
           LineDetails <LineDtls> [0..*]  799
             Identification <Id> [1..*]  799
               Type <Tp> [0..1]  800
                 CodeOrProprietary <CdOrPrtry> [1..1]  800
{Or                   Code <Cd> [1..1] CodeSet 800
Or}                   Proprietary <Prtry> [1..1] Text 800
                 Issuer <Issr> [0..1] Text 801
               Number <Nb> [0..1] Text 801
               RelatedDate <RltdDt> [0..1] Date 801
             Description <Desc> [0..1] Text 801
             Amount <Amt> [0..1]  C39 801
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  802
                 Type <Tp> [1..1]  802
{Or                   Code <Cd> [1..1] CodeSet 803
Or}                   Proprietary <Prtry> [1..1] Text 803
                 Amount <Amt> [1..1] Amount C2, C12 803
               AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  803
                 Amount <Amt> [1..1] Amount C2, C12 803
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 804
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
708 March 2026
```

## File page 709

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                 Reason <Rsn> [0..1] Text 804
                 AdditionalInformation <AddtlInf> [0..1] Text 804
         ReferredDocumentAmount <RfrdDocAmt> [0..1]  C39 804
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  805
             Type <Tp> [1..1]  805
{Or               Code <Cd> [1..1] CodeSet 806
Or}               Proprietary <Prtry> [1..1] Text 806
             Amount <Amt> [1..1] Amount C2, C12 806
           AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  806
             Amount <Amt> [1..1] Amount C2, C12 806
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 807
             Reason <Rsn> [0..1] Text 807
             AdditionalInformation <AddtlInf> [0..1] Text 807
         CreditorReferenceInformation <CdtrRefInf> [0..1]  807
           Type <Tp> [0..1]  808
             CodeOrProprietary <CdOrPrtry> [1..1]  808
{Or               Code <Cd> [1..1] CodeSet 808
Or}               Proprietary <Prtry> [1..1] Text 808
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
           TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 815
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
709 March 2026
```

## File page 710

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
{Or               Code <Cd> [1..1] CodeSet 824
Or}               Proprietary <Prtry> [1..1] Text 824
             Issuer <Issr> [0..1] Text 824
           Garnishee <Grnshee> [0..1] ± 824
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
710 March 2026
```

