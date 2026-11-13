---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.4 FinancialInstrumentDetails <FinInstrmDtls>", "14.4.10.1.4.9 DualFundIndicator <DualFndInd>"]
file_pages: [252]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.4.9 DualFundIndicator <DualFndInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 252 to 252.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 252

```text
14.4.10.1.4.9  DualFundIndicator <DualFndInd>
Presence: [1..1]
Definition: Indicates whether the fund has two prices.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
14.4.10.1.4.10  ProductGroup <PdctGrp>
Presence: [0..1]
Definition: Company specific description of a group of funds.
Datatype: "Max140Text" on page 5402
14.4.10.1.4.11  SeriesIdentification <SrsId>
Presence: [0..1]
Definition: Source of the identification, that is, domestic (national) or proprietary.
Impacted by: C21 "SeriesElementRule"
SeriesIdentification <SrsId> contains the following Series1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SeriesDate <SrsDt> [0..1] ± 252
   SeriesName <SrsNm> [0..1] Text 252
Constraints
• SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
14.4.10.1.4.11.1  SeriesDate <SrsDt>
Presence: [0..1]
Definition: Issue date of the fund series. It is typically applicable to a redemption order, subscription
order confirmation or redemption order confirmation, but may be specified in the subscription order, if
known.
SeriesDate <SrsDt> contains one of the following elements (see "DateFormat42Choice" on page 4467
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   YearMonth <YrMnth> [1..1] YearMonth 4467
Or}   YearMonthDay <YrMnthDay> [1..1] Date 4467
14.4.10.1.4.11.2  SeriesName <SrsNm>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 252 May 2026
```

