---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.18 OpeningBalance6Choice"]
file_pages: [1431]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.18 OpeningBalance6Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1431 to 1431.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1431

```text
On Condition
    /SubBalanceType/Code is equal to value 'EligibleForCollateralPurposes'
Following Must be True
    /Quantity/QuantityAndAvailability Must be absent
• SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
35.1.4.18  OpeningBalance6Choice
Definition: Choice of opening balance.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   First <Frst> [1..1] ± 1431
Or}   Intermediary <Intrmy> [1..1] ± 1431
35.1.4.18.1  First <Frst>
Presence: [1..1]
Definition: Opening balance for the statement period. It always equals the closing balance of the
previous statement.
First <Frst> contains one of the following elements (see "BalanceQuantity14Choice" on page 1735 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1735
Or}   Proprietary <Prtry> [1..1] ± 1736
35.1.4.18.2  Intermediary <Intrmy>
Presence: [1..1]
Definition: Opening balance of this page only. This balance must be the intermediary closing balance of
the previous page of the same statement.
Intermediary <Intrmy> contains one of the following elements (see "BalanceQuantity14Choice" on
page 1735 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1735
Or}   Proprietary <Prtry> [1..1] ± 1736
35.1.4.19  Balance17
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account. A securities balance is calculated from the sum of securities' receipts minus the sum
of securities' deliveries.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1431 March 2026
```

