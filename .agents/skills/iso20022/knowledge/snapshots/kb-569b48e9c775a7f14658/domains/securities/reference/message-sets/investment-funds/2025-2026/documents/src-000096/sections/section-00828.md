---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>"]
file_pages: [1149, 1150, 1151, 1152]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5 Portfolio <Prtfl>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1149 to 1152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1149

```text
Definition: Date the portfolio transfer instruction was executed.
Datatype: "ISODate" on page 5388
36.4.15.5  Portfolio <Prtfl>
Presence: [0..1]
Definition: Choice of tax efficient product, general investment or pension.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1149 May 2026
```

## File page 1150

```text
Portfolio <Prtfl> contains one of the following FundPortfolio7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TaxEfficientProduct <TaxEffcntPdct> [1..1]  1153
     TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 1155
     CurrentYear <CurYr> [0..1] Indicator 1155
     CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1156
     PreviousYears <PrvsYrs> [0..1]  C49 1156
       PreviousYears <PrvsYrs> [1..1]  1156
{Or         AllPreviousYears <AllPrvsYrs> [1..1] Text 1156
Or}         SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1157
       CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1157
     PreviousYearSubscriptionAmount
<PrvsYrSbcptAmt>
[0..1] Amount C1 1157
     PreviousYearsSubscriptionAmount
<PrvsYrsSbcptAmt>
[0..1] Amount C1 1157
     DateOfFirstSubscription <DtOfFrstSbcpt> [0..1] Date 1157
     CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C52 1158
       DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1158
       EquityComponent <EqtyCmpnt> [0..1] Amount C1 1158
       CashComponent <CshCmpnt> [0..1] Amount C1 1158
       TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1159
     BonusOrWithdrawal <BnsOrWdrwl> [0..*]  1159
       TypeOfAmount <TpOfAmt> [1..1]  1160
{Or         Code <Cd> [1..1] CodeSet 1160
Or}         Proprietary <Prtry> [1..1] ± 1160
       Amount <Amt> [0..1] Amount C2 1160
       Reason <Rsn> [0..1]  1161
{Or         Code <Cd> [1..1] CodeSet 1161
Or}         Proprietary <Prtry> [1..1] ± 1161
       UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1161
       Outstanding <Outsdng> [0..1] Indicator 1162
       Reference <Ref> [0..1] Text 1162
       AdditionalInformation <AddtlInf> [0..*] ± 1162
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1150 May 2026
```

## File page 1151

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     WithdrawalForResidentialPurchaseProgress
<WdrwlForResdtlPurchsPrgrs>
[0..1] Indicator 1162
     TransferorAlternateIdentification <TrfrAltrnId> [0..1] Text 1162
     TotalSubscriptionAmount <TtlSbcptAmt> [0..1] Amount C1, C18 1163
     OtherAmount <OthrAmt> [0..*]  1163
       Type <Tp> [1..1] ± 1163
       Amount <Amt> [1..1] Amount C1, C18 1163
     DateFirstQualifyingAddition <DtFrstQlfygAddtn> [0..1] Date 1164
     InvestorTaxReference <InvstrTaxRef> [0..1]  1164
       Type <Tp> [0..1]  1164
{Or         Code <Cd> [1..1] CodeSet 1164
Or}         Proprietary <Prtry> [1..1] ± 1165
       Reference <Ref> [1..1] Text 1165
     InvestmentsToFollowValue <InvstmtsToFllwVal> [0..*] ± 1165
     InnovativeFinance <InnvtvFinc> [0..*]  1165
       Type <Tp> [1..1] ± 1166
       Information <Inf> [1..1] Text 1166
     LowestInvestedAmountCurrentYear
<LwstInvstdAmtCurYr>
[0..1] Amount C1 1166
     TaxCalculationBase <TaxClctnBase> [0..1] Amount C1 1166
     UnusedTaxDeduction <UusdTaxDdctn> [0..1] Amount C1 1167
     CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 1167
     EstimatedValue <EstmtdVal> [0..1] ± 1167
     AdditionalInformation <AddtlInf> [0..*] ± 1168
Or   GeneralInvestment <GnlInvstmt> [1..1] ± 1168
Or}   Pension <Pnsn> [1..1]  C10,
C11,
C42,
C43,
C44,
C45,
C50,
C51,
C54
1168
     Identification <Id> [0..1]  1171
       Identifier <Idr> [1..1] Text 1172
       SubIdentifier <SubIdr> [0..1] Text 1172
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1151 May 2026
```

## File page 1152

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AdditionalInformation <AddtlInf> [0..1] ± 1172
     Type <Tp> [1..1]  1172
{Or       Code <Cd> [1..1] CodeSet 1172
Or}       Proprietary <Prtry> [1..1] ± 1173
     TransferScope <TrfScp> [0..1] ± 1174
     TaxReference <TaxRef> [0..*] ± 1174
     DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1174
     DrawdownStatus <DrwdwnSts> [0..1] ± 1174
     DrawdownType <DrwdwnTp> [0..1] ± 1175
     NumberOfDrawdownTranches <NbOfDrwdwnTrnchs> [0..1] Quantity 1175
     EstimatedValue <EstmtdVal> [0..1] ± 1175
     BlockTransfer <BlckTrf> [0..1] Indicator 1175
     BlockTransferReference <BlckTrfRef> [0..1] Text 1176
     TaxFreeCashProtection <TaxFreeCshPrtcn> [0..1] Indicator 1176
     TaxFreeCashAmount <TaxFreeCshAmt> [0..1] ± 1176
     ValueOfPensionPolicyOrPlanOrScheme
<ValOfPnsnPlcyOrPlanOrSchme>
[0..1] ± 1176
     RetirementAgeProtection <RtrmntAgePrtcn> [0..1] Indicator 1176
     RetirementAge <RtrmntAge> [0..1] Quantity 1177
     Sharing <Shrg> [0..1] Indicator 1177
     LumpSumType <LumpSumTp> [0..*] ± 1177
     PensionOrder <PnsnOrdr> [0..*] ± 1177
     RingFencedDrawdownAssets
<RingFncdDrwdwnAssts>
[0..1] Indicator 1177
     MoneyPurchaseAnnualAllowance
<MnyPurchsAnlAllwnc>
[0..1] ± 1178
     SafeguardBenefit <SfgrdBnft> [0..1] Indicator 1178
     NonSafeguardedGuaranteedBenefits
<NonSfgrddGrntedBnfts>
[0..1] Indicator 1178
     LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 1178
     ClientLifetimeAllowanceProtection
<ClntLftmAllwncPrtcn>
[0..1] Indicator 1178
     BenefitCrystallisationEventOccurred
<BnftCrstllstnEvtOcrd>
[0..1] Indicator 1179
     NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1179
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1152 May 2026
```

