---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.19 Balance17", "35.1.4.19.1 ShortLongIndicator <ShrtLngInd>"]
file_pages: [1432]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.19.1 ShortLongIndicator <ShrtLngInd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1432 to 1432.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1432

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 1432
   Quantity <Qty> [1..1] ± 1432
35.1.4.19.1  ShortLongIndicator <ShrtLngInd>
Presence: [1..1]
Definition: Indication that the position is short or long.
Datatype: "ShortLong1Code" on page 2171
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
35.1.4.19.2  Quantity <Qty>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Quantity <Qty> contains one of the following elements (see "BalanceQuantity13Choice" on page 1727
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 1727
Or}   Proprietary <Prtry> [1..1] ± 1727
35.1.4.20  ClosingBalance5
Definition: Closing balance for the statement period (final closing balance) or of this page (intermediary
closing balance).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 1432
   ClosingBalance <ClsgBal> [1..1] ± 1433
Constraints
• ShortLongDefaultRule
If Shortlong is absent, then the default is long, that is, balance is positive.
35.1.4.20.1  ShortLongIndicator <ShrtLngInd>
Presence: [1..1]
Definition: Indication that the position is short or long.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1432 March 2026
```

