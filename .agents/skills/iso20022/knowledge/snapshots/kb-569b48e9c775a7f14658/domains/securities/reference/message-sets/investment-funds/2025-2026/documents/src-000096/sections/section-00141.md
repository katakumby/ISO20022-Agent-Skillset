---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.15 ValuationStatistics <ValtnSttstcs>", "13.4.9.15.1 Currency <Ccy>"]
file_pages: [208]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.15.1 Currency <Ccy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 208 to 208.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 208

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Amount <Amt> [1..1] Amount C3 218
     LowestPriceValue <LwstPricVal> [0..1]  218
       Amount <Amt> [1..1] Amount C3 218
     PriceChange <PricChng> [0..1]  C5, C6 219
       Amount <Amt> [0..1] Amount C3 219
       AmountSign <AmtSgn> [0..1] Indicator 220
       Rate <Rate> [0..1] Rate 220
     Yield <Yld> [0..1] Rate 220
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
13.4.9.15.1  Currency <Ccy>
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
13.4.9.15.2  PriceTypeChangeBasis <PricTpChngBsis>
Presence: [1..1]
Definition: Type of price from which the change is calculated, eg, bid, offer, or single.
Impacted by: C18 "OtherCodeRule"
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 208 May 2026
```

