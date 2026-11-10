---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.9 Balance6", "7.1.5.9.1 ShortLongIndicator <ShrtLngInd>"]
file_pages: [268]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.9.1 ShortLongIndicator <ShrtLngInd>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 268 to 268.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 268

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 268
   Quantity <Qty> [1..1] ± 268
7.1.5.9.1  ShortLongIndicator <ShrtLngInd>
Presence: [1..1]
Definition: Indication that the position is short or long.
Datatype: "ShortLong1Code" on page 541
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
7.1.5.9.2  Quantity <Qty>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Quantity <Qty> contains one of the following elements (see "BalanceQuantity9Choice" on page 258 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 258
Or}   Proprietary <Prtry> [1..1] ± 258
7.1.5.10  Balance9
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account. A securities balance is calculated from the sum of securities' receipts minus the sum
of securities' deliveries.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 268
   Quantity <Qty> [1..1] ± 269
7.1.5.10.1  ShortLongIndicator <ShrtLngInd>
Presence: [0..1]
Definition: Indication that the position is short or long.
Datatype: "ShortLong1Code" on page 541
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 268 March 2026
```

