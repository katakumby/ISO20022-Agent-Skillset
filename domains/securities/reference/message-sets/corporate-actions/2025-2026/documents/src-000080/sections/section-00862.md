---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.8 PriceFormat72Choice", "16.1.20.8.5 AmountPricePerAmount <AmtPricPerAmt>", "16.1.20.8.5.3 Amount <Amt>"]
file_pages: [1080]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.8.5.3 Amount <Amt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1080 to 1080.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1080

```text
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.20.8.5.3  Amount <Amt>
Presence: [1..1]
Definition: The amount on which the price is based.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.20.8.6  IndexPoints <IndxPts>
Presence: [1..1]
Definition: Price expressed in index points.
Datatype: "DecimalNumber" on page 1246
16.1.20.9  PriceFormat76Choice
Definition: Choice between a percentage price or an amount price or an amount price per amount or an
amount price per financial instrument quantity.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1080 February 2026
```

