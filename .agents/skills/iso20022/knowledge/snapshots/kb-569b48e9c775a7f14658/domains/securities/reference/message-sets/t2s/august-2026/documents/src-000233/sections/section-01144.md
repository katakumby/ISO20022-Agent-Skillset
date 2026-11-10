---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.4 Derivative <Deriv>", "28.4.2.2.1.4.1 Future <Futr>", "28.4.2.2.1.4.1.7 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "28.4.2.2.1.4.1.7.8 EndPrice <EndPric>", "28.4.2.2.1.4.1.7.8.2 Value <Val>"]
file_pages: [1647]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.4.1.7.8.2 Value <Val>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1647 to 1647.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1647

```text
CodeName Name Definition
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
VACT VariableCabinetTrade Cabinet trades are used to indicate
prices that trade at a price lower than
that available on an exchange and they
can be fixed or variable (primarily used
for listed futures and options).
28.4.2.2.1.4.1.7.8.2  Value <Val>
Presence: [1..1]
Definition: Value of the price, eg, as a currency and value.
Value <Val> contains one of the following elements (see "PriceRateOrAmount3Choice" on page 3102
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 3102
Or}   Amount <Amt> [1..1] Amount C1 3102
28.4.2.2.1.4.1.7.8.3  PriceType <PricTp>
Presence: [0..1]
Definition: Type and information about a price.
Datatype: "TypeOfPrice1Code" on page 3314
CodeName Name Definition
AVER Average Price is an average execution price.
AVOV AverageOverride Price is an override of the average price.
COMB Combined Price is composed of the combined
expenses (used in the UK market).
GREX GrossOfAll Price is a gross execution price. The
price is an all inclusive price, ie,
including all charges, fees, and taxes.
LIMI Limit Price is the limit price of a limit order, eg,
a customer might put in a limit order to
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1647 August 2026
```

