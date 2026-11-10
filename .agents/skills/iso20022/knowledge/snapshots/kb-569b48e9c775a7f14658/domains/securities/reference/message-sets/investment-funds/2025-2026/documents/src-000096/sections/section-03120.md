---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.4 Amount", "66.1.4.2 DateAndAmount1", "66.1.4.2.2 Amount <Amt>"]
file_pages: [4344]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.4.2.2 Amount <Amt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4344 to 4344.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4344

```text
Datatype: "ISODate" on page 5388
66.1.4.2.2  Amount <Amt>
Presence: [1..1]
Definition: Amount of money.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.4.3  InitialAmount1Choice
Definition: Choice of an initial amount or number of pre-paid instalments.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   InitialNumberOfInstalments <InitlNbOfInstlmts> [1..1] Quantity 4344
Or}   Amount <Amt> [1..1] Amount C1, C13 4344
66.1.4.3.1  InitialNumberOfInstalments <InitlNbOfInstlmts>
Presence: [1..1]
Definition: Number of pre-paid instalment periods at the time the investment plan is created.
Datatype: "Number" on page 5400
66.1.4.3.2  Amount <Amt>
Presence: [1..1]
Definition: Amount to be paid or redeemed at the time the investment plan is created.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4344 May 2026
```

