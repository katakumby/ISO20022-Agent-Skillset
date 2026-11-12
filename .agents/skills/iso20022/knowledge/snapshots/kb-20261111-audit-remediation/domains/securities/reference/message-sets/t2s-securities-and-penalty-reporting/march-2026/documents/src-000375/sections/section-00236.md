---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.15 AggregateBalancePerSafekeepingPlace44", "7.1.5.15.12 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [312]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.15.12 QuantityBreakdown <QtyBrkdwn>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 312 to 312.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 312

```text
InstrumentCurrencyAmounts <InstrmCcyAmts> contains the following elements (see
"BalanceAmounts3" on page 265 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [0..1] ± 265
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 266
   BookValue <BookVal> [0..1] ± 266
   EligibleCollateralValue <ElgblCollVal> [0..1] ± 266
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 266
Constraints
• EligibleCollateralValueRule
EligibleCollateralValue is only to be used in (I)CSD-participant communication or if bilaterally agreed
between the sender and receiver.
7.1.5.15.12  QuantityBreakdown <QtyBrkdwn>
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
7.1.5.15.13  ExposureType <XpsrTp>
Presence: [0..1]
Definition: Specifies the underlying business area/type of trade causing the collateral movement.
ExposureType <XpsrTp> contains one of the following elements (see "ExposureType25Choice" on
page 360 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 360
Or}   Proprietary <Prtry> [1..1] ± 361
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 312 March 2026
```

