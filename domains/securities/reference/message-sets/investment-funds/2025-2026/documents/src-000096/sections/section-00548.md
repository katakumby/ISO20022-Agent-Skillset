---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.20 NewAveragePrice <NewAvrgPric>"]
file_pages: [747]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.20 NewAveragePrice <NewAvrgPric>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 747 to 747.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 747

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
30.4.7.20  NewAveragePrice <NewAvrgPric>
Presence: [0..1]
Definition: Weighted average price of the units in the account after the transfer was executed.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
30.4.7.21  AverageDate <AvrgDt>
Presence: [0..1]
Definition: Trade date of the average weighted data of units in the account before the transfer was
executed.
Datatype: "ISODate" on page 5388
30.4.7.22  NewAverageDate <NewAvrgDt>
Presence: [0..1]
Definition: Trade date of the average weighted data of units in the account after the transfer was
executed.
Datatype: "ISODate" on page 5388
30.4.7.23  TransferCurrency <TrfCcy>
Presence: [0..1]
Definition: Currency used to transfer the holdings. Some transfer agents register holdings grouped by
currency in addition to using the ISIN for multi-currency fund shares.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 747 May 2026
```

