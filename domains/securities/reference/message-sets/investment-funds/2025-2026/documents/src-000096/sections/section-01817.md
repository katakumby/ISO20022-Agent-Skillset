---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.2 Structure"]
file_pages: [2524, 2525, 2526, 2527, 2528, 2529, 2530, 2531, 2532, 2533]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2524 to 2533.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2524

```text
47.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SbcptBlkOrdr> [1..1]  C2
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..*] ± 2543
   BulkOrderDetails <BlkOrdrDtls> [1..1]  C7, C33,
C35
2544
     MasterReference <MstrRef> [0..1] Text 2561
     PlaceOfTrade <PlcOfTrad> [0..1] ± 2561
     OrderDateTime <OrdrDtTm> [0..1] DateTime 2561
     ExpiryDateTime <XpryDtTm> [0..1] ± 2561
     RequestedFutureTradeDate <ReqdFutrTradDt> [0..1] Date 2562
     CancellationRight <CxlRght> [0..1] ± 2562
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C21 2562
       Identification <Id> [1..1]  2564
{Or         ISIN <ISIN> [1..1] IdentifierSet 2564
Or         SEDOL <SEDOL> [1..1] IdentifierSet 2565
Or         CUSIP <CUSIP> [1..1] IdentifierSet 2565
Or         RIC <RIC> [1..1] IdentifierSet 2565
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 2565
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 2565
Or         CTA <CTA> [1..1] IdentifierSet 2565
Or         QUICK <QUICK> [1..1] IdentifierSet 2565
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 2566
Or         Dutch <Dtch> [1..1] IdentifierSet 2566
Or         Valoren <Vlrn> [1..1] IdentifierSet 2566
Or         Sicovam <SCVM> [1..1] IdentifierSet 2566
Or         Belgian <Belgn> [1..1] IdentifierSet 2566
Or         Common <Cmon> [1..1] IdentifierSet 2566
Or         DTI <DTI> [1..1] IdentifierSet 2566
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  2566
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2524 May 2026
```

## File page 2525

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Identification <Id> [1..1] Text 2567
           IdentificationSource <IdSrc> [1..1] ± 2567
       Name <Nm> [0..1] Text 2567
       ShortName <ShrtNm> [0..1] Text 2567
       SupplementaryIdentification <SplmtryId> [0..1] Text 2567
       ClassType <ClssTp> [0..1] Text 2567
       SecuritiesForm <SctiesForm> [0..1] CodeSet 2568
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 2568
       ProductGroup <PdctGrp> [0..1] Text 2568
       SeriesIdentification <SrsId> [0..1]  C34 2568
         SeriesDate <SrsDt> [0..1] ± 2569
         SeriesName <SrsNm> [0..1] Text 2569
     IndividualOrderDetails <IndvOrdrDtls> [1..*]  C26,
C29,
C30
2569
       OrderReference <OrdrRef> [1..1] Text 2580
       ClientReference <ClntRef> [0..1] Text 2580
       NonceIdentification <NonceId> [0..1] Text 2580
       OrderType <OrdrTp> [0..10] ± 2580
       AmountOrUnits <AmtOrUnits> [1..1]  2581
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 2581
Or         GrossAmount <GrssAmt> [1..1] Amount C4, C9 2581
Or         NetAmount <NetAmt> [1..1] Amount C4, C9 2582
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 2582
       Rounding <Rndg> [0..1] CodeSet 2582
       SettlementAmount <SttlmAmt> [0..1] Amount C3, C10 2582
       CashSettlementDate <CshSttlmDt> [0..1] Date 2583
       SettlementMethod <SttlmMtd> [0..1] CodeSet 2583
       IncomePreference <IncmPref> [0..1] CodeSet 2583
       InvestmentAccountDetails <InvstmtAcctDtls> [1..1]  C25 2583
         AccountIdentification <AcctId> [1..1] Text 2584
         AccountName <AcctNm> [0..1] Text 2584
         AccountDesignation <AcctDsgnt> [0..1] Text 2584
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2525 May 2026
```

## File page 2526

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         OwnerIdentification <OwnrId> [0..*] ± 2584
         AccountServicer <AcctSvcr> [0..1] ± 2585
         OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 2585
         SubAccountDetails <SubAcctDtls> [0..1] ± 2585
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2586
       BeneficiaryDetails <BnfcryDtls> [0..*] ± C28 2586
       ForeignExchangeDetails <FXDtls> [0..1]  2587
         UnitCurrency <UnitCcy> [1..1] CodeSet C3 2588
         QuotedCurrency <QtdCcy> [1..1] CodeSet C3 2588
         ExchangeRate <XchgRate> [1..1] Rate 2588
         QuotationDate <QtnDt> [0..1] DateTime 2589
         QuotingInstitution <QtgInstn> [0..1] ± 2589
       LetterIntentReference <LttrInttRef> [0..1] Text 2589
       AccumulationRightReference <AcmltnRghtRef> [0..1] Text 2589
       TransactionOverhead <TxOvrhd> [0..1]  C19 2589
         CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 2593
         IndividualFee <IndvFee> [0..*]  C18,
C36,
C37
2593
           Type <Tp> [1..1]  2594
{Or             Code <Cd> [1..1] CodeSet 2594
Or}             Proprietary <Prtry> [1..1] ± 2595
           Basis <Bsis> [0..1]  2595
{Or             Code <Cd> [1..1] CodeSet 2596
Or}             Proprietary <Prtry> [1..1] ± 2596
           StandardAmount <StdAmt> [0..1] Amount C3, C10 2596
           StandardRate <StdRate> [0..1] Rate 2597
           DiscountDetails <DscntDtls> [0..1]  C16 2597
             Amount <Amt> [0..1] Amount C3, C10 2597
             Rate <Rate> [0..1] Rate 2598
             Basis <Bsis> [0..1]  2598
{Or               Code <Cd> [1..1] CodeSet 2598
Or}               Proprietary <Prtry> [1..1] ± 2599
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2526 May 2026
```

## File page 2527

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 2599
           RequestedRate <ReqdRate> [0..1] Rate 2599
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 2600
           RecipientIdentification <RcptId> [0..1] ± 2600
         IndividualTax <IndvTax> [0..*]  2600
           Type <Tp> [1..1]  2601
{Or             Code <Cd> [1..1] CodeSet 2601
Or}             Proprietary <Prtry> [1..1] ± 2603
           Tax <Tax> [0..1]  2603
{Or             Amount <Amt> [1..1] Amount C3, C10 2603
Or}             Rate <Rate> [1..1] Rate 2604
           Country <Ctry> [0..1] CodeSet C8 2604
           ExemptionIndicator <XmptnInd> [1..1] Indicator 2604
           ExemptionReason <XmptnRsn> [0..1]  2604
{Or             Code <Cd> [1..1] CodeSet 2604
Or}             Proprietary <Prtry> [1..1] ± 2607
           RecipientIdentification <RcptId> [0..1] ± 2607
           TaxCalculationDetails <TaxClctnDtls> [0..1]  2608
             Basis <Bsis> [1..1]  2608
{Or               Code <Cd> [1..1] CodeSet 2608
Or}               Proprietary <Prtry> [1..1] ± 2608
         DigitalNetworkFee <DgtlNtwkFee> [0..*]  2609
           FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
2609
             ISIN <ISIN> [0..1] IdentifierSet 2611
             OtherIdentification <OthrId> [0..*]  2611
               Identification <Id> [1..1] Text 2611
               Suffix <Sfx> [0..1] Text 2611
               Type <Tp> [1..1]  2611
{Or                 Code <Cd> [1..1] CodeSet 2612
Or}                 Proprietary <Prtry> [1..1] Text 2613
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2527 May 2026
```

## File page 2528

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Description <Desc> [0..1] Text 2613
           Quantity <Qty> [1..1]  2614
{Or             Quantity <Qty> [1..1] ± C15 2614
Or}             ProprietaryQuantity <PrtryQty> [1..1]  2614
               Quantity <Qty> [1..1] Quantity 2615
               QuantityType <QtyTp> [1..1] Text 2615
               Issuer <Issr> [1..1] Text 2615
               SchemeName <SchmeNm> [0..1] Text 2615
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2615
       SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  2615
         SettlementDate <SttlmDt> [0..1] Date 2617
         SettlementPlace <SttlmPlc> [1..1]  2617
           Party <Pty> [1..1]  2618
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C5 2618
Or             ProprietaryIdentification <PrtryId> [1..1] ± 2618
Or             NameAndAddress <NmAndAdr> [1..1] ± 2619
Or}             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2619
           LEI <LEI> [0..1] IdentifierSet 2619
         SafekeepingPlace <SfkpgPlc> [0..1] ± 2619
         SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 2620
         TradeTransactionCondition <TradTxCond> [0..*] ± 2620
         SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2620
         ReceivingSideDetails <RcvgSdDtls> [1..1]  C31,
C32
2621
           ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2622
             PartyIdentification <PtyId> [1..1] ± 2622
             AccountIdentification <AcctId> [0..1] Text 2622
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2622
           ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2623
             PartyIdentification <PtyId> [1..1] ± 2623
             AccountIdentification <AcctId> [0..1] Text 2623
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2623
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2528 May 2026
```

## File page 2529

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2624
             PartyIdentification <PtyId> [1..1] ± 2624
             AccountIdentification <AcctId> [0..1] Text 2624
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2624
           ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2625
             PartyIdentification <PtyId> [1..1] ± 2625
             AccountIdentification <AcctId> [0..1] Text 2625
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2625
         DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C12
2626
           DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2627
             PartyIdentification <PtyId> [1..1] ± 2627
             AccountIdentification <AcctId> [0..1] Text 2627
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2628
           DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2628
             PartyIdentification <PtyId> [1..1] ± 2628
             AccountIdentification <AcctId> [0..1] Text 2628
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2628
           DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2629
             PartyIdentification <PtyId> [1..1] ± 2629
             AccountIdentification <AcctId> [0..1] Text 2629
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2629
           DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2630
             PartyIdentification <PtyId> [1..1] ± 2630
             AccountIdentification <AcctId> [0..1] Text 2630
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2630
       PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 2631
       PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 2631
       CashSettlementDetails <CshSttlmDtls> [0..1]  2631
         PaymentInstrument <PmtInstrm> [1..1]  2636
{Or           PaymentCardDetails <PmtCardDtls> [1..1]  2641
             Type <Tp> [1..1] CodeSet 2642
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2529 May 2026
```

## File page 2530

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Number <Nb> [1..1] Text 2642
             HolderName <HldrNm> [1..1] Text 2642
             StartDate <StartDt> [0..1] YearMonth 2642
             ExpiryDate <XpryDt> [1..1] YearMonth 2642
             CardIssuerName <CardIssrNm> [0..1] Text 2642
             CardIssuerIdentification <CardIssrId> [0..1] ± 2642
             SecurityCode <SctyCd> [0..1] Text 2643
             SequenceNumber <SeqNb> [0..1] Text 2643
Or           CreditTransferDetails <CdtTrfDtls> [1..1]  2643
             Reference <Ref> [0..1] Text 2646
             Debtor <Dbtr> [0..1] ± 2646
             DebtorAccount <DbtrAcct> [0..1]  2646
               Identification <Id> [1..1]  2646
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2647
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2647
Or}                 Other <Othr> [1..1] ± 2647
               Name <Nm> [0..1] Text 2648
             DebtorAgent <DbtrAgt> [0..1]  2648
               Party <Pty> [1..1]  2648
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2649
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2649
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2649
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2650
               LEI <LEI> [0..1] IdentifierSet 2650
             DebtorAgentAccount <DbtrAgtAcct> [0..1]  2651
               Identification <Id> [1..1]  2651
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2651
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2652
Or}                 Other <Othr> [1..1] ± 2652
               Name <Nm> [0..1] Text 2652
             IntermediaryAgent1 <IntrmyAgt1> [0..1]  2652
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2530 May 2026
```

## File page 2531

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Party <Pty> [1..1]  2653
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2653
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2653
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2654
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2655
               LEI <LEI> [0..1] IdentifierSet 2655
             IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2656
               Identification <Id> [1..1]  2656
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2656
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2657
Or}                 Other <Othr> [1..1] ± 2657
               Name <Nm> [0..1] Text 2657
             IntermediaryAgent2 <IntrmyAgt2> [0..1]  2657
               Party <Pty> [1..1]  2658
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2658
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2658
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2659
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2660
               LEI <LEI> [0..1] IdentifierSet 2660
             IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2661
               Identification <Id> [1..1]  2661
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2661
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2662
Or}                 Other <Othr> [1..1] ± 2662
               Name <Nm> [0..1] Text 2662
             CreditorAgent <CdtrAgt> [1..1]  2662
               Party <Pty> [1..1]  2663
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2663
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2663
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2664
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2665
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2531 May 2026
```

## File page 2532

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               LEI <LEI> [0..1] IdentifierSet 2665
             CreditorAgentAccount <CdtrAgtAcct> [0..1]  2666
               Identification <Id> [1..1]  2666
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2666
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2667
Or}                 Other <Othr> [1..1] ± 2667
               Name <Nm> [0..1] Text 2667
             Creditor <Cdtr> [0..1] ± 2667
             CreditorAccount <CdtrAcct> [1..1]  2668
               Identification <Id> [1..1]  2668
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2668
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2669
Or}                 Other <Othr> [1..1] ± 2669
               Name <Nm> [0..1] Text 2669
Or           DirectDebitDetails <DrctDbtDtls> [1..1]  2669
             DebtorAccount <DbtrAcct> [1..1]  2670
               Identification <Id> [1..1]  2671
{Or                 IBAN <IBAN> [1..1] IdentifierSet C20 2671
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2671
Or}                 Other <Othr> [1..1] ± 2672
               Name <Nm> [0..1] Text 2672
             Debtor <Dbtr> [0..1] ± 2672
             DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2672
             DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 2673
             Creditor <Cdtr> [0..1] ± 2673
             DebtorAgent <DbtrAgt> [1..1]  2673
               Party <Pty> [1..1]  2673
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2674
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2674
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2674
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2675
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2532 May 2026
```

## File page 2533

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               LEI <LEI> [0..1] IdentifierSet 2675
             DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2676
             CreditorAgent <CdtrAgt> [0..1]  2676
               Party <Pty> [1..1]  2676
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2677
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2677
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2677
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2678
               LEI <LEI> [0..1] IdentifierSet 2678
             CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2679
             RegistrationIdentification <RegnId> [0..1] Text 2679
             MandateIdentification <MndtId> [0..1] Text 2679
Or           ChequeDetails <ChqDtls> [1..1]  2679
             Number <Nb> [0..1] Text 2680
             PayeeIdentification <PyeeId> [1..1] ± 2680
             DraweeIdentification <DrweeId> [0..1]  2680
               Party <Pty> [1..1]  2681
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2681
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2681
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2682
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 2683
               LEI <LEI> [0..1] IdentifierSet 2683
             DrawerIdentification <DrwrId> [0..1] ± 2684
Or           BankersDraftDetails <BkrsDrftDtls> [1..1]  2684
             Number <Nb> [0..1] Text 2684
             PayeeIdentification <PyeeId> [1..1] ± 2684
             DraweeIdentification <DrweeId> [0..1]  2685
               Party <Pty> [1..1]  2685
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 2685
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 2686
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2686
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2533 May 2026
```

