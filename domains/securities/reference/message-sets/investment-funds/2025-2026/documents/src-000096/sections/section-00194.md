---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.15 ValuationStatistics <ValtnSttstcs>", "14.4.10.1.15.5 ByPredefinedTimePeriods <ByPrdfndTmPrds>", "14.4.10.1.15.5.1 HighestPriceValue12Months <HghstPricVal12Mnths>"]
file_pages: [281]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.15.5.1 HighestPriceValue12Months <HghstPricVal12Mnths>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 281 to 281.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 281

```text
ByPredefinedTimePeriods <ByPrdfndTmPrds> contains the following
StatisticsByPredefinedTimePeriods2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HighestPriceValue12Months <HghstPricVal12Mnths> [0..1]  281
     Amount <Amt> [1..1] Amount C3 281
   LowestPriceValue12Months <LwstPricVal12Mnths> [0..1]  282
     Amount <Amt> [1..1] Amount C3 282
   OneYearPriceChange <OneYrPricChng> [0..1]  C5, C6 282
     Amount <Amt> [0..1] Amount C3 283
     AmountSign <AmtSgn> [0..1] Indicator 283
     Rate <Rate> [0..1] Rate 283
   ThreeYearPriceChange <ThreeYrPricChng> [0..1]  C5, C6 283
     Amount <Amt> [0..1] Amount C3 284
     AmountSign <AmtSgn> [0..1] Indicator 284
     Rate <Rate> [0..1] Rate 284
   FiveYearPriceChange <FiveYrPricChng> [0..1]  C5, C6 284
     Amount <Amt> [0..1] Amount C3 285
     AmountSign <AmtSgn> [0..1] Indicator 285
     Rate <Rate> [0..1] Rate 285
14.4.10.1.15.5.1  HighestPriceValue12Months <HghstPricVal12Mnths>
Presence: [0..1]
Definition: Highest price for the referenced period.
HighestPriceValue12Months <HghstPricVal12Mnths> contains the following PriceValue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C3 281
14.4.10.1.15.5.1.1  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 281 May 2026
```

