---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.4 Derivative <Deriv>", "28.4.2.2.1.4.2 Option <Optn>", "28.4.2.2.1.4.2.16 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "28.4.2.2.1.4.2.16.7 DirtyPrice <DrtyPric>"]
file_pages: [1668]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.4.2.16.7 DirtyPrice <DrtyPric>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1668 to 1668.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1668

```text
CodeName Name Definition
NOGR NotionalGross Price is notional gross (used in the UK
market).
PARV ParValue Price is equal to the nominal or face
value of the instrument.
RDAV RoundedAverage Price is a rounded average price.
STOP Stop Price is a stop price used in an order to
buy. The order becomes a market order
when the financial instrument trades at
or above the stop price after the order is
submitted. In an order to sell the order
becomes a market order when the
financial instrument trades at or below
the stop price.
28.4.2.2.1.4.2.16.7  DirtyPrice <DrtyPric>
Presence: [0..1]
Definition: In a financing deal, price (percent-of-par or per unit) of the underlying security or basket.
"Dirty" means it includes accrued interest.
DirtyPrice <DrtyPric> contains the following Price8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValueType <ValTp> [0..1] CodeSet 1668
   Value <Val> [1..1] ± 1669
   PriceType <PricTp> [0..1] CodeSet 1669
28.4.2.2.1.4.2.16.7.1  ValueType <ValTp>
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1668 August 2026
```

