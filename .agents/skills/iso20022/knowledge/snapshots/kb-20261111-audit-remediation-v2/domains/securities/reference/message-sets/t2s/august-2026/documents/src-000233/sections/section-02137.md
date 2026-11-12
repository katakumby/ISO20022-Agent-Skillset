---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.4 AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts>", "82.1.5.16.4.2 TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>"]
file_pages: [2898]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.4.2 TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2898 to 2898.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2898

```text
TotalHoldingsValueOfPage <TtlHldgsValOfPg> contains the following elements (see
"AmountAndDirection6" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2840
   Sign <Sgn> [1..1] Indicator 2840
82.1.5.16.4.2  TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>
Presence: [1..1]
Definition: Total value of positions reported in this statement (a statement may comprise one or more
messages).
TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> contains the following elements (see
"AmountAndDirection6" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2840
   Sign <Sgn> [1..1] Indicator 2840
82.1.5.16.4.3  TotalBookValueOfStatement <TtlBookValOfStmt>
Presence: [0..1]
Definition: Total book value of positions reported in this statement (a statement may comprise one or
more messages).
TotalBookValueOfStatement <TtlBookValOfStmt> contains the following elements (see
"AmountAndDirection6" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2840
   Sign <Sgn> [1..1] Indicator 2840
82.1.5.16.4.4  TotalEligibleCollateralValue <TtlElgblCollVal>
Presence: [0..1]
Definition: Total value of the holdings eligible for collateral purposes reported in this statement (a
statement may comprise one or more messages).
TotalEligibleCollateralValue <TtlElgblCollVal> contains the following elements (see
"AmountAndDirection6" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2840
   Sign <Sgn> [1..1] Indicator 2840
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2898 August 2026
```

