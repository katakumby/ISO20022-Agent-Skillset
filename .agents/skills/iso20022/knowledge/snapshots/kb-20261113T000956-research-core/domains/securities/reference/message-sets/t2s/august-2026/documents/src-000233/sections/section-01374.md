---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.20 SpreadAndBenchmarkCurve <SprdAndBchmkCrv>", "32.4.3.1.1.3.20.4 BenchmarkCurveCurrency <BchmkCrvCcy>"]
file_pages: [1983]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.20.4 BenchmarkCurveCurrency <BchmkCrvCcy>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1983 to 1983.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1983

```text
CodeName Name Definition
RDAV RoundedAverage Price is a rounded average price.
STOP Stop Price is a stop price used in an order to
buy. The order becomes a market order
when the financial instrument trades at
or above the stop price after the order is
submitted. In an order to sell the order
becomes a market order when the
financial instrument trades at or below
the stop price.
32.4.3.1.1.3.20.4  BenchmarkCurveCurrency <BchmkCrvCcy>
Presence: [0..1]
Definition: Identifies the currency used for the benchmark curve.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 3212
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
32.4.3.1.1.3.20.5  BenchmarkCurveName <BchmkCrvNm>
Presence: [0..1]
Definition: Identifies the name of the benchmark curve.
BenchmarkCurveName <BchmkCrvNm> contains one of the following
BenchmarkCurveName7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1983
Or}   Proprietary <Prtry> [1..1] ± 1984
32.4.3.1.1.3.20.5.1  Code <Cd>
Presence: [1..1]
Definition: Benchmark curve name expressed as an ISO 20022 code.
Datatype: "BenchmarkCurveName1Code" on page 3215
CodeName Name Definition
MAAA MuniAAA Benchmark curve used for municipals
based on the best credit rating for
municipal market debt.
FUSW FutureSWAP Portion of a synthetic curve that is
composed of Eurodollar or Treasury or
similar Futures and Swap rates. The
term usually begins at 3 months to 2
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1983 August 2026
```

