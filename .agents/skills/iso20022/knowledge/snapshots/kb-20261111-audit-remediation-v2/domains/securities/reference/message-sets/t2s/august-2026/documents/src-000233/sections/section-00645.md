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
file_pages: [866, 867, 868, 869, 870, 871, 872, 873, 874, 875]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# Continuation at file page 866

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 866 to 875.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 866

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               TaxIdentificationNumber <TaxIdNb> [0..1] Text 1505
               NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1505
               PostalAddress <PstlAdr> [1..5] ± C10 1505
               PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1505
               SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1506
             IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1506
             FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1506
             IssueSize <IsseSz> [0..1] Quantity 1507
             IssuePrice <IssePric> [0..1] ± 1507
             IssuanceDistribution <IssncDstrbtn> [0..1]  1507
{Or               Code <Cd> [1..1] CodeSet 1508
Or}               Proprietary <Prtry> [1..1] ± 1508
             GoverningLaw <GovngLaw> [0..*]  1508
               Identification <Id> [0..1] Text 1508
               Country <Ctry> [0..1] CodeSet C4 1508
           TradingMarket <TradgMkt> [0..*]  1509
             MarketIdentification <MktId> [0..1] IdentifierSet 1509
             RoundLot <RndLot> [0..1] ± 1509
             TradeLotSize <TradLotSz> [0..1] ± 1510
             SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1510
             MinimumTradedNominalQuantity <MinTraddNmnlQty> [0..1]  1510
{Or               Unit <Unit> [1..1] Quantity 1510
Or}               FaceAmount <FaceAmt> [1..1] Amount C1, C5 1510
             MaximumTradedNominalQuantity <MaxTraddNmnlQty> [0..1]  1511
{Or               Unit <Unit> [1..1] Quantity 1511
Or}               FaceAmount <FaceAmt> [1..1] Amount C1, C5 1511
             MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 1512
             PrimaryPlaceOfListingIdentification <PmryPlcOfListgId> [0..1] IdentifierSet 1512
           SpreadAndBenchmarkCurve <SprdAndBchmkCrv> [0..*]  1512
             Spread <Sprd> [0..1] Quantity 1512
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 866 August 2026
```

## File page 867

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             BenchmarkIdentification <BchmkId> [0..1] ± C6, C7,
C8, C9,
C12
1513
             BenchmarkPrice <BchmkPric> [0..1]  1514
               ValueType <ValTp> [0..1] CodeSet 1514
               Value <Val> [1..1] ± 1515
               PriceType <PricTp> [0..1] CodeSet 1515
             BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 1516
             BenchmarkCurveName <BchmkCrvNm> [0..1]  1516
{Or               Code <Cd> [1..1] CodeSet 1516
Or}               Proprietary <Prtry> [1..1] ± 1517
             BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 1518
           PutType <PutTp> [0..1]  1518
{Or             Code <Cd> [1..1] CodeSet 1518
Or}             Proprietary <Prtry> [1..1] ± 1518
           CallType <CallTp> [0..1]  1519
{Or             Code <Cd> [1..1] CodeSet 1519
Or}             Proprietary <Prtry> [1..1] ± 1519
           FungibleIndicator <FngbInd> [0..1] Indicator 1519
           Confidential <Cnfdtl> [0..1] Indicator 1520
           PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 1520
           ConvertibleIndicator <ConvtblInd> [0..1] Indicator 1520
           ConversionPeriod <ConvsPrd> [0..1] ± 1520
           ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 1521
           ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 1521
           PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 1521
           TradingMethod <TradgMtd> [0..1]  1521
{Or             Unit <Unit> [1..1] Quantity 1522
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1522
           TEFRARule <TEFRARule> [0..1]  1522
{Or             Code <Cd> [1..1] CodeSet 1522
Or}             Proprietary <Prtry> [1..1] ± 1523
           SerieNumber <SrNb> [0..1] Text 1523
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 867 August 2026
```

## File page 868

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Class <Clss> [0..1] Text 1523
           WithholdingTaxRegime <WhldgTaxRgm> [0..*]  1523
             WithholdingTaxValue <WhldgTaxVal> [1..1] ± 1523
             Country <Ctry> [1..1] CodeSet C4 1524
           PaymentStatus <PmtSts> [0..1] ± 1524
           InitialPhysicalForm <InitlPhysForm> [0..1]  1524
{Or             Code <Cd> [1..1] CodeSet 1525
Or}             Proprietary <Prtry> [1..1] ± 1525
           AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  1525
{Or             Code <Cd> [1..1] CodeSet 1525
Or}             Proprietary <Prtry> [1..1] ± 1526
           CommonSafekeeper <CmonSfkpr> [0..1]  1526
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1526
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1526
           RedemptionType <RedTp> [0..1]  1527
{Or             Code <Cd> [1..1] CodeSet 1527
Or}             Proprietary <Prtry> [1..1] ± 1527
           RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 1528
           Restriction <Rstrctn> [0..*]  1528
             EffectivePeriod <FctvPrd> [0..1] ± 1529
             RestrictionType <RstrctnTp> [0..1]  1529
{Or               RestrictionType <RstrctnTp> [1..1] CodeSet 1530
Or}               ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1530
             LegalRestrictionType <LglRstrctnTp> [0..1]  1530
{Or               Code <Cd> [1..1] CodeSet 1530
Or}               Proprietary <Prtry> [1..1] ± 1531
             InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1531
{Or               Code <Cd> [1..1] CodeSet 1531
Or}               Proprietary <Prtry> [1..1] ± 1532
             InvestorType <InvstrTp> [0..*]  1532
{Or               Code <Cd> [1..1] CodeSet 1532
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 868 August 2026
```

## File page 869

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}               Proprietary <Prtry> [1..1] ± 1532
           FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C6, C7,
C8, C9,
C12
1533
           SettlementInformation <SttlmInf> [0..*]  1534
             SecuritiesQuantityType <SctiesQtyTp> [0..1]  1534
{Or               Code <Cd> [1..1] CodeSet 1534
Or}               Proprietary <Prtry> [1..1] ± 1535
             ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 1535
             MinimumDenomination <MinDnmtn> [0..1] ± 1535
             MinimumMultipleQuantity <MinMltplQty> [0..1] ± 1535
             DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 1536
           FinancialInstrumentForm <FinInstrmForm> [0..1]  1536
             BookingAppearance <BookgApprnc> [0..1]  1536
{Or               Code <Cd> [1..1] CodeSet 1537
Or}               Proprietary <Prtry> [1..1] ± 1537
             LegalForm <LglForm> [0..1] ± 1537
           ContactName <CtctNm> [0..1]  1538
             Name <Nm> [1..1] Text 1538
             Identification <Id> [0..1]  1538
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1539
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1539
             Purpose <Purp> [0..1] Text 1539
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1539
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1540
             RegistrationDate <RegnDt> [0..1] Date 1540
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1540
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1540
             PostalAddress <PstlAdr> [1..5] ± C10 1540
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1541
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1541
           LeadManager <LeadMgr> [0..1]  1542
             Name <Nm> [1..1] Text 1542
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 869 August 2026
```

## File page 870

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Identification <Id> [0..1]  1543
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1543
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1543
             Purpose <Purp> [0..1] Text 1543
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1544
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1544
             RegistrationDate <RegnDt> [0..1] Date 1544
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1544
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1544
             PostalAddress <PstlAdr> [1..5] ± C10 1544
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1545
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1545
           PrincipalPayingAgent <PrncplPngAgt> [0..1]  1546
             Name <Nm> [1..1] Text 1546
             Identification <Id> [0..1]  1547
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1547
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1547
             Purpose <Purp> [0..1] Text 1547
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1548
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1548
             RegistrationDate <RegnDt> [0..1] Date 1548
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1548
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1548
             PostalAddress <PstlAdr> [1..5] ± C10 1548
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1549
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1549
           PayingAgent <PngAgt> [0..1]  1550
             Name <Nm> [1..1] Text 1550
             Identification <Id> [0..1]  1551
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1551
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1551
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 870 August 2026
```

## File page 871

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Purpose <Purp> [0..1] Text 1551
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1552
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1552
             RegistrationDate <RegnDt> [0..1] Date 1552
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1552
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1552
             PostalAddress <PstlAdr> [1..5] ± C10 1552
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1553
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1553
           Depository <Dpstry> [0..1]  1554
             Name <Nm> [1..1] Text 1554
             Identification <Id> [0..1]  1555
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1555
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1555
             Purpose <Purp> [0..1] Text 1555
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1556
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1556
             RegistrationDate <RegnDt> [0..1] Date 1556
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1556
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1556
             PostalAddress <PstlAdr> [1..5] ± C10 1556
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1557
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1557
           UnderlyingRisk <UndrlygRsk> [0..1]  1558
             Name <Nm> [1..1] Text 1558
             Identification <Id> [0..1]  1559
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1559
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1559
             Purpose <Purp> [0..1] Text 1559
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1560
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1560
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 871 August 2026
```

## File page 872

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             RegistrationDate <RegnDt> [0..1] Date 1560
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1560
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1560
             PostalAddress <PstlAdr> [1..5] ± C10 1560
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1561
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1561
         SupplementaryData <SplmtryData> [0..*] ± C14 1562
Or}     Replace <Rplc> [1..1]  1562
       FinancialInstrumentType <FinInstrmTp> [0..*]  1578
         Equity <Eqty> [0..1]  1586
           PreferenceToIncome <PrefToIncm> [1..1]  1587
{Or             Code <Cd> [1..1] CodeSet 1587
Or}             Proprietary <Prtry> [1..1] ± 1587
           MaturityDate <MtrtyDt> [0..1] DateTime 1588
           NonPaidAmount <NonPdAmt> [0..1] Amount C1, C5 1588
           ParValue <ParVal> [0..1] Amount C1, C5 1588
           VotingRightsPerShare <VtngRghtsPerShr> [0..1] Quantity 1589
         Warrant <Warrt> [0..1]  1589
           Multiplier <Mltplr> [0..1] Rate 1590
           SubscriptionPrice <SbcptPric> [0..1]  1590
             ValueType <ValTp> [0..1] CodeSet 1591
             Value <Val> [1..1] ± 1591
             PriceType <PricTp> [0..1] CodeSet 1592
           Type <Tp> [0..1]  1592
{Or             Code <Cd> [1..1] CodeSet 1593
Or}             Proprietary <Prtry> [1..1] ± 1593
           WarrantAgent <WarrtAgt> [0..*]  1593
             Name <Nm> [1..1] Text 1594
             Identification <Id> [0..1]  1594
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1594
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1595
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 872 August 2026
```

## File page 873

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Purpose <Purp> [0..1] Text 1595
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1595
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1595
             RegistrationDate <RegnDt> [0..1] Date 1596
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1596
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1596
             PostalAddress <PstlAdr> [1..5] ± C10 1596
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1596
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1597
         Debt <Debt> [0..1]  C11,
C13
1597
           PaymentCurrency <PmtCcy> [0..1] CodeSet C1 1601
           FaceAmount <FaceAmt> [0..1] Amount C1, C5 1601
           PaymentFrequency <PmtFrqcy> [0..1] ± 1602
           InterestFixingDate <IntrstFxgDt> [0..1] DateTime 1602
           DatedDate <DtdDt> [0..1] DateTime 1602
           FirstPaymentDate <FrstPmtDt> [0..1] DateTime 1602
           MaturityDate <MtrtyDt> [0..1] DateTime 1602
           NextCouponDate <NxtCpnDt> [0..1] DateTime 1602
           PutableDate <PutblDt> [0..1] DateTime 1603
           NextCallableDate <NxtCllblDt> [0..1] DateTime 1603
           NextFactorDate <NxtFctrDt> [0..1] DateTime 1603
           ExpirationDate <XprtnDt> [0..1] DateTime 1603
           PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 1603
           InterestRate <IntrstRate> [0..1] Rate 1603
           NextInterestRate <NxtIntrstRate> [0..1] Rate 1603
           OddCouponIndicator <OddCpnInd> [0..1] Indicator 1603
           CallableIndicator <CllblInd> [0..1] Indicator 1604
           CPProgram <CPPrgm> [0..1] Quantity 1604
           CPRegistrationType <CPRegnTp> [0..1] Text 1604
           InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 1604
           PutableIndicator <PutblInd> [0..1] Indicator 1604
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 873 August 2026
```

## File page 874

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           PreFundedIndicator <PreFnddInd> [0..1] Indicator 1605
           EscrowedIndicator <EscrwdInd> [0..1] Indicator 1605
           PerpetualIndicator <PerptlInd> [0..1] Indicator 1605
           SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1605
           ExtendibleIndicator <XtndblInd> [0..1] Indicator 1605
           ExtendiblePeriod <XtndblPrd> [0..1]  1606
{Or             FromDateTime <FrDtTm> [1..1] DateTime 1606
Or             ToDateTime <ToDtTm> [1..1] DateTime 1606
Or}             DateTimeRange <DtTmRg> [1..1] ± 1606
           VariableRateIndicator <VarblRateInd> [0..1] Indicator 1606
           OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1607
           OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1607
           AmortisableIndicator <AmtsblInd> [0..1] Indicator 1607
           InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1607
           CapitalisedInterest <CptlsdIntrst> [0..1]  1607
{Or             Code <Cd> [1..1] CodeSet 1608
Or}             Proprietary <Prtry> [1..1] ± 1608
           ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1608
           CurrentFactor <CurFctr> [0..1] Rate 1609
           NextFactor <NxtFctr> [0..1] Rate 1609
           PreviousFactor <PrvsFctr> [0..1] Rate 1609
           Pieces <Pcs> [0..1] Quantity 1609
           PoolsMaximum <PlsMax> [0..1] Quantity 1609
           PoolsPerMillion <PlsPerMln> [0..1] Quantity 1609
           PoolsPerLot <PlsPerLot> [0..1] Quantity 1609
           PoolsPerTrade <PlsPerTrad> [0..1] Quantity 1610
           ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 1610
           LotIdentification <LotId> [0..1] Text 1610
           ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 1610
           WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 1610
           WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 1610
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 874 August 2026
```

## File page 875

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1610
           WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1611
           InsuredIndicator <InsrdInd> [0..1] Indicator 1611
           BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1611
           YieldCalculation <YldClctn> [0..*]  1611
             Value <Val> [1..1] Rate 1612
             CalculationType <ClctnTp> [0..1]  1612
{Or               Code <Cd> [1..1] CodeSet 1612
Or}               Proprietary <Prtry> [1..1] ± 1615
             RedemptionPrice <RedPric> [0..1]  1615
               ValueType <ValTp> [0..1] CodeSet 1615
               Value <Val> [1..1] ± 1616
               PriceType <PricTp> [0..1] CodeSet 1616
             ValueDate <ValDt> [1..1] Date 1617
             ValuePeriod <ValPrd> [1..1]  1617
{Or               FromDateTime <FrDtTm> [1..1] DateTime 1617
Or               ToDateTime <ToDtTm> [1..1] DateTime 1618
Or}               DateTimeRange <DtTmRg> [1..1] ± 1618
             CalculationDate <ClctnDt> [1..1] DateTime 1618
           InterestType <IntrstTp> [0..1] CodeSet 1618
           InstrumentStructureType <InstrmStrTp> [0..1]  1618
{Or             Code <Cd> [1..1] CodeSet 1619
Or}             Proprietary <Prtry> [1..1] ± 1620
           GlobalType <GblTp> [0..1]  1620
{Or             Code <Cd> [1..1] CodeSet 1620
Or}             Proprietary <Prtry> [1..1] ± 1621
           PotentialEuroSystemEligibility <PotntlEuroSysElgblty> [0..1] Indicator 1621
           Geographics <Geogcs> [0..1] Text 1621
           YieldRange <YldRg> [0..1] ± 1621
           CouponRange <CpnRg> [0..1] ± 1622
           Purpose <Purp> [0..1] Text 1622
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 875 August 2026
```

