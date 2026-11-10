---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.11 SubBalanceQuantity1Choice", "66.1.5.11.3 QuantityAndAvailability <QtyAndAvlbty>", "66.1.5.11.3.2 AvailabilityIndicator <AvlbtyInd>"]
file_pages: [4400]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.11.3.2 AvailabilityIndicator <AvlbtyInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4400 to 4400.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4400

```text
66.1.5.11.3.2  AvailabilityIndicator <AvlbtyInd>
Presence: [1..1]
Definition: Indicates whether the quantity of securities on the sub-balance is available.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.5.12  PaginationBalance1
Definition: Balance of a financial instrument for a specific statement page.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FirstOpeningBalance <FrstOpngBal> [0..1] ± 4400
Or}   IntermediaryOpeningBalance <IntrmyOpngBal> [0..1] ± 4400
{Or   FinalClosingBalance <FnlClsgBal> [0..1] ± 4401
Or}   IntermediaryClosingBalance <IntrmyClsgBal> [0..1] ± 4401
66.1.5.12.1  FirstOpeningBalance <FrstOpngBal>
Presence: [0..1]
Warning   Either FirstOpeningBalance or IntermediaryOpeningBalance may be present, but not
both.
Definition: Opening balance of the financial instrument in the statement.
FirstOpeningBalance <FrstOpngBal> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.5.12.2  IntermediaryOpeningBalance <IntrmyOpngBal>
Presence: [0..1]
Warning   Either FirstOpeningBalance or IntermediaryOpeningBalance may be present, but not
both.
Definition: Opening balance of this page only. It must be the interemdiary closing balance of the
previous page (part of the same statement).
IntermediaryOpeningBalance <IntrmyOpngBal> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4400 May 2026
```

