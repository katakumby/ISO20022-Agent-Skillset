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
file_pages: [919, 920, 921, 922, 923, 924, 925, 926, 927, 928]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# Continuation at file page 919

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 919 to 928.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 919

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1357
         PrincipalPayingAgent <PrncplPngAgt> [0..1]  1358
           Name <Nm> [1..1] Text 1358
           Identification <Id> [0..1]  1359
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1359
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1359
           Purpose <Purp> [0..1] Text 1359
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1360
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1360
           RegistrationDate <RegnDt> [0..1] Date 1360
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1360
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1360
           PostalAddress <PstlAdr> [1..5] ± C10 1360
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1361
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1361
         PayingAgent <PngAgt> [0..1]  1362
           Name <Nm> [1..1] Text 1362
           Identification <Id> [0..1]  1363
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1363
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1363
           Purpose <Purp> [0..1] Text 1363
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1364
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1364
           RegistrationDate <RegnDt> [0..1] Date 1364
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1364
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1364
           PostalAddress <PstlAdr> [1..5] ± C10 1364
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1365
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1365
         Depository <Dpstry> [0..1]  1366
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 919 August 2026
```

## File page 920

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Name <Nm> [1..1] Text 1366
           Identification <Id> [0..1]  1367
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1367
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1367
           Purpose <Purp> [0..1] Text 1367
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1368
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1368
           RegistrationDate <RegnDt> [0..1] Date 1368
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1368
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1368
           PostalAddress <PstlAdr> [1..5] ± C10 1368
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1369
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1369
         UnderlyingRisk <UndrlygRsk> [0..1]  1370
           Name <Nm> [1..1] Text 1370
           Identification <Id> [0..1]  1371
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1371
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1371
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
Or}     Modify <Modfy> [1..1]  1374
       FinancialInstrumentType <FinInstrmTp> [0..*]  1390
         Equity <Eqty> [0..1]  1398
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 920 August 2026
```

## File page 921

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           PreferenceToIncome <PrefToIncm> [1..1]  1399
{Or             Code <Cd> [1..1] CodeSet 1399
Or}             Proprietary <Prtry> [1..1] ± 1399
           MaturityDate <MtrtyDt> [0..1] DateTime 1400
           NonPaidAmount <NonPdAmt> [0..1] Amount C1, C5 1400
           ParValue <ParVal> [0..1] Amount C1, C5 1400
           VotingRightsPerShare <VtngRghtsPerShr> [0..1] Quantity 1401
         Warrant <Warrt> [0..1]  1401
           Multiplier <Mltplr> [0..1] Rate 1402
           SubscriptionPrice <SbcptPric> [0..1]  1402
             ValueType <ValTp> [0..1] CodeSet 1403
             Value <Val> [1..1] ± 1403
             PriceType <PricTp> [0..1] CodeSet 1404
           Type <Tp> [0..1]  1404
{Or             Code <Cd> [1..1] CodeSet 1405
Or}             Proprietary <Prtry> [1..1] ± 1405
           WarrantAgent <WarrtAgt> [0..*]  1405
             Name <Nm> [1..1] Text 1406
             Identification <Id> [0..1]  1406
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1406
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1407
             Purpose <Purp> [0..1] Text 1407
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1407
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1407
             RegistrationDate <RegnDt> [0..1] Date 1408
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1408
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1408
             PostalAddress <PstlAdr> [1..5] ± C10 1408
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1408
             SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1409
         Debt <Debt> [0..1]  C11,
C13
1409
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 921 August 2026
```

## File page 922

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           PaymentCurrency <PmtCcy> [0..1] CodeSet C1 1413
           FaceAmount <FaceAmt> [0..1] Amount C1, C5 1413
           PaymentFrequency <PmtFrqcy> [0..1] ± 1414
           InterestFixingDate <IntrstFxgDt> [0..1] DateTime 1414
           DatedDate <DtdDt> [0..1] DateTime 1414
           FirstPaymentDate <FrstPmtDt> [0..1] DateTime 1414
           MaturityDate <MtrtyDt> [0..1] DateTime 1414
           NextCouponDate <NxtCpnDt> [0..1] DateTime 1414
           PutableDate <PutblDt> [0..1] DateTime 1415
           NextCallableDate <NxtCllblDt> [0..1] DateTime 1415
           NextFactorDate <NxtFctrDt> [0..1] DateTime 1415
           ExpirationDate <XprtnDt> [0..1] DateTime 1415
           PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 1415
           InterestRate <IntrstRate> [0..1] Rate 1415
           NextInterestRate <NxtIntrstRate> [0..1] Rate 1415
           OddCouponIndicator <OddCpnInd> [0..1] Indicator 1415
           CallableIndicator <CllblInd> [0..1] Indicator 1416
           CPProgram <CPPrgm> [0..1] Quantity 1416
           CPRegistrationType <CPRegnTp> [0..1] Text 1416
           InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 1416
           PutableIndicator <PutblInd> [0..1] Indicator 1416
           PreFundedIndicator <PreFnddInd> [0..1] Indicator 1417
           EscrowedIndicator <EscrwdInd> [0..1] Indicator 1417
           PerpetualIndicator <PerptlInd> [0..1] Indicator 1417
           SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1417
           ExtendibleIndicator <XtndblInd> [0..1] Indicator 1417
           ExtendiblePeriod <XtndblPrd> [0..1]  1418
{Or             FromDateTime <FrDtTm> [1..1] DateTime 1418
Or             ToDateTime <ToDtTm> [1..1] DateTime 1418
Or}             DateTimeRange <DtTmRg> [1..1] ± 1418
           VariableRateIndicator <VarblRateInd> [0..1] Indicator 1418
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 922 August 2026
```

## File page 923

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1419
           OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1419
           AmortisableIndicator <AmtsblInd> [0..1] Indicator 1419
           InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1419
           CapitalisedInterest <CptlsdIntrst> [0..1]  1419
{Or             Code <Cd> [1..1] CodeSet 1420
Or}             Proprietary <Prtry> [1..1] ± 1420
           ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1420
           CurrentFactor <CurFctr> [0..1] Rate 1421
           NextFactor <NxtFctr> [0..1] Rate 1421
           PreviousFactor <PrvsFctr> [0..1] Rate 1421
           Pieces <Pcs> [0..1] Quantity 1421
           PoolsMaximum <PlsMax> [0..1] Quantity 1421
           PoolsPerMillion <PlsPerMln> [0..1] Quantity 1421
           PoolsPerLot <PlsPerLot> [0..1] Quantity 1421
           PoolsPerTrade <PlsPerTrad> [0..1] Quantity 1422
           ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 1422
           LotIdentification <LotId> [0..1] Text 1422
           ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 1422
           WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 1422
           WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 1422
           WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1422
           WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1423
           InsuredIndicator <InsrdInd> [0..1] Indicator 1423
           BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1423
           YieldCalculation <YldClctn> [0..*]  1423
             Value <Val> [1..1] Rate 1424
             CalculationType <ClctnTp> [0..1]  1424
{Or               Code <Cd> [1..1] CodeSet 1424
Or}               Proprietary <Prtry> [1..1] ± 1427
             RedemptionPrice <RedPric> [0..1]  1427
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 923 August 2026
```

## File page 924

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               ValueType <ValTp> [0..1] CodeSet 1427
               Value <Val> [1..1] ± 1428
               PriceType <PricTp> [0..1] CodeSet 1428
             ValueDate <ValDt> [1..1] Date 1429
             ValuePeriod <ValPrd> [1..1]  1429
{Or               FromDateTime <FrDtTm> [1..1] DateTime 1429
Or               ToDateTime <ToDtTm> [1..1] DateTime 1430
Or}               DateTimeRange <DtTmRg> [1..1] ± 1430
             CalculationDate <ClctnDt> [1..1] DateTime 1430
           InterestType <IntrstTp> [0..1] CodeSet 1430
           InstrumentStructureType <InstrmStrTp> [0..1]  1430
{Or             Code <Cd> [1..1] CodeSet 1431
Or}             Proprietary <Prtry> [1..1] ± 1432
           GlobalType <GblTp> [0..1]  1432
{Or             Code <Cd> [1..1] CodeSet 1432
Or}             Proprietary <Prtry> [1..1] ± 1433
           PotentialEuroSystemEligibility
<PotntlEuroSysElgblty>
[0..1] Indicator 1433
           Geographics <Geogcs> [0..1] Text 1433
           YieldRange <YldRg> [0..1] ± 1433
           CouponRange <CpnRg> [0..1] ± 1434
           Purpose <Purp> [0..1] Text 1434
           AlternativeMinimumTaxIndicator
<AltrntvMinTaxInd>
[0..1] Indicator 1434
           AutoReinvestment <AutoRinvstmt> [0..1] Rate 1435
           Haircut <Hrcut> [0..1] Rate 1435
           TransactionConditions <TxConds> [0..1] ± 1435
           LookBack <LookBck> [0..1] Quantity 1435
           MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1435
           MinimumIncrement <MinIncrmt> [0..1] ± 1435
           MinimumQuantity <MinQty> [0..1] ± 1436
           Production <Pdctn> [0..1] Text 1436
           RestrictedIndicator <RstrctdInd> [0..1] Indicator 1436
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 924 August 2026
```

## File page 925

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           PriceFrequency <PricFrqcy> [0..1] ± 1436
           Sector <Sctr> [0..1] Text 1437
           SubstitutionFrequency <SbstitnFrqcy> [0..1] ± 1437
           SubstitutionLeft <SbstitnLft> [0..1] Quantity 1437
           WholePoolIndicator <WhlPoolInd> [0..1] Indicator 1437
           PriceSource <PricSrc> [0..1] Text 1437
           PriceRange <PricRg> [0..1] ± 1438
         Derivative <Deriv> [0..1]  1438
           Future <Futr> [0..1]  1442
             ContractSize <CtrctSz> [0..1] Rate 1444
             ExercisePrice <ExrcPric> [0..1]  1444
               ValueType <ValTp> [0..1] CodeSet 1444
               Value <Val> [1..1] ± 1445
               PriceType <PricTp> [0..1] CodeSet 1445
             FutureDate <FutrDt> [0..1] DateTime 1446
             MinimumSize <MinSz> [0..1] Amount C1, C5 1446
             UnitOfMeasure <UnitOfMeasr> [0..1]  1447
{Or               Code <Cd> [1..1] CodeSet 1447
Or}               Proprietary <Prtry> [1..1] ± 1449
             TimeUnit <TmUnit> [0..1]  1449
{Or               Code <Cd> [1..1] CodeSet 1450
Or}               Proprietary <Prtry> [1..1] ± 1450
             AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1450
               AllocationPercentage <AllcnPctg> [0..1] Rate 1452
               Quantity <Qty> [0..1]  1452
{Or                 Unit <Unit> [1..1] Quantity 1452
Or}                 FaceAmount <FaceAmt> [1..1] Amount C1, C5 1452
               SettlementType <SttlmTp> [0..1]  1452
{Or                 Code <Cd> [1..1] CodeSet 1453
Or}                 Proprietary <Prtry> [1..1] ± 1453
               CashAmount <CshAmt> [0..1] Amount C1, C5 1453
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 925 August 2026
```

## File page 926

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               CashType <CshTp> [0..1] Text 1454
               Price <Pric> [0..1]  1454
                 ValueType <ValTp> [0..1] CodeSet 1454
                 Value <Val> [1..1] ± 1455
                 PriceType <PricTp> [0..1] CodeSet 1455
               DirtyPrice <DrtyPric> [0..1]  1456
                 ValueType <ValTp> [0..1] CodeSet 1456
                 Value <Val> [1..1] ± 1457
                 PriceType <PricTp> [0..1] CodeSet 1457
               EndPrice <EndPric> [0..1]  1458
                 ValueType <ValTp> [0..1] CodeSet 1458
                 Value <Val> [1..1] ± 1459
                 PriceType <PricTp> [0..1] CodeSet 1459
               StartValue <StartVal> [0..1] Amount C1, C5 1460
               CurrentValue <CurVal> [0..1] Amount C1, C5 1460
               EndValue <EndVal> [0..1] Amount C1, C5 1461
               AdjustedQuantity <AdjstdQty> [0..1]  1461
{Or                 Unit <Unit> [1..1] Quantity 1461
Or}                 FaceAmount <FaceAmt> [1..1] Amount C1, C5 1462
               ExchangeRate <XchgRate> [0..1] Rate 1462
               CapValue <CapVal> [0..1] Amount C1, C5 1462
           Option <Optn> [0..1]  1462
             OptionSettlementStyle <OptnSttlmStyle> [0..1]  1466
{Or               Code <Cd> [0..*] CodeSet 1466
Or}               Proprietary <Prtry> [1..1] ± 1466
             ConversionDate <ConvsDt> [0..1] DateTime 1466
             StrikePrice <StrkPric> [0..1]  1466
               ValueType <ValTp> [0..1] CodeSet 1467
               Value <Val> [1..1] ± 1467
               PriceType <PricTp> [0..1] CodeSet 1468
             MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1468
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 926 August 2026
```

## File page 927

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             ConversionPeriod <ConvsPrd> [0..1]  1469
{Or               FromDateTime <FrDtTm> [1..1] DateTime 1469
Or               ToDateTime <ToDtTm> [1..1] DateTime 1469
Or}               DateTimeRange <DtTmRg> [1..1] ± 1469
             OptionStyle <OptnStyle> [0..1]  1470
{Or               Code <Cd> [1..1] CodeSet 1470
Or}               Proprietary <Prtry> [1..1] ± 1470
             OptionType <OptnTp> [0..1] ± 1470
             StrikeValue <StrkVal> [0..1] Quantity 1471
             StrikeMultiplier <StrkMltplr> [0..1] Quantity 1471
             InstrumentAssignmentMethod
<InstrmAssgnmtMtd>
[0..1]  1471
{Or               Code <Cd> [1..1] CodeSet 1471
Or}               Proprietary <Prtry> [1..1] ± 1471
             VersionNumber <VrsnNb> [0..1] Quantity 1472
             ExpiryLocation <XpryLctn> [0..1] Text 1472
             Standardisation <Stdstn> [0..1]  1472
{Or               Code <Cd> [1..*] CodeSet 1472
Or}               Proprietary <Prtry> [1..1] ± 1473
             TradingPartyRole <TradgPtyRole> [0..1]  1473
{Or               Code <Cd> [1..*] CodeSet 1473
Or}               Proprietary <Prtry> [1..1] ± 1473
             ContractSize <CtrctSz> [0..1] Rate 1474
             AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1474
               AllocationPercentage <AllcnPctg> [0..1] Rate 1476
               Quantity <Qty> [0..1]  1476
{Or                 Unit <Unit> [1..1] Quantity 1476
Or}                 FaceAmount <FaceAmt> [1..1] Amount C1, C5 1476
               SettlementType <SttlmTp> [0..1]  1476
{Or                 Code <Cd> [1..1] CodeSet 1477
Or}                 Proprietary <Prtry> [1..1] ± 1477
               CashAmount <CshAmt> [0..1] Amount C1, C5 1477
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 927 August 2026
```

## File page 928

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               CashType <CshTp> [0..1] Text 1478
               Price <Pric> [0..1]  1478
                 ValueType <ValTp> [0..1] CodeSet 1478
                 Value <Val> [1..1] ± 1479
                 PriceType <PricTp> [0..1] CodeSet 1479
               DirtyPrice <DrtyPric> [0..1]  1480
                 ValueType <ValTp> [0..1] CodeSet 1480
                 Value <Val> [1..1] ± 1481
                 PriceType <PricTp> [0..1] CodeSet 1481
               EndPrice <EndPric> [0..1]  1482
                 ValueType <ValTp> [0..1] CodeSet 1482
                 Value <Val> [1..1] ± 1483
                 PriceType <PricTp> [0..1] CodeSet 1483
               StartValue <StartVal> [0..1] Amount C1, C5 1484
               CurrentValue <CurVal> [0..1] Amount C1, C5 1484
               EndValue <EndVal> [0..1] Amount C1, C5 1485
               AdjustedQuantity <AdjstdQty> [0..1]  1485
{Or                 Unit <Unit> [1..1] Quantity 1485
Or}                 FaceAmount <FaceAmt> [1..1] Amount C1, C5 1486
               ExchangeRate <XchgRate> [0..1] Rate 1486
               CapValue <CapVal> [0..1] Amount C1, C5 1486
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*]  1486
         SecurityStatus <SctySts> [0..1]  1495
{Or           Code <Cd> [1..1] CodeSet 1495
Or}           Proprietary <Prtry> [1..1] ± 1496
         ISOSecurityLongName <ISOSctyLngNm> [0..1] Text 1496
         ISOSecurityShortName <ISOSctyShrtNm> [0..1] Text 1496
         NameValidFrom <NmVldFr> [0..1] ± 1496
         DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 1496
         CertificateNumber <CertNb> [0..1] Text 1497
         ContractVersionNumber <CtrctVrsnNb> [0..1] Quantity 1497
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 928 August 2026
```

