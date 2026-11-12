---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.2 Option <Optn>", "32.4.3.1.1.2.4.2.16 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "32.4.3.1.1.2.4.2.16.5 CashType <CshTp>"]
file_pages: [1944]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.2.16.5 CashType <CshTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1944 to 1944.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1944

```text
Note: The decimal separator is a dot.
32.4.3.1.1.2.4.2.16.5  CashType <CshTp>
Presence: [0..1]
Definition: Represents how the cash will be calculated. Indicates that the cash is either fixed or a
difference value (difference between strike and current underlying price).
Datatype: "Max35Text" on page 3328
32.4.3.1.1.2.4.2.16.6  Price <Pric>
Presence: [0..1]
Definition: In a financing deal, clean price (percent-of-par or per unit) of the underlying security or
basket.
Price <Pric> contains the following Price8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValueType <ValTp> [0..1] CodeSet 1944
   Value <Val> [1..1] ± 1945
   PriceType <PricTp> [0..1] CodeSet 1945
32.4.3.1.1.2.4.2.16.6.1  ValueType <ValTp>
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1944 August 2026
```

