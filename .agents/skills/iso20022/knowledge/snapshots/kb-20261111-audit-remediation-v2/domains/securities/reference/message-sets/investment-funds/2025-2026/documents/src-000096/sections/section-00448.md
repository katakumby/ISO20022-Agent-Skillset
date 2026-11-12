---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.2 Structure"]
file_pages: [610, 611, 612, 613, 614, 615]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 610 to 615.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 610

```text
28.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <TrfInInstr> [1..1]  C31
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..1] ± 0
   RelatedReference <RltdRef> [0..1] ± 0
   Function <Fctn> [0..1] CodeSet 620
   MasterReference <MstrRef> [0..1] Text 620
   TransferDetails <TrfDtls> [1..*]  C33 0
     TransferReference <TrfRef> [1..1] Text 625
     ClientReference <ClntRef> [0..1] ± 625
     CounterpartyReference <CtrPtyRef> [0..1] ± 626
     BusinessFlowType <BizFlowTp> [0..1] CodeSet 626
     RequestedTransferDate <ReqdTrfDt> [0..1] ± 626
     RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 627
     TransferOrderDateForm <TrfOrdrDtForm> [0..1] Date 627
     TransferReason <TrfRsn> [0..1] ± 627
     HoldingsPlanType <HldgsPlanTp> [0..3] CodeSet 627
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C19 628
       Identification <Id> [1..1]  629
{Or         ISIN <ISIN> [1..1] IdentifierSet 629
Or         SEDOL <SEDOL> [1..1] IdentifierSet 630
Or         CUSIP <CUSIP> [1..1] IdentifierSet 630
Or         RIC <RIC> [1..1] IdentifierSet 630
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 630
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 630
Or         CTA <CTA> [1..1] IdentifierSet 630
Or         QUICK <QUICK> [1..1] IdentifierSet 630
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 631
Or         Dutch <Dtch> [1..1] IdentifierSet 631
Or         Valoren <Vlrn> [1..1] IdentifierSet 631
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 610 May 2026
```

## File page 611

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         Sicovam <SCVM> [1..1] IdentifierSet 631
Or         Belgian <Belgn> [1..1] IdentifierSet 631
Or         Common <Cmon> [1..1] IdentifierSet 631
Or         DTI <DTI> [1..1] IdentifierSet 631
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  631
           Identification <Id> [1..1] Text 632
           IdentificationSource <IdSrc> [1..1] ± 632
       Name <Nm> [0..1] Text 632
       ShortName <ShrtNm> [0..1] Text 632
       SupplementaryIdentification <SplmtryId> [0..1] Text 632
       ClassType <ClssTp> [0..1] Text 632
       SecuritiesForm <SctiesForm> [0..1] CodeSet 633
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 633
       DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 633
     Quantity <Qty> [1..1]  633
{Or       TotalUnitsNumber <TtlUnitsNb> [1..1]  634
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 634
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 634
Or}       TransferRate <TrfRate> [1..1] Rate 634
     UnitsDetails <UnitsDtls> [0..*]  634
       Units <Units> [1..1]  637
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 637
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 637
       OrderDate <OrdrDt> [0..1] Date 637
       AcquisitionDate <AcqstnDt> [0..1] Date 637
       CertificateNumber <CertNb> [0..*] Text 637
       Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 637
       Reference <Ref> [0..1] Text 638
       PriceDetails <PricDtls> [0..1] ± 638
       TransactionOverhead <TxOvrhd> [0..1]  C23,
C34
638
         TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 640
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 611 May 2026
```

## File page 612

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         TotalFees <TtlFees> [0..1] Amount C1, C10 641
         TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 641
         CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 641
         IndividualFee <IndvFee> [0..*]  C6 642
           Type <Tp> [1..1]  642
{Or             Code <Cd> [1..1] CodeSet 643
Or}             Proprietary <Prtry> [1..1] ± 644
           Basis <Bsis> [0..1]  644
{Or             Code <Cd> [1..1] CodeSet 644
Or}             Proprietary <Prtry> [1..1] ± 645
           StandardAmount <StdAmt> [0..1] Amount C1, C10 645
           StandardRate <StdRate> [0..1] Rate 645
           DiscountDetails <DscntDtls> [0..1]  C15 646
             Amount <Amt> [0..1] Amount C1, C10 646
             Rate <Rate> [0..1] Rate 647
             Basis <Bsis> [0..1]  647
{Or               Code <Cd> [1..1] CodeSet 647
Or}               Proprietary <Prtry> [1..1] ± 647
           AppliedAmount <ApldAmt> [0..1] Amount C1, C10 648
           AppliedRate <ApldRate> [0..1] Rate 648
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 648
           RecipientIdentification <RcptId> [0..1] ± 648
           InformativeIndicator <InftvInd> [1..1] Indicator 649
         IndividualTax <IndvTax> [0..*] ± 649
         DigitalNetworkFee <DgtlNtwkFee> [0..2]  649
           FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C24
650
             ISIN <ISIN> [0..1] IdentifierSet 652
             OtherIdentification <OthrId> [0..*]  652
               Identification <Id> [1..1] Text 652
               Suffix <Sfx> [0..1] Text 652
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 612 May 2026
```

## File page 613

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Type <Tp> [1..1]  652
{Or                 Code <Cd> [1..1] CodeSet 653
Or}                 Proprietary <Prtry> [1..1] Text 654
             Description <Desc> [0..1] Text 654
           Quantity <Qty> [1..1]  655
{Or             Quantity <Qty> [1..1] ± C14 655
Or}             ProprietaryQuantity <PrtryQty> [1..1]  655
               Quantity <Qty> [1..1] Quantity 656
               QuantityType <QtyTp> [1..1] Text 656
               Issuer <Issr> [1..1] Text 656
               SchemeName <SchmeNm> [0..1] Text 656
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 656
       OtherAmount <OthrAmt> [0..*]  656
         Type <Tp> [1..1]  657
{Or           Code <Cd> [1..1] CodeSet 657
Or}           ProprietaryCode <PrtryCd> [1..1] ± 657
         Amount <Amt> [1..1] Amount C1, C10 657
     Rounding <Rndg> [0..1] CodeSet 658
     OriginalCost <OrgnlCost> [0..1] Amount C1 658
     AveragePrice <AvrgPric> [0..1] Amount C2 658
     TransferCurrency <TrfCcy> [0..1] CodeSet C2 659
     OwnAccountTransferIndicator <OwnAcctTrfInd> [0..1] Indicator 659
     NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 659
     TransferExpensesPaymentType <TrfExpnssPmtTp> [0..1] ± 659
   AccountDetails <AcctDtls> [1..1]  0
     OwnerIdentification <OwnrId> [0..*] ± 661
     AccountIdentification <AcctId> [1..1] Text 662
     AccountName <AcctNm> [0..1] Text 662
     AccountDesignation <AcctDsgnt> [0..1] Text 662
     AccountServicer <AcctSvcr> [0..1] ± 662
     SubAccountDetails <SubAcctDtls> [0..1] ± 662
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 613 May 2026
```

## File page 614

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 663
     IntermediaryInformation <IntrmyInf> [0..*] ± 663
     SecuritiesForm <SctiesForm> [0..1] CodeSet 663
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 664
     IncomePreference <IncmPref> [0..1] CodeSet 664
     BeneficiaryCertificationCompletion <BnfcryCertfctnCmpltn> [0..1] CodeSet 664
     SafekeepingPlace <SfkpgPlc> [0..1] ± 664
     SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  665
       TradeTransactionCondition <TradTxCond> [0..*] ± 665
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 666
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 666
       ReceivingSideDetails <RcvgSdDtls> [0..1]  C7, C11,
C25,
C26,
C27,
C28,
C32
666
         Depository <Dpstry> [0..1] ± 668
         Party1 <Pty1> [0..1] ± 669
         Party2 <Pty2> [0..1] ± 669
         Party3 <Pty3> [0..1] ± 669
         Party4 <Pty4> [0..1] ± 670
         Party5 <Pty5> [0..1] ± 670
   SettlementDetails <SttlmDtls> [0..1]  C29,
C30
0
     Transferor <Trfr> [0..1] ± 673
     TransferorRegisteredAccount <TrfrRegdAcct> [0..1]  673
       Identification <Id> [0..1] Text 674
       AccountName <AcctNm> [0..1] Text 674
       Designation <Dsgnt> [0..1] Text 674
       Servicer <Svcr> [0..1] ± 674
       SubAccountDetails <SubAcctDtls> [0..1] ± 674
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 675
     IntermediaryInformation <IntrmyInf> [0..*] ± 675
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 614 May 2026
```

## File page 615

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     SecuritiesForm <SctiesForm> [0..1] CodeSet 675
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 676
     IncomePreference <IncmPref> [0..1] CodeSet 676
     BeneficiaryCertificationCompletion <BnfcryCertfctnCmpltn> [0..1] CodeSet 676
     RequestedTradeDate <ReqdTradDt> [0..1] Date 676
     RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 677
     SettlementAmount <SttlmAmt> [0..1] Amount C1, C10 677
     StampDuty <StmpDty> [0..1] CodeSet 677
     NetAmount <NetAmt> [0..1] Amount C1, C10 677
     Fees <Fees> [0..*] ± C18 678
     IndividualTax <IndvTax> [0..*] ± 679
     ForeignExchangeDetails <FXDtls> [0..*] ± 679
     SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  680
       TradeTransactionCondition <TradTxCond> [0..*] ± 681
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 681
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 682
       DeliveringSideDetails <DlvrgSdDtls> [0..1]  C7, C11,
C25,
C26,
C27,
C28,
C32
682
         Depository <Dpstry> [0..1] ± 683
         Party1 <Pty1> [0..1] ± 684
         Party2 <Pty2> [0..1] ± 684
         Party3 <Pty3> [0..1] ± 685
         Party4 <Pty4> [0..1] ± 685
         Party5 <Pty5> [0..1] ± 686
     PhysicalTransfer <PhysTrf> [0..1] CodeSet 686
     PhysicalTransferDetails <PhysTrfDtls> [0..1] ± C22 686
     ClientReference <ClntRef> [0..1] ± 687
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 687
   CopyDetails <CpyDtls> [0..1] ± 0
   Extension <Xtnsn> [0..*] ± C17 0
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 615 May 2026
```

