---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.4 Amount"]
file_pages: [4343]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.4 Amount

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4343 to 4343.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4343

```text
66.1.4 Amount
66.1.4.1  DateAndAmount2
Definition: Date and amount.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [0..1] Date 4343
   Amount <Amt> [1..1] Amount C2, C10 4343
66.1.4.1.1  Date <Dt>
Presence: [0..1]
Definition: Date on which the amount is declared or registered.
Datatype: "ISODate" on page 5388
66.1.4.1.2  Amount <Amt>
Presence: [1..1]
Definition: Amount of money.
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
66.1.4.2  DateAndAmount1
Definition: Date and amount.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [1..1] Date 4343
   Amount <Amt> [1..1] Amount C1, C13 4344
66.1.4.2.1  Date <Dt>
Presence: [1..1]
Definition: Date on which the amount is declared or registered.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4343 May 2026
```

