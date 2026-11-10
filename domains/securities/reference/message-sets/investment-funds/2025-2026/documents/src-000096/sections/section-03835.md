---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.9 ValuationDealingProcessingCharacteristics3", "66.1.34.9.7 PriceMethod <PricMtd>"]
file_pages: [5124]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.9.7 PriceMethod <PricMtd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5124 to 5124.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5124

```text
Definition: Indicates whether the fund has two prices.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.34.9.7  PriceMethod <PricMtd>
Presence: [0..1]
Definition: Type of pricing calculation method.
Datatype: "PriceMethod1Code" on page 5343
CodeName Name Definition
FORW ForwardPrice Price will be calculated after the close of
the dealing period. An investor,
therefore, does not know the exact buy
or sell price.
HIST HistoricalPrice Price is calculated at an earlier valuation
point preceding the dealing period. An
investor, therefore, knows the exact buy
or sell price.
66.1.34.9.8  PriceCurrency <PricCcy>
Presence: [0..*]
Definition: Currencies in which the prices for the investment fund class are published by the fund
management company.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.34.9.9  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the valuation dealing characteristics.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5124 May 2026
```

