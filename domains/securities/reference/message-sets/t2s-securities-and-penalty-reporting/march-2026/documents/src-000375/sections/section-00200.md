---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.10 Balance9", "7.1.5.10.2 Quantity <Qty>"]
file_pages: [269]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.10.2 Quantity <Qty>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 269 to 269.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 269

```text
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
7.1.5.10.2  Quantity <Qty>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Quantity <Qty> contains one of the following elements (see "SubBalanceQuantity6Choice" on
page 269 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 269
Or   Proprietary <Prtry> [1..1] ± 270
Or}   QuantityAndAvailability <QtyAndAvlbty> [1..1]  270
     Quantity <Qty> [1..1] ± 270
     AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 270
7.1.5.11  SubBalanceQuantity6Choice
Definition: Choice between formats for the balance information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 269
Or   Proprietary <Prtry> [1..1] ± 270
Or}   QuantityAndAvailability <QtyAndAvlbty> [1..1]  270
     Quantity <Qty> [1..1] ± 270
     AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 270
7.1.5.11.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity1Choice" on
page 342 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 342
Or   FaceAmount <FaceAmt> [1..1] Amount 342
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 342
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 269 March 2026
```

