---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.2 Structure"]
file_pages: [521, 522, 523, 524, 525, 526]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 521 to 526.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 521

```text
26.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <TrfOutConf> [1..1]  C17,
C32
   MessageIdentification <MsgId> [1..1] ± 530
   PoolReference <PoolRef> [0..1] ± 530
   PreviousReference <PrvsRef> [0..1] ± 0
   RelatedReference <RltdRef> [0..1] ± 0
   MasterReference <MstrRef> [0..1] Text 531
   TransferDetails <TrfDtls> [1..*]  C34 531
     TransferConfirmationReference <TrfConfRef> [1..1] Text 536
     TransferReference <TrfRef> [1..1] Text 536
     ClientReference <ClntRef> [0..1] ± 537
     CounterpartyReference <CtrPtyRef> [0..1] ± 537
     BusinessFlowType <BizFlowTp> [0..1] CodeSet 537
     RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 538
     EffectiveTransferDate <FctvTrfDt> [1..1] ± 538
     EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 538
     TradeDate <TradDt> [0..1] ± 538
     TransferOrderDateForm <TrfOrdrDtForm> [0..1] Date 538
     TransferReason <TrfRsn> [0..1] ± 539
     HoldingsPlanType <HldgsPlanTp> [0..3] CodeSet 539
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C20 539
       Identification <Id> [1..1]  541
{Or         ISIN <ISIN> [1..1] IdentifierSet 541
Or         SEDOL <SEDOL> [1..1] IdentifierSet 541
Or         CUSIP <CUSIP> [1..1] IdentifierSet 542
Or         RIC <RIC> [1..1] IdentifierSet 542
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 542
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 542
Or         CTA <CTA> [1..1] IdentifierSet 542
Or         QUICK <QUICK> [1..1] IdentifierSet 542
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 521 May 2026
```

## File page 522

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 542
Or         Dutch <Dtch> [1..1] IdentifierSet 543
Or         Valoren <Vlrn> [1..1] IdentifierSet 543
Or         Sicovam <SCVM> [1..1] IdentifierSet 543
Or         Belgian <Belgn> [1..1] IdentifierSet 543
Or         Common <Cmon> [1..1] IdentifierSet 543
Or         DTI <DTI> [1..1] IdentifierSet 543
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  543
           Identification <Id> [1..1] Text 544
           IdentificationSource <IdSrc> [1..1] ± 544
       Name <Nm> [0..1] Text 544
       ShortName <ShrtNm> [0..1] Text 544
       SupplementaryIdentification <SplmtryId> [0..1] Text 544
       ClassType <ClssTp> [0..1] Text 544
       SecuritiesForm <SctiesForm> [0..1] CodeSet 545
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 545
       DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 545
     TotalUnitsNumber <TtlUnitsNb> [1..1]  545
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 546
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 546
     TransferRate <TrfRate> [0..1] Rate 546
     UnitsDetails <UnitsDtls> [0..*]  546
       Units <Units> [1..1]  549
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 549
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 549
       OrderDate <OrdrDt> [0..1] Date 549
       AcquisitionDate <AcqstnDt> [0..1] Date 549
       CertificateNumber <CertNb> [0..*] Text 549
       Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 549
       Reference <Ref> [0..1] Text 550
       PriceDetails <PricDtls> [0..1] ± 550
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 522 May 2026
```

## File page 523

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       TransactionOverhead <TxOvrhd> [0..1]  C24,
C35
550
         TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 552
         TotalFees <TtlFees> [0..1] Amount C1, C10 553
         TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 553
         CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 553
         IndividualFee <IndvFee> [0..*]  C6 554
           Type <Tp> [1..1]  554
{Or             Code <Cd> [1..1] CodeSet 555
Or}             Proprietary <Prtry> [1..1] ± 556
           Basis <Bsis> [0..1]  556
{Or             Code <Cd> [1..1] CodeSet 556
Or}             Proprietary <Prtry> [1..1] ± 557
           StandardAmount <StdAmt> [0..1] Amount C1, C10 557
           StandardRate <StdRate> [0..1] Rate 557
           DiscountDetails <DscntDtls> [0..1]  C15 558
             Amount <Amt> [0..1] Amount C1, C10 558
             Rate <Rate> [0..1] Rate 559
             Basis <Bsis> [0..1]  559
{Or               Code <Cd> [1..1] CodeSet 559
Or}               Proprietary <Prtry> [1..1] ± 559
           AppliedAmount <ApldAmt> [0..1] Amount C1, C10 560
           AppliedRate <ApldRate> [0..1] Rate 560
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 560
           RecipientIdentification <RcptId> [0..1] ± 560
           InformativeIndicator <InftvInd> [1..1] Indicator 561
         IndividualTax <IndvTax> [0..*] ± 561
         DigitalNetworkFee <DgtlNtwkFee> [0..2]  561
           FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C21,
C22,
C25
562
             ISIN <ISIN> [0..1] IdentifierSet 564
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 523 May 2026
```

## File page 524

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             OtherIdentification <OthrId> [0..*]  564
               Identification <Id> [1..1] Text 564
               Suffix <Sfx> [0..1] Text 564
               Type <Tp> [1..1]  564
{Or                 Code <Cd> [1..1] CodeSet 565
Or}                 Proprietary <Prtry> [1..1] Text 566
             Description <Desc> [0..1] Text 566
           Quantity <Qty> [1..1]  567
{Or             Quantity <Qty> [1..1] ± C14 567
Or}             ProprietaryQuantity <PrtryQty> [1..1]  567
               Quantity <Qty> [1..1] Quantity 568
               QuantityType <QtyTp> [1..1] Text 568
               Issuer <Issr> [1..1] Text 568
               SchemeName <SchmeNm> [0..1] Text 568
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 568
       OtherAmount <OthrAmt> [0..*]  568
         Type <Tp> [1..1]  569
{Or           Code <Cd> [1..1] CodeSet 569
Or}           ProprietaryCode <PrtryCd> [1..1] ± 569
         Amount <Amt> [1..1] Amount C1, C10 569
     Rounding <Rndg> [0..1] CodeSet 570
     OriginalCost <OrgnlCost> [0..1] Amount C1 570
     AveragePrice <AvrgPric> [0..1] Amount C2 570
     NewAveragePrice <NewAvrgPric> [0..1] Amount C2 571
     AverageDate <AvrgDt> [0..1] Date 571
     NewAverageDate <NewAvrgDt> [0..1] Date 571
     TransferCurrency <TrfCcy> [0..1] CodeSet C2 571
     OwnAccountTransferIndicator <OwnAcctTrfInd> [0..1] Indicator 572
     NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 572
     TransferExpensesPaymentType <TrfExpnssPmtTp> [0..1] ± 572
   AccountDetails <AcctDtls> [1..1]  0
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 524 May 2026
```

## File page 525

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     OwnerIdentification <OwnrId> [0..*] ± 573
     AccountIdentification <AcctId> [1..1] Text 574
     AccountName <AcctNm> [0..1] Text 574
     AccountDesignation <AcctDsgnt> [0..1] Text 574
     AccountServicer <AcctSvcr> [0..1] ± 574
     SubAccountDetails <SubAcctDtls> [0..1] ± 574
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 575
     IntermediaryInformation <IntrmyInf> [0..*] ± 575
     SecuritiesForm <SctiesForm> [0..1] CodeSet 575
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 576
     IncomePreference <IncmPref> [0..1] CodeSet 576
     BeneficiaryCertificationCompletion <BnfcryCertfctnCmpltn> [0..1] CodeSet 576
     SafekeepingPlace <SfkpgPlc> [0..1] ± 576
     SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  577
       TradeTransactionCondition <TradTxCond> [0..*] ± 577
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 578
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 578
       DeliveringSideDetails <DlvrgSdDtls> [0..1]  C7, C11,
C26,
C27,
C28,
C29,
C33
578
         Depository <Dpstry> [0..1] ± 580
         Party1 <Pty1> [0..1] ± 581
         Party2 <Pty2> [0..1] ± 581
         Party3 <Pty3> [0..1] ± 581
         Party4 <Pty4> [0..1] ± 582
         Party5 <Pty5> [0..1] ± 582
   SettlementDetails <SttlmDtls> [0..1]  C30,
C31
0
     Transferee <Trfee> [0..1] ± 585
     TransfereeRegisteredAccount <TrfeeRegdAcct> [0..1]  585
       Identification <Id> [0..1] Text 586
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 525 May 2026
```

## File page 526

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       AccountName <AcctNm> [0..1] Text 586
       Designation <Dsgnt> [0..1] Text 586
       Servicer <Svcr> [0..1] ± 586
       SubAccountDetails <SubAcctDtls> [0..1] ± 586
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 587
     IntermediaryInformation <IntrmyInf> [0..*] ± 587
     SecuritiesForm <SctiesForm> [0..1] CodeSet 587
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 588
     IncomePreference <IncmPref> [0..1] CodeSet 588
     BeneficiaryCertificationCompletion <BnfcryCertfctnCmpltn> [0..1] CodeSet 588
     RequestedTradeDate <ReqdTradDt> [0..1] Date 588
     RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 589
     EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 589
     SettlementAmount <SttlmAmt> [0..1] Amount C1, C10 589
     StampDuty <StmpDty> [0..1] CodeSet 589
     NetAmount <NetAmt> [0..1] Amount C1, C10 590
     Fees <Fees> [0..*] ± C19 590
     IndividualTax <IndvTax> [0..*] ± 591
     ForeignExchangeDetails <FXDtls> [0..*] ± 592
     SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  593
       TradeTransactionCondition <TradTxCond> [0..*] ± 594
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 594
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 594
       ReceivingSideDetails <RcvgSdDtls> [0..1]  C7, C11,
C26,
C27,
C28,
C29,
C33
594
         Depository <Dpstry> [0..1] ± 596
         Party1 <Pty1> [0..1] ± 597
         Party2 <Pty2> [0..1] ± 597
         Party3 <Pty3> [0..1] ± 597
         Party4 <Pty4> [0..1] ± 598
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 526 May 2026
```

