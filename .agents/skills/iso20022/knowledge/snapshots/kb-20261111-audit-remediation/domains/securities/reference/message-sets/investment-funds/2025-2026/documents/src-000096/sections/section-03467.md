---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.2 InvestmentRestrictions3", "66.1.26.2.10 MinimumSwitchSubscriptionUnits <MinSwtchSbcptUnits>"]
file_pages: [4715]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.2.10 MinimumSwitchSubscriptionUnits <MinSwtchSbcptUnits>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4715 to 4715.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4715

```text
66.1.26.2.10  MinimumSwitchSubscriptionUnits <MinSwtchSbcptUnits>
Presence: [0..1]
Definition: Minimum quantity of securities, expressed as number of units/shares that must be
purchased.
Datatype: "DecimalNumber" on page 5400
66.1.26.2.11  MaximumSwitchRedemptionAmount <MaxSwtchRedAmt>
Presence: [0..1]
Definition: Maximum quantity of securities, expressed as an amount, that can be sold.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.26.2.12  MaximumSwitchRedemptionUnits <MaxSwtchRedUnits>
Presence: [0..1]
Definition: Maximum number of shares/units that may be redeemed on a single dealing day.
Datatype: "DecimalNumber" on page 5400
66.1.26.2.13  OtherSwitchRestrictions <OthrSwtchRstrctns>
Presence: [0..1]
Definition: Specifies any other restrictions that may limit an investor's ability to switch.
Datatype: "Max350Text" on page 5403
66.1.26.2.14  MinimumHoldingAmount <MinHldgAmt>
Presence: [0..1]
Definition: Minimum value of units that must be maintained to avoid automatic redemption.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4715 May 2026
```

