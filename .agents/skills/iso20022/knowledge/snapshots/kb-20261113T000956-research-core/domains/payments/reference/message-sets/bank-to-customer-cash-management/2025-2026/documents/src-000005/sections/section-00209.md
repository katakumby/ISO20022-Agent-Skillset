---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.3 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [330]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.3 CreditDebitIndicator <CdtDbtInd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 330 to 330.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 330

```text
Definition: Amount of money in the cash entry.
Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.2.15.3  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the entry is a credit or a debit entry.
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.2.15.4  ReversalIndicator <RvslInd>
Presence: [0..1]
Definition: Indicates whether or not the entry is the result of a reversal.
Usage: This element should only be present if the entry is the result of a reversal.
If the CreditDebitIndicator is CRDT and ReversalIndicator is Yes, the original operation was a debit
entry.
If the CreditDebitIndicator is DBIT and ReversalIndicator is Yes, the original operation was a credit
entry.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 911):
• Meaning When True: True
• Meaning When False: False
3.4.2.15.5  Status <Sts>
Presence: [1..1]
Definition: Status of an entry on the books of the account servicer.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
330 March 2026
```

