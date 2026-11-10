---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["80 semt.040.001.01 SecuritiesAccountPositionResponseV01", "80.4 Message Building Blocks", "80.4.6 PartyBaseCurrencyTotalAmounts <PtyBaseCcyTtlAmts>"]
file_pages: [2758]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.040.001.01"]
---

# 80.4.6 PartyBaseCurrencyTotalAmounts <PtyBaseCcyTtlAmts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2758 to 2758.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2758

```text
Constraints
• BalanceForAccountOrSubAccountRule
BalanceForAccount must be present or SubAccountDetails must be present, both may be present.
80.4.6 PartyBaseCurrencyTotalAmounts
<PtyBaseCcyTtlAmts>
Presence: [0..1]
Definition: Total valuation amounts provided in the base currency of the party.
Impacted by: C40 "TotalEligibleCollateralValueRule"
PartyBaseCurrencyTotalAmounts <PtyBaseCcyTtlAmts> contains the following
TotalValueInPageAndStatement1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 2758
   TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 2758
   TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 2759
   TotalEligibleCollateralValue <TtlElgblCollVal> [0..1] ± 2759
Constraints
• TotalEligibleCollateralValueRule
Total eligible collateral value is only to be used in (I)CSD-participant communication or if bilaterally
agreed between the sender and receiver.
80.4.6.1  TotalHoldingsValueOfPage <TtlHldgsValOfPg>
Presence: [0..1]
Definition: Total value of positions reported in this message.
TotalHoldingsValueOfPage <TtlHldgsValOfPg> contains the following elements (see
"AmountAndDirection6" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2840
   Sign <Sgn> [1..1] Indicator 2840
80.4.6.2  TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>
Presence: [1..1]
Definition: Total value of positions reported in this statement (a statement may comprise one or more
messages).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2758 August 2026
```

