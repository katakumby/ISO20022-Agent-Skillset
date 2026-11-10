---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.1 FinancialInstrumentType <FinInstrmTp>"]
file_pages: [1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.1 FinancialInstrumentType <FinInstrmTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1014 to 1021.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1014

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1183
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1183
       Purpose <Purp> [0..1] Text 1183
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1184
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1184
       RegistrationDate <RegnDt> [0..1] Date 1184
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1184
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1184
       PostalAddress <PstlAdr> [1..5] ± C10 1184
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1185
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1185
   SupplementaryData <SplmtryData> [0..*] ± C14 1186
28.4.2.1.1.1  FinancialInstrumentType <FinInstrmTp>
Presence: [0..*]
Definition: Provides additional details about the financial instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1014 August 2026
```

## File page 1015

```text
FinancialInstrumentType <FinInstrmTp> contains the following FinancialInstrument97 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Equity <Eqty> [0..1]  1022
     PreferenceToIncome <PrefToIncm> [1..1]  1023
{Or       Code <Cd> [1..1] CodeSet 1023
Or}       Proprietary <Prtry> [1..1] ± 1023
     MaturityDate <MtrtyDt> [0..1] DateTime 1024
     NonPaidAmount <NonPdAmt> [0..1] Amount C1, C5 1024
     ParValue <ParVal> [0..1] Amount C1, C5 1024
     VotingRightsPerShare <VtngRghtsPerShr> [0..1] Quantity 1025
   Warrant <Warrt> [0..1]  1025
     Multiplier <Mltplr> [0..1] Rate 1026
     SubscriptionPrice <SbcptPric> [0..1]  1026
       ValueType <ValTp> [0..1] CodeSet 1027
       Value <Val> [1..1] ± 1027
       PriceType <PricTp> [0..1] CodeSet 1028
     Type <Tp> [0..1]  1028
{Or       Code <Cd> [1..1] CodeSet 1029
Or}       Proprietary <Prtry> [1..1] ± 1029
     WarrantAgent <WarrtAgt> [0..*]  1029
       Name <Nm> [1..1] Text 1030
       Identification <Id> [0..1]  1030
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1030
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1031
       Purpose <Purp> [0..1] Text 1031
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1031
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1031
       RegistrationDate <RegnDt> [0..1] Date 1032
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1032
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1032
       PostalAddress <PstlAdr> [1..5] ± C10 1032
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1032
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1015 August 2026
```

## File page 1016

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1033
   Debt <Debt> [0..1]  C11,
C13
1033
     PaymentCurrency <PmtCcy> [0..1] CodeSet C1 1037
     FaceAmount <FaceAmt> [0..1] Amount C1, C5 1037
     PaymentFrequency <PmtFrqcy> [0..1] ± 1038
     InterestFixingDate <IntrstFxgDt> [0..1] DateTime 1038
     DatedDate <DtdDt> [0..1] DateTime 1038
     FirstPaymentDate <FrstPmtDt> [0..1] DateTime 1038
     MaturityDate <MtrtyDt> [0..1] DateTime 1038
     NextCouponDate <NxtCpnDt> [0..1] DateTime 1038
     PutableDate <PutblDt> [0..1] DateTime 1039
     NextCallableDate <NxtCllblDt> [0..1] DateTime 1039
     NextFactorDate <NxtFctrDt> [0..1] DateTime 1039
     ExpirationDate <XprtnDt> [0..1] DateTime 1039
     PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 1039
     InterestRate <IntrstRate> [0..1] Rate 1039
     NextInterestRate <NxtIntrstRate> [0..1] Rate 1039
     OddCouponIndicator <OddCpnInd> [0..1] Indicator 1039
     CallableIndicator <CllblInd> [0..1] Indicator 1040
     CPProgram <CPPrgm> [0..1] Quantity 1040
     CPRegistrationType <CPRegnTp> [0..1] Text 1040
     InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 1040
     PutableIndicator <PutblInd> [0..1] Indicator 1040
     PreFundedIndicator <PreFnddInd> [0..1] Indicator 1041
     EscrowedIndicator <EscrwdInd> [0..1] Indicator 1041
     PerpetualIndicator <PerptlInd> [0..1] Indicator 1041
     SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1041
     ExtendibleIndicator <XtndblInd> [0..1] Indicator 1041
     ExtendiblePeriod <XtndblPrd> [0..1]  1042
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1042
Or       ToDateTime <ToDtTm> [1..1] DateTime 1042
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1016 August 2026
```

## File page 1017

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       DateTimeRange <DtTmRg> [1..1] ± 1042
     VariableRateIndicator <VarblRateInd> [0..1] Indicator 1042
     OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1043
     OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1043
     AmortisableIndicator <AmtsblInd> [0..1] Indicator 1043
     InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1043
     CapitalisedInterest <CptlsdIntrst> [0..1]  1043
{Or       Code <Cd> [1..1] CodeSet 1044
Or}       Proprietary <Prtry> [1..1] ± 1044
     ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1044
     CurrentFactor <CurFctr> [0..1] Rate 1045
     NextFactor <NxtFctr> [0..1] Rate 1045
     PreviousFactor <PrvsFctr> [0..1] Rate 1045
     Pieces <Pcs> [0..1] Quantity 1045
     PoolsMaximum <PlsMax> [0..1] Quantity 1045
     PoolsPerMillion <PlsPerMln> [0..1] Quantity 1045
     PoolsPerLot <PlsPerLot> [0..1] Quantity 1045
     PoolsPerTrade <PlsPerTrad> [0..1] Quantity 1046
     ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 1046
     LotIdentification <LotId> [0..1] Text 1046
     ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 1046
     WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 1046
     WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 1046
     WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1046
     WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1047
     InsuredIndicator <InsrdInd> [0..1] Indicator 1047
     BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1047
     YieldCalculation <YldClctn> [0..*]  1047
       Value <Val> [1..1] Rate 1048
       CalculationType <ClctnTp> [0..1]  1048
{Or         Code <Cd> [1..1] CodeSet 1048
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1017 August 2026
```

## File page 1018

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Proprietary <Prtry> [1..1] ± 1051
       RedemptionPrice <RedPric> [0..1]  1051
         ValueType <ValTp> [0..1] CodeSet 1051
         Value <Val> [1..1] ± 1052
         PriceType <PricTp> [0..1] CodeSet 1052
       ValueDate <ValDt> [1..1] Date 1053
       ValuePeriod <ValPrd> [1..1]  1053
{Or         FromDateTime <FrDtTm> [1..1] DateTime 1053
Or         ToDateTime <ToDtTm> [1..1] DateTime 1054
Or}         DateTimeRange <DtTmRg> [1..1] ± 1054
       CalculationDate <ClctnDt> [1..1] DateTime 1054
     InterestType <IntrstTp> [0..1] CodeSet 1054
     InstrumentStructureType <InstrmStrTp> [0..1]  1054
{Or       Code <Cd> [1..1] CodeSet 1055
Or}       Proprietary <Prtry> [1..1] ± 1056
     GlobalType <GblTp> [0..1]  1056
{Or       Code <Cd> [1..1] CodeSet 1056
Or}       Proprietary <Prtry> [1..1] ± 1057
     PotentialEuroSystemEligibility
<PotntlEuroSysElgblty>
[0..1] Indicator 1057
     Geographics <Geogcs> [0..1] Text 1057
     YieldRange <YldRg> [0..1] ± 1057
     CouponRange <CpnRg> [0..1] ± 1058
     Purpose <Purp> [0..1] Text 1058
     AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 1058
     AutoReinvestment <AutoRinvstmt> [0..1] Rate 1059
     Haircut <Hrcut> [0..1] Rate 1059
     TransactionConditions <TxConds> [0..1] ± 1059
     LookBack <LookBck> [0..1] Quantity 1059
     MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1059
     MinimumIncrement <MinIncrmt> [0..1] ± 1059
     MinimumQuantity <MinQty> [0..1] ± 1060
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1018 August 2026
```

## File page 1019

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Production <Pdctn> [0..1] Text 1060
     RestrictedIndicator <RstrctdInd> [0..1] Indicator 1060
     PriceFrequency <PricFrqcy> [0..1] ± 1060
     Sector <Sctr> [0..1] Text 1061
     SubstitutionFrequency <SbstitnFrqcy> [0..1] ± 1061
     SubstitutionLeft <SbstitnLft> [0..1] Quantity 1061
     WholePoolIndicator <WhlPoolInd> [0..1] Indicator 1061
     PriceSource <PricSrc> [0..1] Text 1061
     PriceRange <PricRg> [0..1] ± 1062
   Derivative <Deriv> [0..1]  1062
     Future <Futr> [0..1]  1066
       ContractSize <CtrctSz> [0..1] Rate 1068
       ExercisePrice <ExrcPric> [0..1]  1068
         ValueType <ValTp> [0..1] CodeSet 1068
         Value <Val> [1..1] ± 1069
         PriceType <PricTp> [0..1] CodeSet 1069
       FutureDate <FutrDt> [0..1] DateTime 1070
       MinimumSize <MinSz> [0..1] Amount C1, C5 1070
       UnitOfMeasure <UnitOfMeasr> [0..1]  1071
{Or         Code <Cd> [1..1] CodeSet 1071
Or}         Proprietary <Prtry> [1..1] ± 1073
       TimeUnit <TmUnit> [0..1]  1073
{Or         Code <Cd> [1..1] CodeSet 1074
Or}         Proprietary <Prtry> [1..1] ± 1074
       AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1074
         AllocationPercentage <AllcnPctg> [0..1] Rate 1076
         Quantity <Qty> [0..1]  1076
{Or           Unit <Unit> [1..1] Quantity 1076
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1076
         SettlementType <SttlmTp> [0..1]  1076
{Or           Code <Cd> [1..1] CodeSet 1077
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1019 August 2026
```

## File page 1020

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 1077
         CashAmount <CshAmt> [0..1] Amount C1, C5 1077
         CashType <CshTp> [0..1] Text 1078
         Price <Pric> [0..1]  1078
           ValueType <ValTp> [0..1] CodeSet 1078
           Value <Val> [1..1] ± 1079
           PriceType <PricTp> [0..1] CodeSet 1079
         DirtyPrice <DrtyPric> [0..1]  1080
           ValueType <ValTp> [0..1] CodeSet 1080
           Value <Val> [1..1] ± 1081
           PriceType <PricTp> [0..1] CodeSet 1081
         EndPrice <EndPric> [0..1]  1082
           ValueType <ValTp> [0..1] CodeSet 1082
           Value <Val> [1..1] ± 1083
           PriceType <PricTp> [0..1] CodeSet 1083
         StartValue <StartVal> [0..1] Amount C1, C5 1084
         CurrentValue <CurVal> [0..1] Amount C1, C5 1084
         EndValue <EndVal> [0..1] Amount C1, C5 1085
         AdjustedQuantity <AdjstdQty> [0..1]  1085
{Or           Unit <Unit> [1..1] Quantity 1085
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1086
         ExchangeRate <XchgRate> [0..1] Rate 1086
         CapValue <CapVal> [0..1] Amount C1, C5 1086
     Option <Optn> [0..1]  1086
       OptionSettlementStyle <OptnSttlmStyle> [0..1]  1090
{Or         Code <Cd> [0..*] CodeSet 1090
Or}         Proprietary <Prtry> [1..1] ± 1090
       ConversionDate <ConvsDt> [0..1] DateTime 1090
       StrikePrice <StrkPric> [0..1]  1090
         ValueType <ValTp> [0..1] CodeSet 1091
         Value <Val> [1..1] ± 1091
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1020 August 2026
```

## File page 1021

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1092
       MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1092
       ConversionPeriod <ConvsPrd> [0..1]  1093
{Or         FromDateTime <FrDtTm> [1..1] DateTime 1093
Or         ToDateTime <ToDtTm> [1..1] DateTime 1093
Or}         DateTimeRange <DtTmRg> [1..1] ± 1093
       OptionStyle <OptnStyle> [0..1]  1094
{Or         Code <Cd> [1..1] CodeSet 1094
Or}         Proprietary <Prtry> [1..1] ± 1094
       OptionType <OptnTp> [0..1] ± 1094
       StrikeValue <StrkVal> [0..1] Quantity 1095
       StrikeMultiplier <StrkMltplr> [0..1] Quantity 1095
       InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1095
{Or         Code <Cd> [1..1] CodeSet 1095
Or}         Proprietary <Prtry> [1..1] ± 1095
       VersionNumber <VrsnNb> [0..1] Quantity 1096
       ExpiryLocation <XpryLctn> [0..1] Text 1096
       Standardisation <Stdstn> [0..1]  1096
{Or         Code <Cd> [1..*] CodeSet 1096
Or}         Proprietary <Prtry> [1..1] ± 1097
       TradingPartyRole <TradgPtyRole> [0..1]  1097
{Or         Code <Cd> [1..*] CodeSet 1097
Or}         Proprietary <Prtry> [1..1] ± 1097
       ContractSize <CtrctSz> [0..1] Rate 1098
       AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1098
         AllocationPercentage <AllcnPctg> [0..1] Rate 1100
         Quantity <Qty> [0..1]  1100
{Or           Unit <Unit> [1..1] Quantity 1100
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1100
         SettlementType <SttlmTp> [0..1]  1100
{Or           Code <Cd> [1..1] CodeSet 1101
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1021 August 2026
```

