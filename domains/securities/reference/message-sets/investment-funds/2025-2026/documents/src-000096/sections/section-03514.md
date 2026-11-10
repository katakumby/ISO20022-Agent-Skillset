---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.17 FundOrderData6", "66.1.26.17.1 SettlementAmount <SttlmAmt>"]
file_pages: [4764]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.17.1 SettlementAmount <SttlmAmt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4764 to 4764.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4764

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [0..1] Amount C1, C13 4764
   SettlementMethod <SttlmMtd> [0..1] CodeSet 4764
   AdditionalAmount <AddtlAmt> [0..1] ± 4765
   UnitCurrency <UnitCcy> [0..1] CodeSet C1 4765
   QuotedCurrency <QtdCcy> [0..1] CodeSet C1 4765
Constraints
• SwitchOrderDataElementRule
One of the elements (SettlementAmount, SettlementMethod, AdditionalAmount, UnitCurrency,
QuotedCurrency) must be present.
66.1.26.17.1  SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Total amount of money paid /to be paid or received in exchange for the financial instrument
in the individual order.
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
66.1.26.17.2  SettlementMethod <SttlmMtd>
Presence: [0..1]
Definition: Method by which the transaction is settled.
Datatype: "DeliveryReceiptType2Code" on page 5294
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4764 May 2026
```

