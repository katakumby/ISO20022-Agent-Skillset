---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.22 SpreadAndBenchmarkCurve <SprdAndBchmkCrv>", "13.1.6.4.22.4 BenchmarkCurveCurrency <BchmkCrvCcy>"]
file_pages: [430]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.22.4 BenchmarkCurveCurrency <BchmkCrvCcy>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 430 to 430.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 430

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
13.1.6.4.22.4  BenchmarkCurveCurrency <BchmkCrvCcy>
Presence: [0..1]
Definition: Identifies the currency used for the benchmark curve.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 508
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
13.1.6.4.22.5  BenchmarkCurveName <BchmkCrvNm>
Presence: [0..1]
Definition: Identifies the name of the benchmark curve.
BenchmarkCurveName <BchmkCrvNm> contains one of the following
BenchmarkCurveName7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 430
Or}   Proprietary <Prtry> [1..1] ± 431
13.1.6.4.22.5.1  Code <Cd>
Presence: [1..1]
Definition: Benchmark curve name expressed as an ISO 20022 code.
Datatype: "BenchmarkCurveName1Code" on page 509
CodeName Name Definition
MAAA MuniAAA Benchmark curve used for municipals
based on the best credit rating for
municipal market debt.
FUSW FutureSWAP Portion of a synthetic curve that is
composed of Eurodollar or Treasury or
similar Futures and Swap rates. The
term usually begins at 3 months to 2
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 430 March 2024
```

