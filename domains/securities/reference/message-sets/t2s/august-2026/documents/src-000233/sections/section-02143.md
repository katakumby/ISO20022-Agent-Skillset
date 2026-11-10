---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.17 AggregateBalancePerSafekeepingPlace44", "82.1.5.17.12 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [2904]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.17.12 QuantityBreakdown <QtyBrkdwn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2904 to 2904.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2904

```text
InstrumentCurrencyAmounts <InstrmCcyAmts> contains the following elements (see
"BalanceAmounts3" on page 2855 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [0..1] ± 2855
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 2855
   BookValue <BookVal> [0..1] ± 2856
   EligibleCollateralValue <ElgblCollVal> [0..1] ± 2856
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 2856
Constraints
• EligibleCollateralValueRule
EligibleCollateralValue is only to be used in (I)CSD-participant communication or if bilaterally agreed
between the sender and receiver.
82.1.5.17.12  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of the aggregate quantity reported into significant lots, for example, tax lots.
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown54" on
page 3111 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 3111
   LotQuantity <LotQty> [0..1] ± 3111
   LotDateTime <LotDtTm> [0..1] ± 3111
   LotPrice <LotPric> [0..1] ± 3112
   TypeOfPrice <TpOfPric> [0..1] ± 3112
82.1.5.17.13  ExposureType <XpsrTp>
Presence: [0..1]
Definition: Specifies the underlying business area/type of trade causing the collateral movement.
ExposureType <XpsrTp> contains one of the following elements (see "ExposureType25Choice" on
page 2975 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2975
Or}   Proprietary <Prtry> [1..1] ± 2976
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2904 August 2026
```

