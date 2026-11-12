---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.2 PreviousReference <PrvsRef>"]
file_pages: [301, 302, 303, 304, 305, 306, 307]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.2 PreviousReference <PrvsRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 301 to 307.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 301

```text
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
15.4.2 PreviousReference <PrvsRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
15.4.3 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
15.4.4 FundReferenceDataReportIdentification
<FndRefDataRptId>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the fund reference data report, as assigned by the
issuer of the report.
Datatype: "Max35Text" on page 5403
15.4.5 Report <Rpt>
Presence: [1..*]
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 301 May 2026
```

## File page 302

```text
Definition: Fund reference data.
Impacted by: C4 "CostsAndCharges1Guideline", C5 "CostsAndCharges2Guideline"
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 302 May 2026
```

## File page 303

```text
Report <Rpt> contains the following FundReferenceDataReport5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 308
   Version <Vrsn> [0..1] ± 308
   AuthorisedProxy <AuthrsdPrxy> [0..1] ± 308
   GeneralReferenceDate <GnlRefDt> [1..1] Date 309
   TargetMarketIndicator <TrgtMktInd> [0..1] Indicator 309
   ExAnteIndicator <ExAnteInd> [0..1] Indicator 309
   ExPostIndicator <ExPstInd> [0..1] Indicator 309
   SecurityIdentification <SctyId> [1..1]  310
     Identification <Id> [1..1]  C12,
C13,
C21,
C22,
C27
312
       OtherIdentification <OthrId> [0..*]  313
         Identification <Id> [1..1] Text 313
         Suffix <Sfx> [0..1] Text 313
         Type <Tp> [1..1] ± 313
       Description <Desc> [0..1] Text 314
       ISIN <ISIN> [0..1] IdentifierSet 314
     Name <Nm> [1..1] Text 314
     ShortName <ShrtNm> [0..1] Text 314
     ClassType <ClssTp> [0..1] Text 314
     UmbrellaName <UmbrllNm> [0..1] Text 314
     NewUmbrella <NewUmbrll> [0..1] Indicator 314
     ClassificationType <ClssfctnTp> [0..1] ± 315
     BaseCurrency <BaseCcy> [0..1] CodeSet C1 315
     CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C6 315
     RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C6 315
     ProductType <PdctTp> [0..1]  316
{Or       Code <Cd> [1..1] CodeSet 316
Or}       Proprietary <Prtry> [1..1] ± 316
     Issuer <Issr> [0..1] ± 317
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 303 May 2026
```

## File page 304

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IssuerProductGovernanceProcess
<IssrPdctGovncPrc>
[0..1] ± 317
     ProductCategory <PdctCtgy> [0..1] Text 317
     ProductCategoryGermany <PdctCtgyDE> [0..1] Text 318
     NotionalOrUnitBased <NtnlOrUnitBased> [0..1]  318
{Or       Code <Cd> [1..1] CodeSet 318
Or}       Proprietary <Prtry> [1..1] ± 318
     QuotationType <QtnTp> [0..1] ± 319
     LeveragedOrContingentLiability
<LvrgdOrCntngntLblty>
[0..1] Indicator 319
     NoRetrocessionIndicator <NoRtrcssnInd> [0..1] Indicator 319
     ExPostCostCalculationBasis <ExPstCostClctnBsis> [0..1]  320
{Or       Code <Cd> [1..1] CodeSet 320
Or}       Proprietary <Prtry> [1..1] ± 320
     AdditionalInformation <AddtlInf> [0..*] ± 320
   FundParties <FndPties> [0..1] ± 321
   MainFundOrderDesk <MainFndOrdrDsk> [0..1] ± 321
   FundManagementCompany <FndMgmtCpny> [0..1] ± 321
   FundDetails <FndDtls> [0..1] ± 322
   ValuationDealingCharacteristics <ValtnDealgChrtcs> [0..1] ± 324
   InvestmentRestrictions <InvstmtRstrctns> [0..1] ± 324
   SubscriptionProcessingCharacteristics
<SbcptPrcgChrtcs>
[0..1] ± C8 325
   RedemptionProcessingCharacteristics
<RedPrcgChrtcs>
[0..1] ± C9 327
   SwitchProcessingCharacteristics <SwtchPrcgChrtcs> [0..1] ± C10 328
   PlanCharacteristics <PlanChrtcs> [0..*] ± C20 329
   PaymentInstrument <PmtInstrm> [0..*] ± 330
   CashSettlementDetails <CshSttlmDtls> [0..*]  331
     Currency <Ccy> [0..1] CodeSet C1 331
     PrimaryAccount <PmryAcct> [0..1]  331
       AccountIdentification <AcctId> [1..1]  332
         Identification <Id> [1..1] ± 332
         Name <Nm> [0..1] Text 332
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 304 May 2026
```

## File page 305

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Servicer <Svcr> [0..1] IdentifierSet C2 332
       AccountTypeDescription <AcctTpDesc> [0..1] Text 333
     SecondaryAccount <ScndryAcct> [0..1]  333
       AccountIdentification <AcctId> [1..1]  333
         Identification <Id> [1..1] ± 333
         Name <Nm> [0..1] Text 334
       Servicer <Svcr> [0..1] IdentifierSet C2 334
       AccountTypeDescription <AcctTpDesc> [0..1] Text 334
   LocalMarketAnnex <LclMktAnx> [0..*]  334
     Country <Ctry> [1..*] CodeSet C6 335
     LocalOrderDesk <LclOrdrDsk> [1..1] ± 336
     SubscriptionProcessingCharacteristics
<SbcptPrcgChrtcs>
[0..1] ± C8 336
     RedemptionProcessingCharacteristics
<RedPrcgChrtcs>
[0..1] ± C11 338
     SwitchProcessingCharacteristics <SwtchPrcgChrtcs> [0..1] ± C10 339
     CashSettlementDetails <CshSttlmDtls> [0..*]  340
       Currency <Ccy> [0..1] CodeSet C1 341
       PrimaryAccount <PmryAcct> [0..1]  341
         AccountIdentification <AcctId> [1..1]  342
           Identification <Id> [1..1] ± 342
           Name <Nm> [0..1] Text 342
         Servicer <Svcr> [0..1] IdentifierSet C2 342
         AccountTypeDescription <AcctTpDesc> [0..1] Text 343
       SecondaryAccount <ScndryAcct> [0..1]  343
         AccountIdentification <AcctId> [1..1]  343
           Identification <Id> [1..1] ± 343
           Name <Nm> [0..1] Text 344
         Servicer <Svcr> [0..1] IdentifierSet C2 344
         AccountTypeDescription <AcctTpDesc> [0..1] Text 344
     AdditionalInformation <AddtlInf> [0..*] ± 344
   TargetMarket <TrgtMkt> [0..1]  345
     ReferenceDate <RefDt> [0..1] Date 347
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 305 May 2026
```

## File page 306

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     InvestorType <InvstrTp> [0..1]  347
       InvestorTypeRetail <InvstrTpRtl> [0..1] CodeSet 347
       InvestorTypeProfessional <InvstrTpPrfssnl> [0..1] ± 348
       InvestorTypeEligibleCounterparty
<InvstrTpElgblCtrPty>
[0..1] CodeSet 348
       Other <Othr> [0..*] ± 348
     KnowledgeAndOrExperience <KnwldgAndOrExprnc> [0..1]  349
       BasicInvestor <BsicInvstr> [0..1] CodeSet 349
       InformedInvestor <InfrmdInvstr> [0..1] CodeSet 349
       AdvancedInvestor <AdvncdInvstr> [0..1] CodeSet 350
       ExpertInvestorGermany <ExprtInvstrDE> [0..1] CodeSet 350
       Other <Othr> [0..*] ± 350
     AbilityToBearLosses <AbltyToBearLosses> [0..1]  351
       NoCapitalLoss <NoCptlLoss> [0..1] CodeSet 351
       LimitedCapitalLoss <LtdCptlLoss> [0..1] CodeSet 351
       LimitedCapitalLossLevel <LtdCptlLossLvl> [0..1] Rate 352
       NoCapitalGuarantee <NoCptlGrnt> [0..1] CodeSet 352
       LossBeyondCapital <LossByndCptl> [0..1] CodeSet 352
       Other <Othr> [0..*] ± 352
     RiskTolerance <RskTlrnce> [0..1]  353
       RiskTolerancePRIIPSMethodology
<RskTlrncePRIIPSMthdlgy>
[0..1] Quantity 353
       RiskToleranceUCITSMethodology
<RskTlrnceUCITSMthdlgy>
[0..1] Quantity 353
       RiskToleranceInternal <RskTlrnceIntl> [0..1] CodeSet 353
       RiskToleranceForNonPRIIPSAndNonUCITSSpain
<RskTlrnceForNonPRIIPSAndNonUCITSES>
[0..1] Quantity 354
       NotForInvestorsWithTheLowestRiskToleranceGer
many <NotForInvstrsWthTheLwstRskTlrnceDE>
[0..1] CodeSet 354
       Other <Othr> [0..*] ± 354
     ClientObjectivesAndNeeds <ClntObjctvsAndNeeds> [0..1]  354
       ReturnProfilePreservation <RtrPrflPrsrvtn> [0..1] CodeSet 355
       ReturnProfileGrowth <RtrPrflGrwth> [0..1] CodeSet 355
       ReturnProfileIncome <RtrPrflIncm> [0..1] CodeSet 356
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 306 May 2026
```

## File page 307

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ReturnProfileHedging <RtrPrflHdgg> [0..1] CodeSet 356
       OptionOrLeveragedReturnProfile
<OptnOrLvrgdRtrPrfl>
[0..1] CodeSet 356
       ReturnProfilePensionSchemeGermany
<RtrPrflPnsnSchmeDE>
[0..1] CodeSet 356
       MinimumHoldingPeriod <MinHldgPrd> [0..1] ± 357
       SustainabilityPreferences <SstnbltyPrefs> [0..1] CodeSet 357
       OtherSpecificInvestmentNeed
<OthrSpcfcInvstmtNeed>
[0..1] ± 357
       Other <Othr> [0..*] ± 358
     Other <Othr> [0..*] ± 358
   DistributionStrategy <DstrbtnStrtgy> [0..1] ± 358
   CostsAndCharges <CostsAndChrgs> [0..2] ± C16,
C19
358
   AdditionalInformationUKMarket <AddtlInfUKMkt> [0..1]  359
     FinancialInstrumentTransactionCostsExAnteUK
<FinInstrmTxCostsExAnteUK>
[0..1] Rate 360
     FinancialInstrumentTransactionCostsExPostUK
<FinInstrmTxCostsExPstUK>
[0..1] Rate 360
   ValueForMoney <ValForMny> [0..1]  C3, C28,
C29,
C30
360
     EMTDataReportingVFMUK <EMTDataRptgVFMUK> [0..1] CodeSet 362
     AssessmentOfValueRequiredUnderCOLLUK
<AssmntOfValReqrdUdrCOLLUK>
[0..1] CodeSet 362
     OutcomeOfCOLLAssessmentOfValueUK
<OutcmOfCOLLAssmntOfValUK>
[0..1] CodeSet 362
     OutcomeOfPRINValueAssessmentOrReviewUK
<OutcmOfPRINValAssmntOrRvwUK>
[0..1] CodeSet 362
     OtherReviewRelatedToValueAndOrChargesUK
<OthrRvwRltdToValAndOrChrgsUK>
[0..1] CodeSet 363
     FurtherInformationUK <FrthrInfUK> [0..1] Text 363
     ReviewDateUK <RvwDtUK> [0..1] Date 363
     ReviewNextDueUK <RvwNxtDueUK> [0..1] Date 363
   Extension <Xtnsn> [0..*] ± C17 363
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 307 May 2026
```

