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
file_pages: [1008, 1009, 1010, 1011, 1012, 1013]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# Continuation at file page 1008

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1008 to 1013.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1008

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         Code <Cd> [1..1] CodeSet 1132
Or}         Proprietary <Prtry> [1..1] ± 1132
       GoverningLaw <GovngLaw> [0..*]  1132
         Identification <Id> [0..1] Text 1132
         Country <Ctry> [0..1] CodeSet C4 1132
     TradingMarket <TradgMkt> [0..*]  1133
       MarketIdentification <MktId> [0..1] IdentifierSet 1133
       RoundLot <RndLot> [0..1] ± 1133
       TradeLotSize <TradLotSz> [0..1] ± 1134
       SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1134
       MinimumTradedNominalQuantity
<MinTraddNmnlQty>
[0..1]  1134
{Or         Unit <Unit> [1..1] Quantity 1134
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1134
       MaximumTradedNominalQuantity
<MaxTraddNmnlQty>
[0..1]  1135
{Or         Unit <Unit> [1..1] Quantity 1135
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1135
       MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 1136
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1008 August 2026
```

## File page 1009

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         Code <Cd> [1..1] CodeSet 1140
Or}         Proprietary <Prtry> [1..1] ± 1141
       BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 1142
     PutType <PutTp> [0..1]  1142
{Or       Code <Cd> [1..1] CodeSet 1142
Or}       Proprietary <Prtry> [1..1] ± 1142
     CallType <CallTp> [0..1]  1143
{Or       Code <Cd> [1..1] CodeSet 1143
Or}       Proprietary <Prtry> [1..1] ± 1143
     FungibleIndicator <FngbInd> [0..1] Indicator 1143
     Confidential <Cnfdtl> [0..1] Indicator 1144
     PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 1144
     ConvertibleIndicator <ConvtblInd> [0..1] Indicator 1144
     ConversionPeriod <ConvsPrd> [0..1] ± 1144
     ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 1145
     ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 1145
     PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 1145
     TradingMethod <TradgMtd> [0..1]  1145
{Or       Unit <Unit> [1..1] Quantity 1146
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1146
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1009 August 2026
```

## File page 1010

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TEFRARule <TEFRARule> [0..1]  1146
{Or       Code <Cd> [1..1] CodeSet 1146
Or}       Proprietary <Prtry> [1..1] ± 1147
     SerieNumber <SrNb> [0..1] Text 1147
     Class <Clss> [0..1] Text 1147
     WithholdingTaxRegime <WhldgTaxRgm> [0..*]  1147
       WithholdingTaxValue <WhldgTaxVal> [1..1] ± 1147
       Country <Ctry> [1..1] CodeSet C4 1148
     PaymentStatus <PmtSts> [0..1] ± 1148
     InitialPhysicalForm <InitlPhysForm> [0..1]  1148
{Or       Code <Cd> [1..1] CodeSet 1149
Or}       Proprietary <Prtry> [1..1] ± 1149
     AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  1149
{Or       Code <Cd> [1..1] CodeSet 1149
Or}       Proprietary <Prtry> [1..1] ± 1150
     CommonSafekeeper <CmonSfkpr> [0..1]  1150
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1150
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1150
     RedemptionType <RedTp> [0..1]  1151
{Or       Code <Cd> [1..1] CodeSet 1151
Or}       Proprietary <Prtry> [1..1] ± 1151
     RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 1152
     Restriction <Rstrctn> [0..*]  1152
       EffectivePeriod <FctvPrd> [0..1] ± 1153
       RestrictionType <RstrctnTp> [0..1]  1153
{Or         RestrictionType <RstrctnTp> [1..1] CodeSet 1154
Or}         ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1154
       LegalRestrictionType <LglRstrctnTp> [0..1]  1154
{Or         Code <Cd> [1..1] CodeSet 1154
Or}         Proprietary <Prtry> [1..1] ± 1155
       InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1155
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1010 August 2026
```

## File page 1011

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         Code <Cd> [1..1] CodeSet 1155
Or}         Proprietary <Prtry> [1..1] ± 1156
       InvestorType <InvstrTp> [0..*]  1156
{Or         Code <Cd> [1..1] CodeSet 1156
Or}         Proprietary <Prtry> [1..1] ± 1156
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C6, C7,
C8, C9,
C12
1157
     SettlementInformation <SttlmInf> [0..*]  1158
       SecuritiesQuantityType <SctiesQtyTp> [0..1]  1158
{Or         Code <Cd> [1..1] CodeSet 1158
Or}         Proprietary <Prtry> [1..1] ± 1159
       ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 1159
       MinimumDenomination <MinDnmtn> [0..1] ± 1159
       MinimumMultipleQuantity <MinMltplQty> [0..1] ± 1159
       DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 1160
     FinancialInstrumentForm <FinInstrmForm> [0..1]  1160
       BookingAppearance <BookgApprnc> [0..1]  1160
{Or         Code <Cd> [1..1] CodeSet 1161
Or}         Proprietary <Prtry> [1..1] ± 1161
       LegalForm <LglForm> [0..1] ± 1161
     ContactName <CtctNm> [0..1]  1162
       Name <Nm> [1..1] Text 1162
       Identification <Id> [0..1]  1162
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1163
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1163
       Purpose <Purp> [0..1] Text 1163
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1163
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1164
       RegistrationDate <RegnDt> [0..1] Date 1164
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1164
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1164
       PostalAddress <PstlAdr> [1..5] ± C10 1164
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1011 August 2026
```

## File page 1012

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1165
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1165
     LeadManager <LeadMgr> [0..1]  1166
       Name <Nm> [1..1] Text 1166
       Identification <Id> [0..1]  1167
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1167
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1167
       Purpose <Purp> [0..1] Text 1167
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1168
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1168
       RegistrationDate <RegnDt> [0..1] Date 1168
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1168
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1168
       PostalAddress <PstlAdr> [1..5] ± C10 1168
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1169
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1169
     PrincipalPayingAgent <PrncplPngAgt> [0..1]  1170
       Name <Nm> [1..1] Text 1170
       Identification <Id> [0..1]  1171
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1171
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1171
       Purpose <Purp> [0..1] Text 1171
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1172
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1172
       RegistrationDate <RegnDt> [0..1] Date 1172
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1172
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1172
       PostalAddress <PstlAdr> [1..5] ± C10 1172
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1173
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1173
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1012 August 2026
```

## File page 1013

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PayingAgent <PngAgt> [0..1]  1174
       Name <Nm> [1..1] Text 1174
       Identification <Id> [0..1]  1175
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1175
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1175
       Purpose <Purp> [0..1] Text 1175
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1176
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1176
       RegistrationDate <RegnDt> [0..1] Date 1176
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1176
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1176
       PostalAddress <PstlAdr> [1..5] ± C10 1176
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1177
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1177
     Depository <Dpstry> [0..1]  1178
       Name <Nm> [1..1] Text 1178
       Identification <Id> [0..1]  1179
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1179
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 1179
       Purpose <Purp> [0..1] Text 1179
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1180
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1180
       RegistrationDate <RegnDt> [0..1] Date 1180
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 1180
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1180
       PostalAddress <PstlAdr> [1..5] ± C10 1180
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1181
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 1181
     UnderlyingRisk <UndrlygRsk> [0..1]  1182
       Name <Nm> [1..1] Text 1182
       Identification <Id> [0..1]  1183
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1013 August 2026
```

