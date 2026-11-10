---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.15 ValuationStatistics <ValtnSttstcs>", "14.4.10.1.15.1 Currency <Ccy>"]
file_pages: [277]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.15.1 Currency <Ccy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 277 to 277.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 277

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Amount <Amt> [1..1] Amount C3 287
     LowestPriceValue <LwstPricVal> [0..1]  287
       Amount <Amt> [1..1] Amount C3 287
     PriceChange <PricChng> [0..1]  C5, C6 288
       Amount <Amt> [0..1] Amount C3 288
       AmountSign <AmtSgn> [0..1] Indicator 289
       Rate <Rate> [0..1] Rate 289
     Yield <Yld> [0..1] Rate 289
Constraints
• CurrencyPredefinedPeriodsRule
Currency in ByPredefinedTimePeriods/HighestPriceValue12Months/Amount,
ByPredefinedTimePeriods/LowestPriceValue12Months/Amount, ByPredefinedTimePeriods/
OneYearPriceChange/Amount, ByPredefinedTimePeriods/ThreeYearPriceChange/Amount and
ByPredefinedTimePeriods/FiveYearPriceChange/Amount must be the same as Currency.
• CurrencyPriceChangeRule
Currency in PriceChange/Amount must be the same as Currency.
• CurrencyUserDefinedPeriodsRule
Currency in ByUserDefinedTimePeriod/HighestPriceValue/Amount, ByUserDefinedTimePeriod/
LowestPriceValue/Amount and ByUserDefinedTimePeriod/PriceChange/Amount must be the same
as Currency.
14.4.10.1.15.1  Currency <Ccy>
Presence: [1..1]
Definition: Currency of the valuation statistics.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
14.4.10.1.15.2  PriceTypeChangeBasis <PricTpChngBsis>
Presence: [1..1]
Definition: Type of price from which the change is calculated, eg, bid, offer, or single.
Impacted by: C19 "OtherCodeRule"
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 277 May 2026
```

