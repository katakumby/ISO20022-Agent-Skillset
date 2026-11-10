---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["5 semt.040.001.01 SecuritiesAccountPositionResponseV01", "5.4 Message Building Blocks", "5.4.6 PartyBaseCurrencyTotalAmounts <PtyBaseCcyTtlAmts>"]
file_pages: [176]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.040.001.01"]
---

# 5.4.6 PartyBaseCurrencyTotalAmounts <PtyBaseCcyTtlAmts>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 176 to 176.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 176

```text
Constraints
• BalanceForAccountOrSubAccountRule
BalanceForAccount must be present or SubAccountDetails must be present, both may be present.
5.4.6 PartyBaseCurrencyTotalAmounts
<PtyBaseCcyTtlAmts>
Presence: [0..1]
Definition: Total valuation amounts provided in the base currency of the party.
Impacted by: C40 "TotalEligibleCollateralValueRule"
PartyBaseCurrencyTotalAmounts <PtyBaseCcyTtlAmts> contains the following
TotalValueInPageAndStatement1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 176
   TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 176
   TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 177
   TotalEligibleCollateralValue <TtlElgblCollVal> [0..1] ± 177
Constraints
• TotalEligibleCollateralValueRule
Total eligible collateral value is only to be used in (I)CSD-participant communication or if bilaterally
agreed between the sender and receiver.
5.4.6.1  TotalHoldingsValueOfPage <TtlHldgsValOfPg>
Presence: [0..1]
Definition: Total value of positions reported in this message.
TotalHoldingsValueOfPage <TtlHldgsValOfPg> contains the following elements (see
"AmountAndDirection6" on page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
5.4.6.2  TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>
Presence: [1..1]
Definition: Total value of positions reported in this statement (a statement may comprise one or more
messages).
Approved by the Securities SEG 19 February 2026. semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities - Securities and Penalty Reporting 176 March 2026
```

