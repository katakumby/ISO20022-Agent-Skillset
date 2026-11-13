---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.1.1.4 Derivative <Deriv>", "28.4.2.1.1.1.4.2 Option <Optn>", "28.4.2.1.1.1.4.2.16 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "28.4.2.1.1.1.4.2.16.12 AdjustedQuantity <AdjstdQty>", "28.4.2.1.1.1.4.2.16.12.2 FaceAmount <FaceAmt>"]
file_pages: [1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.1.4.2.16.12.2 FaceAmount <FaceAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1110 to 1118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1110

```text
Datatype: "DecimalNumber" on page 3324
28.4.2.1.1.1.4.2.16.12.2  FaceAmount <FaceAmt>
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
28.4.2.1.1.1.4.2.16.13  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Foreign exchange rate used to compute the current value.
Datatype: "PercentageRate" on page 3325
28.4.2.1.1.1.4.2.16.14  CapValue <CapVal>
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
28.4.2.1.1.2  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..*]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1110 August 2026
```

## File page 1111

```text
Definition: Provides details about the financial instrument attributes of a particular leg.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1111 August 2026
```

## File page 1112

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following
CommonFinancialInstrumentAttributes12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityStatus <SctySts> [0..1]  1119
{Or     Code <Cd> [1..1] CodeSet 1119
Or}     Proprietary <Prtry> [1..1] ± 1120
   ISOSecurityLongName <ISOSctyLngNm> [0..1] Text 1120
   ISOSecurityShortName <ISOSctyShrtNm> [0..1] Text 1120
   NameValidFrom <NmVldFr> [0..1] ± 1120
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 1120
   CertificateNumber <CertNb> [0..1] Text 1121
   ContractVersionNumber <CtrctVrsnNb> [0..1] Quantity 1121
   CouponAttachedNumber <CpnAttchdNb> [0..1] Text 1121
   TaxLotNumber <TaxLotNb> [0..1] Text 1121
   PoolNumber <PoolNb> [0..1] Text 1121
   CoveredIndicator <CvrdInd> [0..1] Indicator 1121
   LegalRestrictions <LglRstrctns> [0..1]  1122
{Or     Code <Cd> [1..1] CodeSet 1122
Or}     Proprietary <Prtry> [1..1] ± 1122
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1112 August 2026
```

## File page 1113

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IssueDate <IsseDt> [0..1] Date 1126
     AnnouncementDate <AnncmntDt> [0..1] DateTime 1126
     ISINValidFrom <ISINVldFr> [0..1] Date 1126
     IssuerOrganisation <IssrOrg> [0..1]  1126
       Name <Nm> [1..1] Text 1127
       Identification <Id> [0..1]  1127
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1127
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1128
       Purpose <Purp> [0..1] Text 1128
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1128
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1128
       RegistrationDate <RegnDt> [0..1] Date 1129
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1129
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1129
       PostalAddress <PstlAdr> [1..5] ± C10 1129
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1129
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1130
     IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1130
     FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1130
     IssueSize <IsseSz> [0..1] Quantity 1131
     IssuePrice <IssePric> [0..1] ± 1131
     IssuanceDistribution <IssncDstrbtn> [0..1]  1131
{Or       Code <Cd> [1..1] CodeSet 1132
Or}       Proprietary <Prtry> [1..1] ± 1132
     GoverningLaw <GovngLaw> [0..*]  1132
       Identification <Id> [0..1] Text 1132
       Country <Ctry> [0..1] CodeSet C4 1132
   TradingMarket <TradgMkt> [0..*]  1133
     MarketIdentification <MktId> [0..1] IdentifierSet 1133
     RoundLot <RndLot> [0..1] ± 1133
     TradeLotSize <TradLotSz> [0..1] ± 1134
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1113 August 2026
```

## File page 1114

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1134
     MinimumTradedNominalQuantity
<MinTraddNmnlQty>
[0..1]  1134
{Or       Unit <Unit> [1..1] Quantity 1134
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1134
     MaximumTradedNominalQuantity
<MaxTraddNmnlQty>
[0..1]  1135
{Or       Unit <Unit> [1..1] Quantity 1135
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1135
     MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 1136
     PrimaryPlaceOfListingIdentification
<PmryPlcOfListgId>
[0..1] IdentifierSet 1136
   SpreadAndBenchmarkCurve <SprdAndBchmkCrv> [0..*]  1136
     Spread <Sprd> [0..1] Quantity 1136
     BenchmarkIdentification <BchmkId> [0..1] ± C6, C7,
C8, C9,
C12
1137
     BenchmarkPrice <BchmkPric> [0..1]  1138
       ValueType <ValTp> [0..1] CodeSet 1138
       Value <Val> [1..1] ± 1139
       PriceType <PricTp> [0..1] CodeSet 1139
     BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 1140
     BenchmarkCurveName <BchmkCrvNm> [0..1]  1140
{Or       Code <Cd> [1..1] CodeSet 1140
Or}       Proprietary <Prtry> [1..1] ± 1141
     BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 1142
   PutType <PutTp> [0..1]  1142
{Or     Code <Cd> [1..1] CodeSet 1142
Or}     Proprietary <Prtry> [1..1] ± 1142
   CallType <CallTp> [0..1]  1143
{Or     Code <Cd> [1..1] CodeSet 1143
Or}     Proprietary <Prtry> [1..1] ± 1143
   FungibleIndicator <FngbInd> [0..1] Indicator 1143
   Confidential <Cnfdtl> [0..1] Indicator 1144
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1114 August 2026
```

## File page 1115

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 1144
   ConvertibleIndicator <ConvtblInd> [0..1] Indicator 1144
   ConversionPeriod <ConvsPrd> [0..1] ± 1144
   ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 1145
   ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 1145
   PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 1145
   TradingMethod <TradgMtd> [0..1]  1145
{Or     Unit <Unit> [1..1] Quantity 1146
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1146
   TEFRARule <TEFRARule> [0..1]  1146
{Or     Code <Cd> [1..1] CodeSet 1146
Or}     Proprietary <Prtry> [1..1] ± 1147
   SerieNumber <SrNb> [0..1] Text 1147
   Class <Clss> [0..1] Text 1147
   WithholdingTaxRegime <WhldgTaxRgm> [0..*]  1147
     WithholdingTaxValue <WhldgTaxVal> [1..1] ± 1147
     Country <Ctry> [1..1] CodeSet C4 1148
   PaymentStatus <PmtSts> [0..1] ± 1148
   InitialPhysicalForm <InitlPhysForm> [0..1]  1148
{Or     Code <Cd> [1..1] CodeSet 1149
Or}     Proprietary <Prtry> [1..1] ± 1149
   AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  1149
{Or     Code <Cd> [1..1] CodeSet 1149
Or}     Proprietary <Prtry> [1..1] ± 1150
   CommonSafekeeper <CmonSfkpr> [0..1]  1150
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1150
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 1150
   RedemptionType <RedTp> [0..1]  1151
{Or     Code <Cd> [1..1] CodeSet 1151
Or}     Proprietary <Prtry> [1..1] ± 1151
   RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 1152
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1115 August 2026
```

## File page 1116

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Restriction <Rstrctn> [0..*]  1152
     EffectivePeriod <FctvPrd> [0..1] ± 1153
     RestrictionType <RstrctnTp> [0..1]  1153
{Or       RestrictionType <RstrctnTp> [1..1] CodeSet 1154
Or}       ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1154
     LegalRestrictionType <LglRstrctnTp> [0..1]  1154
{Or       Code <Cd> [1..1] CodeSet 1154
Or}       Proprietary <Prtry> [1..1] ± 1155
     InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1155
{Or       Code <Cd> [1..1] CodeSet 1155
Or}       Proprietary <Prtry> [1..1] ± 1156
     InvestorType <InvstrTp> [0..*]  1156
{Or       Code <Cd> [1..1] CodeSet 1156
Or}       Proprietary <Prtry> [1..1] ± 1156
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C6, C7,
C8, C9,
C12
1157
   SettlementInformation <SttlmInf> [0..*]  1158
     SecuritiesQuantityType <SctiesQtyTp> [0..1]  1158
{Or       Code <Cd> [1..1] CodeSet 1158
Or}       Proprietary <Prtry> [1..1] ± 1159
     ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 1159
     MinimumDenomination <MinDnmtn> [0..1] ± 1159
     MinimumMultipleQuantity <MinMltplQty> [0..1] ± 1159
     DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 1160
   FinancialInstrumentForm <FinInstrmForm> [0..1]  1160
     BookingAppearance <BookgApprnc> [0..1]  1160
{Or       Code <Cd> [1..1] CodeSet 1161
Or}       Proprietary <Prtry> [1..1] ± 1161
     LegalForm <LglForm> [0..1] ± 1161
   ContactName <CtctNm> [0..1]  1162
     Name <Nm> [1..1] Text 1162
     Identification <Id> [0..1]  1162
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1116 August 2026
```

## File page 1117

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1163
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1163
     Purpose <Purp> [0..1] Text 1163
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1163
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1164
     RegistrationDate <RegnDt> [0..1] Date 1164
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1164
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1164
     PostalAddress <PstlAdr> [1..5] ± C10 1164
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1165
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1165
   LeadManager <LeadMgr> [0..1]  1166
     Name <Nm> [1..1] Text 1166
     Identification <Id> [0..1]  1167
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1167
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1167
     Purpose <Purp> [0..1] Text 1167
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1168
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1168
     RegistrationDate <RegnDt> [0..1] Date 1168
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1168
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1168
     PostalAddress <PstlAdr> [1..5] ± C10 1168
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1169
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1169
   PrincipalPayingAgent <PrncplPngAgt> [0..1]  1170
     Name <Nm> [1..1] Text 1170
     Identification <Id> [0..1]  1171
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1171
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1171
     Purpose <Purp> [0..1] Text 1171
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1117 August 2026
```

## File page 1118

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1172
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1172
     RegistrationDate <RegnDt> [0..1] Date 1172
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1172
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1172
     PostalAddress <PstlAdr> [1..5] ± C10 1172
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1173
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1173
   PayingAgent <PngAgt> [0..1]  1174
     Name <Nm> [1..1] Text 1174
     Identification <Id> [0..1]  1175
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1175
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1175
     Purpose <Purp> [0..1] Text 1175
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1176
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1176
     RegistrationDate <RegnDt> [0..1] Date 1176
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1176
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1176
     PostalAddress <PstlAdr> [1..5] ± C10 1176
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1177
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1177
   Depository <Dpstry> [0..1]  1178
     Name <Nm> [1..1] Text 1178
     Identification <Id> [0..1]  1179
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1179
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1179
     Purpose <Purp> [0..1] Text 1179
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1180
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1180
     RegistrationDate <RegnDt> [0..1] Date 1180
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1118 August 2026
```

