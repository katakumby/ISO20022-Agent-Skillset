---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.7 Charges <Chrgs>", "4.4.2.14.18.2.7.2 Record <Rcrd>", "4.4.2.14.18.2.7.2.8 Tax <Tax>"]
file_pages: [649]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.7.2.8 Tax <Tax>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 649 to 649.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 649

```text
4.4.2.14.18.2.7.2.8  Tax <Tax>
Presence: [0..1]
Definition: Provides details on the tax applied to charges.
Tax <Tax> contains the following TaxCharges2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 649
   Rate <Rate> [0..1] Rate 649
   Amount <Amt> [0..1] Amount C2, C6 649
4.4.2.14.18.2.7.2.8.1  Identification <Id>
Presence: [0..1]
Definition: Unique reference to unambiguously identify the nature of the tax levied, such as Value
Added Tax (VAT).
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.7.2.8.2  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 913
4.4.2.14.18.2.7.2.8.3  Amount <Amt>
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
4.4.2.14.18.2.8  Interest <Intrst>
Presence: [0..1]
Definition: Provides details of the interest amount included in the entry amount.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
649 March 2026
```

