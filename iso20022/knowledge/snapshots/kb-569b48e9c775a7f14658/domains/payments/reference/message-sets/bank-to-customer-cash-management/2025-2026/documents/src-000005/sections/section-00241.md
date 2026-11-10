---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.1 References <Refs>", "3.4.2.15.18.2.1.16 Proprietary <Prtry>"]
file_pages: [384]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.1.16 Proprietary <Prtry>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 384 to 384.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 384

```text
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.1.16  Proprietary <Prtry>
Presence: [0..*]
Definition: Proprietary reference related to the underlying transaction.
Proprietary <Prtry> contains the following ProprietaryReference1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 384
   Reference <Ref> [1..1] Text 384
3.4.2.15.18.2.1.16.1  Type <Tp>
Presence: [1..1]
Definition: Identifies the type of reference reported.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.1.16.2  Reference <Ref>
Presence: [1..1]
Definition: Proprietary reference specification related to the underlying transaction.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.2  Amount <Amt>
Presence: [0..1]
Definition: Amount of money in the cash transaction.
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
3.4.2.15.18.2.3  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the transaction is a credit or a debit transaction.
Datatype: "CreditDebitCode" on page 892
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
384 March 2026
```

