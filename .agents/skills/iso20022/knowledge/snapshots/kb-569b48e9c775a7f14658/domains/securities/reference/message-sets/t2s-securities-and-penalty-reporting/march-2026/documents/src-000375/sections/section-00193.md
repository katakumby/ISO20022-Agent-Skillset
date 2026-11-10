---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.4 AdditionalBalanceInformation18", "7.1.5.4.2 Quantity <Qty>"]
file_pages: [262]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.4.2 Quantity <Qty>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 262 to 262.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 262

```text
SubBalanceType <SubBalTp> contains one of the following elements (see
"SubBalanceType12Choice" on page 264 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 264
Or}   Proprietary <Prtry> [1..1] ± 265
7.1.5.4.2  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Quantity <Qty> contains the following elements (see "Balance9" on page 268 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 268
   Quantity <Qty> [1..1] ± 269
7.1.5.4.3  SubBalanceAdditionalDetails <SubBalAddtlDtls>
Presence: [0..1]
Definition: Provides additional sub-balance information.
Datatype: "Max140Text" on page 556
7.1.5.4.4  QuantityBreakdown <QtyBrkdwn>
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
7.1.5.5  SecuritiesBalanceType7Choice
Definition: Choice of format for the balance type.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 262 March 2026
```

