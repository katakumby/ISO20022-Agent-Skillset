---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.2 InvestmentRestrictions3", "66.1.26.2.1 MinimumInitialSubscriptionAmount <MinInitlSbcptAmt>"]
file_pages: [4712]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.2.1 MinimumInitialSubscriptionAmount <MinInitlSbcptAmt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4712 to 4712.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4712

```text
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
66.1.26.2.1  MinimumInitialSubscriptionAmount <MinInitlSbcptAmt>
Presence: [0..1]
Definition: Minimum initial quantity of securities, expressed as an amount, that must be purchased at
subscription.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4712 May 2026
```

