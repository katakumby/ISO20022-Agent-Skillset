---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.6 AggregateBalanceInformation4", "66.1.5.6.8 AccruedInterestAmountSign <AcrdIntrstAmtSgn>"]
file_pages: [4373]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.6.8 AccruedInterestAmountSign <AcrdIntrstAmtSgn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4373 to 4373.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4373

```text
Definition: Interest amount that has accrued in between coupon payment periods.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.5.6.8  AccruedInterestAmountSign <AcrdIntrstAmtSgn>
Presence: [0..1]
Definition: Indicates whether the accrued interest is a positive or negative amount.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 5399):
• Meaning When True: Plus
• Meaning When False: Minus
66.1.5.6.9  BookValue <BookVal>
Presence: [0..1]
Definition: Value of a security, as booked in an account. Book value is often different from the current
market value of the security.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.5.6.10  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4373 May 2026
```

