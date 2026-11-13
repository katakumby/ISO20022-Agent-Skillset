---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.20 SpreadAndBenchmarkCurve <SprdAndBchmkCrv>", "32.4.3.1.1.3.20.3 BenchmarkPrice <BchmkPric>"]
file_pages: [1981]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.20.3 BenchmarkPrice <BchmkPric>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1981 to 1981.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1981

```text
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
32.4.3.1.1.3.20.3  BenchmarkPrice <BchmkPric>
Presence: [0..1]
Definition: Identifies the price of the benchmark security.
BenchmarkPrice <BchmkPric> contains the following Price8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValueType <ValTp> [0..1] CodeSet 1981
   Value <Val> [1..1] ± 1982
   PriceType <PricTp> [0..1] CodeSet 1982
32.4.3.1.1.3.20.3.1  ValueType <ValTp>
Presence: [0..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType3Code" on page 3281
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PARV Par Price is the face amount.
YIEL Yield Price expressed as a yield.
SPRE Spread Difference between a market maker's bid
and asked price.
PEUN PerUnit Price expressed per unit.
ABSO Absolute Price is expressed as absolute.
TEDP TEDPrice Price is expressed as Treasury Euro
Dollar price.
TEDY TEDYield Price is expressed as Treasury Euro
Dollar yield.
FICT FixedCabinetTrade Cabinet trades are used to indicate
prices that trade at a price lower than
that available on an exchange and they
can be fixed or variable (primarily used
for listed futures and options).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1981 August 2026
```

