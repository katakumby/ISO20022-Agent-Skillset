---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.10 UnitPrice23", "66.1.34.10.4 AccruedInterestNAV <AcrdIntrstNAV>"]
file_pages: [5126]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.10.4 AccruedInterestNAV <AcrdIntrstNAV>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5126 to 5126.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5126

```text
CodeName Name Definition
FORW ForwardPrice Price will be calculated after the close of
the dealing period. An investor,
therefore, does not know the exact buy
or sell price.
HIST HistoricalPrice Price is calculated at an earlier valuation
point preceding the dealing period. An
investor, therefore, knows the exact buy
or sell price.
66.1.34.10.4  AccruedInterestNAV <AcrdIntrstNAV>
Presence: [0..1]
Definition: Interest that has accumulated between the most recent payment of interest and the sale of
the financial instrument.
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
66.1.34.10.5  NumberOfDaysAccrued <NbOfDaysAcrd>
Presence: [0..1]
Definition: Number of days used for calculating the accrued interest amount.
Datatype: "Number" on page 5400
66.1.34.10.6  TaxableIncomePerShare <TaxblIncmPerShr>
Presence: [0..1]
Definition: Amount included in the NAV that corresponds to gains directly or indirectly derived from
interest payment in the scope of the European Directive on taxation of savings income in the form of
interest payments.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5126 May 2026
```

