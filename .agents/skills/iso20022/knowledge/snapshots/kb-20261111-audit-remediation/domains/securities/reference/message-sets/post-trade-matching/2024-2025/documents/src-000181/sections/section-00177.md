---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.3 Amount", "7.1.3.2 AmountAndDirection29", "7.1.3.2.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [229]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.3.2.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 229 to 229.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 229

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.1.3.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether an entry is a credit or a debit.
Datatype: "CreditDebitCode" on page 623
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
7.1.3.2.3  OriginalCurrencyAndOrderedAmount <OrgnlCcyAndOrdrdAmt>
Presence: [0..1]
Definition: Posting/settlement amount in its original currency when conversion from/into another
currency has occurred.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 612
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.1.3.2.4  ForeignExchangeDetails <FXDtls>
Presence: [0..1]
Definition: Information needed to process a currency exchange or conversion.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 229 February 2025
```

