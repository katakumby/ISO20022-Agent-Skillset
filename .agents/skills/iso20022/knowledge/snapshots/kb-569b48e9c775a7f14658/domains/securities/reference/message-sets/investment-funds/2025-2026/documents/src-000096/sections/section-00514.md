---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.2 Structure"]
file_pages: [697, 698, 699, 700, 701, 702]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 697 to 702.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 697

```text
30.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <TrfInConf> [1..1]  C17,
C32
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 706
   PreviousReference <PrvsRef> [0..1] ± 707
   RelatedReference <RltdRef> [0..1] ± 707
   Function <Fctn> [0..1] CodeSet 0
   MasterReference <MstrRef> [0..1] Text 0
   TransferDetails <TrfDtls> [1..*]  C34 0
     TransferConfirmationReference <TrfConfRef> [1..1] Text 712
     TransferReference <TrfRef> [1..1] Text 712
     ClientReference <ClntRef> [0..1] ± 713
     CounterpartyReference <CtrPtyRef> [0..1] ± 713
     BusinessFlowType <BizFlowTp> [0..1] CodeSet 713
     RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 714
     EffectiveTransferDate <FctvTrfDt> [1..1] ± 714
     EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 714
     TradeDate <TradDt> [0..1] ± 714
     TransferOrderDateForm <TrfOrdrDtForm> [0..1] Date 714
     TransferReason <TrfRsn> [0..1] ± 715
     HoldingsPlanType <HldgsPlanTp> [0..3] CodeSet 715
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C20 715
       Identification <Id> [1..1]  717
{Or         ISIN <ISIN> [1..1] IdentifierSet 717
Or         SEDOL <SEDOL> [1..1] IdentifierSet 717
Or         CUSIP <CUSIP> [1..1] IdentifierSet 718
Or         RIC <RIC> [1..1] IdentifierSet 718
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 718
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 718
Or         CTA <CTA> [1..1] IdentifierSet 718
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 697 May 2026
```

## File page 698

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         QUICK <QUICK> [1..1] IdentifierSet 718
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 718
Or         Dutch <Dtch> [1..1] IdentifierSet 719
Or         Valoren <Vlrn> [1..1] IdentifierSet 719
Or         Sicovam <SCVM> [1..1] IdentifierSet 719
Or         Belgian <Belgn> [1..1] IdentifierSet 719
Or         Common <Cmon> [1..1] IdentifierSet 719
Or         DTI <DTI> [1..1] IdentifierSet 719
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  719
           Identification <Id> [1..1] Text 720
           IdentificationSource <IdSrc> [1..1] ± 720
       Name <Nm> [0..1] Text 720
       ShortName <ShrtNm> [0..1] Text 720
       SupplementaryIdentification <SplmtryId> [0..1] Text 720
       ClassType <ClssTp> [0..1] Text 720
       SecuritiesForm <SctiesForm> [0..1] CodeSet 721
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 721
       DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 721
     TotalUnitsNumber <TtlUnitsNb> [1..1]  721
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 722
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 722
     TransferRate <TrfRate> [0..1] Rate 722
     UnitsDetails <UnitsDtls> [0..*]  722
       Units <Units> [1..1]  725
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 725
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 725
       OrderDate <OrdrDt> [0..1] Date 725
       AcquisitionDate <AcqstnDt> [0..1] Date 725
       CertificateNumber <CertNb> [0..*] Text 725
       Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 725
       Reference <Ref> [0..1] Text 726
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 698 May 2026
```

## File page 699

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       PriceDetails <PricDtls> [0..1] ± 726
       TransactionOverhead <TxOvrhd> [0..1]  C24,
C35
726
         TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 728
         TotalFees <TtlFees> [0..1] Amount C1, C10 729
         TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 729
         CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 729
         IndividualFee <IndvFee> [0..*]  C6 730
           Type <Tp> [1..1]  730
{Or             Code <Cd> [1..1] CodeSet 731
Or}             Proprietary <Prtry> [1..1] ± 732
           Basis <Bsis> [0..1]  732
{Or             Code <Cd> [1..1] CodeSet 732
Or}             Proprietary <Prtry> [1..1] ± 733
           StandardAmount <StdAmt> [0..1] Amount C1, C10 733
           StandardRate <StdRate> [0..1] Rate 733
           DiscountDetails <DscntDtls> [0..1]  C15 734
             Amount <Amt> [0..1] Amount C1, C10 734
             Rate <Rate> [0..1] Rate 735
             Basis <Bsis> [0..1]  735
{Or               Code <Cd> [1..1] CodeSet 735
Or}               Proprietary <Prtry> [1..1] ± 735
           AppliedAmount <ApldAmt> [0..1] Amount C1, C10 736
           AppliedRate <ApldRate> [0..1] Rate 736
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 736
           RecipientIdentification <RcptId> [0..1] ± 736
           InformativeIndicator <InftvInd> [1..1] Indicator 737
         IndividualTax <IndvTax> [0..*] ± 737
         DigitalNetworkFee <DgtlNtwkFee> [0..2]  737
           FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C21,
C22,
C25
738
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 699 May 2026
```

## File page 700

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             ISIN <ISIN> [0..1] IdentifierSet 740
             OtherIdentification <OthrId> [0..*]  740
               Identification <Id> [1..1] Text 740
               Suffix <Sfx> [0..1] Text 740
               Type <Tp> [1..1]  740
{Or                 Code <Cd> [1..1] CodeSet 741
Or}                 Proprietary <Prtry> [1..1] Text 742
             Description <Desc> [0..1] Text 742
           Quantity <Qty> [1..1]  743
{Or             Quantity <Qty> [1..1] ± C14 743
Or}             ProprietaryQuantity <PrtryQty> [1..1]  743
               Quantity <Qty> [1..1] Quantity 744
               QuantityType <QtyTp> [1..1] Text 744
               Issuer <Issr> [1..1] Text 744
               SchemeName <SchmeNm> [0..1] Text 744
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 744
       OtherAmount <OthrAmt> [0..*]  744
         Type <Tp> [1..1]  745
{Or           Code <Cd> [1..1] CodeSet 745
Or}           ProprietaryCode <PrtryCd> [1..1] ± 745
         Amount <Amt> [1..1] Amount C1, C10 745
     Rounding <Rndg> [0..1] CodeSet 746
     OriginalCost <OrgnlCost> [0..1] Amount C1 746
     AveragePrice <AvrgPric> [0..1] Amount C2 746
     NewAveragePrice <NewAvrgPric> [0..1] Amount C2 747
     AverageDate <AvrgDt> [0..1] Date 747
     NewAverageDate <NewAvrgDt> [0..1] Date 747
     TransferCurrency <TrfCcy> [0..1] CodeSet C2 747
     OwnAccountTransferIndicator <OwnAcctTrfInd> [0..1] Indicator 748
     NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 748
     TransferExpensesPaymentType <TrfExpnssPmtTp> [0..1] ± 748
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 700 May 2026
```

## File page 701

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
   AccountDetails <AcctDtls> [1..1]  748
     OwnerIdentification <OwnrId> [0..*] ± 749
     AccountIdentification <AcctId> [1..1] Text 750
     AccountName <AcctNm> [0..1] Text 750
     AccountDesignation <AcctDsgnt> [0..1] Text 750
     AccountServicer <AcctSvcr> [0..1] ± 750
     SubAccountDetails <SubAcctDtls> [0..1] ± 750
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 751
     IntermediaryInformation <IntrmyInf> [0..*] ± 751
     SecuritiesForm <SctiesForm> [0..1] CodeSet 751
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 752
     IncomePreference <IncmPref> [0..1] CodeSet 752
     BeneficiaryCertificationCompletion <BnfcryCertfctnCmpltn> [0..1] CodeSet 752
     SafekeepingPlace <SfkpgPlc> [0..1] ± 752
     SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  753
       TradeTransactionCondition <TradTxCond> [0..*] ± 753
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 754
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 754
       ReceivingSideDetails <RcvgSdDtls> [0..1]  C7, C11,
C26,
C27,
C28,
C29,
C33
754
         Depository <Dpstry> [0..1] ± 756
         Party1 <Pty1> [0..1] ± 757
         Party2 <Pty2> [0..1] ± 757
         Party3 <Pty3> [0..1] ± 757
         Party4 <Pty4> [0..1] ± 758
         Party5 <Pty5> [0..1] ± 758
   SettlementDetails <SttlmDtls> [0..1]  C30,
C31
0
     Transferor <Trfr> [0..1] ± 761
     TransferorRegisteredAccount <TrfrRegdAcct> [0..1]  761
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 701 May 2026
```

## File page 702

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       Identification <Id> [0..1] Text 762
       AccountName <AcctNm> [0..1] Text 762
       Designation <Dsgnt> [0..1] Text 762
       Servicer <Svcr> [0..1] ± 762
       SubAccountDetails <SubAcctDtls> [0..1] ± 762
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 763
     IntermediaryInformation <IntrmyInf> [0..*] ± 763
     SecuritiesForm <SctiesForm> [0..1] CodeSet 763
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 764
     IncomePreference <IncmPref> [0..1] CodeSet 764
     BeneficiaryCertificationCompletion <BnfcryCertfctnCmpltn> [0..1] CodeSet 764
     RequestedTradeDate <ReqdTradDt> [0..1] Date 764
     RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 765
     EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 765
     SettlementAmount <SttlmAmt> [0..1] Amount C1, C10 765
     StampDuty <StmpDty> [0..1] CodeSet 765
     NetAmount <NetAmt> [0..1] Amount C1, C10 766
     Fees <Fees> [0..*] ± C19 766
     IndividualTax <IndvTax> [0..*] ± 767
     ForeignExchangeDetails <FXDtls> [0..*] ± 768
     SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  769
       TradeTransactionCondition <TradTxCond> [0..*] ± 770
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 770
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 770
       DeliveringSideDetails <DlvrgSdDtls> [0..1]  C7, C11,
C26,
C27,
C28,
C29,
C33
770
         Depository <Dpstry> [0..1] ± 772
         Party1 <Pty1> [0..1] ± 773
         Party2 <Pty2> [0..1] ± 773
         Party3 <Pty3> [0..1] ± 773
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 702 May 2026
```

