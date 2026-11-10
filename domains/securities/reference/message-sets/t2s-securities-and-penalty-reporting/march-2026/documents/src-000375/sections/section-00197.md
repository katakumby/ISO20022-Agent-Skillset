---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.7 BalanceAmounts3", "7.1.5.7.2 PreviousHoldingValue <PrvsHldgVal>"]
file_pages: [266]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.7.2 PreviousHoldingValue <PrvsHldgVal>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 266 to 266.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 266

```text
HoldingValue <HldgVal> contains the following elements (see "AmountAndDirection6" on page 252
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
7.1.5.7.2  PreviousHoldingValue <PrvsHldgVal>
Presence: [0..1]
Definition: Previous value of an individual financial instrument holding within a safekeeping account.
PreviousHoldingValue <PrvsHldgVal> contains the following elements (see "AmountAndDirection6"
on page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
7.1.5.7.3  BookValue <BookVal>
Presence: [0..1]
Definition: Value of a financial instrument, as booked/acquired in an account. It may be used to
establish capital gain tax liability.
BookValue <BookVal> contains the following elements (see "AmountAndDirection6" on page 252 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
7.1.5.7.4  EligibleCollateralValue <ElgblCollVal>
Presence: [0..1]
Definition: Value of the position eligible for collateral purposes.
EligibleCollateralValue <ElgblCollVal> contains the following elements (see "AmountAndDirection6"
on page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
7.1.5.7.5  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 266 March 2026
```

