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
file_pages: [991, 992, 993, 994, 995, 996, 997]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# Continuation at file page 991

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 991 to 997.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 991

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       CouponAttachedNumber <CpnAttchdNb> [0..1] Text 1497
       TaxLotNumber <TaxLotNb> [0..1] Text 1497
       PoolNumber <PoolNb> [0..1] Text 1497
       CoveredIndicator <CvrdInd> [0..1] Indicator 1497
       LegalRestrictions <LglRstrctns> [0..1]  1498
{Or         Code <Cd> [1..1] CodeSet 1498
Or}         Proprietary <Prtry> [1..1] ± 1498
       PositionLimit <PosLmt> [0..1] ± 1498
       NearTermPositionLimit <NearTermPosLmt> [0..1] ± 1499
       ListingDate <ListgDt> [0..1] Date 1499
       RecordDate <RcrdDt> [0..1] DateTime 1499
       ExpiryDate <XpryDt> [0..1] Date 1499
       Purpose <Purp> [0..1] Text 1499
       ClassificationType <ClssfctnTp> [0..1]  1499
         ClassificationFinancialInstrument
<ClssfctnFinInstrm>
[0..1] IdentifierSet 1500
         FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 1500
         AlternateClassification <AltrnClssfctn> [0..*] ± 1500
       Issuance <Issnc> [0..1]  1500
         IssuePlace <IssePlc> [0..1] IdentifierSet 1502
         CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 1502
         IssueDate <IsseDt> [0..1] Date 1502
         AnnouncementDate <AnncmntDt> [0..1] DateTime 1502
         ISINValidFrom <ISINVldFr> [0..1] Date 1502
         IssuerOrganisation <IssrOrg> [0..1]  1502
           Name <Nm> [1..1] Text 1503
           Identification <Id> [0..1]  1503
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1503
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1504
           Purpose <Purp> [0..1] Text 1504
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1504
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1504
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 991 August 2026
```

## File page 992

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           RegistrationDate <RegnDt> [0..1] Date 1505
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1505
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1505
           PostalAddress <PstlAdr> [1..5] ± C10 1505
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1505
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1506
         IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1506
         FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1506
         IssueSize <IsseSz> [0..1] Quantity 1507
         IssuePrice <IssePric> [0..1] ± 1507
         IssuanceDistribution <IssncDstrbtn> [0..1]  1507
{Or           Code <Cd> [1..1] CodeSet 1508
Or}           Proprietary <Prtry> [1..1] ± 1508
         GoverningLaw <GovngLaw> [0..*]  1508
           Identification <Id> [0..1] Text 1508
           Country <Ctry> [0..1] CodeSet C4 1508
       TradingMarket <TradgMkt> [0..*]  1509
         MarketIdentification <MktId> [0..1] IdentifierSet 1509
         RoundLot <RndLot> [0..1] ± 1509
         TradeLotSize <TradLotSz> [0..1] ± 1510
         SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1510
         MinimumTradedNominalQuantity
<MinTraddNmnlQty>
[0..1]  1510
{Or           Unit <Unit> [1..1] Quantity 1510
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1510
         MaximumTradedNominalQuantity
<MaxTraddNmnlQty>
[0..1]  1511
{Or           Unit <Unit> [1..1] Quantity 1511
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1511
         MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 1512
         PrimaryPlaceOfListingIdentification
<PmryPlcOfListgId>
[0..1] IdentifierSet 1512
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 992 August 2026
```

## File page 993

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SpreadAndBenchmarkCurve <SprdAndBchmkCrv> [0..*]  1512
         Spread <Sprd> [0..1] Quantity 1512
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
{Or           Code <Cd> [1..1] CodeSet 1516
Or}           Proprietary <Prtry> [1..1] ± 1517
         BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 1518
       PutType <PutTp> [0..1]  1518
{Or         Code <Cd> [1..1] CodeSet 1518
Or}         Proprietary <Prtry> [1..1] ± 1518
       CallType <CallTp> [0..1]  1519
{Or         Code <Cd> [1..1] CodeSet 1519
Or}         Proprietary <Prtry> [1..1] ± 1519
       FungibleIndicator <FngbInd> [0..1] Indicator 1519
       Confidential <Cnfdtl> [0..1] Indicator 1520
       PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 1520
       ConvertibleIndicator <ConvtblInd> [0..1] Indicator 1520
       ConversionPeriod <ConvsPrd> [0..1] ± 1520
       ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 1521
       ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 1521
       PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 1521
       TradingMethod <TradgMtd> [0..1]  1521
{Or         Unit <Unit> [1..1] Quantity 1522
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1522
       TEFRARule <TEFRARule> [0..1]  1522
{Or         Code <Cd> [1..1] CodeSet 1522
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 993 August 2026
```

## File page 994

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Proprietary <Prtry> [1..1] ± 1523
       SerieNumber <SrNb> [0..1] Text 1523
       Class <Clss> [0..1] Text 1523
       WithholdingTaxRegime <WhldgTaxRgm> [0..*]  1523
         WithholdingTaxValue <WhldgTaxVal> [1..1] ± 1523
         Country <Ctry> [1..1] CodeSet C4 1524
       PaymentStatus <PmtSts> [0..1] ± 1524
       InitialPhysicalForm <InitlPhysForm> [0..1]  1524
{Or         Code <Cd> [1..1] CodeSet 1525
Or}         Proprietary <Prtry> [1..1] ± 1525
       AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  1525
{Or         Code <Cd> [1..1] CodeSet 1525
Or}         Proprietary <Prtry> [1..1] ± 1526
       CommonSafekeeper <CmonSfkpr> [0..1]  1526
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1526
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1526
       RedemptionType <RedTp> [0..1]  1527
{Or         Code <Cd> [1..1] CodeSet 1527
Or}         Proprietary <Prtry> [1..1] ± 1527
       RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 1528
       Restriction <Rstrctn> [0..*]  1528
         EffectivePeriod <FctvPrd> [0..1] ± 1529
         RestrictionType <RstrctnTp> [0..1]  1529
{Or           RestrictionType <RstrctnTp> [1..1] CodeSet 1530
Or}           ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1530
         LegalRestrictionType <LglRstrctnTp> [0..1]  1530
{Or           Code <Cd> [1..1] CodeSet 1530
Or}           Proprietary <Prtry> [1..1] ± 1531
         InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1531
{Or           Code <Cd> [1..1] CodeSet 1531
Or}           Proprietary <Prtry> [1..1] ± 1532
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 994 August 2026
```

## File page 995

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         InvestorType <InvstrTp> [0..*]  1532
{Or           Code <Cd> [1..1] CodeSet 1532
Or}           Proprietary <Prtry> [1..1] ± 1532
       FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C6, C7,
C8, C9,
C12
1533
       SettlementInformation <SttlmInf> [0..*]  1534
         SecuritiesQuantityType <SctiesQtyTp> [0..1]  1534
{Or           Code <Cd> [1..1] CodeSet 1534
Or}           Proprietary <Prtry> [1..1] ± 1535
         ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 1535
         MinimumDenomination <MinDnmtn> [0..1] ± 1535
         MinimumMultipleQuantity <MinMltplQty> [0..1] ± 1535
         DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 1536
       FinancialInstrumentForm <FinInstrmForm> [0..1]  1536
         BookingAppearance <BookgApprnc> [0..1]  1536
{Or           Code <Cd> [1..1] CodeSet 1537
Or}           Proprietary <Prtry> [1..1] ± 1537
         LegalForm <LglForm> [0..1] ± 1537
       ContactName <CtctNm> [0..1]  1538
         Name <Nm> [1..1] Text 1538
         Identification <Id> [0..1]  1538
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1539
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1539
         Purpose <Purp> [0..1] Text 1539
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1539
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1540
         RegistrationDate <RegnDt> [0..1] Date 1540
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1540
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1540
         PostalAddress <PstlAdr> [1..5] ± C10 1540
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1541
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 995 August 2026
```

## File page 996

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1541
       LeadManager <LeadMgr> [0..1]  1542
         Name <Nm> [1..1] Text 1542
         Identification <Id> [0..1]  1543
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1543
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1543
         Purpose <Purp> [0..1] Text 1543
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1544
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1544
         RegistrationDate <RegnDt> [0..1] Date 1544
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1544
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1544
         PostalAddress <PstlAdr> [1..5] ± C10 1544
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1545
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1545
       PrincipalPayingAgent <PrncplPngAgt> [0..1]  1546
         Name <Nm> [1..1] Text 1546
         Identification <Id> [0..1]  1547
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1547
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1547
         Purpose <Purp> [0..1] Text 1547
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1548
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1548
         RegistrationDate <RegnDt> [0..1] Date 1548
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1548
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1548
         PostalAddress <PstlAdr> [1..5] ± C10 1548
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1549
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1549
       PayingAgent <PngAgt> [0..1]  1550
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 996 August 2026
```

## File page 997

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Name <Nm> [1..1] Text 1550
         Identification <Id> [0..1]  1551
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1551
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1551
         Purpose <Purp> [0..1] Text 1551
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1552
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1552
         RegistrationDate <RegnDt> [0..1] Date 1552
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1552
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1552
         PostalAddress <PstlAdr> [1..5] ± C10 1552
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1553
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1553
       Depository <Dpstry> [0..1]  1554
         Name <Nm> [1..1] Text 1554
         Identification <Id> [0..1]  1555
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1555
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1555
         Purpose <Purp> [0..1] Text 1555
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1556
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1556
         RegistrationDate <RegnDt> [0..1] Date 1556
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1556
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1556
         PostalAddress <PstlAdr> [1..5] ± C10 1556
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1557
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1557
       UnderlyingRisk <UndrlygRsk> [0..1]  1558
         Name <Nm> [1..1] Text 1558
         Identification <Id> [0..1]  1559
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1559
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 997 August 2026
```

