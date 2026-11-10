---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.6 AggregateBalanceInformation4", "66.1.5.6.16 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "66.1.5.6.16.2 AvailableQuantity <AvlblQty>"]
file_pages: [4378]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.6.16.2 AvailableQuantity <AvlblQty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4378 to 4378.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4378

```text
66.1.5.6.16.2  AvailableQuantity <AvlblQty>
Presence: [0..1]
Definition: Total quantity of financial instrument for the referenced holding that is available.
AvailableQuantity <AvlblQty> contains one of the following elements (see "BalanceQuantity1Choice"
on page 4345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 4346
Or}   QuantityAsDSS <QtyAsDSS> [1..1] ± 4346
66.1.5.6.16.3  NotAvailableQuantity <NotAvlblQty>
Presence: [0..1]
Definition: Total quantity of financial instrument for the referenced holding that is not available.
NotAvailableQuantity <NotAvlblQty> contains one of the following elements (see
"BalanceQuantity1Choice" on page 4345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 4346
Or}   QuantityAsDSS <QtyAsDSS> [1..1] ± 4346
66.1.5.6.16.4  DaysAccrued <DaysAcrd>
Presence: [0..1]
Definition: Specifies the number of days used for calculating the accrued interest amount.
Datatype: "Number" on page 5400
66.1.5.6.16.5  HoldingValue <HldgVal>
Presence: [0..*]
Definition: Total value of a balance of the securities account for a specific financial instrument,
expressed in one or more currencies.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4378 May 2026
```

