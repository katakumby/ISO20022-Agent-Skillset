---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.17 CardTransaction <CardTx>", "4.4.2.14.17.3 AggregatedEntry <AggtdNtry>", "4.4.2.14.17.3.5 TransactionDateRange <TxDtRg>"]
file_pages: [612, 613, 614, 615, 616, 617, 618, 619, 620, 621]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.17.3.5 TransactionDateRange <TxDtRg>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 612 to 621.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 612

```text
Datatype: "Max35Text" on page 916
4.4.2.14.17.3.5  TransactionDateRange <TxDtRg>
Presence: [0..1]
Definition: Date range on which the globalisation applies.
TransactionDateRange <TxDtRg> contains one of the following elements (see
"DateOrDateTimePeriod1Choice" on page 827 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 827
Or}   DateTime <DtTm> [1..1] ± 827
4.4.2.14.17.4  PrePaidAccount <PrePdAcct>
Presence: [0..1]
Definition: Prepaid account for the transfer or loading of an amount of money.
Impacted by: C19 "IdentificationOrProxyPresenceRule", C17 "IdentificationAndProxyGuideline"
PrePaidAccount <PrePdAcct> contains the following elements (see "CashAccount40" on page 796
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 796
   Type <Tp> [0..1] ± 796
   Currency <Ccy> [0..1] CodeSet C1 797
   Name <Nm> [0..1] Text 797
   Proxy <Prxy> [0..1] ± 797
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
4.4.2.14.18  EntryDetails <NtryDtls>
Presence: [0..*]
Definition: Provides details on the entry.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
612 March 2026
```

## File page 613

```text
EntryDetails <NtryDtls> contains the following EntryDetails16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Batch <Btch> [0..1]  625
     MessageIdentification <MsgId> [0..1] Text 625
     PaymentInformationIdentification <PmtInfId> [0..1] Text 625
     NumberOfTransactions <NbOfTxs> [0..1] Text 625
     TotalAmount <TtlAmt> [0..1] Amount C2, C6 625
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 626
   TransactionDetails <TxDtls> [0..*]  C24 626
     References <Refs> [0..1]  638
       MessageIdentification <MsgId> [0..1] Text 639
       AccountServicerReference <AcctSvcrRef> [0..1] Text 639
       PaymentInformationIdentification <PmtInfId> [0..1] Text 639
       InstructionIdentification <InstrId> [0..1] Text 640
       EndToEndIdentification <EndToEndId> [0..1] Text 640
       UETR <UETR> [0..1] IdentifierSet 640
       TransactionIdentification <TxId> [0..1] Text 640
       MandateIdentification <MndtId> [0..1] Text 640
       ChequeNumber <ChqNb> [0..1] Text 641
       ClearingSystemReference <ClrSysRef> [0..1] Text 641
       AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 641
       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 641
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 641
       ProcessingIdentification <PrcgId> [0..1] Text 641
       ReturnIdentification <RtrId> [0..1] Text 641
       Proprietary <Prtry> [0..*]  642
         Type <Tp> [1..1] Text 642
         Reference <Ref> [1..1] Text 642
     Amount <Amt> [0..1] Amount C2, C6 642
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 642
     AmountDetails <AmtDtls> [0..1] ± 643
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
613 March 2026
```

## File page 614

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Availability <Avlbty> [0..*] ± 643
     BankTransactionCode <BkTxCd> [0..1] ± C11,
C14
644
     Charges <Chrgs> [0..1]  644
       TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt> [0..1] Amount C2, C6 645
       Record <Rcrd> [0..*]  645
         Amount <Amt> [1..1] Amount C2, C6 646
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 646
         ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 647
         Type <Tp> [0..1]  647
{Or           Code <Cd> [1..1] CodeSet 647
Or}           Proprietary <Prtry> [1..1] ± 647
         Rate <Rate> [0..1] Rate 647
         Bearer <Br> [0..1] CodeSet 648
         Agent <Agt> [0..1] ± 648
         Tax <Tax> [0..1]  649
           Identification <Id> [0..1] Text 649
           Rate <Rate> [0..1] Rate 649
           Amount <Amt> [0..1] Amount C2, C6 649
     Interest <Intrst> [0..1] ± 649
     RelatedParties <RltdPties> [0..1]  650
       InitiatingParty <InitgPty> [0..1]  651
{Or         Party <Pty> [1..1] ± 652
Or}         Agent <Agt> [1..1] ± 653
       Debtor <Dbtr> [0..1]  654
{Or         Party <Pty> [1..1] ± 654
Or}         Agent <Agt> [1..1] ± 655
       DebtorAccount <DbtrAcct> [0..1] ± C19,
C17
656
       UltimateDebtor <UltmtDbtr> [0..1]  657
{Or         Party <Pty> [1..1] ± 657
Or}         Agent <Agt> [1..1] ± 658
       Creditor <Cdtr> [0..1]  659
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
614 March 2026
```

## File page 615

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         Party <Pty> [1..1] ± 659
Or}         Agent <Agt> [1..1] ± 660
       CreditorAccount <CdtrAcct> [0..1] ± C19,
C17
661
       UltimateCreditor <UltmtCdtr> [0..1]  662
{Or         Party <Pty> [1..1] ± 662
Or}         Agent <Agt> [1..1] ± 663
       TradingParty <TradgPty> [0..1]  664
{Or         Party <Pty> [1..1] ± 664
Or}         Agent <Agt> [1..1] ± 665
       Proprietary <Prtry> [0..*]  666
         Type <Tp> [1..1] Text 666
         Party <Pty> [1..1]  666
{Or           Party <Pty> [1..1] ± 667
Or}           Agent <Agt> [1..1] ± 668
     RelatedAgents <RltdAgts> [0..1]  669
       InstructingAgent <InstgAgt> [0..1] ± 670
       InstructedAgent <InstdAgt> [0..1] ± 671
       DebtorAgent <DbtrAgt> [0..1] ± 672
       CreditorAgent <CdtrAgt> [0..1] ± 673
       IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 673
       IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 674
       IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 675
       ReceivingAgent <RcvgAgt> [0..1] ± 676
       DeliveringAgent <DlvrgAgt> [0..1] ± 677
       IssuingAgent <IssgAgt> [0..1] ± 678
       SettlementPlace <SttlmPlc> [0..1] ± 679
       Proprietary <Prtry> [0..*]  679
         Type <Tp> [1..1] Text 679
         Agent <Agt> [1..1] ± 679
     LocalInstrument <LclInstrm> [0..1]  680
{Or       Code <Cd> [1..1] CodeSet 680
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
615 March 2026
```

## File page 616

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       Proprietary <Prtry> [1..1] Text 680
     PaymentTypeInformation <PmtTpInf> [0..1] ± 681
     Purpose <Purp> [0..1] ± 681
     RelatedRemittanceInformation <RltdRmtInf> [0..10]  681
       RemittanceIdentification <RmtId> [0..1] Text 682
       RemittanceLocationDetails <RmtLctnDtls> [0..*]  682
         Method <Mtd> [1..1] CodeSet 682
         ElectronicAddress <ElctrncAdr> [0..1] Text 683
         PostalAddress <PstlAdr> [0..1]  683
           Name <Nm> [1..1] Text 683
           Address <Adr> [1..1] ± 683
     RemittanceInformation <RmtInf> [0..1]  684
       Unstructured <Ustrd> [0..*] Text 688
       Structured <Strd> [0..*]  688
         ReferredDocumentInformation <RfrdDocInf> [0..*]  692
           Type <Tp> [0..1]  694
             CodeOrProprietary <CdOrPrtry> [1..1]  694
{Or               Code <Cd> [1..1] CodeSet 694
Or}               Proprietary <Prtry> [1..1] Text 694
             Issuer <Issr> [0..1] Text 694
           Number <Nb> [0..1] Text 695
           RelatedDate <RltdDt> [0..1]  695
             Type <Tp> [1..1]  695
{Or               Code <Cd> [1..1] CodeSet 695
Or}               Proprietary <Prtry> [1..1] Text 695
             Date <Dt> [1..1] Date 695
           LineDetails <LineDtls> [0..*]  696
             Identification <Id> [1..*]  696
               Type <Tp> [0..1]  697
                 CodeOrProprietary <CdOrPrtry> [1..1]  697
{Or                   Code <Cd> [1..1] CodeSet 697
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
616 March 2026
```

## File page 617

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}                   Proprietary <Prtry> [1..1] Text 697
                 Issuer <Issr> [0..1] Text 698
               Number <Nb> [0..1] Text 698
               RelatedDate <RltdDt> [0..1] Date 698
             Description <Desc> [0..1] Text 698
             Amount <Amt> [0..1]  C26 698
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  699
                 Type <Tp> [1..1]  699
{Or                   Code <Cd> [1..1] CodeSet 700
Or}                   Proprietary <Prtry> [1..1] Text 700
                 Amount <Amt> [1..1] Amount C2, C6 700
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
{Or               Code <Cd> [1..1] CodeSet 703
Or}               Proprietary <Prtry> [1..1] Text 703
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
{Or               Code <Cd> [1..1] CodeSet 705
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
617 March 2026
```

## File page 618

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}               Proprietary <Prtry> [1..1] Text 705
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
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
618 March 2026
```

## File page 619

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or               Code <Cd> [1..1] CodeSet 721
Or}               Proprietary <Prtry> [1..1] Text 721
             Issuer <Issr> [0..1] Text 721
           Garnishee <Grnshee> [0..1] ± 721
           GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 722
           ReferenceNumber <RefNb> [0..1] Text 723
           Date <Dt> [0..1] Date 724
           RemittedAmount <RmtdAmt> [0..1] Amount C2, C6 724
           FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 724
           EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 724
         SecuritiesData <SctiesData> [0..*]  724
           UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 725
           Amount <Amt> [0..1] Amount C1, C7 725
         AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 725
     RelatedDates <RltdDts> [0..1]  725
       AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 726
       TradeActivityContractualSettlementDate
<TradActvtyCtrctlSttlmDt>
[0..1] Date 726
       TradeDate <TradDt> [0..1] Date 726
       InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 726
       StartDate <StartDt> [0..1] Date 726
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
619 March 2026
```

## File page 620

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       EndDate <EndDt> [0..1] Date 727
       TransactionDateTime <TxDtTm> [0..1] DateTime 727
       Proprietary <Prtry> [0..*]  727
         Type <Tp> [1..1] Text 727
         Date <Dt> [1..1] ± 727
     RelatedPrice <RltdPric> [0..1]  727
{Or       DealPrice <DealPric> [1..1] ± 728
Or}       Proprietary <Prtry> [1..*]  728
         Type <Tp> [1..1] Text 728
         Price <Pric> [1..1] Amount C2, C6 728
     RelatedQuantities <RltdQties> [0..*]  729
{Or       Quantity <Qty> [1..1] ± C10 729
Or       OriginalAndCurrentFaceAmount
<OrgnlAndCurFaceAmt>
[1..1] ± 730
Or}       Proprietary <Prtry> [1..1]  730
         Type <Tp> [1..1] Text 730
         Quantity <Qty> [1..1] Text 730
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C8, C9,
C20,
C21,
C23
730
     Tax <Tax> [0..1]  731
       Creditor <Cdtr> [0..1] ± 733
       Debtor <Dbtr> [0..1] ± 733
       UltimateDebtor <UltmtDbtr> [0..1] ± 733
       AdministrationZone <AdmstnZone> [0..1] Text 734
       ReferenceNumber <RefNb> [0..1] Text 734
       Method <Mtd> [0..1] Text 734
       TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 734
       TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 735
       Date <Dt> [0..1] Date 735
       SequenceNumber <SeqNb> [0..1] Quantity 735
       Record <Rcrd> [0..*]  735
         Type <Tp> [0..1] Text 736
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
620 March 2026
```

## File page 621

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Category <Ctgy> [0..1] Text 736
         CategoryDetails <CtgyDtls> [0..1] Text 736
         DebtorStatus <DbtrSts> [0..1] Text 737
         CertificateIdentification <CertId> [0..1] Text 737
         FormsCode <FrmsCd> [0..1] Text 737
         Period <Prd> [0..1]  737
           Year <Yr> [0..1] Year 737
           Type <Tp> [0..1] CodeSet 737
           FromToDate <FrToDt> [0..1] ± 738
         TaxAmount <TaxAmt> [0..1]  739
           Rate <Rate> [0..1] Rate 739
           TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 739
           TotalAmount <TtlAmt> [0..1] Amount C2, C6 739
           Details <Dtls> [0..*]  740
             Period <Prd> [0..1]  740
               Year <Yr> [0..1] Year 740
               Type <Tp> [0..1] CodeSet 741
               FromToDate <FrToDt> [0..1] ± 741
             Amount <Amt> [1..1] Amount C2, C6 742
         AdditionalInformation <AddtlInf> [0..1] Text 742
     ReturnInformation <RtrInf> [0..1]  C27 742
       OriginalBankTransactionCode <OrgnlBkTxCd> [0..1] ± C11,
C14
743
       Originator <Orgtr> [0..1] ± 744
       Reason <Rsn> [0..1]  745
{Or         Code <Cd> [1..1] CodeSet 746
Or}         Proprietary <Prtry> [1..1] Text 746
       AdditionalInformation <AddtlInf> [0..*] Text 746
     RelatedCorporateAction <RltdCorpActn> [0..1]  746
       EventType <EvtTp> [1..1] ± C12 746
       CorporateActionEventIdentification
<CorpActnEvtId>
[1..1] Text 747
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
621 March 2026
```

