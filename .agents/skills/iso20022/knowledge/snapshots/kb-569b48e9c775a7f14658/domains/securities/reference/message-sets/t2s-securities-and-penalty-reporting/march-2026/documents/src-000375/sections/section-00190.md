---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.1 AdditionalBalanceBreakdown1", "7.1.5.1.4 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [258]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.1.4 QuantityBreakdown <QtyBrkdwn>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 258 to 258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 258

```text
7.1.5.1.4  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of the aggregate quantity reported into significant lots, for example, tax lots.
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown54" on
page 451 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 451
   LotQuantity <LotQty> [0..1] ± 451
   LotDateTime <LotDtTm> [0..1] ± 452
   LotPrice <LotPric> [0..1] ± 452
   TypeOfPrice <TpOfPric> [0..1] ± 452
7.1.5.2  BalanceQuantity9Choice
Definition: Choice between quantity formats for the balance information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 258
Or}   Proprietary <Prtry> [1..1] ± 258
7.1.5.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Quantity <Qty> contains one of the following elements (see "Quantity6Choice" on page 342 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 342
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 343
7.1.5.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 258 March 2026
```

