---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.2 Structure"]
file_pages: [31, 32, 33, 34, 35, 36, 37, 38]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.2 Structure

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 31 to 38.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 31

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTradConf> [1..1]  
   Identification <Id> [1..1]  45
     TransactionIdentification <TxId> [1..1] Text 45
   NumberCount <NbCnt> [0..1] ± C16 46
   References <Refs> [0..*] ± 46
   TradeDetails <TradDtls> [1..1]  C15,
C41,
C50
46
     BusinessProcessType <BizPrcTp> [0..1] ± 49
     OrderIdentification <OrdrId> [0..*] Text 49
     ClientOrderIdentification <ClntOrdrId> [0..*] Text 49
     SecondaryClientOrderIdentification <ScndryClntOrdrId> [0..*] Text 50
     ListIdentification <ListId> [0..*] Text 50
     Side <Sd> [1..1] CodeSet 50
     Payment <Pmt> [0..1] CodeSet 51
     TradeTransactionType <TradTxTp> [0..1] ± 52
     TradeTransactionCondition <TradTxCond> [0..*] ± 52
     PreAdvice <PreAdvc> [0..1] Indicator 52
     PlaceOfTrade <PlcOfTrad> [0..1] ± C23,
C31,
C42
52
     OrderBookingDate <OrdrBookgDt> [0..1] Date 53
     TradeOriginationDate <TradOrgtnDt> [0..1] DateTime 53
     TradeDate <TradDt> [1..1] ± 53
     ProcessingDate <PrcgDt> [0..1] ± 54
     SettlementDate <SttlmDt> [1..1] ± 54
     NAVDate <NAVDt> [0..1] ± 54
     PartialFillDetails <PrtlFillDtls> [0..*] ± C35 55
     ConfirmationQuantity <ConfQty> [1..1] ± 55
     QuantityBreakdown <QtyBrkdwn> [0..*] ± 56
     GrossTradeAmount <GrssTradAmt> [0..1] ± 56
     DealPrice <DealPric> [1..1] ± 56
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 31 February 2025
```

## File page 32

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     TypeOfPrice <TpOfPric> [0..1] ± 57
     CashMargin <CshMrgn> [0..1] CodeSet 57
     Commission <Comssn> [0..1] ± 57
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C33 58
     GiveUpNumberOfDays <GvUpNbOfDays> [0..1] Quantity C33 58
     InterestType <IntrstTp> [0..1] CodeSet 58
     AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 59
     AccruedInterestPercentage <AcrdIntrstPctg> [0..1] Rate 59
     TradeRegulatoryConditionsType <TradRgltryCondsTp> [0..1] CodeSet 59
     CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 59
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 60
     PositionEffect <PosFct> [0..1] CodeSet 60
     DerivativeCovered <DerivCvrd> [0..1] Indicator 60
     ChargeTaxBasisType <ChrgTaxBsisTp> [0..1] ± 61
     CapitalGainType <CptlGnTp> [0..1] ± 61
     MatchStatus <MtchSts> [0..1] ± 61
     CallInType <CallInTp> [0..1] CodeSet 61
     YieldType <YldTp> [0..1] ± 62
     Reporting <Rptg> [0..*] ± 62
     AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1] ± 62
     AdditionalTradeInstructionProcessingInformation
<AddtlTradInstrPrcgInf>
[0..1] Text 63
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C19,
C20,
C27,
C28,
C34
63
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1]  C3, C40 64
     PlaceOfListing <PlcOfListg> [0..1] ± 67
     Rating <Ratg> [0..1] ± 67
     CertificateNumber <CertNb> [0..1] Text 67
     DayCountBasis <DayCntBsis> [0..1] ± 67
     RegistrationForm <RegnForm> [0..1] ± 67
     PaymentFrequency <PmtFrqcy> [0..1] ± 68
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 32 February 2025
```

## File page 33

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     VariableRateChangeFrequency <VarblRateChngFrqcy> [0..1] ± 68
     ClassificationType <ClssfctnTp> [0..1] ± 68
     OptionStyle <OptnStyle> [0..1] ± 68
     OptionType <OptnTp> [0..1] ± 69
     DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 69
     CouponDate <CpnDt> [0..1] Date 69
     ExpiryDate <XpryDt> [0..1] Date 69
     FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 70
     MaturityDate <MtrtyDt> [0..1] Date 70
     IssueDate <IsseDt> [0..1] Date 70
     NextCallableDate <NxtCllblDt> [0..1] Date 70
     ConversionDate <ConvsDt> [0..1] Date 70
     PutableDate <PutblDt> [0..1] Date 70
     DatedDate <DtdDt> [0..1] Date 70
     FirstPaymentDate <FrstPmtDt> [0..1] Date 70
     NextFactorDate <NxtFctrDt> [0..1] Date 71
     PreviousFactor <PrvsFctr> [0..1] Rate 71
     CurrentFactor <CurFctr> [0..1] Rate 71
     NextFactor <NxtFctr> [0..1] Rate 71
     EndFactor <EndFctr> [0..1] Rate 71
     InterestRate <IntrstRate> [0..1] Rate 71
     NextInterestRate <NxtIntrstRate> [0..1] Rate 71
     IndexRateBasis <IndxRateBsis> [0..1] Rate 72
     PercentageOfDebtClaims <PctgOfDebtClms> [0..1] Rate 72
     CouponAttachedNumber <CpnAttchdNb> [0..1] ± 72
     PoolNumber <PoolNb> [0..1] ± 72
     VersionNumber <VrsnNb> [0..1] ± 72
     ConvertibleIndicator <ConvtblInd> [0..1] Indicator 73
     VariableRateIndicator <VarblRateInd> [0..1] Indicator 73
     CoveredIndicator <CvrdInd> [0..1] Indicator 73
     CallableIndicator <CllblInd> [0..1] Indicator 73
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 33 February 2025
```

## File page 34

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     PutableIndicator <PutblInd> [0..1] Indicator 73
     WarrantAttachedOnDelivery <WarrtAttchdOnDlvry> [0..1] Indicator 74
     OddCouponIndicator <OddCpnInd> [0..1] Indicator 74
     RedemptionYieldImpact <RedYldImpct> [0..1] Indicator 74
     YieldVariance <YldVar> [0..1] Indicator 74
     ExercisePrice <ExrcPric> [0..1] ± 75
     SubscriptionPrice <SbcptPric> [0..1] ± 75
     ConversionPrice <ConvsPric> [0..1] ± 75
     TaxableIncomePerShare <TaxblIncmPerShr> [0..1] ± 75
     MinimumNominalQuantity <MinNmnlQty> [0..1] ± 76
     MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 76
     MinimumExercisableMultipleQuantity <MinExrcblMltplQty> [0..1] ± 76
     FaceAmount <FaceAmt> [0..1] Amount 77
     ContractSize <CtrctSz> [0..1] ± 77
     FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 77
   UnderlyingFinancialInstrument <UndrlygFinInstrm> [0..*]  77
     Identification <Id> [1..1] ± C19,
C20,
C27,
C28,
C34
79
     Attributes <Attrbts> [0..1]  C3, C40 80
       PlaceOfListing <PlcOfListg> [0..1] ± 83
       Rating <Ratg> [0..1] ± 84
       CertificateNumber <CertNb> [0..1] Text 84
       DayCountBasis <DayCntBsis> [0..1] ± 84
       RegistrationForm <RegnForm> [0..1] ± 84
       PaymentFrequency <PmtFrqcy> [0..1] ± 85
       VariableRateChangeFrequency <VarblRateChngFrqcy> [0..1] ± 85
       ClassificationType <ClssfctnTp> [0..1] ± 85
       OptionStyle <OptnStyle> [0..1] ± 85
       OptionType <OptnTp> [0..1] ± 86
       DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 86
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 34 February 2025
```

## File page 35

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       CouponDate <CpnDt> [0..1] Date 86
       ExpiryDate <XpryDt> [0..1] Date 86
       FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 87
       MaturityDate <MtrtyDt> [0..1] Date 87
       IssueDate <IsseDt> [0..1] Date 87
       NextCallableDate <NxtCllblDt> [0..1] Date 87
       ConversionDate <ConvsDt> [0..1] Date 87
       PutableDate <PutblDt> [0..1] Date 87
       DatedDate <DtdDt> [0..1] Date 87
       FirstPaymentDate <FrstPmtDt> [0..1] Date 87
       NextFactorDate <NxtFctrDt> [0..1] Date 88
       PreviousFactor <PrvsFctr> [0..1] Rate 88
       CurrentFactor <CurFctr> [0..1] Rate 88
       NextFactor <NxtFctr> [0..1] Rate 88
       EndFactor <EndFctr> [0..1] Rate 88
       InterestRate <IntrstRate> [0..1] Rate 88
       NextInterestRate <NxtIntrstRate> [0..1] Rate 88
       IndexRateBasis <IndxRateBsis> [0..1] Rate 88
       PercentageOfDebtClaims <PctgOfDebtClms> [0..1] Rate 89
       CouponAttachedNumber <CpnAttchdNb> [0..1] ± 89
       PoolNumber <PoolNb> [0..1] ± 89
       VersionNumber <VrsnNb> [0..1] ± 89
       ConvertibleIndicator <ConvtblInd> [0..1] Indicator 90
       VariableRateIndicator <VarblRateInd> [0..1] Indicator 90
       CoveredIndicator <CvrdInd> [0..1] Indicator 90
       CallableIndicator <CllblInd> [0..1] Indicator 90
       PutableIndicator <PutblInd> [0..1] Indicator 90
       WarrantAttachedOnDelivery <WarrtAttchdOnDlvry> [0..1] Indicator 90
       OddCouponIndicator <OddCpnInd> [0..1] Indicator 91
       RedemptionYieldImpact <RedYldImpct> [0..1] Indicator 91
       YieldVariance <YldVar> [0..1] Indicator 91
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 35 February 2025
```

## File page 36

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       ExercisePrice <ExrcPric> [0..1] ± 91
       SubscriptionPrice <SbcptPric> [0..1] ± 92
       ConversionPrice <ConvsPric> [0..1] ± 92
       TaxableIncomePerShare <TaxblIncmPerShr> [0..1] ± 92
       MinimumNominalQuantity <MinNmnlQty> [0..1] ± 92
       MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 93
       MinimumExercisableMultipleQuantity <MinExrcblMltplQty> [0..1] ± 93
       FaceAmount <FaceAmt> [0..1] Amount 93
       ContractSize <CtrctSz> [0..1] ± 93
       FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 94
   Stipulations <Stiptns> [0..1]  94
     Geographics <Geogcs> [0..1] Text 96
     YieldRange <YldRg> [0..1] ± 96
     Rating <Ratg> [0..1] ± 96
     CouponRange <CpnRg> [0..1] ± 97
     AmortisableIndicator <AmtsblInd> [0..1] Indicator 97
     Purpose <Purp> [0..1] Text 97
     AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 97
     AutoReinvestment <AutoRinvstmt> [0..1] Rate 98
     TransactionConditions <TxConds> [0..1] CodeSet 98
     Currency <Ccy> [0..1] CodeSet C1 99
     CustomDate <CstmDt> [0..1] ± 99
     Haircut <Hrcut> [0..1] Rate 99
     InsuredIndicator <InsrdInd> [0..1] Indicator 99
     LookBack <LookBck> [0..1] Quantity 100
     MaturityDate <MtrtyDt> [0..1] YearMonth 100
     IssueDate <IsseDt> [0..1] YearMonth 100
     IssuerIdentification <IssrId> [0..1] IdentifierSet C9 100
     IssueSize <IsseSz> [0..1] Quantity 100
     MinimumDenomination <MinDnmtn> [0..1] ± 100
     MaximumSubstitution <MaxSbstitn> [0..1] Quantity 101
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 36 February 2025
```

## File page 37

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     MinimumIncrement <MinIncrmt> [0..1] ± 101
     PaymentFrequency <PmtFrqcy> [0..1] CodeSet 101
     MinimumQuantity <MinQty> [0..1] ± 102
     Production <Pdctn> [0..1] Text 102
     RestrictedIndicator <RstrctdInd> [0..1] Indicator 102
     PriceFrequency <PricFrqcy> [0..1] CodeSet 102
     Sector <Sctr> [0..1] Text 103
     SubstitutionFrequency <SbstitnFrqcy> [0..1] CodeSet 103
     SubstitutionLeft <SbstitnLft> [0..1] Quantity 103
     WholePoolIndicator <WhlPoolInd> [0..1] Indicator 104
     PriceSource <PricSrc> [0..1] Text 104
     ExpirationDate <XprtnDt> [0..1] DateTime 104
     OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C13 104
     OverAllotmentRate <OverAlltmtRate> [0..1] Rate 104
     PriceRange <PricRg> [0..1] ± 105
     CallableIndicator <CllblInd> [0..1] Indicator 105
     ConvertibleIndicator <ConvtblInd> [0..1] Indicator 105
     PutableIndicator <PutblInd> [0..1] Indicator 105
     PreFundedIndicator <PreFnddInd> [0..1] Indicator 106
     EscrowedIndicator <EscrwdInd> [0..1] Indicator 106
     PerpetualIndicator <PerptlInd> [0..1] Indicator 106
   ConfirmationParties <ConfPties> [1..*]  106
     Buyer <Buyr> [0..1] ± 107
     Borrower <Brrwr> [0..1] ± 107
     Seller <Sellr> [0..1] ± 108
     Lender <Lndr> [0..1] ± 108
     BrokerOfCredit <BrkrOfCdt> [0..1] ± 109
     IntroducingFirm <IntrdcgFirm> [0..1] ± 109
     StepInFirm <StepInFirm> [0..1] ± 109
     StepOutFirm <StepOutFirm> [0..1] ± 110
     ClearingFirm <ClrFirm> [0..1] ± 110
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 37 February 2025
```

## File page 38

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     ExecutingBroker <ExctgBrkr> [0..1] ± 110
     CMUParty <CMUPty> [0..1] ± 111
     CMUCounterparty <CMUCtrPty> [0..1] ± 111
     AffirmingParty <AffrmgPty> [0..1] ± 112
     TradeBeneficiaryParty <TradBnfcryPty> [0..1] ± 112
   SettlementParameters <SttlmParams> [0..1] ± C11,
C21,
C45,
C46
112
   StandingSettlementInstruction <StgSttlmInstr> [0..1] ± C51 115
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C36,
C37,
C38,
C39,
C18
115
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C36,
C37,
C38,
C39,
C18
117
   CashParties <CshPties> [0..1] ± 119
   ClearingDetails <ClrDtls> [0..1]  121
     ClearingMember <ClrMmb> [1..*] ± 121
     ClearingSegment <ClrSgmt> [0..1] ± 122
   SettlementAmount <SttlmAmt> [0..1]  122
     AccruedInterestIndicator <AcrdIntrstInd> [0..1] Indicator 122
     StampDutyIndicator <StmpDtyInd> [0..1] Indicator 122
     Amount <Amt> [1..1] Amount C1, C13 123
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 123
     OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C14 123
     ForeignExchangeDetails <FXDtls> [0..1] ± 124
     ValueDate <ValDt> [0..1] ± 124
   OtherAmounts <OthrAmts> [0..*] ± 124
   OtherPrices <OthrPrics> [0..*] ± 126
   OtherBusinessParties <OthrBizPties> [0..1]  C26,
C44
127
     Investor <Invstr> [0..*] ± C25 127
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 38 February 2025
```

