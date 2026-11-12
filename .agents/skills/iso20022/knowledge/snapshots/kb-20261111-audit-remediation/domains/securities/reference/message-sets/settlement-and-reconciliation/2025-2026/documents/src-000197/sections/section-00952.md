---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.15 AmountAndDirection51", "35.1.3.15.3 OriginalCurrencyAndOrderedAmount <OrgnlCcyAndOrdrdAmt>"]
file_pages: [1388]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.15.3 OriginalCurrencyAndOrderedAmount <OrgnlCcyAndOrdrdAmt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1388 to 1388.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1388

```text
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
35.1.3.15.3  OriginalCurrencyAndOrderedAmount <OrgnlCcyAndOrdrdAmt>
Presence: [0..1]
Definition: Posting/settlement amount in its original currency when conversion from/into another
currency has occurred.
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
35.1.3.16  OtherAmounts47
Definition: Identifies other amounts pertaining to the transaction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1388 March 2026
```

