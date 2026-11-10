---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.4 Derivative <Deriv>", "28.4.2.1.2.1.4.2 Option <Optn>", "28.4.2.1.2.1.4.2.3 StrikePrice <StrkPric>", "28.4.2.1.2.1.4.2.3.3 PriceType <PricTp>"]
file_pages: [1280]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.4.2.3.3 PriceType <PricTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1280 to 1280.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1280

```text
Value <Val> contains one of the following elements (see "PriceRateOrAmount3Choice" on page 3102
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 3102
Or}   Amount <Amt> [1..1] Amount C1 3102
28.4.2.1.2.1.4.2.3.3  PriceType <PricTp>
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
sell financial instruments at 67 or to buy
at 60.
NET2 Net Price is a net price, ie, net only of local
broker's commission, local fees and local
taxes.
NDIS NetDisclosed Price is net to the disclosed client.
NET1 NetOfAll Price is a net price, ie, net of all charges,
fees and taxes.
NUND NetUndisclosed Price is net to the client undisclosed
(used in the UK market).
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
28.4.2.1.2.1.4.2.4  MinimumExercisableQuantity <MinExrcblQty>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1280 August 2026
```

