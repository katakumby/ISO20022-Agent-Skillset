---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.3 Debt <Debt>", "28.4.2.1.3.1.3.52 YieldCalculation <YldClctn>", "28.4.2.1.3.1.3.52.4 ValueDate <ValDt>"]
file_pages: [1429]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.3.52.4 ValueDate <ValDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1429 to 1429.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1429

```text
CodeName Name Definition
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
28.4.2.1.3.1.3.52.4  ValueDate <ValDt>
Presence: [1..1]
Definition: Date/time on which the calculation is based, for example, valuation on October 1 (price date)
based on price of September 19 ( value date).
Datatype: "ISODate" on page 3319
28.4.2.1.3.1.3.52.5  ValuePeriod <ValPrd>
Presence: [1..1]
Definition: Period on which the calculation is based.
ValuePeriod <ValPrd> contains one of the following DateTimePeriod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 1429
Or   ToDateTime <ToDtTm> [1..1] DateTime 1430
Or}   DateTimeRange <DtTmRg> [1..1] ± 1430
28.4.2.1.3.1.3.52.5.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1429 August 2026
```

