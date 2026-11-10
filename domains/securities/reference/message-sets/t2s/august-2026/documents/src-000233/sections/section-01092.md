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
file_pages: [1572, 1573, 1574, 1575, 1576, 1577]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# Continuation at file page 1572

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1572 to 1577.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1572

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         Code <Cd> [1..1] CodeSet 1696
Or}         Proprietary <Prtry> [1..1] ± 1696
       GoverningLaw <GovngLaw> [0..*]  1696
         Identification <Id> [0..1] Text 1696
         Country <Ctry> [0..1] CodeSet C4 1696
     TradingMarket <TradgMkt> [0..*]  1697
       MarketIdentification <MktId> [0..1] IdentifierSet 1697
       RoundLot <RndLot> [0..1] ± 1697
       TradeLotSize <TradLotSz> [0..1] ± 1698
       SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1698
       MinimumTradedNominalQuantity
<MinTraddNmnlQty>
[0..1]  1698
{Or         Unit <Unit> [1..1] Quantity 1698
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1698
       MaximumTradedNominalQuantity
<MaxTraddNmnlQty>
[0..1]  1699
{Or         Unit <Unit> [1..1] Quantity 1699
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1699
       MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 1700
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1572 August 2026
```

## File page 1573

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         Code <Cd> [1..1] CodeSet 1704
Or}         Proprietary <Prtry> [1..1] ± 1705
       BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 1706
     PutType <PutTp> [0..1]  1706
{Or       Code <Cd> [1..1] CodeSet 1706
Or}       Proprietary <Prtry> [1..1] ± 1706
     CallType <CallTp> [0..1]  1707
{Or       Code <Cd> [1..1] CodeSet 1707
Or}       Proprietary <Prtry> [1..1] ± 1707
     FungibleIndicator <FngbInd> [0..1] Indicator 1707
     Confidential <Cnfdtl> [0..1] Indicator 1708
     PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 1708
     ConvertibleIndicator <ConvtblInd> [0..1] Indicator 1708
     ConversionPeriod <ConvsPrd> [0..1] ± 1708
     ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 1709
     ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 1709
     PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 1709
     TradingMethod <TradgMtd> [0..1]  1709
{Or       Unit <Unit> [1..1] Quantity 1710
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1710
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1573 August 2026
```

## File page 1574

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TEFRARule <TEFRARule> [0..1]  1710
{Or       Code <Cd> [1..1] CodeSet 1710
Or}       Proprietary <Prtry> [1..1] ± 1711
     SerieNumber <SrNb> [0..1] Text 1711
     Class <Clss> [0..1] Text 1711
     WithholdingTaxRegime <WhldgTaxRgm> [0..*]  1711
       WithholdingTaxValue <WhldgTaxVal> [1..1] ± 1711
       Country <Ctry> [1..1] CodeSet C4 1712
     PaymentStatus <PmtSts> [0..1] ± 1712
     InitialPhysicalForm <InitlPhysForm> [0..1]  1712
{Or       Code <Cd> [1..1] CodeSet 1713
Or}       Proprietary <Prtry> [1..1] ± 1713
     AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  1713
{Or       Code <Cd> [1..1] CodeSet 1713
Or}       Proprietary <Prtry> [1..1] ± 1714
     CommonSafekeeper <CmonSfkpr> [0..1]  1714
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1714
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1714
     RedemptionType <RedTp> [0..1]  1715
{Or       Code <Cd> [1..1] CodeSet 1715
Or}       Proprietary <Prtry> [1..1] ± 1715
     RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 1716
     Restriction <Rstrctn> [0..*]  1716
       EffectivePeriod <FctvPrd> [0..1] ± 1717
       RestrictionType <RstrctnTp> [0..1]  1717
{Or         RestrictionType <RstrctnTp> [1..1] CodeSet 1718
Or}         ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1718
       LegalRestrictionType <LglRstrctnTp> [0..1]  1718
{Or         Code <Cd> [1..1] CodeSet 1718
Or}         Proprietary <Prtry> [1..1] ± 1719
       InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1719
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1574 August 2026
```

## File page 1575

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         Code <Cd> [1..1] CodeSet 1719
Or}         Proprietary <Prtry> [1..1] ± 1720
       InvestorType <InvstrTp> [0..*]  1720
{Or         Code <Cd> [1..1] CodeSet 1720
Or}         Proprietary <Prtry> [1..1] ± 1720
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C6, C7,
C8, C9,
C12
1721
     SettlementInformation <SttlmInf> [0..*]  1722
       SecuritiesQuantityType <SctiesQtyTp> [0..1]  1722
{Or         Code <Cd> [1..1] CodeSet 1722
Or}         Proprietary <Prtry> [1..1] ± 1723
       ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 1723
       MinimumDenomination <MinDnmtn> [0..1] ± 1723
       MinimumMultipleQuantity <MinMltplQty> [0..1] ± 1723
       DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 1724
     FinancialInstrumentForm <FinInstrmForm> [0..1]  1724
       BookingAppearance <BookgApprnc> [0..1]  1724
{Or         Code <Cd> [1..1] CodeSet 1725
Or}         Proprietary <Prtry> [1..1] ± 1725
       LegalForm <LglForm> [0..1] ± 1725
     ContactName <CtctNm> [0..1]  1726
       Name <Nm> [1..1] Text 1726
       Identification <Id> [0..1]  1726
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1727
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1727
       Purpose <Purp> [0..1] Text 1727
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1727
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1728
       RegistrationDate <RegnDt> [0..1] Date 1728
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1728
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1728
       PostalAddress <PstlAdr> [1..5] ± C10 1728
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1575 August 2026
```

## File page 1576

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1729
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1729
     LeadManager <LeadMgr> [0..1]  1730
       Name <Nm> [1..1] Text 1730
       Identification <Id> [0..1]  1731
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1731
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1731
       Purpose <Purp> [0..1] Text 1731
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1732
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1732
       RegistrationDate <RegnDt> [0..1] Date 1732
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1732
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1732
       PostalAddress <PstlAdr> [1..5] ± C10 1732
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1733
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1733
     PrincipalPayingAgent <PrncplPngAgt> [0..1]  1734
       Name <Nm> [1..1] Text 1734
       Identification <Id> [0..1]  1735
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1735
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1735
       Purpose <Purp> [0..1] Text 1735
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1736
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1736
       RegistrationDate <RegnDt> [0..1] Date 1736
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1736
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1736
       PostalAddress <PstlAdr> [1..5] ± C10 1736
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1737
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1737
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1576 August 2026
```

## File page 1577

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PayingAgent <PngAgt> [0..1]  1738
       Name <Nm> [1..1] Text 1738
       Identification <Id> [0..1]  1739
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1739
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1739
       Purpose <Purp> [0..1] Text 1739
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1740
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1740
       RegistrationDate <RegnDt> [0..1] Date 1740
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1740
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1740
       PostalAddress <PstlAdr> [1..5] ± C10 1740
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1741
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1741
     Depository <Dpstry> [0..1]  1742
       Name <Nm> [1..1] Text 1742
       Identification <Id> [0..1]  1743
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1743
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1743
       Purpose <Purp> [0..1] Text 1743
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1744
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1744
       RegistrationDate <RegnDt> [0..1] Date 1744
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1744
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1744
       PostalAddress <PstlAdr> [1..5] ± C10 1744
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1745
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1745
     UnderlyingRisk <UndrlygRsk> [0..1]  1746
       Name <Nm> [1..1] Text 1746
       Identification <Id> [0..1]  1747
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1577 August 2026
```

