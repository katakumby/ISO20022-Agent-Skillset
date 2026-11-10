---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["2 reda.006.001.01 SecurityCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 Security <Scty>", "2.4.2.2 FinancialInstrumentType <FinInstrmTp>"]
file_pages: [12, 13, 14, 15, 16, 17, 18, 19]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 2.4.2.2 FinancialInstrumentType <FinInstrmTp>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 12 to 19.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 12

```text
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
2.4.2.2  FinancialInstrumentType <FinInstrmTp>
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
2.4.2.3  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..*]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities - Securities Reference Data 12 March 2024
```

## File page 13

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following elements (see
"CommonFinancialInstrumentAttributes10" on page 401 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityStatus <SctySts> [0..1]  409
{Or     Code <Cd> [1..1] CodeSet 409
Or}     Proprietary <Prtry> [1..1] ± 409
   ISOSecurityLongName <ISOSctyLngNm> [0..1] Text 410
   ISOSecurityShortName <ISOSctyShrtNm> [0..1] Text 410
   NameValidFrom <NmVldFr> [0..1] ± 410
   DenominationCurrency <DnmtnCcy> [1..1] CodeSet C2 410
   CertificateNumber <CertNb> [0..1] Text 411
   ContractVersionNumber <CtrctVrsnNb> [0..1] Quantity 411
   CouponAttachedNumber <CpnAttchdNb> [0..1] Text 411
   TaxLotNumber <TaxLotNb> [0..1] Text 411
   PoolNumber <PoolNb> [0..1] Text 411
   CoveredIndicator <CvrdInd> [0..1] Indicator 411
   LegalRestrictions <LglRstrctns> [0..1]  411
{Or     Code <Cd> [1..1] CodeSet 412
Or}     Proprietary <Prtry> [1..1] ± 412
   PositionLimit <PosLmt> [0..1] ± 412
   NearTermPositionLimit <NearTermPosLmt> [0..1] ± 413
   ListingDate <ListgDt> [0..1] Date 413
   RecordDate <RcrdDt> [0..1] DateTime 413
   ExpiryDate <XpryDt> [0..1] Date 413
   Purpose <Purp> [0..1] Text 413
   ClassificationType <ClssfctnTp> [0..1]  414
     ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 414
     FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 414
     AlternateClassification <AltrnClssfctn> [0..*] ± 414
   Issuance <Issnc> [0..1]  414
     IssuePlace <IssePlc> [0..1] IdentifierSet 416
     CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 416
     IssueDate <IsseDt> [0..1] Date 416
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities - Securities Reference Data 13 March 2024
```

## File page 14

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AnnouncementDate <AnncmntDt> [0..1] DateTime 416
     ISINValidFrom <ISINVldFr> [0..1] Date 416
     IssuerOrganisation <IssrOrg> [0..1]  416
       Name <Nm> [1..1] Text 417
       Identification <Id> [0..1]  417
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 417
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 418
       Purpose <Purp> [0..1] Text 418
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 418
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 418
       RegistrationDate <RegnDt> [0..1] Date 419
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 419
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 419
       PostalAddress <PstlAdr> [1..5] ± C10 419
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 419
       SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 420
     IssueNominalAmount <IsseNmnlAmt> [0..1] ± 420
     FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 420
     IssueSize <IsseSz> [0..1] Quantity 421
     IssuePrice <IssePric> [0..1] ± 421
     IssuanceDistribution <IssncDstrbtn> [0..1]  421
{Or       Code <Cd> [1..1] CodeSet 422
Or}       Proprietary <Prtry> [1..1] ± 422
     GoverningLaw <GovngLaw> [0..*]  422
       Identification <Id> [0..1] Text 422
       Country <Ctry> [0..1] CodeSet C4 422
   TradingMarket <TradgMkt> [0..*]  423
     MarketIdentification <MktId> [0..1] IdentifierSet 423
     RoundLot <RndLot> [0..1] ± 423
     TradeLotSize <TradLotSz> [0..1] ± 424
     SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 424
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities - Securities Reference Data 14 March 2024
```

## File page 15

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     MinimumTradedNominalQuantity <MinTraddNmnlQty> [0..1]  424
{Or       Unit <Unit> [1..1] Quantity 424
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 424
     MaximumTradedNominalQuantity <MaxTraddNmnlQty> [0..1]  425
{Or       Unit <Unit> [1..1] Quantity 425
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 425
     MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 426
     PrimaryPlaceOfListingIdentification <PmryPlcOfListgId> [0..1] IdentifierSet 426
   SpreadAndBenchmarkCurve <SprdAndBchmkCrv> [0..*]  426
     Spread <Sprd> [0..1] Quantity 426
     BenchmarkIdentification <BchmkId> [0..1] ± C1, C2,
C3, C4,
C5
427
     BenchmarkPrice <BchmkPric> [0..1]  428
       ValueType <ValTp> [0..1] CodeSet 428
       Value <Val> [1..1] ± 429
       PriceType <PricTp> [0..1] CodeSet 429
     BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 430
     BenchmarkCurveName <BchmkCrvNm> [0..1]  430
{Or       Code <Cd> [1..1] CodeSet 430
Or}       Proprietary <Prtry> [1..1] ± 431
     BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 432
   PutType <PutTp> [0..1]  432
{Or     Code <Cd> [1..1] CodeSet 432
Or}     Proprietary <Prtry> [1..1] ± 432
   CallType <CallTp> [0..1]  433
{Or     Code <Cd> [1..1] CodeSet 433
Or}     Proprietary <Prtry> [1..1] ± 433
   FungibleIndicator <FngbInd> [0..1] Indicator 433
   Confidential <Cnfdtl> [0..1] Indicator 434
   PrivatePlacement <PrvtPlcmnt> [0..1] Indicator 434
   ConvertibleIndicator <ConvtblInd> [0..1] Indicator 434
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities - Securities Reference Data 15 March 2024
```

## File page 16

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ConversionPeriod <ConvsPrd> [0..1] ± 434
   ConversionRatioNumerator <ConvsRatioNmrtr> [0..1] ± 435
   ConversionRatioDenominator <ConvsRatioDnmtr> [0..1] ± 435
   PrimaryPlaceOfDeposit <PmryPlcOfDpst> [0..1] ± 435
   TradingMethod <TradgMtd> [0..1]  435
{Or     Unit <Unit> [1..1] Quantity 436
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 436
   TEFRARule <TEFRARule> [0..1]  436
{Or     Code <Cd> [1..1] CodeSet 436
Or}     Proprietary <Prtry> [1..1] ± 437
   SerieNumber <SrNb> [0..1] Text 437
   Class <Clss> [0..1] Text 437
   WithholdingTaxRegime <WhldgTaxRgm> [0..*]  437
     WithholdingTaxValue <WhldgTaxVal> [1..1] ± 437
     Country <Ctry> [1..1] CodeSet C4 438
   PaymentStatus <PmtSts> [0..1] ± 438
   InitialPhysicalForm <InitlPhysForm> [0..1]  438
{Or     Code <Cd> [1..1] CodeSet 439
Or}     Proprietary <Prtry> [1..1] ± 439
   AfterExchangePhysicalForm <AftrXchgPhysForm> [0..1]  439
{Or     Code <Cd> [1..1] CodeSet 439
Or}     Proprietary <Prtry> [1..1] ± 440
   CommonSafekeeper <CmonSfkpr> [0..1] IdentifierSet C3 440
   RedemptionType <RedTp> [0..1]  440
{Or     Code <Cd> [1..1] CodeSet 440
Or}     Proprietary <Prtry> [1..1] ± 441
   RedemptionPaymentCurrency <RedPmtCcy> [0..1] CodeSet C1 441
   Restriction <Rstrctn> [0..*]  441
     EffectivePeriod <FctvPrd> [0..1] ± 442
     RestrictionType <RstrctnTp> [0..1]  442
{Or       RestrictionType <RstrctnTp> [1..1] CodeSet 443
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities - Securities Reference Data 16 March 2024
```

## File page 17

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       ProprietaryRestriction <PrtryRstrctn> [1..1] ± 443
     LegalRestrictionType <LglRstrctnTp> [0..1]  443
{Or       Code <Cd> [1..1] CodeSet 443
Or}       Proprietary <Prtry> [1..1] ± 444
     InvestorRestrictionType <InvstrRstrctnTp> [0..*]  444
{Or       Code <Cd> [1..1] CodeSet 444
Or}       Proprietary <Prtry> [1..1] ± 445
     InvestorType <InvstrTp> [0..*]  445
{Or       Code <Cd> [1..1] CodeSet 445
Or}       Proprietary <Prtry> [1..1] ± 445
   SettlementInformation <SttlmInf> [0..*]  446
     SecuritiesQuantityType <SctiesQtyTp> [0..1]  446
{Or       Code <Cd> [1..1] CodeSet 446
Or}       Proprietary <Prtry> [1..1] ± 447
     ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 447
     MinimumDenomination <MinDnmtn> [0..1] ± 447
     MinimumMultipleQuantity <MinMltplQty> [0..1] ± 447
     DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 448
   FinancialInstrumentForm <FinInstrmForm> [0..1]  448
     BookingAppearance <BookgApprnc> [0..1]  448
{Or       Code <Cd> [1..1] CodeSet 449
Or}       Proprietary <Prtry> [1..1] ± 449
     LegalForm <LglForm> [0..1] ± 449
   ContactName <CtctNm> [0..1]  450
     Name <Nm> [1..1] Text 450
     Identification <Id> [0..1]  450
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 451
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 451
     Purpose <Purp> [0..1] Text 451
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 451
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 452
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities - Securities Reference Data 17 March 2024
```

## File page 18

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     RegistrationDate <RegnDt> [0..1] Date 452
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 452
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 452
     PostalAddress <PstlAdr> [1..5] ± C10 452
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 453
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 453
   LeadManager <LeadMgr> [0..1]  454
     Name <Nm> [1..1] Text 454
     Identification <Id> [0..1]  455
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 455
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 455
     Purpose <Purp> [0..1] Text 455
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 456
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 456
     RegistrationDate <RegnDt> [0..1] Date 456
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 456
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 456
     PostalAddress <PstlAdr> [1..5] ± C10 456
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 457
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 457
   PrincipalPayingAgent <PrncplPngAgt> [0..1]  458
     Name <Nm> [1..1] Text 458
     Identification <Id> [0..1]  459
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 459
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 459
     Purpose <Purp> [0..1] Text 459
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 460
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 460
     RegistrationDate <RegnDt> [0..1] Date 460
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 460
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 460
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities - Securities Reference Data 18 March 2024
```

## File page 19

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PostalAddress <PstlAdr> [1..5] ± C10 460
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 461
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 461
   PayingAgent <PngAgt> [0..1]  462
     Name <Nm> [1..1] Text 462
     Identification <Id> [0..1]  463
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 463
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 463
     Purpose <Purp> [0..1] Text 463
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 464
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 464
     RegistrationDate <RegnDt> [0..1] Date 464
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 464
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 464
     PostalAddress <PstlAdr> [1..5] ± C10 464
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 465
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 465
   Depository <Dpstry> [0..1]  466
     Name <Nm> [1..1] Text 466
     Identification <Id> [0..1]  467
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 467
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 467
     Purpose <Purp> [0..1] Text 467
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 468
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 468
     RegistrationDate <RegnDt> [0..1] Date 468
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 468
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 468
     PostalAddress <PstlAdr> [1..5] ± C10 468
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 469
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 469
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities - Securities Reference Data 19 March 2024
```

