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
file_pages: [1814, 1815, 1816, 1817, 1818, 1819, 1820]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# Continuation at file page 1814

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1814 to 1820.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1814

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Name <Nm> [1..1] Text 1970
             Identification <Id> [0..1]  1970
{Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1970
Or}               ProprietaryIdentification <PrtryId> [1..1] ± 1971
             Purpose <Purp> [0..1] Text 1971
             TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1971
             RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1971
             RegistrationDate <RegnDt> [0..1] Date 1972
             TaxIdentificationNumber <TaxIdNb> [0..1] Text 1972
             NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1972
             PostalAddress <PstlAdr> [1..5] ± C10 1972
             PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1972
             SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1973
           IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1973
           FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1973
           IssueSize <IsseSz> [0..1] Quantity 1974
           IssuePrice <IssePric> [0..1] ± 1974
           IssuanceDistribution <IssncDstrbtn> [0..1]  1974
{Or             Code <Cd> [1..1] CodeSet 1975
Or}             Proprietary <Prtry> [1..1] ± 1975
           GoverningLaw <GovngLaw> [0..*]  1975
             Identification <Id> [0..1] Text 1975
             Country <Ctry> [0..1] CodeSet C4 1975
         TradingMarket <TradgMkt> [0..*]  1976
           MarketIdentification <MktId> [0..1] IdentifierSet 1976
           RoundLot <RndLot> [0..1] ± 1976
           TradeLotSize <TradLotSz> [0..1] ± 1977
           SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1977
           MinimumTradedNominalQuantity
<MinTraddNmnlQty>
[0..1]  1977
{Or             Unit <Unit> [1..1] Quantity 1977
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1977
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1814 August 2026
```

## File page 1815

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           MaximumTradedNominalQuantity
<MaxTraddNmnlQty>
[0..1]  1978
{Or             Unit <Unit> [1..1] Quantity 1978
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1978
           MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 1979
           PrimaryPlaceOfListingIdentification
<PmryPlcOfListgId>
[0..1] IdentifierSet 1979
         SpreadAndBenchmarkCurve <SprdAndBchmkCrv> [0..*]  1979
           Spread <Sprd> [0..1] Quantity 1979
           BenchmarkIdentification <BchmkId> [0..1] ± C6, C7,
C8, C9,
C12
1980
           BenchmarkPrice <BchmkPric> [0..1]  1981
             ValueType <ValTp> [0..1] CodeSet 1981
             Value <Val> [1..1] ± 1982
             PriceType <PricTp> [0..1] CodeSet 1982
           BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 1983
           BenchmarkCurveName <BchmkCrvNm> [0..1]  1983
{Or             Code <Cd> [1..1] CodeSet 1983
Or}             Proprietary <Prtry> [1..1] ± 1984
           BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 1985
         PutType <PutTp> [0..1]  1985
{Or           Code <Cd> [1..1] CodeSet 1985
Or}           Proprietary <Prtry> [1..1] ± 1985
         CallType <CallTp> [0..1]  1986
{Or           Code <Cd> [1..1] CodeSet 1986
Or}           Proprietary <Prtry> [1..1] ± 1986
         FungibleIndicator <FngbInd> [0..1] Indicator 1986
         Confidential <Cnfdtl> [0..1] Indicator 1987
         PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 1987
         ConvertibleIndicator <ConvtblInd> [0..1] Indicator 1987
         ConversionPeriod <ConvsPrd> [0..1] ± 1987
         ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 1988
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1815 August 2026
```

## File page 1816

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 1988
         PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 1988
         TradingMethod <TradgMtd> [0..1]  1988
{Or           Unit <Unit> [1..1] Quantity 1989
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1989
         TEFRARule <TEFRARule> [0..1]  1989
{Or           Code <Cd> [1..1] CodeSet 1989
Or}           Proprietary <Prtry> [1..1] ± 1990
         SerieNumber <SrNb> [0..1] Text 1990
         Class <Clss> [0..1] Text 1990
         WithholdingTaxRegime <WhldgTaxRgm> [0..*]  1990
           WithholdingTaxValue <WhldgTaxVal> [1..1] ± 1990
           Country <Ctry> [1..1] CodeSet C4 1991
         PaymentStatus <PmtSts> [0..1] ± 1991
         InitialPhysicalForm <InitlPhysForm> [0..1]  1991
{Or           Code <Cd> [1..1] CodeSet 1992
Or}           Proprietary <Prtry> [1..1] ± 1992
         AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  1992
{Or           Code <Cd> [1..1] CodeSet 1992
Or}           Proprietary <Prtry> [1..1] ± 1993
         CommonSafekeeper <CmonSfkpr> [0..1]  1993
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1993
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1993
         RedemptionType <RedTp> [0..1]  1994
{Or           Code <Cd> [1..1] CodeSet 1994
Or}           Proprietary <Prtry> [1..1] ± 1994
         RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 1995
         Restriction <Rstrctn> [0..*]  1995
           EffectivePeriod <FctvPrd> [0..1] ± 1996
           RestrictionType <RstrctnTp> [0..1]  1996
{Or             RestrictionType <RstrctnTp> [1..1] CodeSet 1997
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1816 August 2026
```

## File page 1817

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1997
           LegalRestrictionType <LglRstrctnTp> [0..1]  1997
{Or             Code <Cd> [1..1] CodeSet 1997
Or}             Proprietary <Prtry> [1..1] ± 1998
           InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1998
{Or             Code <Cd> [1..1] CodeSet 1998
Or}             Proprietary <Prtry> [1..1] ± 1999
           InvestorType <InvstrTp> [0..*]  1999
{Or             Code <Cd> [1..1] CodeSet 1999
Or}             Proprietary <Prtry> [1..1] ± 1999
         FinancialInstrumentIdentificationValidity
<FinInstrmIdVldty>
[0..*]  2000
           FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C6, C7,
C8, C9,
C12
2000
           ISINValidFrom <ISINVldFr> [0..1] Date 2001
         SettlementInformation <SttlmInf> [0..*]  2001
           SecuritiesQuantityType <SctiesQtyTp> [0..1]  2002
{Or             Code <Cd> [1..1] CodeSet 2002
Or}             Proprietary <Prtry> [1..1] ± 2002
           ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 2003
           MinimumDenomination <MinDnmtn> [0..1] ± 2003
           MinimumMultipleQuantity <MinMltplQty> [0..1] ± 2003
           DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 2003
         FinancialInstrumentForm <FinInstrmForm> [0..1]  2004
           BookingAppearance <BookgApprnc> [0..1]  2004
{Or             Code <Cd> [1..1] CodeSet 2004
Or}             Proprietary <Prtry> [1..1] ± 2005
           LegalForm <LglForm> [0..1] ± 2005
         ContactName <CtctNm> [0..1]  2005
           Name <Nm> [1..1] Text 2006
           Identification <Id> [0..1]  2006
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 2006
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1817 August 2026
```

## File page 1818

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 2007
           Purpose <Purp> [0..1] Text 2007
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 2007
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 2007
           RegistrationDate <RegnDt> [0..1] Date 2008
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 2008
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 2008
           PostalAddress <PstlAdr> [1..5] ± C10 2008
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 2008
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 2009
         LeadManager <LeadMgr> [0..1]  2009
           Name <Nm> [1..1] Text 2010
           Identification <Id> [0..1]  2010
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 2010
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 2011
           Purpose <Purp> [0..1] Text 2011
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 2011
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 2011
           RegistrationDate <RegnDt> [0..1] Date 2012
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 2012
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 2012
           PostalAddress <PstlAdr> [1..5] ± C10 2012
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 2012
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 2013
         PrincipalPayingAgent <PrncplPngAgt> [0..1]  2013
           Name <Nm> [1..1] Text 2014
           Identification <Id> [0..1]  2014
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 2014
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 2015
           Purpose <Purp> [0..1] Text 2015
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 2015
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1818 August 2026
```

## File page 1819

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 2015
           RegistrationDate <RegnDt> [0..1] Date 2016
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 2016
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 2016
           PostalAddress <PstlAdr> [1..5] ± C10 2016
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 2016
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 2017
         PayingAgent <PngAgt> [0..1]  2017
           Name <Nm> [1..1] Text 2018
           Identification <Id> [0..1]  2018
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 2018
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 2019
           Purpose <Purp> [0..1] Text 2019
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 2019
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 2019
           RegistrationDate <RegnDt> [0..1] Date 2020
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 2020
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 2020
           PostalAddress <PstlAdr> [1..5] ± C10 2020
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 2020
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 2021
         Depository <Dpstry> [0..1]  2021
           Name <Nm> [1..1] Text 2022
           Identification <Id> [0..1]  2022
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 2022
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 2023
           Purpose <Purp> [0..1] Text 2023
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 2023
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 2023
           RegistrationDate <RegnDt> [0..1] Date 2024
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 2024
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1819 August 2026
```

## File page 1820

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 2024
           PostalAddress <PstlAdr> [1..5] ± C10 2024
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 2024
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 2025
         UnderlyingRisk <UndrlygRsk> [0..1]  2025
           Name <Nm> [1..1] Text 2026
           Identification <Id> [0..1]  2026
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 2026
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 2027
           Purpose <Purp> [0..1] Text 2027
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 2027
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 2027
           RegistrationDate <RegnDt> [0..1] Date 2028
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 2028
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 2028
           PostalAddress <PstlAdr> [1..5] ± C10 2028
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 2028
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 2029
         SecurityCSDLink <SctyCSDLk> [0..*]  2029
           ValidFrom <VldFr> [1..1] ± 2030
           ValidTo <VldTo> [0..1] ± 2030
           SecurityMaintenance <SctyMntnc> [0..1] Indicator 2031
           IssuerCSD <IssrCSD> [0..1]  2031
{Or             OrganisationIdentification <OrgId> [1..1] ± 2031
Or}             CombinedIdentification <CmbndId> [1..1] ± 2031
           InvestorCSD <InvstrCSD> [0..1]  2032
{Or             OrganisationIdentification <OrgId> [1..1] ± 2032
Or}             CombinedIdentification <CmbndId> [1..1] ± 2032
           TechnicalIssuerCSD <TechIssrCSD> [0..1]  2032
{Or             OrganisationIdentification <OrgId> [1..1] ± 2033
Or}             CombinedIdentification <CmbndId> [1..1] ± 2033
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1820 August 2026
```

