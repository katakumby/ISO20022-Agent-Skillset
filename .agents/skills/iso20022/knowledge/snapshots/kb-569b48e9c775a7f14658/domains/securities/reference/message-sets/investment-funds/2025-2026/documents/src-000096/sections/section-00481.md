---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.13 Rounding <Rndg>"]
file_pages: [658]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.13 Rounding <Rndg>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 658 to 658.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 658

```text
Impacted by: C1 "ActiveCurrency", C10 "CurrencyAmount"
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
28.4.7.13  Rounding <Rndg>
Presence: [0..1]
Definition: Rounding direction applied to nearest unit.
Datatype: "RoundingDirection2Code" on page 5358
CodeName Name Definition
RDUP RoundUp Round up to the nearest whole number.
RDWN RoundDown Round down to the nearest whole
number.
28.4.7.14  OriginalCost <OrgnlCost>
Presence: [0..1]
Definition: Original amount paid for the asset at the point of purchase. May also be known as the book
cost.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
28.4.7.15  AveragePrice <AvrgPric>
Presence: [0..1]
Definition: Value of the security, as booked in the account. Book value is often different from the current
market value of the security.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 658 May 2026
```

