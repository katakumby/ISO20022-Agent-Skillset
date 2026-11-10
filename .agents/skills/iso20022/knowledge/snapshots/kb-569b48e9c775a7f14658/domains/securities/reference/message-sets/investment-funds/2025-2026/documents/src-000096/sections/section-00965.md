---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.1 MasterReference <MstrRef>"]
file_pages: [1341, 1342, 1343, 1344]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1341 to 1344.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1341

```text
38.4.15.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
38.4.15.2  TransferIdentification <TrfId>
Presence: [1..1]
Definition: Identification assigned to the transfer of assets.
Datatype: "Max35Text" on page 5403
38.4.15.3  TransferConfirmationIdentification <TrfConfId>
Presence: [0..1]
Definition: Identification of the confirmation assigned by the transferor to the transfer.
Datatype: "Max35Text" on page 5403
38.4.15.4  Portfolio <Prtfl>
Presence: [0..1]
Definition: Choice of tax efficient product, general investment or pension.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1341 May 2026
```

## File page 1342

```text
Portfolio <Prtfl> contains one of the following FundPortfolio7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TaxEfficientProduct <TaxEffcntPdct> [1..1]  1345
     TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 1347
     CurrentYear <CurYr> [0..1] Indicator 1347
     CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1348
     PreviousYears <PrvsYrs> [0..1]  C42 1348
       PreviousYears <PrvsYrs> [1..1]  1348
{Or         AllPreviousYears <AllPrvsYrs> [1..1] Text 1348
Or}         SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1349
       CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1349
     PreviousYearSubscriptionAmount
<PrvsYrSbcptAmt>
[0..1] Amount C1 1349
     PreviousYearsSubscriptionAmount
<PrvsYrsSbcptAmt>
[0..1] Amount C1 1349
     DateOfFirstSubscription <DtOfFrstSbcpt> [0..1] Date 1349
     CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C45 1350
       DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1350
       EquityComponent <EqtyCmpnt> [0..1] Amount C1 1350
       CashComponent <CshCmpnt> [0..1] Amount C1 1350
       TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1351
     BonusOrWithdrawal <BnsOrWdrwl> [0..*]  1351
       TypeOfAmount <TpOfAmt> [1..1]  1352
{Or         Code <Cd> [1..1] CodeSet 1352
Or}         Proprietary <Prtry> [1..1] ± 1352
       Amount <Amt> [0..1] Amount C2 1352
       Reason <Rsn> [0..1]  1353
{Or         Code <Cd> [1..1] CodeSet 1353
Or}         Proprietary <Prtry> [1..1] ± 1353
       UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1353
       Outstanding <Outsdng> [0..1] Indicator 1354
       Reference <Ref> [0..1] Text 1354
       AdditionalInformation <AddtlInf> [0..*] ± 1354
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1342 May 2026
```

## File page 1343

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     WithdrawalForResidentialPurchaseProgress
<WdrwlForResdtlPurchsPrgrs>
[0..1] Indicator 1354
     TransferorAlternateIdentification <TrfrAltrnId> [0..1] Text 1354
     TotalSubscriptionAmount <TtlSbcptAmt> [0..1] Amount C1, C15 1355
     OtherAmount <OthrAmt> [0..*]  1355
       Type <Tp> [1..1] ± 1355
       Amount <Amt> [1..1] Amount C1, C15 1355
     DateFirstQualifyingAddition <DtFrstQlfygAddtn> [0..1] Date 1356
     InvestorTaxReference <InvstrTaxRef> [0..1]  1356
       Type <Tp> [0..1]  1356
{Or         Code <Cd> [1..1] CodeSet 1356
Or}         Proprietary <Prtry> [1..1] ± 1357
       Reference <Ref> [1..1] Text 1357
     InvestmentsToFollowValue <InvstmtsToFllwVal> [0..*] ± 1357
     InnovativeFinance <InnvtvFinc> [0..*]  1357
       Type <Tp> [1..1] ± 1358
       Information <Inf> [1..1] Text 1358
     LowestInvestedAmountCurrentYear
<LwstInvstdAmtCurYr>
[0..1] Amount C1 1358
     TaxCalculationBase <TaxClctnBase> [0..1] Amount C1 1358
     UnusedTaxDeduction <UusdTaxDdctn> [0..1] Amount C1 1359
     CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 1359
     EstimatedValue <EstmtdVal> [0..1] ± 1359
     AdditionalInformation <AddtlInf> [0..*] ± 1360
Or   GeneralInvestment <GnlInvstmt> [1..1] ± 1360
Or}   Pension <Pnsn> [1..1]  C9, C10,
C36,
C37,
C38,
C39,
C43,
C44,
C47
1360
     Identification <Id> [0..1]  1363
       Identifier <Idr> [1..1] Text 1364
       SubIdentifier <SubIdr> [0..1] Text 1364
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1343 May 2026
```

## File page 1344

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AdditionalInformation <AddtlInf> [0..1] ± 1364
     Type <Tp> [1..1]  1364
{Or       Code <Cd> [1..1] CodeSet 1364
Or}       Proprietary <Prtry> [1..1] ± 1365
     TransferScope <TrfScp> [0..1] ± 1366
     TaxReference <TaxRef> [0..*] ± 1366
     DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1366
     DrawdownStatus <DrwdwnSts> [0..1] ± 1366
     DrawdownType <DrwdwnTp> [0..1] ± 1367
     NumberOfDrawdownTranches <NbOfDrwdwnTrnchs> [0..1] Quantity 1367
     EstimatedValue <EstmtdVal> [0..1] ± 1367
     BlockTransfer <BlckTrf> [0..1] Indicator 1367
     BlockTransferReference <BlckTrfRef> [0..1] Text 1368
     TaxFreeCashProtection <TaxFreeCshPrtcn> [0..1] Indicator 1368
     TaxFreeCashAmount <TaxFreeCshAmt> [0..1] ± 1368
     ValueOfPensionPolicyOrPlanOrScheme
<ValOfPnsnPlcyOrPlanOrSchme>
[0..1] ± 1368
     RetirementAgeProtection <RtrmntAgePrtcn> [0..1] Indicator 1368
     RetirementAge <RtrmntAge> [0..1] Quantity 1369
     Sharing <Shrg> [0..1] Indicator 1369
     LumpSumType <LumpSumTp> [0..*] ± 1369
     PensionOrder <PnsnOrdr> [0..*] ± 1369
     RingFencedDrawdownAssets
<RingFncdDrwdwnAssts>
[0..1] Indicator 1369
     MoneyPurchaseAnnualAllowance
<MnyPurchsAnlAllwnc>
[0..1] ± 1370
     SafeguardBenefit <SfgrdBnft> [0..1] Indicator 1370
     NonSafeguardedGuaranteedBenefits
<NonSfgrddGrntedBnfts>
[0..1] Indicator 1370
     LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 1370
     ClientLifetimeAllowanceProtection
<ClntLftmAllwncPrtcn>
[0..1] Indicator 1370
     BenefitCrystallisationEventOccurred
<BnftCrstllstnEvtOcrd>
[0..1] Indicator 1371
     NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1371
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1344 May 2026
```

