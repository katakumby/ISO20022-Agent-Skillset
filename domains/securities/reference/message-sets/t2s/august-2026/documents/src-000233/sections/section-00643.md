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
file_pages: [846, 847, 848, 849, 850, 851, 852, 853, 854, 855]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# Continuation at file page 846

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 846 to 855.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 846

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                 Value <Val> [1..1] ± 1257
                 PriceType <PricTp> [0..1] CodeSet 1257
               FutureDate <FutrDt> [0..1] DateTime 1258
               MinimumSize <MinSz> [0..1] Amount C1, C5 1258
               UnitOfMeasure <UnitOfMeasr> [0..1]  1259
{Or                 Code <Cd> [1..1] CodeSet 1259
Or}                 Proprietary <Prtry> [1..1] ± 1261
               TimeUnit <TmUnit> [0..1]  1261
{Or                 Code <Cd> [1..1] CodeSet 1262
Or}                 Proprietary <Prtry> [1..1] ± 1262
               AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1262
                 AllocationPercentage <AllcnPctg> [0..1] Rate 1264
                 Quantity <Qty> [0..1]  1264
{Or                   Unit <Unit> [1..1] Quantity 1264
Or}                   FaceAmount <FaceAmt> [1..1] Amount C1, C5 1264
                 SettlementType <SttlmTp> [0..1]  1264
{Or                   Code <Cd> [1..1] CodeSet 1265
Or}                   Proprietary <Prtry> [1..1] ± 1265
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 846 August 2026
```

## File page 847

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                   PriceType <PricTp> [0..1] CodeSet 1271
                 StartValue <StartVal> [0..1] Amount C1, C5 1272
                 CurrentValue <CurVal> [0..1] Amount C1, C5 1272
                 EndValue <EndVal> [0..1] Amount C1, C5 1273
                 AdjustedQuantity <AdjstdQty> [0..1]  1273
{Or                   Unit <Unit> [1..1] Quantity 1273
Or}                   FaceAmount <FaceAmt> [1..1] Amount C1, C5 1274
                 ExchangeRate <XchgRate> [0..1] Rate 1274
                 CapValue <CapVal> [0..1] Amount C1, C5 1274
             Option <Optn> [0..1]  1274
               OptionSettlementStyle <OptnSttlmStyle> [0..1]  1278
{Or                 Code <Cd> [0..*] CodeSet 1278
Or}                 Proprietary <Prtry> [1..1] ± 1278
               ConversionDate <ConvsDt> [0..1] DateTime 1278
               StrikePrice <StrkPric> [0..1]  1278
                 ValueType <ValTp> [0..1] CodeSet 1279
                 Value <Val> [1..1] ± 1279
                 PriceType <PricTp> [0..1] CodeSet 1280
               MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1280
               ConversionPeriod <ConvsPrd> [0..1]  1281
{Or                 FromDateTime <FrDtTm> [1..1] DateTime 1281
Or                 ToDateTime <ToDtTm> [1..1] DateTime 1281
Or}                 DateTimeRange <DtTmRg> [1..1] ± 1281
               OptionStyle <OptnStyle> [0..1]  1282
{Or                 Code <Cd> [1..1] CodeSet 1282
Or}                 Proprietary <Prtry> [1..1] ± 1282
               OptionType <OptnTp> [0..1] ± 1282
               StrikeValue <StrkVal> [0..1] Quantity 1283
               StrikeMultiplier <StrkMltplr> [0..1] Quantity 1283
               InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1283
{Or                 Code <Cd> [1..1] CodeSet 1283
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 847 August 2026
```

## File page 848

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}                 Proprietary <Prtry> [1..1] ± 1283
               VersionNumber <VrsnNb> [0..1] Quantity 1284
               ExpiryLocation <XpryLctn> [0..1] Text 1284
               Standardisation <Stdstn> [0..1]  1284
{Or                 Code <Cd> [1..*] CodeSet 1284
Or}                 Proprietary <Prtry> [1..1] ± 1285
               TradingPartyRole <TradgPtyRole> [0..1]  1285
{Or                 Code <Cd> [1..*] CodeSet 1285
Or}                 Proprietary <Prtry> [1..1] ± 1285
               ContractSize <CtrctSz> [0..1] Rate 1286
               AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1286
                 AllocationPercentage <AllcnPctg> [0..1] Rate 1288
                 Quantity <Qty> [0..1]  1288
{Or                   Unit <Unit> [1..1] Quantity 1288
Or}                   FaceAmount <FaceAmt> [1..1] Amount C1, C5 1288
                 SettlementType <SttlmTp> [0..1]  1288
{Or                   Code <Cd> [1..1] CodeSet 1289
Or}                   Proprietary <Prtry> [1..1] ± 1289
                 CashAmount <CshAmt> [0..1] Amount C1, C5 1289
                 CashType <CshTp> [0..1] Text 1290
                 Price <Pric> [0..1]  1290
                   ValueType <ValTp> [0..1] CodeSet 1290
                   Value <Val> [1..1] ± 1291
                   PriceType <PricTp> [0..1] CodeSet 1291
                 DirtyPrice <DrtyPric> [0..1]  1292
                   ValueType <ValTp> [0..1] CodeSet 1292
                   Value <Val> [1..1] ± 1293
                   PriceType <PricTp> [0..1] CodeSet 1293
                 EndPrice <EndPric> [0..1]  1294
                   ValueType <ValTp> [0..1] CodeSet 1294
                   Value <Val> [1..1] ± 1295
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 848 August 2026
```

## File page 849

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                   PriceType <PricTp> [0..1] CodeSet 1295
                 StartValue <StartVal> [0..1] Amount C1, C5 1296
                 CurrentValue <CurVal> [0..1] Amount C1, C5 1296
                 EndValue <EndVal> [0..1] Amount C1, C5 1297
                 AdjustedQuantity <AdjstdQty> [0..1]  1297
{Or                   Unit <Unit> [1..1] Quantity 1297
Or}                   FaceAmount <FaceAmt> [1..1] Amount C1, C5 1298
                 ExchangeRate <XchgRate> [0..1] Rate 1298
                 CapValue <CapVal> [0..1] Amount C1, C5 1298
         FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*]  1298
           SecurityStatus <SctySts> [0..1]  1307
{Or             Code <Cd> [1..1] CodeSet 1307
Or}             Proprietary <Prtry> [1..1] ± 1308
           ISOSecurityLongName <ISOSctyLngNm> [0..1] Text 1308
           ISOSecurityShortName <ISOSctyShrtNm> [0..1] Text 1308
           NameValidFrom <NmVldFr> [0..1] ± 1308
           DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 1308
           CertificateNumber <CertNb> [0..1] Text 1309
           ContractVersionNumber <CtrctVrsnNb> [0..1] Quantity 1309
           CouponAttachedNumber <CpnAttchdNb> [0..1] Text 1309
           TaxLotNumber <TaxLotNb> [0..1] Text 1309
           PoolNumber <PoolNb> [0..1] Text 1309
           CoveredIndicator <CvrdInd> [0..1] Indicator 1309
           LegalRestrictions <LglRstrctns> [0..1]  1310
{Or             Code <Cd> [1..1] CodeSet 1310
Or}             Proprietary <Prtry> [1..1] ± 1310
           PositionLimit <PosLmt> [0..1] ± 1310
           NearTermPositionLimit <NearTermPosLmt> [0..1] ± 1311
           ListingDate <ListgDt> [0..1] Date 1311
           RecordDate <RcrdDt> [0..1] DateTime 1311
           ExpiryDate <XpryDt> [0..1] Date 1311
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 849 August 2026
```

## File page 850

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Purpose <Purp> [0..1] Text 1311
           ClassificationType <ClssfctnTp> [0..1]  1311
             ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 1312
             FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 1312
             AlternateClassification <AltrnClssfctn> [0..*] ± 1312
           Issuance <Issnc> [0..1]  1312
             IssuePlace <IssePlc> [0..1] IdentifierSet 1314
             CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 1314
             IssueDate <IsseDt> [0..1] Date 1314
             AnnouncementDate <AnncmntDt> [0..1] DateTime 1314
             ISINValidFrom <ISINVldFr> [0..1] Date 1314
             IssuerOrganisation <IssrOrg> [0..1]  1314
               Name <Nm> [1..1] Text 1315
               Identification <Id> [0..1]  1315
{Or                 AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1315
Or}                 ProprietaryIdentification <PrtryId> [1..1] ± 1316
               Purpose <Purp> [0..1] Text 1316
               TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1316
               RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1316
               RegistrationDate <RegnDt> [0..1] Date 1317
               TaxIdentificationNumber <TaxIdNb> [0..1] Text 1317
               NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1317
               PostalAddress <PstlAdr> [1..5] ± C10 1317
               PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1317
               SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1318
             IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1318
             FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1318
             IssueSize <IsseSz> [0..1] Quantity 1319
             IssuePrice <IssePric> [0..1] ± 1319
             IssuanceDistribution <IssncDstrbtn> [0..1]  1319
{Or               Code <Cd> [1..1] CodeSet 1320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 850 August 2026
```

## File page 851

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}               Proprietary <Prtry> [1..1] ± 1320
             GoverningLaw <GovngLaw> [0..*]  1320
               Identification <Id> [0..1] Text 1320
               Country <Ctry> [0..1] CodeSet C4 1320
           TradingMarket <TradgMkt> [0..*]  1321
             MarketIdentification <MktId> [0..1] IdentifierSet 1321
             RoundLot <RndLot> [0..1] ± 1321
             TradeLotSize <TradLotSz> [0..1] ± 1322
             SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1322
             MinimumTradedNominalQuantity <MinTraddNmnlQty> [0..1]  1322
{Or               Unit <Unit> [1..1] Quantity 1322
Or}               FaceAmount <FaceAmt> [1..1] Amount C1, C5 1322
             MaximumTradedNominalQuantity <MaxTraddNmnlQty> [0..1]  1323
{Or               Unit <Unit> [1..1] Quantity 1323
Or}               FaceAmount <FaceAmt> [1..1] Amount C1, C5 1323
             MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 1324
             PrimaryPlaceOfListingIdentification <PmryPlcOfListgId> [0..1] IdentifierSet 1324
           SpreadAndBenchmarkCurve <SprdAndBchmkCrv> [0..*]  1324
             Spread <Sprd> [0..1] Quantity 1324
             BenchmarkIdentification <BchmkId> [0..1] ± C6, C7,
C8, C9,
C12
1325
             BenchmarkPrice <BchmkPric> [0..1]  1326
               ValueType <ValTp> [0..1] CodeSet 1326
               Value <Val> [1..1] ± 1327
               PriceType <PricTp> [0..1] CodeSet 1327
             BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 1328
             BenchmarkCurveName <BchmkCrvNm> [0..1]  1328
{Or               Code <Cd> [1..1] CodeSet 1328
Or}               Proprietary <Prtry> [1..1] ± 1329
             BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 1330
           PutType <PutTp> [0..1]  1330
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 851 August 2026
```

## File page 852

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or             Code <Cd> [1..1] CodeSet 1330
Or}             Proprietary <Prtry> [1..1] ± 1330
           CallType <CallTp> [0..1]  1331
{Or             Code <Cd> [1..1] CodeSet 1331
Or}             Proprietary <Prtry> [1..1] ± 1331
           FungibleIndicator <FngbInd> [0..1] Indicator 1331
           Confidential <Cnfdtl> [0..1] Indicator 1332
           PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 1332
           ConvertibleIndicator <ConvtblInd> [0..1] Indicator 1332
           ConversionPeriod <ConvsPrd> [0..1] ± 1332
           ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 1333
           ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 1333
           PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 1333
           TradingMethod <TradgMtd> [0..1]  1333
{Or             Unit <Unit> [1..1] Quantity 1334
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1334
           TEFRARule <TEFRARule> [0..1]  1334
{Or             Code <Cd> [1..1] CodeSet 1334
Or}             Proprietary <Prtry> [1..1] ± 1335
           SerieNumber <SrNb> [0..1] Text 1335
           Class <Clss> [0..1] Text 1335
           WithholdingTaxRegime <WhldgTaxRgm> [0..*]  1335
             WithholdingTaxValue <WhldgTaxVal> [1..1] ± 1335
             Country <Ctry> [1..1] CodeSet C4 1336
           PaymentStatus <PmtSts> [0..1] ± 1336
           InitialPhysicalForm <InitlPhysForm> [0..1]  1336
{Or             Code <Cd> [1..1] CodeSet 1337
Or}             Proprietary <Prtry> [1..1] ± 1337
           AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  1337
{Or             Code <Cd> [1..1] CodeSet 1337
Or}             Proprietary <Prtry> [1..1] ± 1338
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 852 August 2026
```

## File page 853

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           CommonSafekeeper <CmonSfkpr> [0..1]  1338
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1338
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1338
           RedemptionType <RedTp> [0..1]  1339
{Or             Code <Cd> [1..1] CodeSet 1339
Or}             Proprietary <Prtry> [1..1] ± 1339
           RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 1340
           Restriction <Rstrctn> [0..*]  1340
             EffectivePeriod <FctvPrd> [0..1] ± 1341
             RestrictionType <RstrctnTp> [0..1]  1341
{Or               RestrictionType <RstrctnTp> [1..1] CodeSet 1342
Or}               ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1342
             LegalRestrictionType <LglRstrctnTp> [0..1]  1342
{Or               Code <Cd> [1..1] CodeSet 1342
Or}               Proprietary <Prtry> [1..1] ± 1343
             InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1343
{Or               Code <Cd> [1..1] CodeSet 1343
Or}               Proprietary <Prtry> [1..1] ± 1344
             InvestorType <InvstrTp> [0..*]  1344
{Or               Code <Cd> [1..1] CodeSet 1344
Or}               Proprietary <Prtry> [1..1] ± 1344
           FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C6, C7,
C8, C9,
C12
1345
           SettlementInformation <SttlmInf> [0..*]  1346
             SecuritiesQuantityType <SctiesQtyTp> [0..1]  1346
{Or               Code <Cd> [1..1] CodeSet 1346
Or}               Proprietary <Prtry> [1..1] ± 1347
             ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 1347
             MinimumDenomination <MinDnmtn> [0..1] ± 1347
             MinimumMultipleQuantity <MinMltplQty> [0..1] ± 1347
             DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 1348
           FinancialInstrumentForm <FinInstrmForm> [0..1]  1348
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 853 August 2026
```

## File page 854

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             BookingAppearance <BookgApprnc> [0..1]  1348
{Or               Code <Cd> [1..1] CodeSet 1349
Or}               Proprietary <Prtry> [1..1] ± 1349
             LegalForm <LglForm> [0..1] ± 1349
           ContactName <CtctNm> [0..1]  1350
             Name <Nm> [1..1] Text 1350
             Identification <Id> [0..1]  1350
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1351
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1351
             Purpose <Purp> [0..1] Text 1351
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1351
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1352
             RegistrationDate <RegnDt> [0..1] Date 1352
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1352
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1352
             PostalAddress <PstlAdr> [1..5] ± C10 1352
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1353
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1353
           LeadManager <LeadMgr> [0..1]  1354
             Name <Nm> [1..1] Text 1354
             Identification <Id> [0..1]  1355
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1355
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1355
             Purpose <Purp> [0..1] Text 1355
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1356
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1356
             RegistrationDate <RegnDt> [0..1] Date 1356
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1356
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1356
             PostalAddress <PstlAdr> [1..5] ± C10 1356
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1357
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 854 August 2026
```

## File page 855

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1357
           PrincipalPayingAgent <PrncplPngAgt> [0..1]  1358
             Name <Nm> [1..1] Text 1358
             Identification <Id> [0..1]  1359
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1359
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1359
             Purpose <Purp> [0..1] Text 1359
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1360
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1360
             RegistrationDate <RegnDt> [0..1] Date 1360
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1360
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1360
             PostalAddress <PstlAdr> [1..5] ± C10 1360
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1361
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1361
           PayingAgent <PngAgt> [0..1]  1362
             Name <Nm> [1..1] Text 1362
             Identification <Id> [0..1]  1363
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1363
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1363
             Purpose <Purp> [0..1] Text 1363
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1364
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1364
             RegistrationDate <RegnDt> [0..1] Date 1364
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1364
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1364
             PostalAddress <PstlAdr> [1..5] ± C10 1364
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1365
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1365
           Depository <Dpstry> [0..1]  1366
             Name <Nm> [1..1] Text 1366
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 855 August 2026
```

