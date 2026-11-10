---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.12 Interest <Intrst>", "3.4.2.12.5 Tax <Tax>", "3.4.2.12.5.2 Rate <Rate>"]
file_pages: [312]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.12.5.2 Rate <Rate>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 312 to 312.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 312

```text
3.4.2.12.5.2  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 913
3.4.2.12.5.3  Amount <Amt>
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
3.4.2.13  Balance <Bal>
Presence: [1..*]
Definition: Set of elements used to define the balance as a numerical representation of the net
increases and decreases in an account at a specific point in time.
Impacted by: C15 "ForwardBalanceAndAvailabilityRule"
Balance <Bal> contains the following elements (see "CashBalance8" on page 818 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 818
   CreditLine <CdtLine> [0..*] ± 819
   Amount <Amt> [1..1] Amount C1, C5 819
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 820
   Date <Dt> [1..1] ± 820
   Availability <Avlbty> [0..*] ± 820
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
312 March 2026
```

