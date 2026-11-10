---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["7 reda.012.001.01 SecurityReportV01", "7.4 Message Building Blocks", "7.4.3 SecurityReportOrError <SctyRptOrErr>", "7.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "7.4.3.1.1 SecurityReport <SctyRpt>", "7.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [102, 103, 104, 105, 106, 107, 108, 109, 110]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 7.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 102 to 110.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 102

```text
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
7.4.3.1.1.3  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..*]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 102 March 2024
```

## File page 103

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following elements (see
"CommonFinancialInstrumentAttributes11" on page 322 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityStatus <SctySts> [0..1]  330
{Or     Code <Cd> [1..1] CodeSet 331
Or}     Proprietary <Prtry> [1..1] ± 331
   FinancialInstrumentName <FinInstrmNm> [0..*]  331
     ISOShortName <ISOShrtNm> [0..1] Text 332
     ISOLongName <ISOLngNm> [0..1] Text 332
     ValidFrom <VldFr> [0..1] ± 332
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 332
   CertificateNumber <CertNb> [0..1] Text 332
   ContractVersionNumber <CtrctVrsnNb> [0..1] Quantity 332
   CouponAttachedNumber <CpnAttchdNb> [0..1] Text 333
   TaxLotNumber <TaxLotNb> [0..1] Text 333
   PoolNumber <PoolNb> [0..1] Text 333
   CoveredIndicator <CvrdInd> [0..1] Indicator 333
   LegalRestrictions <LglRstrctns> [0..1]  333
{Or     Code <Cd> [1..1] CodeSet 333
Or}     Proprietary <Prtry> [1..1] ± 334
   PositionLimit <PosLmt> [0..1] ± 334
   NearTermPositionLimit <NearTermPosLmt> [0..1] ± 334
   ListingDate <ListgDt> [0..1] Date 335
   RecordDate <RcrdDt> [0..1] DateTime 335
   ExpiryDate <XpryDt> [0..1] Date 335
   Purpose <Purp> [0..1] Text 335
   ClassificationType <ClssfctnTp> [0..1]  335
     ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 336
     FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 336
     AlternateClassification <AltrnClssfctn> [0..*] ± 336
   Issuance <Issnc> [0..1]  336
     IssuePlace <IssePlc> [0..1] IdentifierSet 337
     CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 338
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 103 March 2024
```

## File page 104

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IssueDate <IsseDt> [0..1] Date 338
     AnnouncementDate <AnncmntDt> [0..1] DateTime 338
     IssuerOrganisation <IssrOrg> [0..1]  338
       Name <Nm> [1..1] Text 339
       Identification <Id> [0..1]  339
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 339
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 340
       Purpose <Purp> [0..1] Text 340
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 340
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 340
       RegistrationDate <RegnDt> [0..1] Date 341
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 341
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 341
       PostalAddress <PstlAdr> [1..5] ± C10 341
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 341
       SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 342
     IssueNominalAmount <IsseNmnlAmt> [0..1] ± 342
     FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 342
     IssueSize <IsseSz> [0..1] Quantity 343
     IssuePrice <IssePric> [0..1] ± 343
     IssuanceDistribution <IssncDstrbtn> [0..1]  343
{Or       Code <Cd> [1..1] CodeSet 344
Or}       Proprietary <Prtry> [1..1] ± 344
     GoverningLaw <GovngLaw> [0..*]  344
       Identification <Id> [0..1] Text 344
       Country <Ctry> [0..1] CodeSet C4 344
   TradingMarket <TradgMkt> [0..*]  345
     MarketIdentification <MktId> [0..1] IdentifierSet 345
     RoundLot <RndLot> [0..1] ± 345
     TradeLotSize <TradLotSz> [0..1] ± 346
     SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 346
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 104 March 2024
```

## File page 105

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     MinimumTradedNominalQuantity <MinTraddNmnlQty> [0..1]  346
{Or       Unit <Unit> [1..1] Quantity 346
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 346
     MaximumTradedNominalQuantity <MaxTraddNmnlQty> [0..1]  347
{Or       Unit <Unit> [1..1] Quantity 347
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 347
     MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 348
     PrimaryPlaceOfListingIdentification <PmryPlcOfListgId> [0..1] IdentifierSet 348
   SpreadAndBenchmarkCurve <SprdAndBchmkCrv> [0..*]  348
     Spread <Sprd> [0..1] Quantity 348
     BenchmarkIdentification <BchmkId> [0..1] ± C1, C2,
C3, C4,
C5
349
     BenchmarkPrice <BchmkPric> [0..1]  350
       ValueType <ValTp> [0..1] CodeSet 350
       Value <Val> [1..1] ± 351
       PriceType <PricTp> [0..1] CodeSet 351
     BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 352
     BenchmarkCurveName <BchmkCrvNm> [0..1]  352
{Or       Code <Cd> [1..1] CodeSet 352
Or}       Proprietary <Prtry> [1..1] ± 353
     BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 354
   PutType <PutTp> [0..1]  354
{Or     Code <Cd> [1..1] CodeSet 354
Or}     Proprietary <Prtry> [1..1] ± 354
   CallType <CallTp> [0..1]  355
{Or     Code <Cd> [1..1] CodeSet 355
Or}     Proprietary <Prtry> [1..1] ± 355
   FungibleIndicator <FngbInd> [0..1] Indicator 355
   Confidential <Cnfdtl> [0..1] Indicator 356
   PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 356
   ConvertibleIndicator <ConvtblInd> [0..1] Indicator 356
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 105 March 2024
```

## File page 106

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ConversionPeriod <ConvsPrd> [0..1] ± 356
   ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 357
   ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 357
   PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 357
   TradingMethod <TradgMtd> [0..1]  357
{Or     Unit <Unit> [1..1] Quantity 358
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 358
   TEFRARule <TEFRARule> [0..1]  358
{Or     Code <Cd> [1..1] CodeSet 358
Or}     Proprietary <Prtry> [1..1] ± 359
   SerieNumber <SrNb> [0..1] Text 359
   Class <Clss> [0..1] Text 359
   WithholdingTaxRegime <WhldgTaxRgm> [0..*]  359
     WithholdingTaxValue <WhldgTaxVal> [1..1] ± 359
     Country <Ctry> [1..1] CodeSet C4 360
   PaymentStatus <PmtSts> [0..1] ± 360
   InitialPhysicalForm <InitlPhysForm> [0..1]  360
{Or     Code <Cd> [1..1] CodeSet 361
Or}     Proprietary <Prtry> [1..1] ± 361
   AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  361
{Or     Code <Cd> [1..1] CodeSet 361
Or}     Proprietary <Prtry> [1..1] ± 362
   CommonSafekeeper <CmonSfkpr> [0..1]  362
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 362
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 362
   RedemptionType <RedTp> [0..1]  363
{Or     Code <Cd> [1..1] CodeSet 363
Or}     Proprietary <Prtry> [1..1] ± 363
   RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 364
   Restriction <Rstrctn> [0..*]  364
     EffectivePeriod <FctvPrd> [0..1] ± 365
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 106 March 2024
```

## File page 107

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     RestrictionType <RstrctnTp> [0..1]  365
{Or       RestrictionType <RstrctnTp> [1..1] CodeSet 366
Or}       ProprietaryRestriction <PrtryRstrctn> [1..1] ± 366
     LegalRestrictionType <LglRstrctnTp> [0..1]  366
{Or       Code <Cd> [1..1] CodeSet 366
Or}       Proprietary <Prtry> [1..1] ± 367
     InvestorRestrictionType <InvstrRstrctnTp> [0..*]  367
{Or       Code <Cd> [1..1] CodeSet 367
Or}       Proprietary <Prtry> [1..1] ± 368
     InvestorType <InvstrTp> [0..*]  368
{Or       Code <Cd> [1..1] CodeSet 368
Or}       Proprietary <Prtry> [1..1] ± 368
   FinancialInstrumentIdentificationValidity
<FinInstrmIdVldty>
[0..*]  369
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C1, C2,
C3, C4,
C5
369
     ISINValidFrom <ISINVldFr> [0..1] Date 370
   SettlementInformation <SttlmInf> [0..*]  370
     SecuritiesQuantityType <SctiesQtyTp> [0..1]  371
{Or       Code <Cd> [1..1] CodeSet 371
Or}       Proprietary <Prtry> [1..1] ± 371
     ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 372
     MinimumDenomination <MinDnmtn> [0..1] ± 372
     MinimumMultipleQuantity <MinMltplQty> [0..1] ± 372
     DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 372
   FinancialInstrumentForm <FinInstrmForm> [0..1]  373
     BookingAppearance <BookgApprnc> [0..1]  373
{Or       Code <Cd> [1..1] CodeSet 373
Or}       Proprietary <Prtry> [1..1] ± 374
     LegalForm <LglForm> [0..1] ± 374
   ContactName <CtctNm> [0..1]  374
     Name <Nm> [1..1] Text 375
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 107 March 2024
```

## File page 108

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Identification <Id> [0..1]  375
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 375
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 376
     Purpose <Purp> [0..1] Text 376
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 376
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 376
     RegistrationDate <RegnDt> [0..1] Date 377
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 377
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 377
     PostalAddress <PstlAdr> [1..5] ± C10 377
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 377
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 378
   LeadManager <LeadMgr> [0..1]  378
     Name <Nm> [1..1] Text 379
     Identification <Id> [0..1]  379
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 379
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 380
     Purpose <Purp> [0..1] Text 380
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 380
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 380
     RegistrationDate <RegnDt> [0..1] Date 381
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 381
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 381
     PostalAddress <PstlAdr> [1..5] ± C10 381
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 381
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 382
   PrincipalPayingAgent <PrncplPngAgt> [0..1]  382
     Name <Nm> [1..1] Text 383
     Identification <Id> [0..1]  383
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 383
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 384
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 108 March 2024
```

## File page 109

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Purpose <Purp> [0..1] Text 384
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 384
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 384
     RegistrationDate <RegnDt> [0..1] Date 385
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 385
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 385
     PostalAddress <PstlAdr> [1..5] ± C10 385
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 385
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 386
   PayingAgent <PngAgt> [0..1]  386
     Name <Nm> [1..1] Text 387
     Identification <Id> [0..1]  387
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 387
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 388
     Purpose <Purp> [0..1] Text 388
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 388
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 388
     RegistrationDate <RegnDt> [0..1] Date 389
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 389
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 389
     PostalAddress <PstlAdr> [1..5] ± C10 389
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 389
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 390
   Depository <Dpstry> [0..1]  390
     Name <Nm> [1..1] Text 391
     Identification <Id> [0..1]  391
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 391
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 392
     Purpose <Purp> [0..1] Text 392
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 392
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 392
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 109 March 2024
```

## File page 110

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     RegistrationDate <RegnDt> [0..1] Date 393
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 393
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 393
     PostalAddress <PstlAdr> [1..5] ± C10 393
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 393
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 394
   UnderlyingRisk <UndrlygRsk> [0..1]  394
     Name <Nm> [1..1] Text 395
     Identification <Id> [0..1]  395
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 395
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 396
     Purpose <Purp> [0..1] Text 396
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 396
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 396
     RegistrationDate <RegnDt> [0..1] Date 397
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 397
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 397
     PostalAddress <PstlAdr> [1..5] ± C10 397
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 397
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 398
   SecurityCSDLink <SctyCSDLk> [0..*]  398
     ValidFrom <VldFr> [1..1] ± 399
     ValidTo <VldTo> [0..1] ± 399
     SecurityMaintenance <SctyMntnc> [0..1] Indicator 399
     IssuerCSD <IssrCSD> [0..1] ± 400
     InvestorCSD <InvstrCSD> [0..1] ± 400
     TechnicalIssuerCSD <TechIssrCSD> [0..1] ± 400
     IssuanceAccount <IssncAcct> [0..*]  400
       IssuanceAccount <IssncAcct> [1..1] ± 401
       PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 401
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 110 March 2024
```

