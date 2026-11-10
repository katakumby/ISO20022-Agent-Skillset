---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.15 ValuationStatistics <ValtnSttstcs>", "14.4.10.1.15.6 ByUserDefinedTimePeriod <ByUsrDfndTmPrd>", "14.4.10.1.15.6.1 Period <Prd>", "14.4.10.1.15.6.1.2 DateTime <DtTm>"]
file_pages: [287]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.15.6.1.2 DateTime <DtTm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 287 to 287.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 287

```text
14.4.10.1.15.6.1.2  DateTime <DtTm>
Presence: [1..1]
Definition: Period expressed with dates and times.
DateTime <DtTm> contains the following elements (see "DateTimePeriod1" on page 4474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 4474
   ToDateTime <ToDtTm> [1..1] DateTime 4475
14.4.10.1.15.6.2  HighestPriceValue <HghstPricVal>
Presence: [0..1]
Definition: Highest price for the referenced period.
HighestPriceValue <HghstPricVal> contains the following PriceValue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C3 287
14.4.10.1.15.6.2.1  Amount <Amt>
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
14.4.10.1.15.6.3  LowestPriceValue <LwstPricVal>
Presence: [0..1]
Definition: Lowest price for the referenced period.
LowestPriceValue <LwstPricVal> contains the following PriceValue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C3 287
14.4.10.1.15.6.3.1  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 287 May 2026
```

