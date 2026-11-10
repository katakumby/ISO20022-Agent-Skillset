---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.52 YieldCalculation <YldClctn>", "13.1.2.3.52.4 ValueDate <ValDt>"]
file_pages: [218]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.52.4 ValueDate <ValDt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 218 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 218

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
13.1.2.3.52.4  ValueDate <ValDt>
Presence: [1..1]
Definition: Date/time on which the calculation is based, for example, valuation on October 1 (price date)
based on price of September 19 ( value date).
Datatype: "ISODate" on page 529
13.1.2.3.52.5  ValuePeriod <ValPrd>
Presence: [1..1]
Definition: Period on which the calculation is based.
ValuePeriod <ValPrd> contains one of the following DateTimePeriod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 218
Or   ToDateTime <ToDtTm> [1..1] DateTime 219
Or}   DateTimeRange <DtTmRg> [1..1] ± 219
13.1.2.3.52.5.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 529
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 218 March 2024
```

