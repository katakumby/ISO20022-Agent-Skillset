---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.8 Stipulations <Stiptns>", "3.4.8.30 WholePoolIndicator <WhlPoolInd>"]
file_pages: [104]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.8.30 WholePoolIndicator <WhlPoolInd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 104 to 104.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 104

```text
3.4.8.30  WholePoolIndicator <WhlPoolInd>
Presence: [0..1]
Definition: Indicates a search criterion when looking to buy an MBS that either is [yes] or is not [no] an
entire pool.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.8.31  PriceSource <PricSrc>
Presence: [0..1]
Definition: Identifies the Benchmark source price (eg. BB Generic, BB Fairvalue, Brokertec.).
Datatype: "Max35Text" on page 669
3.4.8.32  ExpirationDate <XprtnDt>
Presence: [0..1]
Definition: Date/time at which an interest bearing security becomes due and assets are to be repaid.
Datatype: "ISODateTime" on page 662
3.4.8.33  OverAllotmentAmount <OverAlltmtAmt>
Presence: [0..1]
Definition: Amount for which a security can be overalloted (as in greenshoe option).
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 611
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.8.34  OverAllotmentRate <OverAlltmtRate>
Presence: [0..1]
Definition: Percentage for which a security can be overalloted (as in greenshoe option).
Datatype: "PercentageRate" on page 667
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 104 February 2025
```

