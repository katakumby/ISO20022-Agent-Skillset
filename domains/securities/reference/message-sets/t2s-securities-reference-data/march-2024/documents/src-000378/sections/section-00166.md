---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.4 Warrant4", "13.1.2.4.2 SubscriptionPrice <SbcptPric>", "13.1.2.4.2.3 PriceType <PricTp>"]
file_pages: [230]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.4.2.3 PriceType <PricTp>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 230 to 230.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 230

```text
Value <Val> contains one of the following elements (see "PriceRateOrAmount3Choice" on page 497
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 497
Or}   Amount <Amt> [1..1] Amount C2 497
13.1.2.4.2.3  PriceType <PricTp>
Presence: [0..1]
Definition: Type and information about a price.
Datatype: "TypeOfPrice1Code" on page 526
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
13.1.2.4.3  Type <Tp>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 230 March 2024
```

