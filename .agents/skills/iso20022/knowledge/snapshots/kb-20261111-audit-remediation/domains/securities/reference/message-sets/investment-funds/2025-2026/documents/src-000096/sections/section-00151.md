---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.15 ValuationStatistics <ValtnSttstcs>", "13.4.9.15.6 ByUserDefinedTimePeriod <ByUsrDfndTmPrd>", "13.4.9.15.6.1 Period <Prd>", "13.4.9.15.6.1.2 DateTime <DtTm>"]
file_pages: [218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.15.6.1.2 DateTime <DtTm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 218 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 218

```text
13.4.9.15.6.1.2  DateTime <DtTm>
Presence: [1..1]
Definition: Period expressed with dates and times.
DateTime <DtTm> contains the following elements (see "DateTimePeriod1" on page 4474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 4474
   ToDateTime <ToDtTm> [1..1] DateTime 4475
13.4.9.15.6.2  HighestPriceValue <HghstPricVal>
Presence: [0..1]
Definition: Highest price for the referenced period.
HighestPriceValue <HghstPricVal> contains the following PriceValue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C3 218
13.4.9.15.6.2.1  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
13.4.9.15.6.3  LowestPriceValue <LwstPricVal>
Presence: [0..1]
Definition: Lowest price for the referenced period.
LowestPriceValue <LwstPricVal> contains the following PriceValue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C3 218
13.4.9.15.6.3.1  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 218 May 2026
```

