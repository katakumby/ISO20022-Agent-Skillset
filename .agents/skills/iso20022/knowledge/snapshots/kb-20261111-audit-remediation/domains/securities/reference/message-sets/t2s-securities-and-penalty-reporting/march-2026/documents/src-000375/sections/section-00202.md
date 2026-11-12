---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.12 Balance8"]
file_pages: [271]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.12 Balance8

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 271 to 271.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 271

```text
7.1.5.12  Balance8
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account. A securities balance is calculated from the sum of securities' receipts minus the sum
of securities' deliveries.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 271
   Quantity <Qty> [1..1] ± 271
7.1.5.12.1  ShortLongIndicator <ShrtLngInd>
Presence: [0..1]
Definition: Indication that the position is short or long.
Datatype: "ShortLong1Code" on page 541
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
7.1.5.12.2  Quantity <Qty>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Quantity <Qty> contains one of the following elements (see "BalanceQuantity8Choice" on page 387 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 387
Or}   Proprietary <Prtry> [1..1] ± 388
7.1.5.13  SubBalanceInformation18
Definition: Net position of a segregated holding of a single security within the overall position held in the
securities account, for example, sub-balance per status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 272
   Quantity <Qty> [1..1] ± 272
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 272
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 272
   AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± C20,
C36
273
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 271 March 2026
```

