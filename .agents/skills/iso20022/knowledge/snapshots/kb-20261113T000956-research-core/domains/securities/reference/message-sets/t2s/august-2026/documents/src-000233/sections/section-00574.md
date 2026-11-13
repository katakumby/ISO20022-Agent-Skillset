---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.4 Derivative <Deriv>", "27.4.2.2.4.2 Option <Optn>", "27.4.2.2.4.2.16 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "27.4.2.2.4.2.16.12 AdjustedQuantity <AdjstdQty>", "27.4.2.2.4.2.16.12.2 FaceAmount <FaceAmt>"]
file_pages: [750, 751, 752, 753, 754, 755, 756, 757, 758]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.4.2.16.12.2 FaceAmount <FaceAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 750 to 758.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 750

```text
Datatype: "DecimalNumber" on page 3324
27.4.2.2.4.2.16.12.2  FaceAmount <FaceAmt>
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
27.4.2.2.4.2.16.13  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Foreign exchange rate used to compute the current value.
Datatype: "PercentageRate" on page 3325
27.4.2.2.4.2.16.14  CapValue <CapVal>
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
27.4.2.3  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..*]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 750 August 2026
```

## File page 751

```text
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 751 August 2026
```

## File page 752

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following
CommonFinancialInstrumentAttributes10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityStatus <SctySts> [0..1]  759
{Or     Code <Cd> [1..1] CodeSet 759
Or}     Proprietary <Prtry> [1..1] ± 760
   ISOSecurityLongName <ISOSctyLngNm> [0..1] Text 760
   ISOSecurityShortName <ISOSctyShrtNm> [0..1] Text 760
   NameValidFrom <NmVldFr> [0..1] ± 760
   DenominationCurrency <DnmtnCcy> [1..1] CodeSet C2 760
   CertificateNumber <CertNb> [0..1] Text 761
   ContractVersionNumber <CtrctVrsnNb> [0..1] Quantity 761
   CouponAttachedNumber <CpnAttchdNb> [0..1] Text 761
   TaxLotNumber <TaxLotNb> [0..1] Text 761
   PoolNumber <PoolNb> [0..1] Text 761
   CoveredIndicator <CvrdInd> [0..1] Indicator 761
   LegalRestrictions <LglRstrctns> [0..1]  762
{Or     Code <Cd> [1..1] CodeSet 762
Or}     Proprietary <Prtry> [1..1] ± 762
   PositionLimit <PosLmt> [0..1] ± 762
   NearTermPositionLimit <NearTermPosLmt> [0..1] ± 763
   ListingDate <ListgDt> [0..1] Date 763
   RecordDate <RcrdDt> [0..1] DateTime 763
   ExpiryDate <XpryDt> [0..1] Date 763
   Purpose <Purp> [0..1] Text 763
   ClassificationType <ClssfctnTp> [0..1]  764
     ClassificationFinancialInstrument
<ClssfctnFinInstrm>
[0..1] IdentifierSet 764
     FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 764
     AlternateClassification <AltrnClssfctn> [0..*] ± 764
   Issuance <Issnc> [0..1]  764
     IssuePlace <IssePlc> [0..1] IdentifierSet 766
     CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 766
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 752 August 2026
```

## File page 753

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IssueDate <IsseDt> [0..1] Date 766
     AnnouncementDate <AnncmntDt> [0..1] DateTime 766
     ISINValidFrom <ISINVldFr> [0..1] Date 766
     IssuerOrganisation <IssrOrg> [0..1]  766
       Name <Nm> [1..1] Text 767
       Identification <Id> [0..1]  767
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 767
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 768
       Purpose <Purp> [0..1] Text 768
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 768
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 768
       RegistrationDate <RegnDt> [0..1] Date 769
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 769
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 769
       PostalAddress <PstlAdr> [1..5] ± C10 769
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 769
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 770
     IssueNominalAmount <IsseNmnlAmt> [0..1] ± 770
     FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 770
     IssueSize <IsseSz> [0..1] Quantity 771
     IssuePrice <IssePric> [0..1] ± 771
     IssuanceDistribution <IssncDstrbtn> [0..1]  771
{Or       Code <Cd> [1..1] CodeSet 772
Or}       Proprietary <Prtry> [1..1] ± 772
     GoverningLaw <GovngLaw> [0..*]  772
       Identification <Id> [0..1] Text 772
       Country <Ctry> [0..1] CodeSet C4 772
   TradingMarket <TradgMkt> [0..*]  773
     MarketIdentification <MktId> [0..1] IdentifierSet 773
     RoundLot <RndLot> [0..1] ± 773
     TradeLotSize <TradLotSz> [0..1] ± 774
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 753 August 2026
```

## File page 754

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 774
     MinimumTradedNominalQuantity
<MinTraddNmnlQty>
[0..1]  774
{Or       Unit <Unit> [1..1] Quantity 774
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 774
     MaximumTradedNominalQuantity
<MaxTraddNmnlQty>
[0..1]  775
{Or       Unit <Unit> [1..1] Quantity 775
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 775
     MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 776
     PrimaryPlaceOfListingIdentification
<PmryPlcOfListgId>
[0..1] IdentifierSet 776
   SpreadAndBenchmarkCurve <SprdAndBchmkCrv> [0..*]  776
     Spread <Sprd> [0..1] Quantity 776
     BenchmarkIdentification <BchmkId> [0..1] ± C6, C7,
C8, C9,
C12
777
     BenchmarkPrice <BchmkPric> [0..1]  778
       ValueType <ValTp> [0..1] CodeSet 778
       Value <Val> [1..1] ± 779
       PriceType <PricTp> [0..1] CodeSet 779
     BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 780
     BenchmarkCurveName <BchmkCrvNm> [0..1]  780
{Or       Code <Cd> [1..1] CodeSet 780
Or}       Proprietary <Prtry> [1..1] ± 781
     BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 782
   PutType <PutTp> [0..1]  782
{Or     Code <Cd> [1..1] CodeSet 782
Or}     Proprietary <Prtry> [1..1] ± 782
   CallType <CallTp> [0..1]  783
{Or     Code <Cd> [1..1] CodeSet 783
Or}     Proprietary <Prtry> [1..1] ± 783
   FungibleIndicator <FngbInd> [0..1] Indicator 783
   Confidential <Cnfdtl> [0..1] Indicator 784
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 754 August 2026
```

## File page 755

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 784
   ConvertibleIndicator <ConvtblInd> [0..1] Indicator 784
   ConversionPeriod <ConvsPrd> [0..1] ± 784
   ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 785
   ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 785
   PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 785
   TradingMethod <TradgMtd> [0..1]  785
{Or     Unit <Unit> [1..1] Quantity 786
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 786
   TEFRARule <TEFRARule> [0..1]  786
{Or     Code <Cd> [1..1] CodeSet 786
Or}     Proprietary <Prtry> [1..1] ± 787
   SerieNumber <SrNb> [0..1] Text 787
   Class <Clss> [0..1] Text 787
   WithholdingTaxRegime <WhldgTaxRgm> [0..*]  787
     WithholdingTaxValue <WhldgTaxVal> [1..1] ± 787
     Country <Ctry> [1..1] CodeSet C4 788
   PaymentStatus <PmtSts> [0..1] ± 788
   InitialPhysicalForm <InitlPhysForm> [0..1]  788
{Or     Code <Cd> [1..1] CodeSet 789
Or}     Proprietary <Prtry> [1..1] ± 789
   AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  789
{Or     Code <Cd> [1..1] CodeSet 789
Or}     Proprietary <Prtry> [1..1] ± 790
   CommonSafekeeper <CmonSfkpr> [0..1] IdentifierSet C3 790
   RedemptionType <RedTp> [0..1]  790
{Or     Code <Cd> [1..1] CodeSet 790
Or}     Proprietary <Prtry> [1..1] ± 791
   RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 791
   Restriction <Rstrctn> [0..*]  791
     EffectivePeriod <FctvPrd> [0..1] ± 792
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 755 August 2026
```

## File page 756

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     RestrictionType <RstrctnTp> [0..1]  792
{Or       RestrictionType <RstrctnTp> [1..1] CodeSet 793
Or}       ProprietaryRestriction <PrtryRstrctn> [1..1] ± 793
     LegalRestrictionType <LglRstrctnTp> [0..1]  793
{Or       Code <Cd> [1..1] CodeSet 793
Or}       Proprietary <Prtry> [1..1] ± 794
     InvestorRestrictionType <InvstrRstrctnTp> [0..*]  794
{Or       Code <Cd> [1..1] CodeSet 794
Or}       Proprietary <Prtry> [1..1] ± 795
     InvestorType <InvstrTp> [0..*]  795
{Or       Code <Cd> [1..1] CodeSet 795
Or}       Proprietary <Prtry> [1..1] ± 795
   SettlementInformation <SttlmInf> [0..*]  796
     SecuritiesQuantityType <SctiesQtyTp> [0..1]  796
{Or       Code <Cd> [1..1] CodeSet 796
Or}       Proprietary <Prtry> [1..1] ± 797
     ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 797
     MinimumDenomination <MinDnmtn> [0..1] ± 797
     MinimumMultipleQuantity <MinMltplQty> [0..1] ± 797
     DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 798
   FinancialInstrumentForm <FinInstrmForm> [0..1]  798
     BookingAppearance <BookgApprnc> [0..1]  798
{Or       Code <Cd> [1..1] CodeSet 799
Or}       Proprietary <Prtry> [1..1] ± 799
     LegalForm <LglForm> [0..1] ± 799
   ContactName <CtctNm> [0..1]  800
     Name <Nm> [1..1] Text 800
     Identification <Id> [0..1]  800
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 801
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 801
     Purpose <Purp> [0..1] Text 801
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 756 August 2026
```

## File page 757

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 801
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 802
     RegistrationDate <RegnDt> [0..1] Date 802
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 802
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 802
     PostalAddress <PstlAdr> [1..5] ± C10 802
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 803
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 803
   LeadManager <LeadMgr> [0..1]  804
     Name <Nm> [1..1] Text 804
     Identification <Id> [0..1]  805
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 805
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 805
     Purpose <Purp> [0..1] Text 805
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 806
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 806
     RegistrationDate <RegnDt> [0..1] Date 806
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 806
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 806
     PostalAddress <PstlAdr> [1..5] ± C10 806
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 807
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 807
   PrincipalPayingAgent <PrncplPngAgt> [0..1]  808
     Name <Nm> [1..1] Text 808
     Identification <Id> [0..1]  809
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 809
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 809
     Purpose <Purp> [0..1] Text 809
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 810
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 810
     RegistrationDate <RegnDt> [0..1] Date 810
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 757 August 2026
```

## File page 758

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 810
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 810
     PostalAddress <PstlAdr> [1..5] ± C10 810
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 811
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 811
   PayingAgent <PngAgt> [0..1]  812
     Name <Nm> [1..1] Text 812
     Identification <Id> [0..1]  813
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 813
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 813
     Purpose <Purp> [0..1] Text 813
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 814
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 814
     RegistrationDate <RegnDt> [0..1] Date 814
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 814
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 814
     PostalAddress <PstlAdr> [1..5] ± C10 814
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 815
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 815
   Depository <Dpstry> [0..1]  816
     Name <Nm> [1..1] Text 816
     Identification <Id> [0..1]  817
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 817
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 817
     Purpose <Purp> [0..1] Text 817
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 818
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 818
     RegistrationDate <RegnDt> [0..1] Date 818
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 818
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 818
     PostalAddress <PstlAdr> [1..5] ± C10 818
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 758 August 2026
```

