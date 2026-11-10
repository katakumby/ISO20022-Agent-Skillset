---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.2 InvestmentRestrictions3", "66.1.26.2.6 MaximumRedemptionUnits <MaxRedUnits>"]
file_pages: [4714]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.2.6 MaximumRedemptionUnits <MaxRedUnits>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4714 to 4714.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4714

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.26.2.6  MaximumRedemptionUnits <MaxRedUnits>
Presence: [0..1]
Definition: Maximum number of shares/units that may be redeemed on a single dealing day.
Datatype: "DecimalNumber" on page 5400
66.1.26.2.7  MinimumRedemptionPercentage <MinRedPctg>
Presence: [0..1]
Definition: Minimum percentage of holding that may be redeemed.
Datatype: "DecimalNumber" on page 5400
66.1.26.2.8  OtherRedemptionRestrictions <OthrRedRstrctns>
Presence: [0..1]
Definition: Specifies any other restrictions that may limit an investor's ability to redeem.
Datatype: "Max350Text" on page 5403
66.1.26.2.9  MinimumSwitchSubscriptionAmount <MinSwtchSbcptAmt>
Presence: [0..1]
Definition: Minimum quantity of securities, expressed as an amount, that must be purchased.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4714 May 2026
```

