---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["3 reda.007.001.01 SecurityMaintenanceRequestV01", "3.4 Message Building Blocks", "3.4.2 UpdateType <UpdTp>", "3.4.2.2 Replace <Rplc>"]
file_pages: [54, 55, 56, 57, 58, 59, 60, 61]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 3.4.2.2 Replace <Rplc>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 54 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 54

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
3.4.2.2  Replace <Rplc>
Presence: [1..1]
Definition: Request to replace all present data of a security.
Replace <Rplc> contains the following SecurityAttributes12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentType <FinInstrmTp> [0..*] ± 54
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*] ± 54
   SupplementaryData <SplmtryData> [0..*] ± C14 62
3.4.2.2.1  FinancialInstrumentType <FinInstrmTp>
Presence: [0..*]
Definition: Provides additional details about the financial instrument.
FinancialInstrumentType <FinInstrmTp> contains the following elements (see
"FinancialInstrument97" on page 237 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Equity <Eqty> [0..1] ± 237
   Warrant <Warrt> [0..1] ± 238
   Debt <Debt> [0..1] ± C11,
C13
239
   Derivative <Deriv> [0..1] ± 243
3.4.2.2.2  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..*]
Definition: Provides details about the financial instrument attributes of a particular leg.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities - Securities Reference Data 54 March 2024
```

## File page 55

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following elements (see
"CommonFinancialInstrumentAttributes12" on page 247 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityStatus <SctySts> [0..1]  255
{Or     Code <Cd> [1..1] CodeSet 255
Or}     Proprietary <Prtry> [1..1] ± 256
   ISOSecurityLongName <ISOSctyLngNm> [0..1] Text 256
   ISOSecurityShortName <ISOSctyShrtNm> [0..1] Text 256
   NameValidFrom <NmVldFr> [0..1] ± 256
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 256
   CertificateNumber <CertNb> [0..1] Text 257
   ContractVersionNumber <CtrctVrsnNb> [0..1] Quantity 257
   CouponAttachedNumber <CpnAttchdNb> [0..1] Text 257
   TaxLotNumber <TaxLotNb> [0..1] Text 257
   PoolNumber <PoolNb> [0..1] Text 257
   CoveredIndicator <CvrdInd> [0..1] Indicator 257
   LegalRestrictions <LglRstrctns> [0..1]  258
{Or     Code <Cd> [1..1] CodeSet 258
Or}     Proprietary <Prtry> [1..1] ± 258
   PositionLimit <PosLmt> [0..1] ± 258
   NearTermPositionLimit <NearTermPosLmt> [0..1] ± 259
   ListingDate <ListgDt> [0..1] Date 259
   RecordDate <RcrdDt> [0..1] DateTime 259
   ExpiryDate <XpryDt> [0..1] Date 259
   Purpose <Purp> [0..1] Text 259
   ClassificationType <ClssfctnTp> [0..1]  260
     ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 260
     FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 260
     AlternateClassification <AltrnClssfctn> [0..*] ± 260
   Issuance <Issnc> [0..1]  260
     IssuePlace <IssePlc> [0..1] IdentifierSet 262
     CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 262
     IssueDate <IsseDt> [0..1] Date 262
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities - Securities Reference Data 55 March 2024
```

## File page 56

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AnnouncementDate <AnncmntDt> [0..1] DateTime 262
     ISINValidFrom <ISINVldFr> [0..1] Date 262
     IssuerOrganisation <IssrOrg> [0..1]  262
       Name <Nm> [1..1] Text 263
       Identification <Id> [0..1]  263
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 263
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 264
       Purpose <Purp> [0..1] Text 264
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 264
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 264
       RegistrationDate <RegnDt> [0..1] Date 265
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 265
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 265
       PostalAddress <PstlAdr> [1..5] ± C10 265
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 265
       SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 266
     IssueNominalAmount <IsseNmnlAmt> [0..1] ± 266
     FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 266
     IssueSize <IsseSz> [0..1] Quantity 267
     IssuePrice <IssePric> [0..1] ± 267
     IssuanceDistribution <IssncDstrbtn> [0..1]  267
{Or       Code <Cd> [1..1] CodeSet 268
Or}       Proprietary <Prtry> [1..1] ± 268
     GoverningLaw <GovngLaw> [0..*]  268
       Identification <Id> [0..1] Text 268
       Country <Ctry> [0..1] CodeSet C4 268
   TradingMarket <TradgMkt> [0..*]  269
     MarketIdentification <MktId> [0..1] IdentifierSet 269
     RoundLot <RndLot> [0..1] ± 269
     TradeLotSize <TradLotSz> [0..1] ± 270
     SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 270
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities - Securities Reference Data 56 March 2024
```

## File page 57

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     MinimumTradedNominalQuantity <MinTraddNmnlQty> [0..1]  270
{Or       Unit <Unit> [1..1] Quantity 270
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 270
     MaximumTradedNominalQuantity <MaxTraddNmnlQty> [0..1]  271
{Or       Unit <Unit> [1..1] Quantity 271
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 271
     MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 272
     PrimaryPlaceOfListingIdentification <PmryPlcOfListgId> [0..1] IdentifierSet 272
   SpreadAndBenchmarkCurve <SprdAndBchmkCrv> [0..*]  272
     Spread <Sprd> [0..1] Quantity 272
     BenchmarkIdentification <BchmkId> [0..1] ± C1, C2,
C3, C4,
C5
273
     BenchmarkPrice <BchmkPric> [0..1]  274
       ValueType <ValTp> [0..1] CodeSet 274
       Value <Val> [1..1] ± 275
       PriceType <PricTp> [0..1] CodeSet 275
     BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 276
     BenchmarkCurveName <BchmkCrvNm> [0..1]  276
{Or       Code <Cd> [1..1] CodeSet 276
Or}       Proprietary <Prtry> [1..1] ± 277
     BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 278
   PutType <PutTp> [0..1]  278
{Or     Code <Cd> [1..1] CodeSet 278
Or}     Proprietary <Prtry> [1..1] ± 278
   CallType <CallTp> [0..1]  279
{Or     Code <Cd> [1..1] CodeSet 279
Or}     Proprietary <Prtry> [1..1] ± 279
   FungibleIndicator <FngbInd> [0..1] Indicator 279
   Confidential <Cnfdtl> [0..1] Indicator 280
   PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 280
   ConvertibleIndicator <ConvtblInd> [0..1] Indicator 280
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities - Securities Reference Data 57 March 2024
```

## File page 58

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ConversionPeriod <ConvsPrd> [0..1] ± 280
   ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 281
   ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 281
   PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 281
   TradingMethod <TradgMtd> [0..1]  281
{Or     Unit <Unit> [1..1] Quantity 282
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 282
   TEFRARule <TEFRARule> [0..1]  282
{Or     Code <Cd> [1..1] CodeSet 282
Or}     Proprietary <Prtry> [1..1] ± 283
   SerieNumber <SrNb> [0..1] Text 283
   Class <Clss> [0..1] Text 283
   WithholdingTaxRegime <WhldgTaxRgm> [0..*]  283
     WithholdingTaxValue <WhldgTaxVal> [1..1] ± 283
     Country <Ctry> [1..1] CodeSet C4 284
   PaymentStatus <PmtSts> [0..1] ± 284
   InitialPhysicalForm <InitlPhysForm> [0..1]  284
{Or     Code <Cd> [1..1] CodeSet 285
Or}     Proprietary <Prtry> [1..1] ± 285
   AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  285
{Or     Code <Cd> [1..1] CodeSet 285
Or}     Proprietary <Prtry> [1..1] ± 286
   CommonSafekeeper <CmonSfkpr> [0..1]  286
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 286
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 286
   RedemptionType <RedTp> [0..1]  287
{Or     Code <Cd> [1..1] CodeSet 287
Or}     Proprietary <Prtry> [1..1] ± 287
   RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 288
   Restriction <Rstrctn> [0..*]  288
     EffectivePeriod <FctvPrd> [0..1] ± 289
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities - Securities Reference Data 58 March 2024
```

## File page 59

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     RestrictionType <RstrctnTp> [0..1]  289
{Or       RestrictionType <RstrctnTp> [1..1] CodeSet 290
Or}       ProprietaryRestriction <PrtryRstrctn> [1..1] ± 290
     LegalRestrictionType <LglRstrctnTp> [0..1]  290
{Or       Code <Cd> [1..1] CodeSet 290
Or}       Proprietary <Prtry> [1..1] ± 291
     InvestorRestrictionType <InvstrRstrctnTp> [0..*]  291
{Or       Code <Cd> [1..1] CodeSet 291
Or}       Proprietary <Prtry> [1..1] ± 292
     InvestorType <InvstrTp> [0..*]  292
{Or       Code <Cd> [1..1] CodeSet 292
Or}       Proprietary <Prtry> [1..1] ± 292
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C1, C2,
C3, C4,
C5
293
   SettlementInformation <SttlmInf> [0..*]  294
     SecuritiesQuantityType <SctiesQtyTp> [0..1]  294
{Or       Code <Cd> [1..1] CodeSet 294
Or}       Proprietary <Prtry> [1..1] ± 295
     ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 295
     MinimumDenomination <MinDnmtn> [0..1] ± 295
     MinimumMultipleQuantity <MinMltplQty> [0..1] ± 295
     DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 296
   FinancialInstrumentForm <FinInstrmForm> [0..1]  296
     BookingAppearance <BookgApprnc> [0..1]  296
{Or       Code <Cd> [1..1] CodeSet 297
Or}       Proprietary <Prtry> [1..1] ± 297
     LegalForm <LglForm> [0..1] ± 297
   ContactName <CtctNm> [0..1]  298
     Name <Nm> [1..1] Text 298
     Identification <Id> [0..1]  298
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 299
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 299
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities - Securities Reference Data 59 March 2024
```

## File page 60

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Purpose <Purp> [0..1] Text 299
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 299
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 300
     RegistrationDate <RegnDt> [0..1] Date 300
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 300
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 300
     PostalAddress <PstlAdr> [1..5] ± C10 300
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 301
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 301
   LeadManager <LeadMgr> [0..1]  302
     Name <Nm> [1..1] Text 302
     Identification <Id> [0..1]  303
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 303
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 303
     Purpose <Purp> [0..1] Text 303
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 304
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 304
     RegistrationDate <RegnDt> [0..1] Date 304
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 304
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 304
     PostalAddress <PstlAdr> [1..5] ± C10 304
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 305
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 305
   PrincipalPayingAgent <PrncplPngAgt> [0..1]  306
     Name <Nm> [1..1] Text 306
     Identification <Id> [0..1]  307
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 307
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 307
     Purpose <Purp> [0..1] Text 307
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 308
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 308
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities - Securities Reference Data 60 March 2024
```

## File page 61

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     RegistrationDate <RegnDt> [0..1] Date 308
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 308
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 308
     PostalAddress <PstlAdr> [1..5] ± C10 308
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 309
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 309
   PayingAgent <PngAgt> [0..1]  310
     Name <Nm> [1..1] Text 310
     Identification <Id> [0..1]  311
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 311
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 311
     Purpose <Purp> [0..1] Text 311
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 312
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 312
     RegistrationDate <RegnDt> [0..1] Date 312
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 312
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 312
     PostalAddress <PstlAdr> [1..5] ± C10 312
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 313
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 313
   Depository <Dpstry> [0..1]  314
     Name <Nm> [1..1] Text 314
     Identification <Id> [0..1]  315
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 315
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 315
     Purpose <Purp> [0..1] Text 315
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 316
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 316
     RegistrationDate <RegnDt> [0..1] Date 316
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 316
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 316
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities - Securities Reference Data 61 March 2024
```

