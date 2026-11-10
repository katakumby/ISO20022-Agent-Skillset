---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.6 AggregateBalanceInformation4", "66.1.5.6.1 AggregateQuantity <AggtQty>"]
file_pages: [4371]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.6.1 AggregateQuantity <AggtQty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4371 to 4371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4371

```text
Constraints
• AccruedInterestAmountSignRule
if AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
• AggregateQuantityGuideline
The AggregateQuantity should be the sum of AvailableQuantity and NotAvailableQuantity if
AvailableQuantity and NotAvailableQuantity are both present.
• BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
66.1.5.6.1  AggregateQuantity <AggtQty>
Presence: [1..1]
Definition: Total quantity of financial instrument for the referenced holding.
AggregateQuantity <AggtQty> contains one of the following elements (see "BalanceQuantity1Choice"
on page 4345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 4346
Or}   QuantityAsDSS <QtyAsDSS> [1..1] ± 4346
66.1.5.6.2  AvailableQuantity <AvlblQty>
Presence: [0..1]
Definition: Total quantity of financial instrument for the referenced holding that is available.
AvailableQuantity <AvlblQty> contains one of the following elements (see "BalanceQuantity1Choice"
on page 4345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 4346
Or}   QuantityAsDSS <QtyAsDSS> [1..1] ± 4346
66.1.5.6.3  NotAvailableQuantity <NotAvlblQty>
Presence: [0..1]
Definition: Total quantity of financial instrument for the referenced holding that is not available.
NotAvailableQuantity <NotAvlblQty> contains one of the following elements (see
"BalanceQuantity1Choice" on page 4345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 4346
Or}   QuantityAsDSS <QtyAsDSS> [1..1] ± 4346
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4371 May 2026
```

