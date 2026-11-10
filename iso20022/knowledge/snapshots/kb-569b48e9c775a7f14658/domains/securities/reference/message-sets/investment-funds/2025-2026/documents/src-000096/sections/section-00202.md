---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.15 ValuationStatistics <ValtnSttstcs>", "14.4.10.1.15.6 ByUserDefinedTimePeriod <ByUsrDfndTmPrd>", "14.4.10.1.15.6.4 PriceChange <PricChng>", "14.4.10.1.15.6.4.2 AmountSign <AmtSgn>"]
file_pages: [289]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.15.6.4.2 AmountSign <AmtSgn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 289 to 289.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 289

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
14.4.10.1.15.6.4.2  AmountSign <AmtSgn>
Presence: [0..1]
Definition: Indicates a positive or negative amount change.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 5399):
• Meaning When True: Plus
• Meaning When False: Minus
14.4.10.1.15.6.4.3  Rate <Rate>
Presence: [0..1]
Definition: Rate by which the price has changed.
Datatype: "PercentageRate" on page 5401
14.4.10.1.15.6.5  Yield <Yld>
Presence: [0..1]
Definition: Rate of income from the financial instrument, usually calculated as total dividends or coupon
interest available to investors in the last year,divided by the current price.
Datatype: "PercentageRate" on page 5401
14.4.10.1.16  PerformanceDetails <PrfrmncDtls>
Presence: [0..1]
Definition: Factors that give indications about the performance of a fund.
Impacted by: C1 "AccumulationPeriodRule"
PerformanceDetails <PrfrmncDtls> contains the following PerformanceFactors5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CorporateActionFactor <CorpActnFctr> [0..1] Quantity 289
   CumulativeCorporateActionFactor
<CmltvCorpActnFctr>
[0..1] Quantity 290
   AccumulationPeriod <AcmltnPrd> [0..1] ± 290
   NormalPerformance <NrmlPrfrmnc> [0..1] Quantity 290
Constraints
• AccumulationPeriodRule
AccumulationPeriod must be present if CumulativeCorporateActionFactor is present.
14.4.10.1.16.1  CorporateActionFactor <CorpActnFctr>
Presence: [0..1]
Definition: Value of the NAV before all corporate events of the valuation date, divided by the value of
the NAV after the corporate event.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 289 May 2026
```

