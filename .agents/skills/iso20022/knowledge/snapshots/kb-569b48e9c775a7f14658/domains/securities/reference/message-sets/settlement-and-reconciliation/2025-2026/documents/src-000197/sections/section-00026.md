---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.8 BalanceForAccount <BalForAcct>", "2.4.8.18 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "2.4.8.18.12 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.8.18.12 QuantityBreakdown <QtyBrkdwn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
InstrumentCurrencyAmounts <InstrmCcyAmts> contains the following elements (see
"BalanceAmounts3" on page 1419 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [0..1] ± 1419
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 1420
   BookValue <BookVal> [0..1] ± 1420
   EligibleCollateralValue <ElgblCollVal> [0..1] ± 1420
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1420
Constraints
• EligibleCollateralValueRule
EligibleCollateralValue is only to be used in (I)CSD-participant communication or if bilaterally agreed
between the sender and receiver.
2.4.8.18.12  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of the aggregate quantity reported into significant lots, for example, tax lots.
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown57" on
page 1722 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1722
   LotQuantity <LotQty> [0..1] ± 1723
   LotDateTime <LotDtTm> [0..1] ± 1723
   LotPrice <LotPric> [0..1] ± 1723
   TypeOfPrice <TpOfPric> [0..1] ± 1723
2.4.8.18.13  ExposureType <XpsrTp>
Presence: [0..1]
Definition: Specifies the underlying business area/type of trade causing the collateral movement.
ExposureType <XpsrTp> contains one of the following elements (see "ExposureType25Choice" on
page 1529 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1530
Or}   Proprietary <Prtry> [1..1] ± 1531
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 49 March 2026
```

