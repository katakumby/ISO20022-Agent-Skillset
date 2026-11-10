---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>"]
file_pages: [951, 952, 953, 954, 955, 956, 957, 958, 959, 960]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1 UpdateType <UpdTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 951 to 960.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 951

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1747
Or}           ProprietaryIdentification <PrtryId> [1..1] ± 1747
         Purpose <Purp> [0..1] Text 1747
         TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1748
         RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1748
         RegistrationDate <RegnDt> [0..1] Date 1748
         TaxIdentificationNumber <TaxIdNb> [0..1] Text 1748
         NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1748
         PostalAddress <PstlAdr> [1..5] ± C10 1748
         PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1749
         SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1749
     SupplementaryData <SplmtryData> [0..*] ± C14 1750
28.4.2.1  UpdateType <UpdTp>
Presence: [1..3]
Definition: Request to add, modify or delete data's of a security.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 951 August 2026
```

## File page 952

```text
UpdateType <UpdTp> contains one of the following UpdateType35Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Add <Add> [1..1]  998
     FinancialInstrumentType <FinInstrmTp> [0..*]  1014
       Equity <Eqty> [0..1]  1022
         PreferenceToIncome <PrefToIncm> [1..1]  1023
{Or           Code <Cd> [1..1] CodeSet 1023
Or}           Proprietary <Prtry> [1..1] ± 1023
         MaturityDate <MtrtyDt> [0..1] DateTime 1024
         NonPaidAmount <NonPdAmt> [0..1] Amount C1, C5 1024
         ParValue <ParVal> [0..1] Amount C1, C5 1024
         VotingRightsPerShare <VtngRghtsPerShr> [0..1] Quantity 1025
       Warrant <Warrt> [0..1]  1025
         Multiplier <Mltplr> [0..1] Rate 1026
         SubscriptionPrice <SbcptPric> [0..1]  1026
           ValueType <ValTp> [0..1] CodeSet 1027
           Value <Val> [1..1] ± 1027
           PriceType <PricTp> [0..1] CodeSet 1028
         Type <Tp> [0..1]  1028
{Or           Code <Cd> [1..1] CodeSet 1029
Or}           Proprietary <Prtry> [1..1] ± 1029
         WarrantAgent <WarrtAgt> [0..*]  1029
           Name <Nm> [1..1] Text 1030
           Identification <Id> [0..1]  1030
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1030
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1031
           Purpose <Purp> [0..1] Text 1031
           TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1031
           RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1031
           RegistrationDate <RegnDt> [0..1] Date 1032
           TaxIdentificationNumber <TaxIdNb> [0..1] Text 1032
           NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1032
           PostalAddress <PstlAdr> [1..5] ± C10 1032
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 952 August 2026
```

## File page 953

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1032
           SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1033
       Debt <Debt> [0..1]  C11,
C13
1033
         PaymentCurrency <PmtCcy> [0..1] CodeSet C1 1037
         FaceAmount <FaceAmt> [0..1] Amount C1, C5 1037
         PaymentFrequency <PmtFrqcy> [0..1] ± 1038
         InterestFixingDate <IntrstFxgDt> [0..1] DateTime 1038
         DatedDate <DtdDt> [0..1] DateTime 1038
         FirstPaymentDate <FrstPmtDt> [0..1] DateTime 1038
         MaturityDate <MtrtyDt> [0..1] DateTime 1038
         NextCouponDate <NxtCpnDt> [0..1] DateTime 1038
         PutableDate <PutblDt> [0..1] DateTime 1039
         NextCallableDate <NxtCllblDt> [0..1] DateTime 1039
         NextFactorDate <NxtFctrDt> [0..1] DateTime 1039
         ExpirationDate <XprtnDt> [0..1] DateTime 1039
         PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 1039
         InterestRate <IntrstRate> [0..1] Rate 1039
         NextInterestRate <NxtIntrstRate> [0..1] Rate 1039
         OddCouponIndicator <OddCpnInd> [0..1] Indicator 1039
         CallableIndicator <CllblInd> [0..1] Indicator 1040
         CPProgram <CPPrgm> [0..1] Quantity 1040
         CPRegistrationType <CPRegnTp> [0..1] Text 1040
         InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 1040
         PutableIndicator <PutblInd> [0..1] Indicator 1040
         PreFundedIndicator <PreFnddInd> [0..1] Indicator 1041
         EscrowedIndicator <EscrwdInd> [0..1] Indicator 1041
         PerpetualIndicator <PerptlInd> [0..1] Indicator 1041
         SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1041
         ExtendibleIndicator <XtndblInd> [0..1] Indicator 1041
         ExtendiblePeriod <XtndblPrd> [0..1]  1042
{Or           FromDateTime <FrDtTm> [1..1] DateTime 1042
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 953 August 2026
```

## File page 954

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           ToDateTime <ToDtTm> [1..1] DateTime 1042
Or}           DateTimeRange <DtTmRg> [1..1] ± 1042
         VariableRateIndicator <VarblRateInd> [0..1] Indicator 1042
         OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1043
         OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1043
         AmortisableIndicator <AmtsblInd> [0..1] Indicator 1043
         InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1043
         CapitalisedInterest <CptlsdIntrst> [0..1]  1043
{Or           Code <Cd> [1..1] CodeSet 1044
Or}           Proprietary <Prtry> [1..1] ± 1044
         ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1044
         CurrentFactor <CurFctr> [0..1] Rate 1045
         NextFactor <NxtFctr> [0..1] Rate 1045
         PreviousFactor <PrvsFctr> [0..1] Rate 1045
         Pieces <Pcs> [0..1] Quantity 1045
         PoolsMaximum <PlsMax> [0..1] Quantity 1045
         PoolsPerMillion <PlsPerMln> [0..1] Quantity 1045
         PoolsPerLot <PlsPerLot> [0..1] Quantity 1045
         PoolsPerTrade <PlsPerTrad> [0..1] Quantity 1046
         ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 1046
         LotIdentification <LotId> [0..1] Text 1046
         ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 1046
         WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 1046
         WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 1046
         WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1046
         WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1047
         InsuredIndicator <InsrdInd> [0..1] Indicator 1047
         BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1047
         YieldCalculation <YldClctn> [0..*]  1047
           Value <Val> [1..1] Rate 1048
           CalculationType <ClctnTp> [0..1]  1048
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 954 August 2026
```

## File page 955

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or             Code <Cd> [1..1] CodeSet 1048
Or}             Proprietary <Prtry> [1..1] ± 1051
           RedemptionPrice <RedPric> [0..1]  1051
             ValueType <ValTp> [0..1] CodeSet 1051
             Value <Val> [1..1] ± 1052
             PriceType <PricTp> [0..1] CodeSet 1052
           ValueDate <ValDt> [1..1] Date 1053
           ValuePeriod <ValPrd> [1..1]  1053
{Or             FromDateTime <FrDtTm> [1..1] DateTime 1053
Or             ToDateTime <ToDtTm> [1..1] DateTime 1054
Or}             DateTimeRange <DtTmRg> [1..1] ± 1054
           CalculationDate <ClctnDt> [1..1] DateTime 1054
         InterestType <IntrstTp> [0..1] CodeSet 1054
         InstrumentStructureType <InstrmStrTp> [0..1]  1054
{Or           Code <Cd> [1..1] CodeSet 1055
Or}           Proprietary <Prtry> [1..1] ± 1056
         GlobalType <GblTp> [0..1]  1056
{Or           Code <Cd> [1..1] CodeSet 1056
Or}           Proprietary <Prtry> [1..1] ± 1057
         PotentialEuroSystemEligibility
<PotntlEuroSysElgblty>
[0..1] Indicator 1057
         Geographics <Geogcs> [0..1] Text 1057
         YieldRange <YldRg> [0..1] ± 1057
         CouponRange <CpnRg> [0..1] ± 1058
         Purpose <Purp> [0..1] Text 1058
         AlternativeMinimumTaxIndicator
<AltrntvMinTaxInd>
[0..1] Indicator 1058
         AutoReinvestment <AutoRinvstmt> [0..1] Rate 1059
         Haircut <Hrcut> [0..1] Rate 1059
         TransactionConditions <TxConds> [0..1] ± 1059
         LookBack <LookBck> [0..1] Quantity 1059
         MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1059
         MinimumIncrement <MinIncrmt> [0..1] ± 1059
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 955 August 2026
```

## File page 956

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         MinimumQuantity <MinQty> [0..1] ± 1060
         Production <Pdctn> [0..1] Text 1060
         RestrictedIndicator <RstrctdInd> [0..1] Indicator 1060
         PriceFrequency <PricFrqcy> [0..1] ± 1060
         Sector <Sctr> [0..1] Text 1061
         SubstitutionFrequency <SbstitnFrqcy> [0..1] ± 1061
         SubstitutionLeft <SbstitnLft> [0..1] Quantity 1061
         WholePoolIndicator <WhlPoolInd> [0..1] Indicator 1061
         PriceSource <PricSrc> [0..1] Text 1061
         PriceRange <PricRg> [0..1] ± 1062
       Derivative <Deriv> [0..1]  1062
         Future <Futr> [0..1]  1066
           ContractSize <CtrctSz> [0..1] Rate 1068
           ExercisePrice <ExrcPric> [0..1]  1068
             ValueType <ValTp> [0..1] CodeSet 1068
             Value <Val> [1..1] ± 1069
             PriceType <PricTp> [0..1] CodeSet 1069
           FutureDate <FutrDt> [0..1] DateTime 1070
           MinimumSize <MinSz> [0..1] Amount C1, C5 1070
           UnitOfMeasure <UnitOfMeasr> [0..1]  1071
{Or             Code <Cd> [1..1] CodeSet 1071
Or}             Proprietary <Prtry> [1..1] ± 1073
           TimeUnit <TmUnit> [0..1]  1073
{Or             Code <Cd> [1..1] CodeSet 1074
Or}             Proprietary <Prtry> [1..1] ± 1074
           AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1074
             AllocationPercentage <AllcnPctg> [0..1] Rate 1076
             Quantity <Qty> [0..1]  1076
{Or               Unit <Unit> [1..1] Quantity 1076
Or}               FaceAmount <FaceAmt> [1..1] Amount C1, C5 1076
             SettlementType <SttlmTp> [0..1]  1076
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 956 August 2026
```

## File page 957

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or               Code <Cd> [1..1] CodeSet 1077
Or}               Proprietary <Prtry> [1..1] ± 1077
             CashAmount <CshAmt> [0..1] Amount C1, C5 1077
             CashType <CshTp> [0..1] Text 1078
             Price <Pric> [0..1]  1078
               ValueType <ValTp> [0..1] CodeSet 1078
               Value <Val> [1..1] ± 1079
               PriceType <PricTp> [0..1] CodeSet 1079
             DirtyPrice <DrtyPric> [0..1]  1080
               ValueType <ValTp> [0..1] CodeSet 1080
               Value <Val> [1..1] ± 1081
               PriceType <PricTp> [0..1] CodeSet 1081
             EndPrice <EndPric> [0..1]  1082
               ValueType <ValTp> [0..1] CodeSet 1082
               Value <Val> [1..1] ± 1083
               PriceType <PricTp> [0..1] CodeSet 1083
             StartValue <StartVal> [0..1] Amount C1, C5 1084
             CurrentValue <CurVal> [0..1] Amount C1, C5 1084
             EndValue <EndVal> [0..1] Amount C1, C5 1085
             AdjustedQuantity <AdjstdQty> [0..1]  1085
{Or               Unit <Unit> [1..1] Quantity 1085
Or}               FaceAmount <FaceAmt> [1..1] Amount C1, C5 1086
             ExchangeRate <XchgRate> [0..1] Rate 1086
             CapValue <CapVal> [0..1] Amount C1, C5 1086
         Option <Optn> [0..1]  1086
           OptionSettlementStyle <OptnSttlmStyle> [0..1]  1090
{Or             Code <Cd> [0..*] CodeSet 1090
Or}             Proprietary <Prtry> [1..1] ± 1090
           ConversionDate <ConvsDt> [0..1] DateTime 1090
           StrikePrice <StrkPric> [0..1]  1090
             ValueType <ValTp> [0..1] CodeSet 1091
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 957 August 2026
```

## File page 958

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Value <Val> [1..1] ± 1091
             PriceType <PricTp> [0..1] CodeSet 1092
           MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1092
           ConversionPeriod <ConvsPrd> [0..1]  1093
{Or             FromDateTime <FrDtTm> [1..1] DateTime 1093
Or             ToDateTime <ToDtTm> [1..1] DateTime 1093
Or}             DateTimeRange <DtTmRg> [1..1] ± 1093
           OptionStyle <OptnStyle> [0..1]  1094
{Or             Code <Cd> [1..1] CodeSet 1094
Or}             Proprietary <Prtry> [1..1] ± 1094
           OptionType <OptnTp> [0..1] ± 1094
           StrikeValue <StrkVal> [0..1] Quantity 1095
           StrikeMultiplier <StrkMltplr> [0..1] Quantity 1095
           InstrumentAssignmentMethod
<InstrmAssgnmtMtd>
[0..1]  1095
{Or             Code <Cd> [1..1] CodeSet 1095
Or}             Proprietary <Prtry> [1..1] ± 1095
           VersionNumber <VrsnNb> [0..1] Quantity 1096
           ExpiryLocation <XpryLctn> [0..1] Text 1096
           Standardisation <Stdstn> [0..1]  1096
{Or             Code <Cd> [1..*] CodeSet 1096
Or}             Proprietary <Prtry> [1..1] ± 1097
           TradingPartyRole <TradgPtyRole> [0..1]  1097
{Or             Code <Cd> [1..*] CodeSet 1097
Or}             Proprietary <Prtry> [1..1] ± 1097
           ContractSize <CtrctSz> [0..1] Rate 1098
           AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  1098
             AllocationPercentage <AllcnPctg> [0..1] Rate 1100
             Quantity <Qty> [0..1]  1100
{Or               Unit <Unit> [1..1] Quantity 1100
Or}               FaceAmount <FaceAmt> [1..1] Amount C1, C5 1100
             SettlementType <SttlmTp> [0..1]  1100
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 958 August 2026
```

## File page 959

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or               Code <Cd> [1..1] CodeSet 1101
Or}               Proprietary <Prtry> [1..1] ± 1101
             CashAmount <CshAmt> [0..1] Amount C1, C5 1101
             CashType <CshTp> [0..1] Text 1102
             Price <Pric> [0..1]  1102
               ValueType <ValTp> [0..1] CodeSet 1102
               Value <Val> [1..1] ± 1103
               PriceType <PricTp> [0..1] CodeSet 1103
             DirtyPrice <DrtyPric> [0..1]  1104
               ValueType <ValTp> [0..1] CodeSet 1104
               Value <Val> [1..1] ± 1105
               PriceType <PricTp> [0..1] CodeSet 1105
             EndPrice <EndPric> [0..1]  1106
               ValueType <ValTp> [0..1] CodeSet 1106
               Value <Val> [1..1] ± 1107
               PriceType <PricTp> [0..1] CodeSet 1107
             StartValue <StartVal> [0..1] Amount C1, C5 1108
             CurrentValue <CurVal> [0..1] Amount C1, C5 1108
             EndValue <EndVal> [0..1] Amount C1, C5 1109
             AdjustedQuantity <AdjstdQty> [0..1]  1109
{Or               Unit <Unit> [1..1] Quantity 1109
Or}               FaceAmount <FaceAmt> [1..1] Amount C1, C5 1110
             ExchangeRate <XchgRate> [0..1] Rate 1110
             CapValue <CapVal> [0..1] Amount C1, C5 1110
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*]  1110
       SecurityStatus <SctySts> [0..1]  1119
{Or         Code <Cd> [1..1] CodeSet 1119
Or}         Proprietary <Prtry> [1..1] ± 1120
       ISOSecurityLongName <ISOSctyLngNm> [0..1] Text 1120
       ISOSecurityShortName <ISOSctyShrtNm> [0..1] Text 1120
       NameValidFrom <NmVldFr> [0..1] ± 1120
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 959 August 2026
```

## File page 960

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 1120
       CertificateNumber <CertNb> [0..1] Text 1121
       ContractVersionNumber <CtrctVrsnNb> [0..1] Quantity 1121
       CouponAttachedNumber <CpnAttchdNb> [0..1] Text 1121
       TaxLotNumber <TaxLotNb> [0..1] Text 1121
       PoolNumber <PoolNb> [0..1] Text 1121
       CoveredIndicator <CvrdInd> [0..1] Indicator 1121
       LegalRestrictions <LglRstrctns> [0..1]  1122
{Or         Code <Cd> [1..1] CodeSet 1122
Or}         Proprietary <Prtry> [1..1] ± 1122
       PositionLimit <PosLmt> [0..1] ± 1122
       NearTermPositionLimit <NearTermPosLmt> [0..1] ± 1123
       ListingDate <ListgDt> [0..1] Date 1123
       RecordDate <RcrdDt> [0..1] DateTime 1123
       ExpiryDate <XpryDt> [0..1] Date 1123
       Purpose <Purp> [0..1] Text 1123
       ClassificationType <ClssfctnTp> [0..1]  1123
         ClassificationFinancialInstrument
<ClssfctnFinInstrm>
[0..1] IdentifierSet 1124
         FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 1124
         AlternateClassification <AltrnClssfctn> [0..*] ± 1124
       Issuance <Issnc> [0..1]  1124
         IssuePlace <IssePlc> [0..1] IdentifierSet 1126
         CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 1126
         IssueDate <IsseDt> [0..1] Date 1126
         AnnouncementDate <AnncmntDt> [0..1] DateTime 1126
         ISINValidFrom <ISINVldFr> [0..1] Date 1126
         IssuerOrganisation <IssrOrg> [0..1]  1126
           Name <Nm> [1..1] Text 1127
           Identification <Id> [0..1]  1127
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1127
Or}             ProprietaryIdentification <PrtryId> [1..1] ± 1128
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 960 August 2026
```

