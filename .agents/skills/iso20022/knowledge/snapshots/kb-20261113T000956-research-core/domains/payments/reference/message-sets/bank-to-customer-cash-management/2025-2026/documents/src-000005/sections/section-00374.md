---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.1.5 OriginalBusinessQuery <OrgnlBizQry>"]
file_pages: [545, 546, 547, 548, 549, 550, 551, 552, 553, 554]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.1.5 OriginalBusinessQuery <OrgnlBizQry>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 545 to 554.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 545

```text
MessagePagination <MsgPgntn> contains the following elements (see "Pagination1" on page 844
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 844
   LastPageIndicator <LastPgInd> [1..1] Indicator 845
4.4.1.5  OriginalBusinessQuery <OrgnlBizQry>
Presence: [0..1]
Definition: Unique identification, as assigned by the original requestor, to unambiguously identify the
business query message.
OriginalBusinessQuery <OrgnlBizQry> contains the following elements (see
"OriginalBusinessQuery1" on page 858 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 858
   MessageNameIdentification <MsgNmId> [0..1] Text 858
   CreationDateTime <CreDtTm> [0..1] DateTime 859
4.4.1.6  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Further details of the message.
Datatype: "Max500Text" on page 917
4.4.2 Notification <Ntfctn>
Presence: [1..*]
Definition: Notifies debit and credit entries for the account.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
545 March 2026
```

## File page 546

```text
Notification <Ntfctn> contains the following AccountNotification25 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 561
   NotificationPagination <NtfctnPgntn> [0..1] ± 562
   ElectronicSequenceNumber <ElctrncSeqNb> [0..1] Quantity 562
   ReportingSequence <RptgSeq> [0..1] ± 562
   LegalSequenceNumber <LglSeqNb> [0..1] Quantity 562
   CreationDateTime <CreDtTm> [0..1] DateTime 563
   FromToDate <FrToDt> [0..1] ± 563
   CopyDuplicateIndicator <CpyDplctInd> [0..1] CodeSet 563
   ReportingSource <RptgSrc> [0..1] ± 563
   Account <Acct> [1..1]  C18,
C16
564
     Identification <Id> [0..1] ± 564
     Type <Tp> [0..1] ± 564
     Currency <Ccy> [0..1] CodeSet C2 565
     Name <Nm> [0..1] Text 565
     Proxy <Prxy> [0..1] ± 565
     Owner <Ownr> [0..1] ± 566
     Servicer <Svcr> [0..1] ± 566
   RelatedAccount <RltdAcct> [0..1] ± C19,
C17
567
   Interest <Intrst> [0..*]  568
     Type <Tp> [0..1]  568
{Or       Code <Cd> [1..1] CodeSet 569
Or}       Proprietary <Prtry> [1..1] Text 569
     Rate <Rate> [0..*]  569
       Type <Tp> [1..1] ± 569
       ValidityRange <VldtyRg> [0..1] ± 569
     FromToDate <FrToDt> [0..1] ± 570
     Reason <Rsn> [0..1] Text 570
     Tax <Tax> [0..1]  570
       Identification <Id> [0..1] Text 570
       Rate <Rate> [0..1] Rate 571
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
546 March 2026
```

## File page 547

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Amount <Amt> [0..1] Amount C2, C6 571
   TransactionsSummary <TxsSummry> [0..1] ± 571
   Entry <Ntry> [0..*]  C25 572
     EntryReference <NtryRef> [0..1] Text 587
     Amount <Amt> [1..1] Amount C2, C6 587
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 588
     ReversalIndicator <RvslInd> [0..1] Indicator 588
     Status <Sts> [1..1] ± 588
     BookingDate <BookgDt> [0..1] ± 589
     ValueDate <ValDt> [0..1] ± 589
     AccountServicerReference <AcctSvcrRef> [0..1] Text 589
     Availability <Avlbty> [0..*] ± 590
     BankTransactionCode <BkTxCd> [1..1] ± C11,
C14
590
     CommissionWaiverIndicator <ComssnWvrInd> [0..1] Indicator 591
     AdditionalInformationIndicator <AddtlInfInd> [0..1]  591
       MessageNameIdentification <MsgNmId> [0..1] Text 591
       MessageIdentification <MsgId> [0..1] Text 591
     AmountDetails <AmtDtls> [0..1] ± 591
     Charges <Chrgs> [0..1]  592
       TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt> [0..1] Amount C2, C6 592
       Record <Rcrd> [0..*]  593
         Amount <Amt> [1..1] Amount C2, C6 593
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 594
         ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 594
         Type <Tp> [0..1]  594
{Or           Code <Cd> [1..1] CodeSet 594
Or}           Proprietary <Prtry> [1..1] ± 595
         Rate <Rate> [0..1] Rate 595
         Bearer <Br> [0..1] CodeSet 595
         Agent <Agt> [0..1] ± 595
         Tax <Tax> [0..1]  596
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
547 March 2026
```

## File page 548

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Identification <Id> [0..1] Text 596
           Rate <Rate> [0..1] Rate 596
           Amount <Amt> [0..1] Amount C2, C6 597
     TechnicalInputChannel <TechInptChanl> [0..1]  597
{Or       Code <Cd> [1..1] CodeSet 597
Or}       Proprietary <Prtry> [1..1] Text 597
     Interest <Intrst> [0..1] ± 597
     CardTransaction <CardTx> [0..1]  598
       Card <Card> [0..1]  600
         PlainCardData <PlainCardData> [0..1]  601
           PAN <PAN> [1..1] Text 602
           CardSequenceNumber <CardSeqNb> [0..1] Text 602
           EffectiveDate <FctvDt> [0..1] YearMonth 602
           ExpiryDate <XpryDt> [1..1] YearMonth 602
           ServiceCode <SvcCd> [0..1] Text 602
           TrackData <TrckData> [0..*]  603
             TrackNumber <TrckNb> [0..1] Text 603
             TrackValue <TrckVal> [1..1] Text 603
           CardSecurityCode <CardSctyCd> [0..1]  603
             CSCManagement <CSCMgmt> [1..1] CodeSet 603
             CSCValue <CSCVal> [0..1] Text 604
         CardCountryCode <CardCtryCd> [0..1] Text 604
         CardBrand <CardBrnd> [0..1] ± 604
         AdditionalCardData <AddtlCardData> [0..1] Text 604
       POI <POI> [0..1]  604
         Identification <Id> [1..1] ± 605
         SystemName <SysNm> [0..1] Text 606
         GroupIdentification <GrpId> [0..1] Text 606
         Capabilities <Cpblties> [0..1]  606
           CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 606
           CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 607
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
548 March 2026
```

## File page 549

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 607
           DisplayCapabilities <DispCpblties> [0..*]  608
             DisplayType <DispTp> [1..1] CodeSet 608
             NumberOfLines <NbOfLines> [1..1] Text 608
             LineWidth <LineWidth> [1..1] Text 608
           PrintLineWidth <PrtLineWidth> [0..1] Text 608
         Component <Cmpnt> [0..*]  608
           POIComponentType <POICmpntTp> [1..1] CodeSet 609
           ManufacturerIdentification <ManfctrId> [0..1] Text 609
           Model <Mdl> [0..1] Text 609
           VersionNumber <VrsnNb> [0..1] Text 609
           SerialNumber <SrlNb> [0..1] Text 610
           ApprovalNumber <ApprvlNb> [0..*] Text 610
       AggregatedEntry <AggtdNtry> [0..1]  610
         AdditionalService <AddtlSvc> [0..1] CodeSet 610
         TransactionCategory <TxCtgy> [0..1] CodeSet 611
         SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 611
         SequenceNumberRange <SeqNbRg> [0..1]  611
           FirstTransaction <FrstTx> [0..1] Text 611
           LastTransaction <LastTx> [0..1] Text 611
         TransactionDateRange <TxDtRg> [0..1] ± 612
       PrePaidAccount <PrePdAcct> [0..1] ± C19,
C17
612
     EntryDetails <NtryDtls> [0..*]  612
       Batch <Btch> [0..1]  625
         MessageIdentification <MsgId> [0..1] Text 625
         PaymentInformationIdentification <PmtInfId> [0..1] Text 625
         NumberOfTransactions <NbOfTxs> [0..1] Text 625
         TotalAmount <TtlAmt> [0..1] Amount C2, C6 625
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 626
       TransactionDetails <TxDtls> [0..*]  C24 626
         References <Refs> [0..1]  638
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
549 March 2026
```

## File page 550

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
         Availability <Avlbty> [0..*] ± 643
         BankTransactionCode <BkTxCd> [0..1] ± C11,
C14
644
         Charges <Chrgs> [0..1]  644
           TotalChargesAndTaxAmount
<TtlChrgsAndTaxAmt>
[0..1] Amount C2, C6 645
           Record <Rcrd> [0..*]  645
             Amount <Amt> [1..1] Amount C2, C6 646
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 646
             ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 647
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
550 March 2026
```

## File page 551

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Type <Tp> [0..1]  647
{Or               Code <Cd> [1..1] CodeSet 647
Or}               Proprietary <Prtry> [1..1] ± 647
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
{Or             Party <Pty> [1..1] ± 652
Or}             Agent <Agt> [1..1] ± 653
           Debtor <Dbtr> [0..1]  654
{Or             Party <Pty> [1..1] ± 654
Or}             Agent <Agt> [1..1] ± 655
           DebtorAccount <DbtrAcct> [0..1] ± C19,
C17
656
           UltimateDebtor <UltmtDbtr> [0..1]  657
{Or             Party <Pty> [1..1] ± 657
Or}             Agent <Agt> [1..1] ± 658
           Creditor <Cdtr> [0..1]  659
{Or             Party <Pty> [1..1] ± 659
Or}             Agent <Agt> [1..1] ± 660
           CreditorAccount <CdtrAcct> [0..1] ± C19,
C17
661
           UltimateCreditor <UltmtCdtr> [0..1]  662
{Or             Party <Pty> [1..1] ± 662
Or}             Agent <Agt> [1..1] ± 663
           TradingParty <TradgPty> [0..1]  664
{Or             Party <Pty> [1..1] ± 664
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
551 March 2026
```

## File page 552

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             Agent <Agt> [1..1] ± 665
           Proprietary <Prtry> [0..*]  666
             Type <Tp> [1..1] Text 666
             Party <Pty> [1..1]  666
{Or               Party <Pty> [1..1] ± 667
Or}               Agent <Agt> [1..1] ± 668
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
{Or           Code <Cd> [1..1] CodeSet 680
Or}           Proprietary <Prtry> [1..1] Text 680
         PaymentTypeInformation <PmtTpInf> [0..1] ± 681
         Purpose <Purp> [0..1] ± 681
         RelatedRemittanceInformation <RltdRmtInf> [0..10]  681
           RemittanceIdentification <RmtId> [0..1] Text 682
           RemittanceLocationDetails <RmtLctnDtls> [0..*]  682
             Method <Mtd> [1..1] CodeSet 682
             ElectronicAddress <ElctrncAdr> [0..1] Text 683
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
552 March 2026
```

## File page 553

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             PostalAddress <PstlAdr> [0..1]  683
               Name <Nm> [1..1] Text 683
               Address <Adr> [1..1] ± 683
         RemittanceInformation <RmtInf> [0..1]  684
           Unstructured <Ustrd> [0..*] Text 688
           Structured <Strd> [0..*]  688
             ReferredDocumentInformation <RfrdDocInf> [0..*]  692
               Type <Tp> [0..1]  694
                 CodeOrProprietary <CdOrPrtry> [1..1]  694
{Or                   Code <Cd> [1..1] CodeSet 694
Or}                   Proprietary <Prtry> [1..1] Text 694
                 Issuer <Issr> [0..1] Text 694
               Number <Nb> [0..1] Text 695
               RelatedDate <RltdDt> [0..1]  695
                 Type <Tp> [1..1]  695
{Or                   Code <Cd> [1..1] CodeSet 695
Or}                   Proprietary <Prtry> [1..1] Text 695
                 Date <Dt> [1..1] Date 695
               LineDetails <LineDtls> [0..*]  696
                 Identification <Id> [1..*]  696
                   Type <Tp> [0..1]  697
                     CodeOrProprietary <CdOrPrtry> [1..1]  697
{Or                       Code <Cd> [1..1] CodeSet 697
Or}                       Proprietary <Prtry> [1..1] Text 697
                     Issuer <Issr> [0..1] Text 698
                   Number <Nb> [0..1] Text 698
                   RelatedDate <RltdDt> [0..1] Date 698
                 Description <Desc> [0..1] Text 698
                 Amount <Amt> [0..1]  C26 698
                   RemittanceAmountAndType
<RmtAmtAndTp>
[0..*]  699
                     Type <Tp> [1..1]  699
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
553 March 2026
```

## File page 554

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or                       Code <Cd> [1..1] CodeSet 700
Or}                       Proprietary <Prtry> [1..1] Text 700
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
{Or                   Code <Cd> [1..1] CodeSet 703
Or}                   Proprietary <Prtry> [1..1] Text 703
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
{Or                   Code <Cd> [1..1] CodeSet 705
Or}                   Proprietary <Prtry> [1..1] Text 705
                 Issuer <Issr> [0..1] Text 706
               Reference <Ref> [0..1] Text 706
             Invoicer <Invcr> [0..1] ± 706
             Invoicee <Invcee> [0..1] ± 707
             TaxRemittance <TaxRmt> [0..1]  708
               Creditor <Cdtr> [0..1] ± 710
               Debtor <Dbtr> [0..1] ± 710
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
554 March 2026
```

