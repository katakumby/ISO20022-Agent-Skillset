---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.15 ValuationStatistics <ValtnSttstcs>", "14.4.10.1.15.6 ByUserDefinedTimePeriod <ByUsrDfndTmPrd>"]
file_pages: [286]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.15.6 ByUserDefinedTimePeriod <ByUsrDfndTmPrd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 286 to 286.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 286

```text
14.4.10.1.15.6  ByUserDefinedTimePeriod <ByUsrDfndTmPrd>
Presence: [0..*]
Definition: Information related to price variations, expressed using user-defined periods.
ByUserDefinedTimePeriod <ByUsrDfndTmPrd> contains the following
StatisticsByUserDefinedTimePeriod3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Period <Prd> [1..1]  286
{Or     Date <Dt> [1..1] ± 286
Or}     DateTime <DtTm> [1..1] ± 287
   HighestPriceValue <HghstPricVal> [0..1]  287
     Amount <Amt> [1..1] Amount C3 287
   LowestPriceValue <LwstPricVal> [0..1]  287
     Amount <Amt> [1..1] Amount C3 287
   PriceChange <PricChng> [0..1]  C5, C6 288
     Amount <Amt> [0..1] Amount C3 288
     AmountSign <AmtSgn> [0..1] Indicator 289
     Rate <Rate> [0..1] Rate 289
   Yield <Yld> [0..1] Rate 289
14.4.10.1.15.6.1  Period <Prd>
Presence: [1..1]
Definition: Reference period for the valuation.
Period <Prd> contains one of the following DateOrDateTimePeriod4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 286
Or}   DateTime <DtTm> [1..1] ± 287
14.4.10.1.15.6.1.1  Date <Dt>
Presence: [1..1]
Definition: Period expressed with dates.
Date <Dt> contains the following elements (see "DatePeriod2" on page 4464 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 4464
   ToDate <ToDt> [1..1] Date 4464
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 286 May 2026
```

