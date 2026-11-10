---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.9 TotalValueInPageAndStatement", "66.1.5.9.1 TotalHoldingsValueOfPage <TtlHldgsValOfPg>"]
file_pages: [4391]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.9.1 TotalHoldingsValueOfPage <TtlHldgsValOfPg>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4391 to 4391.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4391

```text
66.1.5.9.1  TotalHoldingsValueOfPage <TtlHldgsValOfPg>
Presence: [0..1]
Definition: Total value of positions reported in this message.
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
66.1.5.9.2  TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>
Presence: [1..1]
Definition: Total value of positions reported in this statement (a statement may comprise one or more
messages).
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
66.1.5.10  AggregateBalanceInformation3
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account. A securities balance is calculated from the sum of securities' receipts minus the sum
of securities' deliveries.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4391 May 2026
```

