---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.20 Tax <Tax>", "4.4.2.14.18.2.20.8 TotalTaxAmount <TtlTaxAmt>"]
file_pages: [735]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.20.8 TotalTaxAmount <TtlTaxAmt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 735 to 735.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 735

```text
Note: The decimal separator is a dot.
4.4.2.14.18.2.20.8  TotalTaxAmount <TtlTaxAmt>
Presence: [0..1]
Definition: Total amount of money as result of the calculation of the tax.
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
4.4.2.14.18.2.20.9  Date <Dt>
Presence: [0..1]
Definition: Date by which tax is due.
Datatype: "ISODate" on page 908
4.4.2.14.18.2.20.10  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Sequential number of the tax report.
Datatype: "Number" on page 912
4.4.2.14.18.2.20.11  Record <Rcrd>
Presence: [0..*]
Definition: Record of tax details.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
735 March 2026
```

