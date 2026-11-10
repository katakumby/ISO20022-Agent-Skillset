---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.3 AmountAndDirection47"]
file_pages: [1359]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.3 AmountAndDirection47

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1359 to 1359.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1359

```text
CodeName Name Definition
DBIT Debit Operation is a decrease.
35.1.3.3  AmountAndDirection47
Definition: Amount of money debited or credited on the books of an account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
35.1.3.3.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money in the cash entry.
Impacted by: C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 2041
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
35.1.3.3.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether an entry is a credit or a debit.
Datatype: "CreditDebitCode" on page 2057
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
35.1.3.3.3  ForeignExchangeDetails <FXDtls>
Presence: [0..1]
Definition: Information needed to process a currency exchange or conversion.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1359 March 2026
```

