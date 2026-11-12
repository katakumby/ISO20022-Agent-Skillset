---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.4 AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts>", "7.1.5.14.4.2 TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>"]
file_pages: [306]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.4.2 TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 306 to 306.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 306

```text
TotalHoldingsValueOfPage <TtlHldgsValOfPg> contains the following elements (see
"AmountAndDirection6" on page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
7.1.5.14.4.2  TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>
Presence: [1..1]
Definition: Total value of positions reported in this statement (a statement may comprise one or more
messages).
TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> contains the following elements (see
"AmountAndDirection6" on page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
7.1.5.14.4.3  TotalBookValueOfStatement <TtlBookValOfStmt>
Presence: [0..1]
Definition: Total book value of positions reported in this statement (a statement may comprise one or
more messages).
TotalBookValueOfStatement <TtlBookValOfStmt> contains the following elements (see
"AmountAndDirection6" on page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
7.1.5.14.4.4  TotalEligibleCollateralValue <TtlElgblCollVal>
Presence: [0..1]
Definition: Total value of the holdings eligible for collateral purposes reported in this statement (a
statement may comprise one or more messages).
TotalEligibleCollateralValue <TtlElgblCollVal> contains the following elements (see
"AmountAndDirection6" on page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 306 March 2026
```

