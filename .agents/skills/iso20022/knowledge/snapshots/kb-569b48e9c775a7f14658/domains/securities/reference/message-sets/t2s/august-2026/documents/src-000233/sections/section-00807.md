---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>"]
file_pages: [1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1202 to 1209.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1202

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1371
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1371
       Purpose <Purp> [0..1] Text 1371
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1372
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1372
       RegistrationDate <RegnDt> [0..1] Date 1372
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1372
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1372
       PostalAddress <PstlAdr> [1..5] ± C10 1372
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1373
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1373
   SupplementaryData <SplmtryData> [0..*] ± C14 1374
28.4.2.1.2.1  FinancialInstrumentType <FinInstrmTp>
Presence: [0..*]
Definition: Provides additional details about the financial instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1202 August 2026
```

## File page 1203

```text
FinancialInstrumentType <FinInstrmTp> contains the following FinancialInstrument97 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Equity <Eqty> [0..1]  1210
     PreferenceToIncome <PrefToIncm> [1..1]  1211
{Or       Code <Cd> [1..1] CodeSet 1211
Or}       Proprietary <Prtry> [1..1] ± 1211
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
{Or       Code <Cd> [1..1] CodeSet 1217
Or}       Proprietary <Prtry> [1..1] ± 1217
     WarrantAgent <WarrtAgt> [0..*]  1217
       Name <Nm> [1..1] Text 1218
       Identification <Id> [0..1]  1218
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1218
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1219
       Purpose <Purp> [0..1] Text 1219
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1219
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1219
       RegistrationDate <RegnDt> [0..1] Date 1220
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1220
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1220
       PostalAddress <PstlAdr> [1..5] ± C10 1220
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1220
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1203 August 2026
```

## File page 1204

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1230
Or       ToDateTime <ToDtTm> [1..1] DateTime 1230
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1204 August 2026
```

## File page 1205

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       DateTimeRange <DtTmRg> [1..1] ± 1230
     VariableRateIndicator <VarblRateInd> [0..1] Indicator 1230
     OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1231
     OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1231
     AmortisableIndicator <AmtsblInd> [0..1] Indicator 1231
     InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1231
     CapitalisedInterest <CptlsdIntrst> [0..1]  1231
{Or       Code <Cd> [1..1] CodeSet 1232
Or}       Proprietary <Prtry> [1..1] ± 1232
     ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1232
     CurrentFactor <CurFctr> [0..1] Rate 1233
     NextFactor <NxtFctr> [0..1] Rate 1233
     PreviousFactor <PrvsFctr> [0..1] Rate 1233
     Pieces <Pcs> [0..1] Quantity 1233
     PoolsMaximum <PlsMax> [0..1] Quantity 1233
     PoolsPerMillion <PlsPerMln> [0..1] Quantity 1233
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
{Or         Code <Cd> [1..1] CodeSet 1236
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1205 August 2026
```

## File page 1206

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Proprietary <Prtry> [1..1] ± 1239
       RedemptionPrice <RedPric> [0..1]  1239
         ValueType <ValTp> [0..1] CodeSet 1239
         Value <Val> [1..1] ± 1240
         PriceType <PricTp> [0..1] CodeSet 1240
       ValueDate <ValDt> [1..1] Date 1241
       ValuePeriod <ValPrd> [1..1]  1241
{Or         FromDateTime <FrDtTm> [1..1] DateTime 1241
Or         ToDateTime <ToDtTm> [1..1] DateTime 1242
Or}         DateTimeRange <DtTmRg> [1..1] ± 1242
       CalculationDate <ClctnDt> [1..1] DateTime 1242
     InterestType <IntrstTp> [0..1] CodeSet 1242
     InstrumentStructureType <InstrmStrTp> [0..1]  1242
{Or       Code <Cd> [1..1] CodeSet 1243
Or}       Proprietary <Prtry> [1..1] ± 1244
     GlobalType <GblTp> [0..1]  1244
{Or       Code <Cd> [1..1] CodeSet 1244
Or}       Proprietary <Prtry> [1..1] ± 1245
     PotentialEuroSystemEligibility
<PotntlEuroSysElgblty>
[0..1] Indicator 1245
     Geographics <Geogcs> [0..1] Text 1245
     YieldRange <YldRg> [0..1] ± 1245
     CouponRange <CpnRg> [0..1] ± 1246
     Purpose <Purp> [0..1] Text 1246
     AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 1246
     AutoReinvestment <AutoRinvstmt> [0..1] Rate 1247
     Haircut <Hrcut> [0..1] Rate 1247
     TransactionConditions <TxConds> [0..1] ± 1247
     LookBack <LookBck> [0..1] Quantity 1247
     MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1247
     MinimumIncrement <MinIncrmt> [0..1] ± 1247
     MinimumQuantity <MinQty> [0..1] ± 1248
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1206 August 2026
```

## File page 1207

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Production <Pdctn> [0..1] Text 1248
     RestrictedIndicator <RstrctdInd> [0..1] Indicator 1248
     PriceFrequency <PricFrqcy> [0..1] ± 1248
     Sector <Sctr> [0..1] Text 1249
     SubstitutionFrequency <SbstitnFrqcy> [0..1] ± 1249
     SubstitutionLeft <SbstitnLft> [0..1] Quantity 1249
     WholePoolIndicator <WhlPoolInd> [0..1] Indicator 1249
     PriceSource <PricSrc> [0..1] Text 1249
     PriceRange <PricRg> [0..1] ± 1250
   Derivative <Deriv> [0..1]  1250
     Future <Futr> [0..1]  1254
       ContractSize <CtrctSz> [0..1] Rate 1256
       ExercisePrice <ExrcPric> [0..1]  1256
         ValueType <ValTp> [0..1] CodeSet 1256
         Value <Val> [1..1] ± 1257
         PriceType <PricTp> [0..1] CodeSet 1257
       FutureDate <FutrDt> [0..1] DateTime 1258
       MinimumSize <MinSz> [0..1] Amount C1, C5 1258
       UnitOfMeasure <UnitOfMeasr> [0..1]  1259
{Or         Code <Cd> [1..1] CodeSet 1259
Or}         Proprietary <Prtry> [1..1] ± 1261
       TimeUnit <TmUnit> [0..1]  1261
{Or         Code <Cd> [1..1] CodeSet 1262
Or}         Proprietary <Prtry> [1..1] ± 1262
       AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1262
         AllocationPercentage <AllcnPctg> [0..1] Rate 1264
         Quantity <Qty> [0..1]  1264
{Or           Unit <Unit> [1..1] Quantity 1264
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1264
         SettlementType <SttlmTp> [0..1]  1264
{Or           Code <Cd> [1..1] CodeSet 1265
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1207 August 2026
```

## File page 1208

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 1265
         CashAmount <CshAmt> [0..1] Amount C1, C5 1265
         CashType <CshTp> [0..1] Text 1266
         Price <Pric> [0..1]  1266
           ValueType <ValTp> [0..1] CodeSet 1266
           Value <Val> [1..1] ± 1267
           PriceType <PricTp> [0..1] CodeSet 1267
         DirtyPrice <DrtyPric> [0..1]  1268
           ValueType <ValTp> [0..1] CodeSet 1268
           Value <Val> [1..1] ± 1269
           PriceType <PricTp> [0..1] CodeSet 1269
         EndPrice <EndPric> [0..1]  1270
           ValueType <ValTp> [0..1] CodeSet 1270
           Value <Val> [1..1] ± 1271
           PriceType <PricTp> [0..1] CodeSet 1271
         StartValue <StartVal> [0..1] Amount C1, C5 1272
         CurrentValue <CurVal> [0..1] Amount C1, C5 1272
         EndValue <EndVal> [0..1] Amount C1, C5 1273
         AdjustedQuantity <AdjstdQty> [0..1]  1273
{Or           Unit <Unit> [1..1] Quantity 1273
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1274
         ExchangeRate <XchgRate> [0..1] Rate 1274
         CapValue <CapVal> [0..1] Amount C1, C5 1274
     Option <Optn> [0..1]  1274
       OptionSettlementStyle <OptnSttlmStyle> [0..1]  1278
{Or         Code <Cd> [0..*] CodeSet 1278
Or}         Proprietary <Prtry> [1..1] ± 1278
       ConversionDate <ConvsDt> [0..1] DateTime 1278
       StrikePrice <StrkPric> [0..1]  1278
         ValueType <ValTp> [0..1] CodeSet 1279
         Value <Val> [1..1] ± 1279
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1208 August 2026
```

## File page 1209

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1280
       MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1280
       ConversionPeriod <ConvsPrd> [0..1]  1281
{Or         FromDateTime <FrDtTm> [1..1] DateTime 1281
Or         ToDateTime <ToDtTm> [1..1] DateTime 1281
Or}         DateTimeRange <DtTmRg> [1..1] ± 1281
       OptionStyle <OptnStyle> [0..1]  1282
{Or         Code <Cd> [1..1] CodeSet 1282
Or}         Proprietary <Prtry> [1..1] ± 1282
       OptionType <OptnTp> [0..1] ± 1282
       StrikeValue <StrkVal> [0..1] Quantity 1283
       StrikeMultiplier <StrkMltplr> [0..1] Quantity 1283
       InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1283
{Or         Code <Cd> [1..1] CodeSet 1283
Or}         Proprietary <Prtry> [1..1] ± 1283
       VersionNumber <VrsnNb> [0..1] Quantity 1284
       ExpiryLocation <XpryLctn> [0..1] Text 1284
       Standardisation <Stdstn> [0..1]  1284
{Or         Code <Cd> [1..*] CodeSet 1284
Or}         Proprietary <Prtry> [1..1] ± 1285
       TradingPartyRole <TradgPtyRole> [0..1]  1285
{Or         Code <Cd> [1..*] CodeSet 1285
Or}         Proprietary <Prtry> [1..1] ± 1285
       ContractSize <CtrctSz> [0..1] Rate 1286
       AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1286
         AllocationPercentage <AllcnPctg> [0..1] Rate 1288
         Quantity <Qty> [0..1]  1288
{Or           Unit <Unit> [1..1] Quantity 1288
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1288
         SettlementType <SttlmTp> [0..1]  1288
{Or           Code <Cd> [1..1] CodeSet 1289
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1209 August 2026
```

