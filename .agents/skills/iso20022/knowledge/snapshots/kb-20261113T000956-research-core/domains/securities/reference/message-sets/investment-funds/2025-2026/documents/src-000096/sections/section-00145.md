---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.15 ValuationStatistics <ValtnSttstcs>", "13.4.9.15.5 ByPredefinedTimePeriods <ByPrdfndTmPrds>", "13.4.9.15.5.1 HighestPriceValue12Months <HghstPricVal12Mnths>"]
file_pages: [212]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.15.5.1 HighestPriceValue12Months <HghstPricVal12Mnths>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 212 to 212.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 212

```text
ByPredefinedTimePeriods <ByPrdfndTmPrds> contains the following
StatisticsByPredefinedTimePeriods2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HighestPriceValue12Months <HghstPricVal12Mnths> [0..1]  212
     Amount <Amt> [1..1] Amount C3 212
   LowestPriceValue12Months <LwstPricVal12Mnths> [0..1]  213
     Amount <Amt> [1..1] Amount C3 213
   OneYearPriceChange <OneYrPricChng> [0..1]  C5, C6 213
     Amount <Amt> [0..1] Amount C3 214
     AmountSign <AmtSgn> [0..1] Indicator 214
     Rate <Rate> [0..1] Rate 214
   ThreeYearPriceChange <ThreeYrPricChng> [0..1]  C5, C6 214
     Amount <Amt> [0..1] Amount C3 215
     AmountSign <AmtSgn> [0..1] Indicator 215
     Rate <Rate> [0..1] Rate 215
   FiveYearPriceChange <FiveYrPricChng> [0..1]  C5, C6 215
     Amount <Amt> [0..1] Amount C3 216
     AmountSign <AmtSgn> [0..1] Indicator 216
     Rate <Rate> [0..1] Rate 216
13.4.9.15.5.1  HighestPriceValue12Months <HghstPricVal12Mnths>
Presence: [0..1]
Definition: Highest price for the referenced period.
HighestPriceValue12Months <HghstPricVal12Mnths> contains the following PriceValue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C3 212
13.4.9.15.5.1.1  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 212 May 2026
```

