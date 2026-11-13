---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.2 OriginalGroupInformation <OrgnlGrpInf>", "5.4.2.4 ReversalReasonInformation <RvslRsnInf>", "5.4.2.4.2 Reason <Rsn>", "5.4.2.4.2.1 Code <Cd>"]
file_pages: [593, 594, 595, 596, 597, 598, 599, 600]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.2.4.2.1 Code <Cd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 593 to 600.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 593

```text
Reason <Rsn> contains one of the following ReversalReason4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 593
Or}   Proprietary <Prtry> [1..1] Text 593
5.4.2.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the reversal, as published in an external reason code list.
Datatype: "ExternalReversalReason1Code" on page 1233
5.4.2.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the reversal, in a proprietary form.
Datatype: "Max35Text" on page 1246
5.4.2.4.3  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the reversal reason.
Datatype: "Max105Text" on page 1244
5.4.3 TransactionInformation <TxInf>
Presence: [0..*]
Definition: Information concerning the original transactions, to which the reversal message refers.
Impacted by: C7 "ChargesInformationAndReversedInstructedAmountRule", C28
"ReversedInstructedAmountAndExchangeRate1Rule", C29
"ReversedInstructedAmountAndExchangeRate2Rule"
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
593 March 2026
```

## File page 594

```text
TransactionInformation <TxInf> contains the following PaymentTransaction182 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReversalIdentification <RvslId> [0..1] Text 601
   OriginalGroupInformation <OrgnlGrpInf> [0..1]  601
     OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 602
     OriginalMessageNameIdentification
<OrgnlMsgNmId>
[1..1] Text 602
     OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 602
   OriginalInstructionIdentification <OrgnlInstrId> [0..1] Text 602
   OriginalEndToEndIdentification <OrgnlEndToEndId> [0..1] Text 602
   OriginalTransactionIdentification <OrgnlTxId> [0..1] Text 602
   OriginalUETR <OrgnlUETR> [0..1] IdentifierSet 603
   OriginalClearingSystemReference <OrgnlClrSysRef> [0..1] Text 603
   OriginalInterbankSettlementAmount
<OrgnlIntrBkSttlmAmt>
[0..1] Amount C2, C11 603
   ReversedInterbankSettlementAmount
<RvsdIntrBkSttlmAmt>
[1..1] Amount C1, C10 603
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 604
   SettlementPriority <SttlmPrty> [0..1] CodeSet 604
   SettlementTimeIndication <SttlmTmIndctn> [0..1]  604
     DebitDateTime <DbtDtTm> [0..1] DateTime 605
     CreditDateTime <CdtDtTm> [0..1] DateTime 605
   ReversedInstructedAmount <RvsdInstdAmt> [0..1] Amount C2, C11 605
   ExchangeRate <XchgRate> [0..1] Rate 605
   CompensationAmount <CompstnAmt> [0..1] Amount C2, C11 605
   ChargeBearer <ChrgBr> [0..1] CodeSet 606
   ChargesInformation <ChrgsInf> [0..*]  606
     Amount <Amt> [1..1] Amount C2, C11 607
     Agent <Agt> [1..1] ± 607
     Type <Tp> [0..1]  608
{Or       Code <Cd> [1..1] CodeSet 608
Or}       Proprietary <Prtry> [1..1] ± 608
   InstructingAgent <InstgAgt> [0..1] ± 609
   InstructedAgent <InstdAgt> [0..1] ± 609
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
594 March 2026
```

## File page 595

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReversalReasonInformation <RvslRsnInf> [0..*]  610
     Originator <Orgtr> [0..1] ± 610
     Reason <Rsn> [0..1]  611
{Or       Code <Cd> [1..1] CodeSet 612
Or}       Proprietary <Prtry> [1..1] Text 612
     AdditionalInformation <AddtlInf> [0..*] Text 612
   OriginalTransactionReference <OrgnlTxRef> [0..1]  612
     InterbankSettlementAmount <IntrBkSttlmAmt> [0..1] Amount C2, C11 618
     Amount <Amt> [0..1] ± 619
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 619
     RequestedCollectionDate <ReqdColltnDt> [0..1] Date 619
     RequestedExecutionDate <ReqdExctnDt> [0..1] ± 619
     CreditorSchemeIdentification <CdtrSchmeId> [0..1] ± 620
     SettlementInformation <SttlmInf> [0..1]  C22,
C24,
C30,
C31,
C32,
C33,
C36,
C37
621
       SettlementMethod <SttlmMtd> [1..1] CodeSet 623
       SettlementAccount <SttlmAcct> [0..1] ± C20,
C19
624
       ClearingSystem <ClrSys> [0..1]  624
{Or         Code <Cd> [1..1] CodeSet 625
Or}         Proprietary <Prtry> [1..1] Text 625
       InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 625
       InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C20,
C19
626
       InstructedReimbursementAgent
<InstdRmbrsmntAgt>
[0..1] ± 626
       InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C20,
C19
627
       ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 628
       ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C20,
C19
628
     PaymentTypeInformation <PmtTpInf> [0..1] ± 629
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
595 March 2026
```

## File page 596

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PaymentMethod <PmtMtd> [0..1] CodeSet 630
     MandateRelatedInformation <MndtRltdInf> [0..1]  630
{Or       DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 632
         MandateIdentification <MndtId> [0..1] Text 634
         DateOfSignature <DtOfSgntr> [0..1] Date 634
         AmendmentIndicator <AmdmntInd> [0..1] Indicator 634
         AmendmentInformationDetails <AmdmntInfDtls> [0..1]  634
           OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 635
           OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 635
           OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 636
           OriginalCreditorAgentAccount
<OrgnlCdtrAgtAcct>
[0..1] ± C20,
C19
637
           OriginalDebtor <OrgnlDbtr> [0..1] ± 638
           OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C20,
C19
639
           OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 640
           OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C20,
C19
641
           OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 642
           OriginalFrequency <OrgnlFrqcy> [0..1] ± 642
           OriginalReason <OrgnlRsn> [0..1]  642
{Or             Code <Cd> [1..1] CodeSet 642
Or}             Proprietary <Prtry> [1..1] Text 642
           OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 643
         ElectronicSignature <ElctrncSgntr> [0..1] Text 643
         FirstCollectionDate <FrstColltnDt> [0..1] Date 643
         FinalCollectionDate <FnlColltnDt> [0..1] Date 643
         Frequency <Frqcy> [0..1] ± 643
         Reason <Rsn> [0..1]  643
{Or           Code <Cd> [1..1] CodeSet 644
Or}           Proprietary <Prtry> [1..1] Text 644
         TrackingDays <TrckgDays> [0..1] Text 644
Or}       CreditTransferMandate <CdtTrfMndt> [1..1] ± 644
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
596 March 2026
```

## File page 597

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     RemittanceInformation <RmtInf> [0..1]  645
       Unstructured <Ustrd> [0..*] Text 649
       Structured <Strd> [0..*]  649
         ReferredDocumentInformation <RfrdDocInf> [0..*]  653
           Type <Tp> [0..1]  655
             CodeOrProprietary <CdOrPrtry> [1..1]  655
{Or               Code <Cd> [1..1] CodeSet 655
Or}               Proprietary <Prtry> [1..1] Text 655
             Issuer <Issr> [0..1] Text 655
           Number <Nb> [0..1] Text 656
           RelatedDate <RltdDt> [0..1]  656
             Type <Tp> [1..1]  656
{Or               Code <Cd> [1..1] CodeSet 656
Or}               Proprietary <Prtry> [1..1] Text 656
             Date <Dt> [1..1] Date 656
           LineDetails <LineDtls> [0..*]  657
             Identification <Id> [1..*]  657
               Type <Tp> [0..1]  658
                 CodeOrProprietary <CdOrPrtry> [1..1]  658
{Or                   Code <Cd> [1..1] CodeSet 658
Or}                   Proprietary <Prtry> [1..1] Text 658
                 Issuer <Issr> [0..1] Text 659
               Number <Nb> [0..1] Text 659
               RelatedDate <RltdDt> [0..1] Date 659
             Description <Desc> [0..1] Text 659
             Amount <Amt> [0..1]  C27 659
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  660
                 Type <Tp> [1..1]  660
{Or                   Code <Cd> [1..1] CodeSet 661
Or}                   Proprietary <Prtry> [1..1] Text 661
                 Amount <Amt> [1..1] Amount C2, C11 661
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
597 March 2026
```

## File page 598

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
{Or               Code <Cd> [1..1] CodeSet 664
Or}               Proprietary <Prtry> [1..1] Text 664
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
{Or               Code <Cd> [1..1] CodeSet 666
Or}               Proprietary <Prtry> [1..1] Text 666
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
598 March 2026
```

## File page 599

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
{Or               Code <Cd> [1..1] CodeSet 682
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
599 March 2026
```

## File page 600

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}               Proprietary <Prtry> [1..1] Text 682
             Issuer <Issr> [0..1] Text 682
           Garnishee <Grnshee> [0..1] ± 682
           GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 683
           ReferenceNumber <RefNb> [0..1] Text 684
           Date <Dt> [0..1] Date 685
           RemittedAmount <RmtdAmt> [0..1] Amount C2, C11 685
           FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 685
           EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 685
         SecuritiesData <SctiesData> [0..*]  685
           UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 686
           Amount <Amt> [0..1] Amount C1, C10 686
         AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 686
     UltimateDebtor <UltmtDbtr> [0..1]  686
{Or       Party <Pty> [1..1] ± 687
Or}       Agent <Agt> [1..1] ± 688
     Debtor <Dbtr> [0..1]  689
{Or       Party <Pty> [1..1] ± 689
Or}       Agent <Agt> [1..1] ± 690
     DebtorAccount <DbtrAcct> [0..1] ± C20,
C19
691
     DebtorAgent <DbtrAgt> [0..1] ± 692
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C20,
C19
692
     CreditorAgent <CdtrAgt> [0..1] ± 693
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C20,
C19
694
     Creditor <Cdtr> [0..1]  695
{Or       Party <Pty> [1..1] ± 695
Or}       Agent <Agt> [1..1] ± 696
     CreditorAccount <CdtrAcct> [0..1] ± C20,
C19
697
     UltimateCreditor <UltmtCdtr> [0..1]  698
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
600 March 2026
```

