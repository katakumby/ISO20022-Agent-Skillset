---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.12 PaginationBalance1", "66.1.5.12.3 FinalClosingBalance <FnlClsgBal>"]
file_pages: [4401]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.12.3 FinalClosingBalance <FnlClsgBal>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4401 to 4401.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4401

```text
66.1.5.12.3  FinalClosingBalance <FnlClsgBal>
Presence: [0..1]
Warning   Either FinalClosingBalance or IntermediaryClosingBalance may be present, but not both.
Definition: Closing balance of the financial instrument in the statement.
FinalClosingBalance <FnlClsgBal> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.5.12.4  IntermediaryClosingBalance <IntrmyClsgBal>
Presence: [0..1]
Warning   Either FinalClosingBalance or IntermediaryClosingBalance may be present, but not both.
Definition: Closing Balance of this page only. Must be the interemdiary opening balance of the next
page (part of the same statement).
IntermediaryClosingBalance <IntrmyClsgBal> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.5.13  AccountingStatementOfHoldings2
Definition: Information about an accounting statement of holdings.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4401 May 2026
```

