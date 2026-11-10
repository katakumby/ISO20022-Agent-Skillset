---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.15 SubscriptionProcessingCharacteristics <SbcptPrcgChrtcs>"]
file_pages: [325, 326]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.15 SubscriptionProcessingCharacteristics <SbcptPrcgChrtcs>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 325 to 326.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 325

```text
InvestmentRestrictions <InvstmtRstrctns> contains the following elements (see
"InvestmentRestrictions3" on page 4711 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MinimumInitialSubscriptionAmount <MinInitlSbcptAmt> [0..1] Amount C1, C13 4712
   MinimumInitialSubscriptionUnits <MinInitlSbcptUnits> [0..1] Quantity 4713
   MinimumSubsequentSubscriptionAmount
<MinSbsqntSbcptAmt>
[0..1] Amount C1, C13 4713
   MinimumSubsequentSubscriptionUnits
<MinSbsqntSbcptUnits>
[0..1] Quantity 4713
   MaximumRedemptionAmount <MaxRedAmt> [0..1] Amount C1, C13 4713
   MaximumRedemptionUnits <MaxRedUnits> [0..1] Quantity 4714
   MinimumRedemptionPercentage <MinRedPctg> [0..1] Quantity 4714
   OtherRedemptionRestrictions <OthrRedRstrctns> [0..1] Text 4714
   MinimumSwitchSubscriptionAmount
<MinSwtchSbcptAmt>
[0..1] Amount C1, C13 4714
   MinimumSwitchSubscriptionUnits <MinSwtchSbcptUnits> [0..1] Quantity 4715
   MaximumSwitchRedemptionAmount
<MaxSwtchRedAmt>
[0..1] Amount C1, C13 4715
   MaximumSwitchRedemptionUnits <MaxSwtchRedUnits> [0..1] Quantity 4715
   OtherSwitchRestrictions <OthrSwtchRstrctns> [0..1] Text 4715
   MinimumHoldingAmount <MinHldgAmt> [0..1] Amount C1, C13 4715
   MinimumHoldingUnits <MinHldgUnits> [0..1] Quantity 4716
   MinimumHoldingPeriod <MinHldgPrd> [0..1] Text 4716
   HoldingTransferable <HldgTrfbl> [0..1] CodeSet 4716
   AdditionalInformation <AddtlInf> [0..*] ± 4716
15.4.5.15  SubscriptionProcessingCharacteristics <SbcptPrcgChrtcs>
Presence: [0..1]
Definition: Processing characteristics linked to a subscription to the investment fund or alternative/
hedge fund.
Impacted by: C8 "DealingCutOffTimeFrameRule"
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 325 May 2026
```

## File page 326

```text
SubscriptionProcessingCharacteristics <SbcptPrcgChrtcs> contains the following elements (see
"ProcessingCharacteristics11" on page 4755 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DealingCurrencyAccepted <DealgCcyAccptd> [0..*] CodeSet C1 4756
   InitialInvestmentApplication <InitlInvstmtAppl> [0..1]  4756
     ApplicationForm <ApplForm> [1..1] Indicator 4756
     SignatureType <SgntrTp> [1..1] CodeSet 4756
   SubsequentInvestmentApplication <SbsqntInvstmtAppl> [0..1]  4757
     ApplicationForm <ApplForm> [1..1] Indicator 4757
     SignatureType <SgntrTp> [1..1] CodeSet 4757
   AmountIndicator <AmtInd> [0..1] Indicator 4758
   UnitsIndicator <UnitsInd> [0..1] Indicator 4758
   Rounding <Rndg> [0..1] CodeSet 4758
   MainFundOrderDeskLocation <MainFndOrdrDskLctn> [0..1] ± 4758
   DealingFrequency <DealgFrqcy> [0..1] CodeSet 4759
   DealingFrequencyDescription <DealgFrqcyDesc> [0..1] Text 4759
   DealingCutOffTime <DealgCutOffTm> [0..1] Time 4759
   DealingCutOffTimeFrame <DealgCutOffTmFrame> [0..1] ± C23,
C33
4760
   DealConfirmationTime <DealConfTm> [0..1] Time 4760
   DealConfirmationTimeFrame <DealConfTmFrame> [0..1] ± C24,
C34
4760
   LimitedPeriod <LtdPrd> [0..1] Text 4761
   SettlementCycle <SttlmCycl> [0..1]  4761
{Or     TradePlus <TPlus> [1..1] Quantity 4761
Or}     Prepayment <Prepmt> [1..1] Indicator 4762
   AdditionalInformation <AddtlInf> [0..*] ± 4762
Constraints
• DealingCutOffTimeFrameRule
If DealingCutOffTimeFrame is present, then DealingCutOffTimeFrame/OtherTimeFrameDescription
or DealingCutOffTimeFrame/ReferToOrderDesk or DealingCutOffTimeFrame/TradeMinus must be
present.
On Condition
    /DealingCutOffTimeFrame is present
Following Must be True
    /DealingCutOffTimeFrame/OtherTimeFrameDescription Must be present
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 326 May 2026
```

