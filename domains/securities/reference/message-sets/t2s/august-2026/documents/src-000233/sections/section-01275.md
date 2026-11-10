---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>"]
file_pages: [1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1 SecurityReport <SctyRpt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1838 to 1847.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1838

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         IssuanceAccount <IssncAcct> [0..*]  2033
           IssuanceAccount <IssncAcct> [1..1] ± 2033
           PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 2034
Or}   BusinessError <BizErr> [1..*]  2034
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C6, C7,
C8, C9,
C12
2034
     BusinessError <BizErr> [1..*]  2035
       Error <Err> [1..1]  2036
{Or         Code <Cd> [1..1] CodeSet 2036
Or}         Proprietary <Prtry> [1..1] Text 2036
       Description <Desc> [0..1] Text 2036
32.4.3.1.1  SecurityReport <SctyRpt>
Presence: [1..*]
Definition: Provides the financial instruments details.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1838 August 2026
```

## File page 1839

```text
SecurityReport <SctyRpt> contains the following SecurityAttributes11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C6, C7,
C8, C9,
C12
1855
   FinancialInstrumentType <FinInstrmTp> [0..1]  1856
     Equity <Eqty> [0..1]  1864
       PreferenceToIncome <PrefToIncm> [1..1]  1865
{Or         Code <Cd> [1..1] CodeSet 1865
Or}         Proprietary <Prtry> [1..1] ± 1865
       MaturityDate <MtrtyDt> [0..1] DateTime 1866
       NonPaidAmount <NonPdAmt> [0..1] Amount C1, C5 1866
       ParValue <ParVal> [0..1] Amount C1, C5 1866
       VotingRightsPerShare <VtngRghtsPerShr> [0..1] Quantity 1867
     Warrant <Warrt> [0..1]  1867
       Multiplier <Mltplr> [0..1] Rate 1868
       SubscriptionPrice <SbcptPric> [0..1]  1868
         ValueType <ValTp> [0..1] CodeSet 1869
         Value <Val> [1..1] ± 1869
         PriceType <PricTp> [0..1] CodeSet 1870
       Type <Tp> [0..1]  1870
{Or         Code <Cd> [1..1] CodeSet 1871
Or}         Proprietary <Prtry> [1..1] ± 1871
       WarrantAgent <WarrtAgt> [0..*]  1871
         Name <Nm> [1..1] Text 1872
         Identification <Id> [0..1]  1872
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1872
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1873
         Purpose <Purp> [0..1] Text 1873
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1873
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1873
         RegistrationDate <RegnDt> [0..1] Date 1874
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1874
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1874
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1839 August 2026
```

## File page 1840

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PostalAddress <PstlAdr> [1..5] ± C10 1874
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1874
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1875
     Debt <Debt> [0..1]  C11,
C13
1875
       PaymentCurrency <PmtCcy> [0..1] CodeSet C1 1879
       FaceAmount <FaceAmt> [0..1] Amount C1, C5 1879
       PaymentFrequency <PmtFrqcy> [0..1] ± 1880
       InterestFixingDate <IntrstFxgDt> [0..1] DateTime 1880
       DatedDate <DtdDt> [0..1] DateTime 1880
       FirstPaymentDate <FrstPmtDt> [0..1] DateTime 1880
       MaturityDate <MtrtyDt> [0..1] DateTime 1880
       NextCouponDate <NxtCpnDt> [0..1] DateTime 1880
       PutableDate <PutblDt> [0..1] DateTime 1881
       NextCallableDate <NxtCllblDt> [0..1] DateTime 1881
       NextFactorDate <NxtFctrDt> [0..1] DateTime 1881
       ExpirationDate <XprtnDt> [0..1] DateTime 1881
       PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 1881
       InterestRate <IntrstRate> [0..1] Rate 1881
       NextInterestRate <NxtIntrstRate> [0..1] Rate 1881
       OddCouponIndicator <OddCpnInd> [0..1] Indicator 1881
       CallableIndicator <CllblInd> [0..1] Indicator 1882
       CPProgram <CPPrgm> [0..1] Quantity 1882
       CPRegistrationType <CPRegnTp> [0..1] Text 1882
       InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 1882
       PutableIndicator <PutblInd> [0..1] Indicator 1882
       PreFundedIndicator <PreFnddInd> [0..1] Indicator 1883
       EscrowedIndicator <EscrwdInd> [0..1] Indicator 1883
       PerpetualIndicator <PerptlInd> [0..1] Indicator 1883
       SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1883
       ExtendibleIndicator <XtndblInd> [0..1] Indicator 1883
       ExtendiblePeriod <XtndblPrd> [0..1]  1884
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1840 August 2026
```

## File page 1841

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         FromDateTime <FrDtTm> [1..1] DateTime 1884
Or         ToDateTime <ToDtTm> [1..1] DateTime 1884
Or}         DateTimeRange <DtTmRg> [1..1] ± 1884
       VariableRateIndicator <VarblRateInd> [0..1] Indicator 1884
       OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1885
       OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1885
       AmortisableIndicator <AmtsblInd> [0..1] Indicator 1885
       InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1885
       CapitalisedInterest <CptlsdIntrst> [0..1]  1885
{Or         Code <Cd> [1..1] CodeSet 1886
Or}         Proprietary <Prtry> [1..1] ± 1886
       ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1886
       CurrentFactor <CurFctr> [0..1] Rate 1887
       NextFactor <NxtFctr> [0..1] Rate 1887
       PreviousFactor <PrvsFctr> [0..1] Rate 1887
       Pieces <Pcs> [0..1] Quantity 1887
       PoolsMaximum <PlsMax> [0..1] Quantity 1887
       PoolsPerMillion <PlsPerMln> [0..1] Quantity 1887
       PoolsPerLot <PlsPerLot> [0..1] Quantity 1887
       PoolsPerTrade <PlsPerTrad> [0..1] Quantity 1888
       ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 1888
       LotIdentification <LotId> [0..1] Text 1888
       ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 1888
       WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 1888
       WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 1888
       WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1888
       WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1889
       InsuredIndicator <InsrdInd> [0..1] Indicator 1889
       BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1889
       YieldCalculation <YldClctn> [0..*]  1889
         Value <Val> [1..1] Rate 1890
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1841 August 2026
```

## File page 1842

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         CalculationType <ClctnTp> [0..1]  1890
{Or           Code <Cd> [1..1] CodeSet 1890
Or}           Proprietary <Prtry> [1..1] ± 1893
         RedemptionPrice <RedPric> [0..1]  1893
           ValueType <ValTp> [0..1] CodeSet 1893
           Value <Val> [1..1] ± 1894
           PriceType <PricTp> [0..1] CodeSet 1894
         ValueDate <ValDt> [1..1] Date 1895
         ValuePeriod <ValPrd> [1..1]  1895
{Or           FromDateTime <FrDtTm> [1..1] DateTime 1895
Or           ToDateTime <ToDtTm> [1..1] DateTime 1896
Or}           DateTimeRange <DtTmRg> [1..1] ± 1896
         CalculationDate <ClctnDt> [1..1] DateTime 1896
       InterestType <IntrstTp> [0..1] CodeSet 1896
       InstrumentStructureType <InstrmStrTp> [0..1]  1896
{Or         Code <Cd> [1..1] CodeSet 1897
Or}         Proprietary <Prtry> [1..1] ± 1898
       GlobalType <GblTp> [0..1]  1898
{Or         Code <Cd> [1..1] CodeSet 1898
Or}         Proprietary <Prtry> [1..1] ± 1899
       PotentialEuroSystemEligibility
<PotntlEuroSysElgblty>
[0..1] Indicator 1899
       Geographics <Geogcs> [0..1] Text 1899
       YieldRange <YldRg> [0..1] ± 1899
       CouponRange <CpnRg> [0..1] ± 1900
       Purpose <Purp> [0..1] Text 1900
       AlternativeMinimumTaxIndicator
<AltrntvMinTaxInd>
[0..1] Indicator 1900
       AutoReinvestment <AutoRinvstmt> [0..1] Rate 1901
       Haircut <Hrcut> [0..1] Rate 1901
       TransactionConditions <TxConds> [0..1] ± 1901
       LookBack <LookBck> [0..1] Quantity 1901
       MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1901
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1842 August 2026
```

## File page 1843

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       MinimumIncrement <MinIncrmt> [0..1] ± 1901
       MinimumQuantity <MinQty> [0..1] ± 1902
       Production <Pdctn> [0..1] Text 1902
       RestrictedIndicator <RstrctdInd> [0..1] Indicator 1902
       PriceFrequency <PricFrqcy> [0..1] ± 1902
       Sector <Sctr> [0..1] Text 1903
       SubstitutionFrequency <SbstitnFrqcy> [0..1] ± 1903
       SubstitutionLeft <SbstitnLft> [0..1] Quantity 1903
       WholePoolIndicator <WhlPoolInd> [0..1] Indicator 1903
       PriceSource <PricSrc> [0..1] Text 1903
       PriceRange <PricRg> [0..1] ± 1904
     Derivative <Deriv> [0..1]  1904
       Future <Futr> [0..1]  1908
         ContractSize <CtrctSz> [0..1] Rate 1910
         ExercisePrice <ExrcPric> [0..1]  1910
           ValueType <ValTp> [0..1] CodeSet 1910
           Value <Val> [1..1] ± 1911
           PriceType <PricTp> [0..1] CodeSet 1911
         FutureDate <FutrDt> [0..1] DateTime 1912
         MinimumSize <MinSz> [0..1] Amount C1, C5 1912
         UnitOfMeasure <UnitOfMeasr> [0..1]  1913
{Or           Code <Cd> [1..1] CodeSet 1913
Or}           Proprietary <Prtry> [1..1] ± 1915
         TimeUnit <TmUnit> [0..1]  1915
{Or           Code <Cd> [1..1] CodeSet 1916
Or}           Proprietary <Prtry> [1..1] ± 1916
         AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1916
           AllocationPercentage <AllcnPctg> [0..1] Rate 1918
           Quantity <Qty> [0..1]  1918
{Or             Unit <Unit> [1..1] Quantity 1918
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1918
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1843 August 2026
```

## File page 1844

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           SettlementType <SttlmTp> [0..1]  1918
{Or             Code <Cd> [1..1] CodeSet 1919
Or}             Proprietary <Prtry> [1..1] ± 1919
           CashAmount <CshAmt> [0..1] Amount C1, C5 1919
           CashType <CshTp> [0..1] Text 1920
           Price <Pric> [0..1]  1920
             ValueType <ValTp> [0..1] CodeSet 1920
             Value <Val> [1..1] ± 1921
             PriceType <PricTp> [0..1] CodeSet 1921
           DirtyPrice <DrtyPric> [0..1]  1922
             ValueType <ValTp> [0..1] CodeSet 1922
             Value <Val> [1..1] ± 1923
             PriceType <PricTp> [0..1] CodeSet 1923
           EndPrice <EndPric> [0..1]  1924
             ValueType <ValTp> [0..1] CodeSet 1924
             Value <Val> [1..1] ± 1925
             PriceType <PricTp> [0..1] CodeSet 1925
           StartValue <StartVal> [0..1] Amount C1, C5 1926
           CurrentValue <CurVal> [0..1] Amount C1, C5 1926
           EndValue <EndVal> [0..1] Amount C1, C5 1927
           AdjustedQuantity <AdjstdQty> [0..1]  1927
{Or             Unit <Unit> [1..1] Quantity 1927
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1928
           ExchangeRate <XchgRate> [0..1] Rate 1928
           CapValue <CapVal> [0..1] Amount C1, C5 1928
       Option <Optn> [0..1]  1928
         OptionSettlementStyle <OptnSttlmStyle> [0..1]  1932
{Or           Code <Cd> [0..*] CodeSet 1932
Or}           Proprietary <Prtry> [1..1] ± 1932
         ConversionDate <ConvsDt> [0..1] DateTime 1932
         StrikePrice <StrkPric> [0..1]  1932
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1844 August 2026
```

## File page 1845

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           ValueType <ValTp> [0..1] CodeSet 1933
           Value <Val> [1..1] ± 1933
           PriceType <PricTp> [0..1] CodeSet 1934
         MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1934
         ConversionPeriod <ConvsPrd> [0..1]  1935
{Or           FromDateTime <FrDtTm> [1..1] DateTime 1935
Or           ToDateTime <ToDtTm> [1..1] DateTime 1935
Or}           DateTimeRange <DtTmRg> [1..1] ± 1935
         OptionStyle <OptnStyle> [0..1]  1936
{Or           Code <Cd> [1..1] CodeSet 1936
Or}           Proprietary <Prtry> [1..1] ± 1936
         OptionType <OptnTp> [0..1] ± 1936
         StrikeValue <StrkVal> [0..1] Quantity 1937
         StrikeMultiplier <StrkMltplr> [0..1] Quantity 1937
         InstrumentAssignmentMethod
<InstrmAssgnmtMtd>
[0..1]  1937
{Or           Code <Cd> [1..1] CodeSet 1937
Or}           Proprietary <Prtry> [1..1] ± 1937
         VersionNumber <VrsnNb> [0..1] Quantity 1938
         ExpiryLocation <XpryLctn> [0..1] Text 1938
         Standardisation <Stdstn> [0..1]  1938
{Or           Code <Cd> [1..*] CodeSet 1938
Or}           Proprietary <Prtry> [1..1] ± 1939
         TradingPartyRole <TradgPtyRole> [0..1]  1939
{Or           Code <Cd> [1..*] CodeSet 1939
Or}           Proprietary <Prtry> [1..1] ± 1939
         ContractSize <CtrctSz> [0..1] Rate 1940
         AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1940
           AllocationPercentage <AllcnPctg> [0..1] Rate 1942
           Quantity <Qty> [0..1]  1942
{Or             Unit <Unit> [1..1] Quantity 1942
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1942
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1845 August 2026
```

## File page 1846

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           SettlementType <SttlmTp> [0..1]  1942
{Or             Code <Cd> [1..1] CodeSet 1943
Or}             Proprietary <Prtry> [1..1] ± 1943
           CashAmount <CshAmt> [0..1] Amount C1, C5 1943
           CashType <CshTp> [0..1] Text 1944
           Price <Pric> [0..1]  1944
             ValueType <ValTp> [0..1] CodeSet 1944
             Value <Val> [1..1] ± 1945
             PriceType <PricTp> [0..1] CodeSet 1945
           DirtyPrice <DrtyPric> [0..1]  1946
             ValueType <ValTp> [0..1] CodeSet 1946
             Value <Val> [1..1] ± 1947
             PriceType <PricTp> [0..1] CodeSet 1947
           EndPrice <EndPric> [0..1]  1948
             ValueType <ValTp> [0..1] CodeSet 1948
             Value <Val> [1..1] ± 1949
             PriceType <PricTp> [0..1] CodeSet 1949
           StartValue <StartVal> [0..1] Amount C1, C5 1950
           CurrentValue <CurVal> [0..1] Amount C1, C5 1950
           EndValue <EndVal> [0..1] Amount C1, C5 1951
           AdjustedQuantity <AdjstdQty> [0..1]  1951
{Or             Unit <Unit> [1..1] Quantity 1951
Or}             FaceAmount <FaceAmt> [1..1] Amount C1, C5 1952
           ExchangeRate <XchgRate> [0..1] Rate 1952
           CapValue <CapVal> [0..1] Amount C1, C5 1952
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*]  1952
     SecurityStatus <SctySts> [0..1]  1962
{Or       Code <Cd> [1..1] CodeSet 1962
Or}       Proprietary <Prtry> [1..1] ± 1962
     FinancialInstrumentName <FinInstrmNm> [0..*]  1963
       ISOShortName <ISOShrtNm> [0..1] Text 1963
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1846 August 2026
```

## File page 1847

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ISOLongName <ISOLngNm> [0..1] Text 1963
       ValidFrom <VldFr> [0..1] ± 1963
     DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 1963
     CertificateNumber <CertNb> [0..1] Text 1964
     ContractVersionNumber <CtrctVrsnNb> [0..1] Quantity 1964
     CouponAttachedNumber <CpnAttchdNb> [0..1] Text 1964
     TaxLotNumber <TaxLotNb> [0..1] Text 1964
     PoolNumber <PoolNb> [0..1] Text 1964
     CoveredIndicator <CvrdInd> [0..1] Indicator 1964
     LegalRestrictions <LglRstrctns> [0..1]  1964
{Or       Code <Cd> [1..1] CodeSet 1965
Or}       Proprietary <Prtry> [1..1] ± 1965
     PositionLimit <PosLmt> [0..1] ± 1965
     NearTermPositionLimit <NearTermPosLmt> [0..1] ± 1966
     ListingDate <ListgDt> [0..1] Date 1966
     RecordDate <RcrdDt> [0..1] DateTime 1966
     ExpiryDate <XpryDt> [0..1] Date 1966
     Purpose <Purp> [0..1] Text 1966
     ClassificationType <ClssfctnTp> [0..1]  1966
       ClassificationFinancialInstrument
<ClssfctnFinInstrm>
[0..1] IdentifierSet 1967
       FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 1967
       AlternateClassification <AltrnClssfctn> [0..*] ± 1967
     Issuance <Issnc> [0..1]  1967
       IssuePlace <IssePlc> [0..1] IdentifierSet 1968
       CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 1969
       IssueDate <IsseDt> [0..1] Date 1969
       AnnouncementDate <AnncmntDt> [0..1] DateTime 1969
       IssuerOrganisation <IssrOrg> [0..1]  1969
         Name <Nm> [1..1] Text 1970
         Identification <Id> [0..1]  1970
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1970
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1847 August 2026
```

