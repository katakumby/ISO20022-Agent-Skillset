---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.5 Financial Instrument"]
file_pages: [324]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.5 Financial Instrument

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 324 to 324.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 324

```text
22.1.5 Financial Instrument
22.1.5.1  FinancialInstrumentQuantity25Choice
Definition: Defines the format for the quantity of security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 324
Or   NominalValue <NmnlVal> [1..1] Amount C2, C5 324
Or}   MonetaryValue <MntryVal> [1..1] Amount C2, C5 324
22.1.5.1.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, such as a number of shares.
Datatype: "DecimalNumber" on page 451
22.1.5.1.2  NominalValue <NmnlVal>
Presence: [1..1]
Definition: TBC.
Impacted by: C2 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 416
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
22.1.5.1.3  MonetaryValue <MntryVal>
Presence: [1..1]
Definition: TBC.
Impacted by: C2 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 416
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
324 July 2025
```

