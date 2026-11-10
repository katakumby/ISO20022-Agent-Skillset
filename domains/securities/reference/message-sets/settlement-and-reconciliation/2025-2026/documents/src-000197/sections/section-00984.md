---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.8 BalanceAmounts3", "35.1.4.8.2 PreviousHoldingValue <PrvsHldgVal>"]
file_pages: [1420]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.8.2 PreviousHoldingValue <PrvsHldgVal>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1420 to 1420.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1420

```text
HoldingValue <HldgVal> contains the following elements (see "AmountAndDirection6" on page 1361
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
35.1.4.8.2  PreviousHoldingValue <PrvsHldgVal>
Presence: [0..1]
Definition: Previous value of an individual financial instrument holding within a safekeeping account.
PreviousHoldingValue <PrvsHldgVal> contains the following elements (see "AmountAndDirection6"
on page 1361 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
35.1.4.8.3  BookValue <BookVal>
Presence: [0..1]
Definition: Value of a financial instrument, as booked/acquired in an account. It may be used to
establish capital gain tax liability.
BookValue <BookVal> contains the following elements (see "AmountAndDirection6" on page 1361 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
35.1.4.8.4  EligibleCollateralValue <ElgblCollVal>
Presence: [0..1]
Definition: Value of the position eligible for collateral purposes.
EligibleCollateralValue <ElgblCollVal> contains the following elements (see "AmountAndDirection6"
on page 1361 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
35.1.4.8.5  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1420 March 2026
```

