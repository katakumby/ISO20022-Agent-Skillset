---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.2 Structure"]
file_pages: [293, 294, 295, 296, 297]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 293 to 297.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 293

```text
15.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FndRefDataRpt> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 300
   PreviousReference <PrvsRef> [0..*] ± 301
   RelatedReference <RltdRef> [0..1] ± 301
   FundReferenceDataReportIdentification <FndRefDataRptId> [0..1] Text 301
   Report <Rpt> [1..*]  C4, C5 301
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
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 293 May 2026
```

## File page 294

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C6 315
       RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C6 315
       ProductType <PdctTp> [0..1]  316
{Or         Code <Cd> [1..1] CodeSet 316
Or}         Proprietary <Prtry> [1..1] ± 316
       Issuer <Issr> [0..1] ± 317
       IssuerProductGovernanceProcess <IssrPdctGovncPrc> [0..1] ± 317
       ProductCategory <PdctCtgy> [0..1] Text 317
       ProductCategoryGermany <PdctCtgyDE> [0..1] Text 318
       NotionalOrUnitBased <NtnlOrUnitBased> [0..1]  318
{Or         Code <Cd> [1..1] CodeSet 318
Or}         Proprietary <Prtry> [1..1] ± 318
       QuotationType <QtnTp> [0..1] ± 319
       LeveragedOrContingentLiability <LvrgdOrCntngntLblty> [0..1] Indicator 319
       NoRetrocessionIndicator <NoRtrcssnInd> [0..1] Indicator 319
       ExPostCostCalculationBasis <ExPstCostClctnBsis> [0..1]  320
{Or         Code <Cd> [1..1] CodeSet 320
Or}         Proprietary <Prtry> [1..1] ± 320
       AdditionalInformation <AddtlInf> [0..*] ± 320
     FundParties <FndPties> [0..1] ± 321
     MainFundOrderDesk <MainFndOrdrDsk> [0..1] ± 321
     FundManagementCompany <FndMgmtCpny> [0..1] ± 321
     FundDetails <FndDtls> [0..1] ± 322
     ValuationDealingCharacteristics <ValtnDealgChrtcs> [0..1] ± 324
     InvestmentRestrictions <InvstmtRstrctns> [0..1] ± 324
     SubscriptionProcessingCharacteristics <SbcptPrcgChrtcs> [0..1] ± C8 325
     RedemptionProcessingCharacteristics <RedPrcgChrtcs> [0..1] ± C9 327
     SwitchProcessingCharacteristics <SwtchPrcgChrtcs> [0..1] ± C10 328
     PlanCharacteristics <PlanChrtcs> [0..*] ± C20 329
     PaymentInstrument <PmtInstrm> [0..*] ± 330
     CashSettlementDetails <CshSttlmDtls> [0..*]  331
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 294 May 2026
```

## File page 295

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       Currency <Ccy> [0..1] CodeSet C1 331
       PrimaryAccount <PmryAcct> [0..1]  331
         AccountIdentification <AcctId> [1..1]  332
           Identification <Id> [1..1] ± 332
           Name <Nm> [0..1] Text 332
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
       SubscriptionProcessingCharacteristics <SbcptPrcgChrtcs> [0..1] ± C8 336
       RedemptionProcessingCharacteristics <RedPrcgChrtcs> [0..1] ± C11 338
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
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 295 May 2026
```

## File page 296

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Servicer <Svcr> [0..1] IdentifierSet C2 344
           AccountTypeDescription <AcctTpDesc> [0..1] Text 344
       AdditionalInformation <AddtlInf> [0..*] ± 344
     TargetMarket <TrgtMkt> [0..1]  345
       ReferenceDate <RefDt> [0..1] Date 347
       InvestorType <InvstrTp> [0..1]  347
         InvestorTypeRetail <InvstrTpRtl> [0..1] CodeSet 347
         InvestorTypeProfessional <InvstrTpPrfssnl> [0..1] ± 348
         InvestorTypeEligibleCounterparty <InvstrTpElgblCtrPty> [0..1] CodeSet 348
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
         NotForInvestorsWithTheLowestRiskToleranceGermany
<NotForInvstrsWthTheLwstRskTlrnceDE>
[0..1] CodeSet 354
         Other <Othr> [0..*] ± 354
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 296 May 2026
```

## File page 297

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       ClientObjectivesAndNeeds <ClntObjctvsAndNeeds> [0..1]  354
         ReturnProfilePreservation <RtrPrflPrsrvtn> [0..1] CodeSet 355
         ReturnProfileGrowth <RtrPrflGrwth> [0..1] CodeSet 355
         ReturnProfileIncome <RtrPrflIncm> [0..1] CodeSet 356
         ReturnProfileHedging <RtrPrflHdgg> [0..1] CodeSet 356
         OptionOrLeveragedReturnProfile <OptnOrLvrgdRtrPrfl> [0..1] CodeSet 356
         ReturnProfilePensionSchemeGermany
<RtrPrflPnsnSchmeDE>
[0..1] CodeSet 356
         MinimumHoldingPeriod <MinHldgPrd> [0..1] ± 357
         SustainabilityPreferences <SstnbltyPrefs> [0..1] CodeSet 357
         OtherSpecificInvestmentNeed <OthrSpcfcInvstmtNeed> [0..1] ± 357
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
Investment Funds - Maintenance 2025 - 2026 297 May 2026
```

