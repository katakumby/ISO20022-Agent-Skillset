---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.8 TransactionInterest4", "6.1.15.8.2 Record <Rcrd>", "6.1.15.8.2.7 Tax <Tax>"]
file_pages: [856]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.8.2.7 Tax <Tax>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 856 to 856.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 856

```text
6.1.15.8.2.7  Tax <Tax>
Presence: [0..1]
Definition: Provides details on the tax applied to charges.
Tax <Tax> contains the following TaxCharges2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 856
   Rate <Rate> [0..1] Rate 856
   Amount <Amt> [0..1] Amount C1, C5 856
6.1.15.8.2.7.1  Identification <Id>
Presence: [0..1]
Definition: Unique reference to unambiguously identify the nature of the tax levied, such as Value
Added Tax (VAT).
Datatype: "Max35Text" on page 916
6.1.15.8.2.7.2  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 913
6.1.15.8.2.7.3  Amount <Amt>
Presence: [0..1]
Definition: Amount of money resulting from the calculation of the tax.
Impacted by: C1 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
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
6.1.15.9  YieldedOrValueType1Choice
Definition: Choice of value type.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
856 March 2026
```

