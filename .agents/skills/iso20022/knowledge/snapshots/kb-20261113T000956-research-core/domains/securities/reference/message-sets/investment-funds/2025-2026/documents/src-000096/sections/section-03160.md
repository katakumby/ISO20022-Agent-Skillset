---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.8 FundBalance1", "66.1.5.8.3 TotalCashFromUnitOrders <TtlCshFrUnitOrdrs>"]
file_pages: [4390]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.8.3 TotalCashFromUnitOrders <TtlCshFrUnitOrdrs>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4390 to 4390.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4390

```text
66.1.5.8.3  TotalCashFromUnitOrders <TtlCshFrUnitOrdrs>
Presence: [0..1]
Definition: Total amount of cash derived from orders placed as units.
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
66.1.5.8.4  TotalCashFromCashOrders <TtlCshFrCshOrdrs>
Presence: [0..1]
Definition: Total amount of cash from orders placed in cash.
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
66.1.5.9  TotalValueInPageAndStatement
Definition: Value of total holdings reported.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] Amount C1, C13 4391
   TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] Amount C1, C13 4391
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4390 May 2026
```

