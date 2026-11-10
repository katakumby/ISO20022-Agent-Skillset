---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.3 SupplementaryData <SplmtryData>"]
file_pages: [1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.3 SupplementaryData <SplmtryData>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1562 to 1571.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1562

```text
SecondaryCommunicationAddress <ScndryComAdr> contains the following elements (see
"CommunicationAddress3" on page 3100 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Email <Email> [0..1] Text 3100
   Phone <Phne> [0..1] Text 3100
   Mobile <Mob> [0..1] Text 3101
   FaxNumber <FaxNb> [0..1] Text 3101
   TelexAddress <TlxAdr> [0..1] Text 3101
   URLAddress <URLAdr> [0..1] Text 3101
28.4.2.1.3.3  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C14 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
28.4.2.2  Replace <Rplc>
Presence: [1..1]
Definition: Request to replace all present data of a security.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1562 August 2026
```

## File page 1563

```text
Replace <Rplc> contains the following SecurityAttributes12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentType <FinInstrmTp> [0..*]  1578
     Equity <Eqty> [0..1]  1586
       PreferenceToIncome <PrefToIncm> [1..1]  1587
{Or         Code <Cd> [1..1] CodeSet 1587
Or}         Proprietary <Prtry> [1..1] ± 1587
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
{Or         Code <Cd> [1..1] CodeSet 1593
Or}         Proprietary <Prtry> [1..1] ± 1593
       WarrantAgent <WarrtAgt> [0..*]  1593
         Name <Nm> [1..1] Text 1594
         Identification <Id> [0..1]  1594
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1594
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1595
         Purpose <Purp> [0..1] Text 1595
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1595
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1595
         RegistrationDate <RegnDt> [0..1] Date 1596
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1596
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1596
         PostalAddress <PstlAdr> [1..5] ± C10 1596
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1596
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1563 August 2026
```

## File page 1564

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1597
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
       PreFundedIndicator <PreFnddInd> [0..1] Indicator 1605
       EscrowedIndicator <EscrwdInd> [0..1] Indicator 1605
       PerpetualIndicator <PerptlInd> [0..1] Indicator 1605
       SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1605
       ExtendibleIndicator <XtndblInd> [0..1] Indicator 1605
       ExtendiblePeriod <XtndblPrd> [0..1]  1606
{Or         FromDateTime <FrDtTm> [1..1] DateTime 1606
Or         ToDateTime <ToDtTm> [1..1] DateTime 1606
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1564 August 2026
```

## File page 1565

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         DateTimeRange <DtTmRg> [1..1] ± 1606
       VariableRateIndicator <VarblRateInd> [0..1] Indicator 1606
       OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1607
       OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1607
       AmortisableIndicator <AmtsblInd> [0..1] Indicator 1607
       InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1607
       CapitalisedInterest <CptlsdIntrst> [0..1]  1607
{Or         Code <Cd> [1..1] CodeSet 1608
Or}         Proprietary <Prtry> [1..1] ± 1608
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
       WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1610
       WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1611
       InsuredIndicator <InsrdInd> [0..1] Indicator 1611
       BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1611
       YieldCalculation <YldClctn> [0..*]  1611
         Value <Val> [1..1] Rate 1612
         CalculationType <ClctnTp> [0..1]  1612
{Or           Code <Cd> [1..1] CodeSet 1612
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1565 August 2026
```

## File page 1566

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 1615
         RedemptionPrice <RedPric> [0..1]  1615
           ValueType <ValTp> [0..1] CodeSet 1615
           Value <Val> [1..1] ± 1616
           PriceType <PricTp> [0..1] CodeSet 1616
         ValueDate <ValDt> [1..1] Date 1617
         ValuePeriod <ValPrd> [1..1]  1617
{Or           FromDateTime <FrDtTm> [1..1] DateTime 1617
Or           ToDateTime <ToDtTm> [1..1] DateTime 1618
Or}           DateTimeRange <DtTmRg> [1..1] ± 1618
         CalculationDate <ClctnDt> [1..1] DateTime 1618
       InterestType <IntrstTp> [0..1] CodeSet 1618
       InstrumentStructureType <InstrmStrTp> [0..1]  1618
{Or         Code <Cd> [1..1] CodeSet 1619
Or}         Proprietary <Prtry> [1..1] ± 1620
       GlobalType <GblTp> [0..1]  1620
{Or         Code <Cd> [1..1] CodeSet 1620
Or}         Proprietary <Prtry> [1..1] ± 1621
       PotentialEuroSystemEligibility
<PotntlEuroSysElgblty>
[0..1] Indicator 1621
       Geographics <Geogcs> [0..1] Text 1621
       YieldRange <YldRg> [0..1] ± 1621
       CouponRange <CpnRg> [0..1] ± 1622
       Purpose <Purp> [0..1] Text 1622
       AlternativeMinimumTaxIndicator
<AltrntvMinTaxInd>
[0..1] Indicator 1622
       AutoReinvestment <AutoRinvstmt> [0..1] Rate 1623
       Haircut <Hrcut> [0..1] Rate 1623
       TransactionConditions <TxConds> [0..1] ± 1623
       LookBack <LookBck> [0..1] Quantity 1623
       MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1623
       MinimumIncrement <MinIncrmt> [0..1] ± 1623
       MinimumQuantity <MinQty> [0..1] ± 1624
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1566 August 2026
```

## File page 1567

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or           Code <Cd> [1..1] CodeSet 1635
Or}           Proprietary <Prtry> [1..1] ± 1637
         TimeUnit <TmUnit> [0..1]  1637
{Or           Code <Cd> [1..1] CodeSet 1638
Or}           Proprietary <Prtry> [1..1] ± 1638
         AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1638
           AllocationPercentage <AllcnPctg> [0..1] Rate 1640
           Quantity <Qty> [0..1]  1640
{Or             Unit <Unit> [1..1] Quantity 1640
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1640
           SettlementType <SttlmTp> [0..1]  1640
{Or             Code <Cd> [1..1] CodeSet 1641
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1567 August 2026
```

## File page 1568

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             Proprietary <Prtry> [1..1] ± 1641
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
{Or             Unit <Unit> [1..1] Quantity 1649
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1650
           ExchangeRate <XchgRate> [0..1] Rate 1650
           CapValue <CapVal> [0..1] Amount C1, C5 1650
       Option <Optn> [0..1]  1650
         OptionSettlementStyle <OptnSttlmStyle> [0..1]  1654
{Or           Code <Cd> [0..*] CodeSet 1654
Or}           Proprietary <Prtry> [1..1] ± 1654
         ConversionDate <ConvsDt> [0..1] DateTime 1654
         StrikePrice <StrkPric> [0..1]  1654
           ValueType <ValTp> [0..1] CodeSet 1655
           Value <Val> [1..1] ± 1655
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1568 August 2026
```

## File page 1569

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           PriceType <PricTp> [0..1] CodeSet 1656
         MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1656
         ConversionPeriod <ConvsPrd> [0..1]  1657
{Or           FromDateTime <FrDtTm> [1..1] DateTime 1657
Or           ToDateTime <ToDtTm> [1..1] DateTime 1657
Or}           DateTimeRange <DtTmRg> [1..1] ± 1657
         OptionStyle <OptnStyle> [0..1]  1658
{Or           Code <Cd> [1..1] CodeSet 1658
Or}           Proprietary <Prtry> [1..1] ± 1658
         OptionType <OptnTp> [0..1] ± 1658
         StrikeValue <StrkVal> [0..1] Quantity 1659
         StrikeMultiplier <StrkMltplr> [0..1] Quantity 1659
         InstrumentAssignmentMethod
<InstrmAssgnmtMtd>
[0..1]  1659
{Or           Code <Cd> [1..1] CodeSet 1659
Or}           Proprietary <Prtry> [1..1] ± 1659
         VersionNumber <VrsnNb> [0..1] Quantity 1660
         ExpiryLocation <XpryLctn> [0..1] Text 1660
         Standardisation <Stdstn> [0..1]  1660
{Or           Code <Cd> [1..*] CodeSet 1660
Or}           Proprietary <Prtry> [1..1] ± 1661
         TradingPartyRole <TradgPtyRole> [0..1]  1661
{Or           Code <Cd> [1..*] CodeSet 1661
Or}           Proprietary <Prtry> [1..1] ± 1661
         ContractSize <CtrctSz> [0..1] Rate 1662
         AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1662
           AllocationPercentage <AllcnPctg> [0..1] Rate 1664
           Quantity <Qty> [0..1]  1664
{Or             Unit <Unit> [1..1] Quantity 1664
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1664
           SettlementType <SttlmTp> [0..1]  1664
{Or             Code <Cd> [1..1] CodeSet 1665
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1569 August 2026
```

## File page 1570

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             Proprietary <Prtry> [1..1] ± 1665
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
{Or             Unit <Unit> [1..1] Quantity 1673
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1674
           ExchangeRate <XchgRate> [0..1] Rate 1674
           CapValue <CapVal> [0..1] Amount C1, C5 1674
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*]  1674
     SecurityStatus <SctySts> [0..1]  1683
{Or       Code <Cd> [1..1] CodeSet 1683
Or}       Proprietary <Prtry> [1..1] ± 1684
     ISOSecurityLongName <ISOSctyLngNm> [0..1] Text 1684
     ISOSecurityShortName <ISOSctyShrtNm> [0..1] Text 1684
     NameValidFrom <NmVldFr> [0..1] ± 1684
     DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 1684
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1570 August 2026
```

## File page 1571

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     CertificateNumber <CertNb> [0..1] Text 1685
     ContractVersionNumber <CtrctVrsnNb> [0..1] Quantity 1685
     CouponAttachedNumber <CpnAttchdNb> [0..1] Text 1685
     TaxLotNumber <TaxLotNb> [0..1] Text 1685
     PoolNumber <PoolNb> [0..1] Text 1685
     CoveredIndicator <CvrdInd> [0..1] Indicator 1685
     LegalRestrictions <LglRstrctns> [0..1]  1686
{Or       Code <Cd> [1..1] CodeSet 1686
Or}       Proprietary <Prtry> [1..1] ± 1686
     PositionLimit <PosLmt> [0..1] ± 1686
     NearTermPositionLimit <NearTermPosLmt> [0..1] ± 1687
     ListingDate <ListgDt> [0..1] Date 1687
     RecordDate <RcrdDt> [0..1] DateTime 1687
     ExpiryDate <XpryDt> [0..1] Date 1687
     Purpose <Purp> [0..1] Text 1687
     ClassificationType <ClssfctnTp> [0..1]  1687
       ClassificationFinancialInstrument
<ClssfctnFinInstrm>
[0..1] IdentifierSet 1688
       FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 1688
       AlternateClassification <AltrnClssfctn> [0..*] ± 1688
     Issuance <Issnc> [0..1]  1688
       IssuePlace <IssePlc> [0..1] IdentifierSet 1690
       CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 1690
       IssueDate <IsseDt> [0..1] Date 1690
       AnnouncementDate <AnncmntDt> [0..1] DateTime 1690
       ISINValidFrom <ISINVldFr> [0..1] Date 1690
       IssuerOrganisation <IssrOrg> [0..1]  1690
         Name <Nm> [1..1] Text 1691
         Identification <Id> [0..1]  1691
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1691
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1692
         Purpose <Purp> [0..1] Text 1692
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1571 August 2026
```

