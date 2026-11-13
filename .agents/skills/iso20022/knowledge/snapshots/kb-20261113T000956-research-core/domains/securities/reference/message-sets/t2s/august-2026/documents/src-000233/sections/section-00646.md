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
file_pages: [876, 877, 878, 879, 880, 881, 882, 883, 884, 885]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# Continuation at file page 876

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 876 to 885.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 876

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 1622
           AutoReinvestment <AutoRinvstmt> [0..1] Rate 1623
           Haircut <Hrcut> [0..1] Rate 1623
           TransactionConditions <TxConds> [0..1] ± 1623
           LookBack <LookBck> [0..1] Quantity 1623
           MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1623
           MinimumIncrement <MinIncrmt> [0..1] ± 1623
           MinimumQuantity <MinQty> [0..1] ± 1624
           Production <Pdctn> [0..1] Text 1624
           RestrictedIndicator <RstrctdInd> [0..1] Indicator 1624
           PriceFrequency <PricFrqcy> [0..1] ± 1624
           Sector <Sctr> [0..1] Text 1625
           SubstitutionFrequency <SbstitnFrqcy> [0..1] ± 1625
           SubstitutionLeft <SbstitnLft> [0..1] Quantity 1625
           WholePoolIndicator <WhlPoolInd> [0..1] Indicator 1625
           PriceSource <PricSrc> [0..1] Text 1625
           PriceRange <PricRg> [0..1] ± 1626
         Derivative <Deriv> [0..1]  1626
           Future <Futr> [0..1]  1630
             ContractSize <CtrctSz> [0..1] Rate 1632
             ExercisePrice <ExrcPric> [0..1]  1632
               ValueType <ValTp> [0..1] CodeSet 1632
               Value <Val> [1..1] ± 1633
               PriceType <PricTp> [0..1] CodeSet 1633
             FutureDate <FutrDt> [0..1] DateTime 1634
             MinimumSize <MinSz> [0..1] Amount C1, C5 1634
             UnitOfMeasure <UnitOfMeasr> [0..1]  1635
{Or               Code <Cd> [1..1] CodeSet 1635
Or}               Proprietary <Prtry> [1..1] ± 1637
             TimeUnit <TmUnit> [0..1]  1637
{Or               Code <Cd> [1..1] CodeSet 1638
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 876 August 2026
```

## File page 877

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}               Proprietary <Prtry> [1..1] ± 1638
             AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1638
               AllocationPercentage <AllcnPctg> [0..1] Rate 1640
               Quantity <Qty> [0..1]  1640
{Or                 Unit <Unit> [1..1] Quantity 1640
Or}                 FaceAmount <FaceAmt> [1..1] Amount C1, C5 1640
               SettlementType <SttlmTp> [0..1]  1640
{Or                 Code <Cd> [1..1] CodeSet 1641
Or}                 Proprietary <Prtry> [1..1] ± 1641
               CashAmount <CshAmt> [0..1] Amount C1, C5 1641
               CashType <CshTp> [0..1] Text 1642
               Price <Pric> [0..1]  1642
                 ValueType <ValTp> [0..1] CodeSet 1642
                 Value <Val> [1..1] ± 1643
                 PriceType <PricTp> [0..1] CodeSet 1643
               DirtyPrice <DrtyPric> [0..1]  1644
                 ValueType <ValTp> [0..1] CodeSet 1644
                 Value <Val> [1..1] ± 1645
                 PriceType <PricTp> [0..1] CodeSet 1645
               EndPrice <EndPric> [0..1]  1646
                 ValueType <ValTp> [0..1] CodeSet 1646
                 Value <Val> [1..1] ± 1647
                 PriceType <PricTp> [0..1] CodeSet 1647
               StartValue <StartVal> [0..1] Amount C1, C5 1648
               CurrentValue <CurVal> [0..1] Amount C1, C5 1648
               EndValue <EndVal> [0..1] Amount C1, C5 1649
               AdjustedQuantity <AdjstdQty> [0..1]  1649
{Or                 Unit <Unit> [1..1] Quantity 1649
Or}                 FaceAmount <FaceAmt> [1..1] Amount C1, C5 1650
               ExchangeRate <XchgRate> [0..1] Rate 1650
               CapValue <CapVal> [0..1] Amount C1, C5 1650
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 877 August 2026
```

## File page 878

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Option <Optn> [0..1]  1650
             OptionSettlementStyle <OptnSttlmStyle> [0..1]  1654
{Or               Code <Cd> [0..*] CodeSet 1654
Or}               Proprietary <Prtry> [1..1] ± 1654
             ConversionDate <ConvsDt> [0..1] DateTime 1654
             StrikePrice <StrkPric> [0..1]  1654
               ValueType <ValTp> [0..1] CodeSet 1655
               Value <Val> [1..1] ± 1655
               PriceType <PricTp> [0..1] CodeSet 1656
             MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1656
             ConversionPeriod <ConvsPrd> [0..1]  1657
{Or               FromDateTime <FrDtTm> [1..1] DateTime 1657
Or               ToDateTime <ToDtTm> [1..1] DateTime 1657
Or}               DateTimeRange <DtTmRg> [1..1] ± 1657
             OptionStyle <OptnStyle> [0..1]  1658
{Or               Code <Cd> [1..1] CodeSet 1658
Or}               Proprietary <Prtry> [1..1] ± 1658
             OptionType <OptnTp> [0..1] ± 1658
             StrikeValue <StrkVal> [0..1] Quantity 1659
             StrikeMultiplier <StrkMltplr> [0..1] Quantity 1659
             InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1659
{Or               Code <Cd> [1..1] CodeSet 1659
Or}               Proprietary <Prtry> [1..1] ± 1659
             VersionNumber <VrsnNb> [0..1] Quantity 1660
             ExpiryLocation <XpryLctn> [0..1] Text 1660
             Standardisation <Stdstn> [0..1]  1660
{Or               Code <Cd> [1..*] CodeSet 1660
Or}               Proprietary <Prtry> [1..1] ± 1661
             TradingPartyRole <TradgPtyRole> [0..1]  1661
{Or               Code <Cd> [1..*] CodeSet 1661
Or}               Proprietary <Prtry> [1..1] ± 1661
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 878 August 2026
```

## File page 879

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             ContractSize <CtrctSz> [0..1] Rate 1662
             AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1662
               AllocationPercentage <AllcnPctg> [0..1] Rate 1664
               Quantity <Qty> [0..1]  1664
{Or                 Unit <Unit> [1..1] Quantity 1664
Or}                 FaceAmount <FaceAmt> [1..1] Amount C1, C5 1664
               SettlementType <SttlmTp> [0..1]  1664
{Or                 Code <Cd> [1..1] CodeSet 1665
Or}                 Proprietary <Prtry> [1..1] ± 1665
               CashAmount <CshAmt> [0..1] Amount C1, C5 1665
               CashType <CshTp> [0..1] Text 1666
               Price <Pric> [0..1]  1666
                 ValueType <ValTp> [0..1] CodeSet 1666
                 Value <Val> [1..1] ± 1667
                 PriceType <PricTp> [0..1] CodeSet 1667
               DirtyPrice <DrtyPric> [0..1]  1668
                 ValueType <ValTp> [0..1] CodeSet 1668
                 Value <Val> [1..1] ± 1669
                 PriceType <PricTp> [0..1] CodeSet 1669
               EndPrice <EndPric> [0..1]  1670
                 ValueType <ValTp> [0..1] CodeSet 1670
                 Value <Val> [1..1] ± 1671
                 PriceType <PricTp> [0..1] CodeSet 1671
               StartValue <StartVal> [0..1] Amount C1, C5 1672
               CurrentValue <CurVal> [0..1] Amount C1, C5 1672
               EndValue <EndVal> [0..1] Amount C1, C5 1673
               AdjustedQuantity <AdjstdQty> [0..1]  1673
{Or                 Unit <Unit> [1..1] Quantity 1673
Or}                 FaceAmount <FaceAmt> [1..1] Amount C1, C5 1674
               ExchangeRate <XchgRate> [0..1] Rate 1674
               CapValue <CapVal> [0..1] Amount C1, C5 1674
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 879 August 2026
```

## File page 880

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*]  1674
         SecurityStatus <SctySts> [0..1]  1683
{Or           Code <Cd> [1..1] CodeSet 1683
Or}           Proprietary <Prtry> [1..1] ± 1684
         ISOSecurityLongName <ISOSctyLngNm> [0..1] Text 1684
         ISOSecurityShortName <ISOSctyShrtNm> [0..1] Text 1684
         NameValidFrom <NmVldFr> [0..1] ± 1684
         DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 1684
         CertificateNumber <CertNb> [0..1] Text 1685
         ContractVersionNumber <CtrctVrsnNb> [0..1] Quantity 1685
         CouponAttachedNumber <CpnAttchdNb> [0..1] Text 1685
         TaxLotNumber <TaxLotNb> [0..1] Text 1685
         PoolNumber <PoolNb> [0..1] Text 1685
         CoveredIndicator <CvrdInd> [0..1] Indicator 1685
         LegalRestrictions <LglRstrctns> [0..1]  1686
{Or           Code <Cd> [1..1] CodeSet 1686
Or}           Proprietary <Prtry> [1..1] ± 1686
         PositionLimit <PosLmt> [0..1] ± 1686
         NearTermPositionLimit <NearTermPosLmt> [0..1] ± 1687
         ListingDate <ListgDt> [0..1] Date 1687
         RecordDate <RcrdDt> [0..1] DateTime 1687
         ExpiryDate <XpryDt> [0..1] Date 1687
         Purpose <Purp> [0..1] Text 1687
         ClassificationType <ClssfctnTp> [0..1]  1687
           ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 1688
           FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 1688
           AlternateClassification <AltrnClssfctn> [0..*] ± 1688
         Issuance <Issnc> [0..1]  1688
           IssuePlace <IssePlc> [0..1] IdentifierSet 1690
           CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 1690
           IssueDate <IsseDt> [0..1] Date 1690
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 880 August 2026
```

## File page 881

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           AnnouncementDate <AnncmntDt> [0..1] DateTime 1690
           ISINValidFrom <ISINVldFr> [0..1] Date 1690
           IssuerOrganisation <IssrOrg> [0..1]  1690
             Name <Nm> [1..1] Text 1691
             Identification <Id> [0..1]  1691
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1691
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1692
             Purpose <Purp> [0..1] Text 1692
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1692
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1692
             RegistrationDate <RegnDt> [0..1] Date 1693
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1693
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1693
             PostalAddress <PstlAdr> [1..5] ± C10 1693
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1693
             SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1694
           IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1694
           FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1694
           IssueSize <IsseSz> [0..1] Quantity 1695
           IssuePrice <IssePric> [0..1] ± 1695
           IssuanceDistribution <IssncDstrbtn> [0..1]  1695
{Or             Code <Cd> [1..1] CodeSet 1696
Or}             Proprietary <Prtry> [1..1] ± 1696
           GoverningLaw <GovngLaw> [0..*]  1696
             Identification <Id> [0..1] Text 1696
             Country <Ctry> [0..1] CodeSet C4 1696
         TradingMarket <TradgMkt> [0..*]  1697
           MarketIdentification <MktId> [0..1] IdentifierSet 1697
           RoundLot <RndLot> [0..1] ± 1697
           TradeLotSize <TradLotSz> [0..1] ± 1698
           SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1698
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 881 August 2026
```

## File page 882

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           MinimumTradedNominalQuantity <MinTraddNmnlQty> [0..1]  1698
{Or             Unit <Unit> [1..1] Quantity 1698
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1698
           MaximumTradedNominalQuantity <MaxTraddNmnlQty> [0..1]  1699
{Or             Unit <Unit> [1..1] Quantity 1699
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1699
           MinimumTradingPricingIncrement <MinTradgPricgIncrmt> [0..1] Quantity 1700
           PrimaryPlaceOfListingIdentification <PmryPlcOfListgId> [0..1] IdentifierSet 1700
         SpreadAndBenchmarkCurve <SprdAndBchmkCrv> [0..*]  1700
           Spread <Sprd> [0..1] Quantity 1700
           BenchmarkIdentification <BchmkId> [0..1] ± C6, C7,
C8, C9,
C12
1701
           BenchmarkPrice <BchmkPric> [0..1]  1702
             ValueType <ValTp> [0..1] CodeSet 1702
             Value <Val> [1..1] ± 1703
             PriceType <PricTp> [0..1] CodeSet 1703
           BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 1704
           BenchmarkCurveName <BchmkCrvNm> [0..1]  1704
{Or             Code <Cd> [1..1] CodeSet 1704
Or}             Proprietary <Prtry> [1..1] ± 1705
           BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 1706
         PutType <PutTp> [0..1]  1706
{Or           Code <Cd> [1..1] CodeSet 1706
Or}           Proprietary <Prtry> [1..1] ± 1706
         CallType <CallTp> [0..1]  1707
{Or           Code <Cd> [1..1] CodeSet 1707
Or}           Proprietary <Prtry> [1..1] ± 1707
         FungibleIndicator <FngbInd> [0..1] Indicator 1707
         Confidential <Cnfdtl> [0..1] Indicator 1708
         PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 1708
         ConvertibleIndicator <ConvtblInd> [0..1] Indicator 1708
         ConversionPeriod <ConvsPrd> [0..1] ± 1708
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 882 August 2026
```

## File page 883

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 1709
         ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 1709
         PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 1709
         TradingMethod <TradgMtd> [0..1]  1709
{Or           Unit <Unit> [1..1] Quantity 1710
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1710
         TEFRARule <TEFRARule> [0..1]  1710
{Or           Code <Cd> [1..1] CodeSet 1710
Or}           Proprietary <Prtry> [1..1] ± 1711
         SerieNumber <SrNb> [0..1] Text 1711
         Class <Clss> [0..1] Text 1711
         WithholdingTaxRegime <WhldgTaxRgm> [0..*]  1711
           WithholdingTaxValue <WhldgTaxVal> [1..1] ± 1711
           Country <Ctry> [1..1] CodeSet C4 1712
         PaymentStatus <PmtSts> [0..1] ± 1712
         InitialPhysicalForm <InitlPhysForm> [0..1]  1712
{Or           Code <Cd> [1..1] CodeSet 1713
Or}           Proprietary <Prtry> [1..1] ± 1713
         AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  1713
{Or           Code <Cd> [1..1] CodeSet 1713
Or}           Proprietary <Prtry> [1..1] ± 1714
         CommonSafekeeper <CmonSfkpr> [0..1]  1714
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1714
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1714
         RedemptionType <RedTp> [0..1]  1715
{Or           Code <Cd> [1..1] CodeSet 1715
Or}           Proprietary <Prtry> [1..1] ± 1715
         RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 1716
         Restriction <Rstrctn> [0..*]  1716
           EffectivePeriod <FctvPrd> [0..1] ± 1717
           RestrictionType <RstrctnTp> [0..1]  1717
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 883 August 2026
```

## File page 884

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or             RestrictionType <RstrctnTp> [1..1] CodeSet 1718
Or}             ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1718
           LegalRestrictionType <LglRstrctnTp> [0..1]  1718
{Or             Code <Cd> [1..1] CodeSet 1718
Or}             Proprietary <Prtry> [1..1] ± 1719
           InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1719
{Or             Code <Cd> [1..1] CodeSet 1719
Or}             Proprietary <Prtry> [1..1] ± 1720
           InvestorType <InvstrTp> [0..*]  1720
{Or             Code <Cd> [1..1] CodeSet 1720
Or}             Proprietary <Prtry> [1..1] ± 1720
         FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C6, C7,
C8, C9,
C12
1721
         SettlementInformation <SttlmInf> [0..*]  1722
           SecuritiesQuantityType <SctiesQtyTp> [0..1]  1722
{Or             Code <Cd> [1..1] CodeSet 1722
Or}             Proprietary <Prtry> [1..1] ± 1723
           ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 1723
           MinimumDenomination <MinDnmtn> [0..1] ± 1723
           MinimumMultipleQuantity <MinMltplQty> [0..1] ± 1723
           DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 1724
         FinancialInstrumentForm <FinInstrmForm> [0..1]  1724
           BookingAppearance <BookgApprnc> [0..1]  1724
{Or             Code <Cd> [1..1] CodeSet 1725
Or}             Proprietary <Prtry> [1..1] ± 1725
           LegalForm <LglForm> [0..1] ± 1725
         ContactName <CtctNm> [0..1]  1726
           Name <Nm> [1..1] Text 1726
           Identification <Id> [0..1]  1726
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1727
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1727
           Purpose <Purp> [0..1] Text 1727
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 884 August 2026
```

## File page 885

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1727
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1728
           RegistrationDate <RegnDt> [0..1] Date 1728
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1728
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1728
           PostalAddress <PstlAdr> [1..5] ± C10 1728
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1729
           SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1729
         LeadManager <LeadMgr> [0..1]  1730
           Name <Nm> [1..1] Text 1730
           Identification <Id> [0..1]  1731
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1731
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1731
           Purpose <Purp> [0..1] Text 1731
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1732
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1732
           RegistrationDate <RegnDt> [0..1] Date 1732
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1732
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1732
           PostalAddress <PstlAdr> [1..5] ± C10 1732
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1733
           SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1733
         PrincipalPayingAgent <PrncplPngAgt> [0..1]  1734
           Name <Nm> [1..1] Text 1734
           Identification <Id> [0..1]  1735
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1735
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1735
           Purpose <Purp> [0..1] Text 1735
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1736
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1736
           RegistrationDate <RegnDt> [0..1] Date 1736
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 885 August 2026
```

