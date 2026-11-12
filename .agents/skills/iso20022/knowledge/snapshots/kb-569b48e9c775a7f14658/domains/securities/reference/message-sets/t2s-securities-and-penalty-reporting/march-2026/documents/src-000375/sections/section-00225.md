---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.3 SubAccountDetails <SubAcctDtls>", "7.1.5.14.3.4 BalanceForSubAccount <BalForSubAcct>", "7.1.5.14.3.4.14 AccountBaseCurrencyAmounts <AcctBaseCcyAmts>"]
file_pages: [301]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.3.4.14 AccountBaseCurrencyAmounts <AcctBaseCcyAmts>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 301 to 301.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 301

```text
7.1.5.14.3.4.14  AccountBaseCurrencyAmounts <AcctBaseCcyAmts>
Presence: [0..1]
Definition: Valuation amounts provided in the base currency of the account.
Impacted by: C19 "EligibleCollateralValueRule"
AccountBaseCurrencyAmounts <AcctBaseCcyAmts> contains the following elements (see
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
7.1.5.14.3.4.15  InstrumentCurrencyAmounts <InstrmCcyAmts>
Presence: [0..1]
Definition: Valuation amounts provided in the currency of the financial instrument.
Impacted by: C19 "EligibleCollateralValueRule"
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
7.1.5.14.3.4.16  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 301 March 2026
```

