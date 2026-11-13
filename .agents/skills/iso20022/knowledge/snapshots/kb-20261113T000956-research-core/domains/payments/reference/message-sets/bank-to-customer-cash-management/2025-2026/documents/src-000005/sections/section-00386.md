---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.12 Interest <Intrst>", "4.4.2.12.5 Tax <Tax>", "4.4.2.12.5.2 Rate <Rate>"]
file_pages: [571]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.12.5.2 Rate <Rate>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 571 to 571.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 571

```text
4.4.2.12.5.2  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 913
4.4.2.12.5.3  Amount <Amt>
Presence: [0..1]
Definition: Amount of money resulting from the calculation of the tax.
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
4.4.2.13  TransactionsSummary <TxsSummry>
Presence: [0..1]
Definition: Provides summary information on entries.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
571 March 2026
```

