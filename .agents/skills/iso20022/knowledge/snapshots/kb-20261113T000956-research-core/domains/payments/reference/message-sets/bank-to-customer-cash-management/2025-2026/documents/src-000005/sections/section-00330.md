---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.20 Tax <Tax>", "3.4.2.15.18.2.20.11 Record <Rcrd>", "3.4.2.15.18.2.20.11.8 TaxAmount <TaxAmt>", "3.4.2.15.18.2.20.11.8.4 Details <Dtls>"]
file_pages: [482]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.20.11.8.4 Details <Dtls>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 482 to 482.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 482

```text
Definition: Total amount that is the result of the calculation of the tax for the record.
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
3.4.2.15.18.2.20.11.8.4  Details <Dtls>
Presence: [0..*]
Definition: Set of elements used to provide details on the tax period and amount.
Details <Dtls> contains the following TaxRecordDetails3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Period <Prd> [0..1]  482
     Year <Yr> [0..1] Year 482
     Type <Tp> [0..1] CodeSet 483
     FromToDate <FrToDt> [0..1] ± 483
   Amount <Amt> [1..1] Amount C2, C6 484
3.4.2.15.18.2.20.11.8.4.1  Period <Prd>
Presence: [0..1]
Definition: Set of elements used to provide details on the period of time related to the tax payment.
Period <Prd> contains the following TaxPeriod3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Year <Yr> [0..1] Year 482
   Type <Tp> [0..1] CodeSet 483
   FromToDate <FrToDt> [0..1] ± 483
3.4.2.15.18.2.20.11.8.4.1.1  Year <Yr>
Presence: [0..1]
Definition: Year related to the tax payment.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
482 March 2026
```

