---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.5 Portfolio <Prtfl>"]
file_pages: [1532, 1533, 1534, 1535]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.5 Portfolio <Prtfl>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1532 to 1535.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1532

```text
Definition: Date the portfolio transfer instruction was executed.
Datatype: "ISODate" on page 5388
40.4.15.5  Portfolio <Prtfl>
Presence: [0..1]
Definition: Choice of tax efficient product, general investment or pension.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1532 May 2026
```

## File page 1533

```text
Portfolio <Prtfl> contains one of the following FundPortfolio7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TaxEfficientProduct <TaxEffcntPdct> [1..1]  1536
     TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 1538
     CurrentYear <CurYr> [0..1] Indicator 1538
     CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1539
     PreviousYears <PrvsYrs> [0..1]  C49 1539
       PreviousYears <PrvsYrs> [1..1]  1539
{Or         AllPreviousYears <AllPrvsYrs> [1..1] Text 1539
Or}         SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1540
       CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1540
     PreviousYearSubscriptionAmount
<PrvsYrSbcptAmt>
[0..1] Amount C1 1540
     PreviousYearsSubscriptionAmount
<PrvsYrsSbcptAmt>
[0..1] Amount C1 1540
     DateOfFirstSubscription <DtOfFrstSbcpt> [0..1] Date 1540
     CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C52 1541
       DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1541
       EquityComponent <EqtyCmpnt> [0..1] Amount C1 1541
       CashComponent <CshCmpnt> [0..1] Amount C1 1541
       TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1542
     BonusOrWithdrawal <BnsOrWdrwl> [0..*]  1542
       TypeOfAmount <TpOfAmt> [1..1]  1543
{Or         Code <Cd> [1..1] CodeSet 1543
Or}         Proprietary <Prtry> [1..1] ± 1543
       Amount <Amt> [0..1] Amount C2 1543
       Reason <Rsn> [0..1]  1544
{Or         Code <Cd> [1..1] CodeSet 1544
Or}         Proprietary <Prtry> [1..1] ± 1544
       UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1544
       Outstanding <Outsdng> [0..1] Indicator 1545
       Reference <Ref> [0..1] Text 1545
       AdditionalInformation <AddtlInf> [0..*] ± 1545
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1533 May 2026
```

## File page 1534

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     WithdrawalForResidentialPurchaseProgress
<WdrwlForResdtlPurchsPrgrs>
[0..1] Indicator 1545
     TransferorAlternateIdentification <TrfrAltrnId> [0..1] Text 1545
     TotalSubscriptionAmount <TtlSbcptAmt> [0..1] Amount C1, C18 1546
     OtherAmount <OthrAmt> [0..*]  1546
       Type <Tp> [1..1] ± 1546
       Amount <Amt> [1..1] Amount C1, C18 1546
     DateFirstQualifyingAddition <DtFrstQlfygAddtn> [0..1] Date 1547
     InvestorTaxReference <InvstrTaxRef> [0..1]  1547
       Type <Tp> [0..1]  1547
{Or         Code <Cd> [1..1] CodeSet 1547
Or}         Proprietary <Prtry> [1..1] ± 1548
       Reference <Ref> [1..1] Text 1548
     InvestmentsToFollowValue <InvstmtsToFllwVal> [0..*] ± 1548
     InnovativeFinance <InnvtvFinc> [0..*]  1548
       Type <Tp> [1..1] ± 1549
       Information <Inf> [1..1] Text 1549
     LowestInvestedAmountCurrentYear
<LwstInvstdAmtCurYr>
[0..1] Amount C1 1549
     TaxCalculationBase <TaxClctnBase> [0..1] Amount C1 1549
     UnusedTaxDeduction <UusdTaxDdctn> [0..1] Amount C1 1550
     CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 1550
     EstimatedValue <EstmtdVal> [0..1] ± 1550
     AdditionalInformation <AddtlInf> [0..*] ± 1551
Or   GeneralInvestment <GnlInvstmt> [1..1] ± 1551
Or}   Pension <Pnsn> [1..1]  C10,
C11,
C42,
C43,
C44,
C45,
C50,
C51,
C54
1551
     Identification <Id> [0..1]  1554
       Identifier <Idr> [1..1] Text 1555
       SubIdentifier <SubIdr> [0..1] Text 1555
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1534 May 2026
```

## File page 1535

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AdditionalInformation <AddtlInf> [0..1] ± 1555
     Type <Tp> [1..1]  1555
{Or       Code <Cd> [1..1] CodeSet 1555
Or}       Proprietary <Prtry> [1..1] ± 1556
     TransferScope <TrfScp> [0..1] ± 1557
     TaxReference <TaxRef> [0..*] ± 1557
     DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1557
     DrawdownStatus <DrwdwnSts> [0..1] ± 1557
     DrawdownType <DrwdwnTp> [0..1] ± 1558
     NumberOfDrawdownTranches <NbOfDrwdwnTrnchs> [0..1] Quantity 1558
     EstimatedValue <EstmtdVal> [0..1] ± 1558
     BlockTransfer <BlckTrf> [0..1] Indicator 1558
     BlockTransferReference <BlckTrfRef> [0..1] Text 1559
     TaxFreeCashProtection <TaxFreeCshPrtcn> [0..1] Indicator 1559
     TaxFreeCashAmount <TaxFreeCshAmt> [0..1] ± 1559
     ValueOfPensionPolicyOrPlanOrScheme
<ValOfPnsnPlcyOrPlanOrSchme>
[0..1] ± 1559
     RetirementAgeProtection <RtrmntAgePrtcn> [0..1] Indicator 1559
     RetirementAge <RtrmntAge> [0..1] Quantity 1560
     Sharing <Shrg> [0..1] Indicator 1560
     LumpSumType <LumpSumTp> [0..*] ± 1560
     PensionOrder <PnsnOrdr> [0..*] ± 1560
     RingFencedDrawdownAssets
<RingFncdDrwdwnAssts>
[0..1] Indicator 1560
     MoneyPurchaseAnnualAllowance
<MnyPurchsAnlAllwnc>
[0..1] ± 1561
     SafeguardBenefit <SfgrdBnft> [0..1] Indicator 1561
     NonSafeguardedGuaranteedBenefits
<NonSfgrddGrntedBnfts>
[0..1] Indicator 1561
     LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 1561
     ClientLifetimeAllowanceProtection
<ClntLftmAllwncPrtcn>
[0..1] Indicator 1561
     BenefitCrystallisationEventOccurred
<BnftCrstllstnEvtOcrd>
[0..1] Indicator 1562
     NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1562
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1535 May 2026
```

