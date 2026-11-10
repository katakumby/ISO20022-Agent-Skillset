---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.4 Derivative <Deriv>", "28.4.2.2.1.4.2 Option <Optn>", "28.4.2.2.1.4.2.16 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "28.4.2.2.1.4.2.16.12 AdjustedQuantity <AdjstdQty>", "28.4.2.2.1.4.2.16.12.2 FaceAmount <FaceAmt>"]
file_pages: [1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.4.2.16.12.2 FaceAmount <FaceAmt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1674 to 1682.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1674

```text
Datatype: "DecimalNumber" on page 3324
28.4.2.2.1.4.2.16.12.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, ie, the principal, of a debt
instrument.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
28.4.2.2.1.4.2.16.13  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Foreign exchange rate used to compute the current value.
Datatype: "PercentageRate" on page 3325
28.4.2.2.1.4.2.16.14  CapValue <CapVal>
Presence: [0..1]
Definition: Maximum notional value for a financial instrument that is capped.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
28.4.2.2.2  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..*]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1674 August 2026
```

## File page 1675

```text
Definition: Provides details about the financial instrument attributes of a particular leg.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1675 August 2026
```

## File page 1676

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following
CommonFinancialInstrumentAttributes12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityStatus <SctySts> [0..1]  1683
{Or     Code <Cd> [1..1] CodeSet 1683
Or}     Proprietary <Prtry> [1..1] ± 1684
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
{Or     Code <Cd> [1..1] CodeSet 1686
Or}     Proprietary <Prtry> [1..1] ± 1686
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1676 August 2026
```

## File page 1677

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IssueDate <IsseDt> [0..1] Date 1690
     AnnouncementDate <AnncmntDt> [0..1] DateTime 1690
     ISINValidFrom <ISINVldFr> [0..1] Date 1690
     IssuerOrganisation <IssrOrg> [0..1]  1690
       Name <Nm> [1..1] Text 1691
       Identification <Id> [0..1]  1691
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1691
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1692
       Purpose <Purp> [0..1] Text 1692
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1692
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1692
       RegistrationDate <RegnDt> [0..1] Date 1693
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1693
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1693
       PostalAddress <PstlAdr> [1..5] ± C10 1693
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1693
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1694
     IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1694
     FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1694
     IssueSize <IsseSz> [0..1] Quantity 1695
     IssuePrice <IssePric> [0..1] ± 1695
     IssuanceDistribution <IssncDstrbtn> [0..1]  1695
{Or       Code <Cd> [1..1] CodeSet 1696
Or}       Proprietary <Prtry> [1..1] ± 1696
     GoverningLaw <GovngLaw> [0..*]  1696
       Identification <Id> [0..1] Text 1696
       Country <Ctry> [0..1] CodeSet C4 1696
   TradingMarket <TradgMkt> [0..*]  1697
     MarketIdentification <MktId> [0..1] IdentifierSet 1697
     RoundLot <RndLot> [0..1] ± 1697
     TradeLotSize <TradLotSz> [0..1] ± 1698
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1677 August 2026
```

## File page 1678

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1698
     MinimumTradedNominalQuantity
<MinTraddNmnlQty>
[0..1]  1698
{Or       Unit <Unit> [1..1] Quantity 1698
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1698
     MaximumTradedNominalQuantity
<MaxTraddNmnlQty>
[0..1]  1699
{Or       Unit <Unit> [1..1] Quantity 1699
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1699
     MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 1700
     PrimaryPlaceOfListingIdentification
<PmryPlcOfListgId>
[0..1] IdentifierSet 1700
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
{Or       Code <Cd> [1..1] CodeSet 1704
Or}       Proprietary <Prtry> [1..1] ± 1705
     BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 1706
   PutType <PutTp> [0..1]  1706
{Or     Code <Cd> [1..1] CodeSet 1706
Or}     Proprietary <Prtry> [1..1] ± 1706
   CallType <CallTp> [0..1]  1707
{Or     Code <Cd> [1..1] CodeSet 1707
Or}     Proprietary <Prtry> [1..1] ± 1707
   FungibleIndicator <FngbInd> [0..1] Indicator 1707
   Confidential <Cnfdtl> [0..1] Indicator 1708
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1678 August 2026
```

## File page 1679

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 1708
   ConvertibleIndicator <ConvtblInd> [0..1] Indicator 1708
   ConversionPeriod <ConvsPrd> [0..1] ± 1708
   ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 1709
   ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 1709
   PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 1709
   TradingMethod <TradgMtd> [0..1]  1709
{Or     Unit <Unit> [1..1] Quantity 1710
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1710
   TEFRARule <TEFRARule> [0..1]  1710
{Or     Code <Cd> [1..1] CodeSet 1710
Or}     Proprietary <Prtry> [1..1] ± 1711
   SerieNumber <SrNb> [0..1] Text 1711
   Class <Clss> [0..1] Text 1711
   WithholdingTaxRegime <WhldgTaxRgm> [0..*]  1711
     WithholdingTaxValue <WhldgTaxVal> [1..1] ± 1711
     Country <Ctry> [1..1] CodeSet C4 1712
   PaymentStatus <PmtSts> [0..1] ± 1712
   InitialPhysicalForm <InitlPhysForm> [0..1]  1712
{Or     Code <Cd> [1..1] CodeSet 1713
Or}     Proprietary <Prtry> [1..1] ± 1713
   AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  1713
{Or     Code <Cd> [1..1] CodeSet 1713
Or}     Proprietary <Prtry> [1..1] ± 1714
   CommonSafekeeper <CmonSfkpr> [0..1]  1714
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1714
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 1714
   RedemptionType <RedTp> [0..1]  1715
{Or     Code <Cd> [1..1] CodeSet 1715
Or}     Proprietary <Prtry> [1..1] ± 1715
   RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 1716
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1679 August 2026
```

## File page 1680

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Restriction <Rstrctn> [0..*]  1716
     EffectivePeriod <FctvPrd> [0..1] ± 1717
     RestrictionType <RstrctnTp> [0..1]  1717
{Or       RestrictionType <RstrctnTp> [1..1] CodeSet 1718
Or}       ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1718
     LegalRestrictionType <LglRstrctnTp> [0..1]  1718
{Or       Code <Cd> [1..1] CodeSet 1718
Or}       Proprietary <Prtry> [1..1] ± 1719
     InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1719
{Or       Code <Cd> [1..1] CodeSet 1719
Or}       Proprietary <Prtry> [1..1] ± 1720
     InvestorType <InvstrTp> [0..*]  1720
{Or       Code <Cd> [1..1] CodeSet 1720
Or}       Proprietary <Prtry> [1..1] ± 1720
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C6, C7,
C8, C9,
C12
1721
   SettlementInformation <SttlmInf> [0..*]  1722
     SecuritiesQuantityType <SctiesQtyTp> [0..1]  1722
{Or       Code <Cd> [1..1] CodeSet 1722
Or}       Proprietary <Prtry> [1..1] ± 1723
     ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 1723
     MinimumDenomination <MinDnmtn> [0..1] ± 1723
     MinimumMultipleQuantity <MinMltplQty> [0..1] ± 1723
     DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 1724
   FinancialInstrumentForm <FinInstrmForm> [0..1]  1724
     BookingAppearance <BookgApprnc> [0..1]  1724
{Or       Code <Cd> [1..1] CodeSet 1725
Or}       Proprietary <Prtry> [1..1] ± 1725
     LegalForm <LglForm> [0..1] ± 1725
   ContactName <CtctNm> [0..1]  1726
     Name <Nm> [1..1] Text 1726
     Identification <Id> [0..1]  1726
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1680 August 2026
```

## File page 1681

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1727
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1727
     Purpose <Purp> [0..1] Text 1727
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
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1731
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1731
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
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1735
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1735
     Purpose <Purp> [0..1] Text 1735
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1681 August 2026
```

## File page 1682

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1736
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1736
     RegistrationDate <RegnDt> [0..1] Date 1736
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1736
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1736
     PostalAddress <PstlAdr> [1..5] ± C10 1736
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1737
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1737
   PayingAgent <PngAgt> [0..1]  1738
     Name <Nm> [1..1] Text 1738
     Identification <Id> [0..1]  1739
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1739
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1739
     Purpose <Purp> [0..1] Text 1739
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1740
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1740
     RegistrationDate <RegnDt> [0..1] Date 1740
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1740
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1740
     PostalAddress <PstlAdr> [1..5] ± C10 1740
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1741
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1741
   Depository <Dpstry> [0..1]  1742
     Name <Nm> [1..1] Text 1742
     Identification <Id> [0..1]  1743
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1743
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1743
     Purpose <Purp> [0..1] Text 1743
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1744
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1744
     RegistrationDate <RegnDt> [0..1] Date 1744
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1682 August 2026
```

