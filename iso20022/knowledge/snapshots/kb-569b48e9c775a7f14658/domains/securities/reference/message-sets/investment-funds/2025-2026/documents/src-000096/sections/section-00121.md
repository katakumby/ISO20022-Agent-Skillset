---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.8 NextValuationDateTime <NxtValtnDtTm>"]
file_pages: [185]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.8 NextValuationDateTime <NxtValtnDtTm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 185 to 185.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 185

```text
13.4.9.8  NextValuationDateTime <NxtValtnDtTm>
Presence: [0..1]
Definition: Date and time of the next price valuation for the investment fund/fund class.
NextValuationDateTime <NxtValtnDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
13.4.9.9  PreviousValuationDateTime <PrvsValtnDtTm>
Presence: [0..1]
Definition: Date and time of the previous price valuation for the investment fund/fund class.
PreviousValuationDateTime <PrvsValtnDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
13.4.9.10  ValuationType <ValtnTp>
Presence: [1..1]
Definition: Specifies how the valuation is done, based on the schedule stated in the prospectus.
Datatype: "ValuationTiming1Code" on page 5388
CodeName Name Definition
EXCP Exceptional Price valuation is done exceptionally,
outside the timeframe specified in the
prospectus.
USUA Usual Price valuation is done within the
timeframe specified in the prospectus.
PATC Particular Price valuation that is done outside the
usual timeframe, but in conformance
with a case specified in the prospectus,
eg, market closing day.
13.4.9.11  ValuationFrequency <ValtnFrqcy>
Presence: [0..1]
Definition: Frequency of the valuation.
Datatype: "EventFrequency1Code" on page 5297
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 185 May 2026
```

