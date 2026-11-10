---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: []
file_pages: [961, 962, 963, 964, 965, 966, 967, 968, 969, 970]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# Continuation at file page 961

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 961 to 970.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 961

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Purpose <Purp> [0..1] Text 1128
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1128
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1128
           RegistrationDate <RegnDt> [0..1] Date 1129
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1129
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1129
           PostalAddress <PstlAdr> [1..5] ± C10 1129
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1129
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1130
         IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1130
         FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1130
         IssueSize <IsseSz> [0..1] Quantity 1131
         IssuePrice <IssePric> [0..1] ± 1131
         IssuanceDistribution <IssncDstrbtn> [0..1]  1131
{Or           Code <Cd> [1..1] CodeSet 1132
Or}           Proprietary <Prtry> [1..1] ± 1132
         GoverningLaw <GovngLaw> [0..*]  1132
           Identification <Id> [0..1] Text 1132
           Country <Ctry> [0..1] CodeSet C4 1132
       TradingMarket <TradgMkt> [0..*]  1133
         MarketIdentification <MktId> [0..1] IdentifierSet 1133
         RoundLot <RndLot> [0..1] ± 1133
         TradeLotSize <TradLotSz> [0..1] ± 1134
         SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1134
         MinimumTradedNominalQuantity
<MinTraddNmnlQty>
[0..1]  1134
{Or           Unit <Unit> [1..1] Quantity 1134
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1134
         MaximumTradedNominalQuantity
<MaxTraddNmnlQty>
[0..1]  1135
{Or           Unit <Unit> [1..1] Quantity 1135
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1135
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 961 August 2026
```

## File page 962

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 1136
         PrimaryPlaceOfListingIdentification
<PmryPlcOfListgId>
[0..1] IdentifierSet 1136
       SpreadAndBenchmarkCurve <SprdAndBchmkCrv> [0..*]  1136
         Spread <Sprd> [0..1] Quantity 1136
         BenchmarkIdentification <BchmkId> [0..1] ± C6, C7,
C8, C9,
C12
1137
         BenchmarkPrice <BchmkPric> [0..1]  1138
           ValueType <ValTp> [0..1] CodeSet 1138
           Value <Val> [1..1] ± 1139
           PriceType <PricTp> [0..1] CodeSet 1139
         BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 1140
         BenchmarkCurveName <BchmkCrvNm> [0..1]  1140
{Or           Code <Cd> [1..1] CodeSet 1140
Or}           Proprietary <Prtry> [1..1] ± 1141
         BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 1142
       PutType <PutTp> [0..1]  1142
{Or         Code <Cd> [1..1] CodeSet 1142
Or}         Proprietary <Prtry> [1..1] ± 1142
       CallType <CallTp> [0..1]  1143
{Or         Code <Cd> [1..1] CodeSet 1143
Or}         Proprietary <Prtry> [1..1] ± 1143
       FungibleIndicator <FngbInd> [0..1] Indicator 1143
       Confidential <Cnfdtl> [0..1] Indicator 1144
       PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 1144
       ConvertibleIndicator <ConvtblInd> [0..1] Indicator 1144
       ConversionPeriod <ConvsPrd> [0..1] ± 1144
       ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 1145
       ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 1145
       PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 1145
       TradingMethod <TradgMtd> [0..1]  1145
{Or         Unit <Unit> [1..1] Quantity 1146
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 962 August 2026
```

## File page 963

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1146
       TEFRARule <TEFRARule> [0..1]  1146
{Or         Code <Cd> [1..1] CodeSet 1146
Or}         Proprietary <Prtry> [1..1] ± 1147
       SerieNumber <SrNb> [0..1] Text 1147
       Class <Clss> [0..1] Text 1147
       WithholdingTaxRegime <WhldgTaxRgm> [0..*]  1147
         WithholdingTaxValue <WhldgTaxVal> [1..1] ± 1147
         Country <Ctry> [1..1] CodeSet C4 1148
       PaymentStatus <PmtSts> [0..1] ± 1148
       InitialPhysicalForm <InitlPhysForm> [0..1]  1148
{Or         Code <Cd> [1..1] CodeSet 1149
Or}         Proprietary <Prtry> [1..1] ± 1149
       AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  1149
{Or         Code <Cd> [1..1] CodeSet 1149
Or}         Proprietary <Prtry> [1..1] ± 1150
       CommonSafekeeper <CmonSfkpr> [0..1]  1150
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1150
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1150
       RedemptionType <RedTp> [0..1]  1151
{Or         Code <Cd> [1..1] CodeSet 1151
Or}         Proprietary <Prtry> [1..1] ± 1151
       RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 1152
       Restriction <Rstrctn> [0..*]  1152
         EffectivePeriod <FctvPrd> [0..1] ± 1153
         RestrictionType <RstrctnTp> [0..1]  1153
{Or           RestrictionType <RstrctnTp> [1..1] CodeSet 1154
Or}           ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1154
         LegalRestrictionType <LglRstrctnTp> [0..1]  1154
{Or           Code <Cd> [1..1] CodeSet 1154
Or}           Proprietary <Prtry> [1..1] ± 1155
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 963 August 2026
```

## File page 964

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1155
{Or           Code <Cd> [1..1] CodeSet 1155
Or}           Proprietary <Prtry> [1..1] ± 1156
         InvestorType <InvstrTp> [0..*]  1156
{Or           Code <Cd> [1..1] CodeSet 1156
Or}           Proprietary <Prtry> [1..1] ± 1156
       FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C6, C7,
C8, C9,
C12
1157
       SettlementInformation <SttlmInf> [0..*]  1158
         SecuritiesQuantityType <SctiesQtyTp> [0..1]  1158
{Or           Code <Cd> [1..1] CodeSet 1158
Or}           Proprietary <Prtry> [1..1] ± 1159
         ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 1159
         MinimumDenomination <MinDnmtn> [0..1] ± 1159
         MinimumMultipleQuantity <MinMltplQty> [0..1] ± 1159
         DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 1160
       FinancialInstrumentForm <FinInstrmForm> [0..1]  1160
         BookingAppearance <BookgApprnc> [0..1]  1160
{Or           Code <Cd> [1..1] CodeSet 1161
Or}           Proprietary <Prtry> [1..1] ± 1161
         LegalForm <LglForm> [0..1] ± 1161
       ContactName <CtctNm> [0..1]  1162
         Name <Nm> [1..1] Text 1162
         Identification <Id> [0..1]  1162
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1163
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1163
         Purpose <Purp> [0..1] Text 1163
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1163
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1164
         RegistrationDate <RegnDt> [0..1] Date 1164
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1164
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1164
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 964 August 2026
```

## File page 965

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PostalAddress <PstlAdr> [1..5] ± C10 1164
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1165
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1165
       LeadManager <LeadMgr> [0..1]  1166
         Name <Nm> [1..1] Text 1166
         Identification <Id> [0..1]  1167
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1167
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1167
         Purpose <Purp> [0..1] Text 1167
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1168
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1168
         RegistrationDate <RegnDt> [0..1] Date 1168
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1168
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1168
         PostalAddress <PstlAdr> [1..5] ± C10 1168
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1169
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1169
       PrincipalPayingAgent <PrncplPngAgt> [0..1]  1170
         Name <Nm> [1..1] Text 1170
         Identification <Id> [0..1]  1171
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1171
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1171
         Purpose <Purp> [0..1] Text 1171
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1172
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1172
         RegistrationDate <RegnDt> [0..1] Date 1172
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1172
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1172
         PostalAddress <PstlAdr> [1..5] ± C10 1172
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1173
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 965 August 2026
```

## File page 966

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1173
       PayingAgent <PngAgt> [0..1]  1174
         Name <Nm> [1..1] Text 1174
         Identification <Id> [0..1]  1175
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1175
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1175
         Purpose <Purp> [0..1] Text 1175
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1176
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1176
         RegistrationDate <RegnDt> [0..1] Date 1176
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1176
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1176
         PostalAddress <PstlAdr> [1..5] ± C10 1176
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1177
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1177
       Depository <Dpstry> [0..1]  1178
         Name <Nm> [1..1] Text 1178
         Identification <Id> [0..1]  1179
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1179
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1179
         Purpose <Purp> [0..1] Text 1179
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1180
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1180
         RegistrationDate <RegnDt> [0..1] Date 1180
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1180
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1180
         PostalAddress <PstlAdr> [1..5] ± C10 1180
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1181
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1181
       UnderlyingRisk <UndrlygRsk> [0..1]  1182
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 966 August 2026
```

## File page 967

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Name <Nm> [1..1] Text 1182
         Identification <Id> [0..1]  1183
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1183
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1183
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
Or   Delete <Del> [1..1]  1186
     FinancialInstrumentType <FinInstrmTp> [0..*]  1202
       Equity <Eqty> [0..1]  1210
         PreferenceToIncome <PrefToIncm> [1..1]  1211
{Or           Code <Cd> [1..1] CodeSet 1211
Or}           Proprietary <Prtry> [1..1] ± 1211
         MaturityDate <MtrtyDt> [0..1] DateTime 1212
         NonPaidAmount <NonPdAmt> [0..1] Amount C1, C5 1212
         ParValue <ParVal> [0..1] Amount C1, C5 1212
         VotingRightsPerShare <VtngRghtsPerShr> [0..1] Quantity 1213
       Warrant <Warrt> [0..1]  1213
         Multiplier <Mltplr> [0..1] Rate 1214
         SubscriptionPrice <SbcptPric> [0..1]  1214
           ValueType <ValTp> [0..1] CodeSet 1215
           Value <Val> [1..1] ± 1215
           PriceType <PricTp> [0..1] CodeSet 1216
         Type <Tp> [0..1]  1216
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 967 August 2026
```

## File page 968

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           Code <Cd> [1..1] CodeSet 1217
Or}           Proprietary <Prtry> [1..1] ± 1217
         WarrantAgent <WarrtAgt> [0..*]  1217
           Name <Nm> [1..1] Text 1218
           Identification <Id> [0..1]  1218
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1218
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1219
           Purpose <Purp> [0..1] Text 1219
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1219
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1219
           RegistrationDate <RegnDt> [0..1] Date 1220
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1220
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1220
           PostalAddress <PstlAdr> [1..5] ± C10 1220
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1220
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1221
       Debt <Debt> [0..1]  C11,
C13
1221
         PaymentCurrency <PmtCcy> [0..1] CodeSet C1 1225
         FaceAmount <FaceAmt> [0..1] Amount C1, C5 1225
         PaymentFrequency <PmtFrqcy> [0..1] ± 1226
         InterestFixingDate <IntrstFxgDt> [0..1] DateTime 1226
         DatedDate <DtdDt> [0..1] DateTime 1226
         FirstPaymentDate <FrstPmtDt> [0..1] DateTime 1226
         MaturityDate <MtrtyDt> [0..1] DateTime 1226
         NextCouponDate <NxtCpnDt> [0..1] DateTime 1226
         PutableDate <PutblDt> [0..1] DateTime 1227
         NextCallableDate <NxtCllblDt> [0..1] DateTime 1227
         NextFactorDate <NxtFctrDt> [0..1] DateTime 1227
         ExpirationDate <XprtnDt> [0..1] DateTime 1227
         PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 1227
         InterestRate <IntrstRate> [0..1] Rate 1227
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 968 August 2026
```

## File page 969

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         NextInterestRate <NxtIntrstRate> [0..1] Rate 1227
         OddCouponIndicator <OddCpnInd> [0..1] Indicator 1227
         CallableIndicator <CllblInd> [0..1] Indicator 1228
         CPProgram <CPPrgm> [0..1] Quantity 1228
         CPRegistrationType <CPRegnTp> [0..1] Text 1228
         InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 1228
         PutableIndicator <PutblInd> [0..1] Indicator 1228
         PreFundedIndicator <PreFnddInd> [0..1] Indicator 1229
         EscrowedIndicator <EscrwdInd> [0..1] Indicator 1229
         PerpetualIndicator <PerptlInd> [0..1] Indicator 1229
         SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1229
         ExtendibleIndicator <XtndblInd> [0..1] Indicator 1229
         ExtendiblePeriod <XtndblPrd> [0..1]  1230
{Or           FromDateTime <FrDtTm> [1..1] DateTime 1230
Or           ToDateTime <ToDtTm> [1..1] DateTime 1230
Or}           DateTimeRange <DtTmRg> [1..1] ± 1230
         VariableRateIndicator <VarblRateInd> [0..1] Indicator 1230
         OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1231
         OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1231
         AmortisableIndicator <AmtsblInd> [0..1] Indicator 1231
         InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1231
         CapitalisedInterest <CptlsdIntrst> [0..1]  1231
{Or           Code <Cd> [1..1] CodeSet 1232
Or}           Proprietary <Prtry> [1..1] ± 1232
         ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1232
         CurrentFactor <CurFctr> [0..1] Rate 1233
         NextFactor <NxtFctr> [0..1] Rate 1233
         PreviousFactor <PrvsFctr> [0..1] Rate 1233
         Pieces <Pcs> [0..1] Quantity 1233
         PoolsMaximum <PlsMax> [0..1] Quantity 1233
         PoolsPerMillion <PlsPerMln> [0..1] Quantity 1233
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 969 August 2026
```

## File page 970

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PoolsPerLot <PlsPerLot> [0..1] Quantity 1233
         PoolsPerTrade <PlsPerTrad> [0..1] Quantity 1234
         ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 1234
         LotIdentification <LotId> [0..1] Text 1234
         ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 1234
         WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 1234
         WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 1234
         WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1234
         WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1235
         InsuredIndicator <InsrdInd> [0..1] Indicator 1235
         BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1235
         YieldCalculation <YldClctn> [0..*]  1235
           Value <Val> [1..1] Rate 1236
           CalculationType <ClctnTp> [0..1]  1236
{Or             Code <Cd> [1..1] CodeSet 1236
Or}             Proprietary <Prtry> [1..1] ± 1239
           RedemptionPrice <RedPric> [0..1]  1239
             ValueType <ValTp> [0..1] CodeSet 1239
             Value <Val> [1..1] ± 1240
             PriceType <PricTp> [0..1] CodeSet 1240
           ValueDate <ValDt> [1..1] Date 1241
           ValuePeriod <ValPrd> [1..1]  1241
{Or             FromDateTime <FrDtTm> [1..1] DateTime 1241
Or             ToDateTime <ToDtTm> [1..1] DateTime 1242
Or}             DateTimeRange <DtTmRg> [1..1] ± 1242
           CalculationDate <ClctnDt> [1..1] DateTime 1242
         InterestType <IntrstTp> [0..1] CodeSet 1242
         InstrumentStructureType <InstrmStrTp> [0..1]  1242
{Or           Code <Cd> [1..1] CodeSet 1243
Or}           Proprietary <Prtry> [1..1] ± 1244
         GlobalType <GblTp> [0..1]  1244
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 970 August 2026
```

