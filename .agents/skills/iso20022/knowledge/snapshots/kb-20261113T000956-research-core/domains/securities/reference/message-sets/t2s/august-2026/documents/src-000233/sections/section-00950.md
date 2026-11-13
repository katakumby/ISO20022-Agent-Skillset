---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>"]
file_pages: [1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1390 to 1397.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1390

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1559
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1559
       Purpose <Purp> [0..1] Text 1559
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1560
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1560
       RegistrationDate <RegnDt> [0..1] Date 1560
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1560
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1560
       PostalAddress <PstlAdr> [1..5] ± C10 1560
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1561
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1561
   SupplementaryData <SplmtryData> [0..*] ± C14 1562
28.4.2.1.3.1  FinancialInstrumentType <FinInstrmTp>
Presence: [0..*]
Definition: Provides additional details about the financial instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1390 August 2026
```

## File page 1391

```text
FinancialInstrumentType <FinInstrmTp> contains the following FinancialInstrument97 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Equity <Eqty> [0..1]  1398
     PreferenceToIncome <PrefToIncm> [1..1]  1399
{Or       Code <Cd> [1..1] CodeSet 1399
Or}       Proprietary <Prtry> [1..1] ± 1399
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
{Or       Code <Cd> [1..1] CodeSet 1405
Or}       Proprietary <Prtry> [1..1] ± 1405
     WarrantAgent <WarrtAgt> [0..*]  1405
       Name <Nm> [1..1] Text 1406
       Identification <Id> [0..1]  1406
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1406
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1407
       Purpose <Purp> [0..1] Text 1407
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1407
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1407
       RegistrationDate <RegnDt> [0..1] Date 1408
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1408
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1408
       PostalAddress <PstlAdr> [1..5] ± C10 1408
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1408
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1391 August 2026
```

## File page 1392

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1409
   Debt <Debt> [0..1]  C11,
C13
1409
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
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1418
Or       ToDateTime <ToDtTm> [1..1] DateTime 1418
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1392 August 2026
```

## File page 1393

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       DateTimeRange <DtTmRg> [1..1] ± 1418
     VariableRateIndicator <VarblRateInd> [0..1] Indicator 1418
     OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1419
     OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1419
     AmortisableIndicator <AmtsblInd> [0..1] Indicator 1419
     InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1419
     CapitalisedInterest <CptlsdIntrst> [0..1]  1419
{Or       Code <Cd> [1..1] CodeSet 1420
Or}       Proprietary <Prtry> [1..1] ± 1420
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
{Or         Code <Cd> [1..1] CodeSet 1424
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1393 August 2026
```

## File page 1394

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Proprietary <Prtry> [1..1] ± 1427
       RedemptionPrice <RedPric> [0..1]  1427
         ValueType <ValTp> [0..1] CodeSet 1427
         Value <Val> [1..1] ± 1428
         PriceType <PricTp> [0..1] CodeSet 1428
       ValueDate <ValDt> [1..1] Date 1429
       ValuePeriod <ValPrd> [1..1]  1429
{Or         FromDateTime <FrDtTm> [1..1] DateTime 1429
Or         ToDateTime <ToDtTm> [1..1] DateTime 1430
Or}         DateTimeRange <DtTmRg> [1..1] ± 1430
       CalculationDate <ClctnDt> [1..1] DateTime 1430
     InterestType <IntrstTp> [0..1] CodeSet 1430
     InstrumentStructureType <InstrmStrTp> [0..1]  1430
{Or       Code <Cd> [1..1] CodeSet 1431
Or}       Proprietary <Prtry> [1..1] ± 1432
     GlobalType <GblTp> [0..1]  1432
{Or       Code <Cd> [1..1] CodeSet 1432
Or}       Proprietary <Prtry> [1..1] ± 1433
     PotentialEuroSystemEligibility
<PotntlEuroSysElgblty>
[0..1] Indicator 1433
     Geographics <Geogcs> [0..1] Text 1433
     YieldRange <YldRg> [0..1] ± 1433
     CouponRange <CpnRg> [0..1] ± 1434
     Purpose <Purp> [0..1] Text 1434
     AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 1434
     AutoReinvestment <AutoRinvstmt> [0..1] Rate 1435
     Haircut <Hrcut> [0..1] Rate 1435
     TransactionConditions <TxConds> [0..1] ± 1435
     LookBack <LookBck> [0..1] Quantity 1435
     MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1435
     MinimumIncrement <MinIncrmt> [0..1] ± 1435
     MinimumQuantity <MinQty> [0..1] ± 1436
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1394 August 2026
```

## File page 1395

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Production <Pdctn> [0..1] Text 1436
     RestrictedIndicator <RstrctdInd> [0..1] Indicator 1436
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
{Or         Code <Cd> [1..1] CodeSet 1447
Or}         Proprietary <Prtry> [1..1] ± 1449
       TimeUnit <TmUnit> [0..1]  1449
{Or         Code <Cd> [1..1] CodeSet 1450
Or}         Proprietary <Prtry> [1..1] ± 1450
       AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1450
         AllocationPercentage <AllcnPctg> [0..1] Rate 1452
         Quantity <Qty> [0..1]  1452
{Or           Unit <Unit> [1..1] Quantity 1452
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1452
         SettlementType <SttlmTp> [0..1]  1452
{Or           Code <Cd> [1..1] CodeSet 1453
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1395 August 2026
```

## File page 1396

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 1453
         CashAmount <CshAmt> [0..1] Amount C1, C5 1453
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
{Or           Unit <Unit> [1..1] Quantity 1461
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1462
         ExchangeRate <XchgRate> [0..1] Rate 1462
         CapValue <CapVal> [0..1] Amount C1, C5 1462
     Option <Optn> [0..1]  1462
       OptionSettlementStyle <OptnSttlmStyle> [0..1]  1466
{Or         Code <Cd> [0..*] CodeSet 1466
Or}         Proprietary <Prtry> [1..1] ± 1466
       ConversionDate <ConvsDt> [0..1] DateTime 1466
       StrikePrice <StrkPric> [0..1]  1466
         ValueType <ValTp> [0..1] CodeSet 1467
         Value <Val> [1..1] ± 1467
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1396 August 2026
```

## File page 1397

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1468
       MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1468
       ConversionPeriod <ConvsPrd> [0..1]  1469
{Or         FromDateTime <FrDtTm> [1..1] DateTime 1469
Or         ToDateTime <ToDtTm> [1..1] DateTime 1469
Or}         DateTimeRange <DtTmRg> [1..1] ± 1469
       OptionStyle <OptnStyle> [0..1]  1470
{Or         Code <Cd> [1..1] CodeSet 1470
Or}         Proprietary <Prtry> [1..1] ± 1470
       OptionType <OptnTp> [0..1] ± 1470
       StrikeValue <StrkVal> [0..1] Quantity 1471
       StrikeMultiplier <StrkMltplr> [0..1] Quantity 1471
       InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1471
{Or         Code <Cd> [1..1] CodeSet 1471
Or}         Proprietary <Prtry> [1..1] ± 1471
       VersionNumber <VrsnNb> [0..1] Quantity 1472
       ExpiryLocation <XpryLctn> [0..1] Text 1472
       Standardisation <Stdstn> [0..1]  1472
{Or         Code <Cd> [1..*] CodeSet 1472
Or}         Proprietary <Prtry> [1..1] ± 1473
       TradingPartyRole <TradgPtyRole> [0..1]  1473
{Or         Code <Cd> [1..*] CodeSet 1473
Or}         Proprietary <Prtry> [1..1] ± 1473
       ContractSize <CtrctSz> [0..1] Rate 1474
       AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1474
         AllocationPercentage <AllcnPctg> [0..1] Rate 1476
         Quantity <Qty> [0..1]  1476
{Or           Unit <Unit> [1..1] Quantity 1476
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1476
         SettlementType <SttlmTp> [0..1]  1476
{Or           Code <Cd> [1..1] CodeSet 1477
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1397 August 2026
```

