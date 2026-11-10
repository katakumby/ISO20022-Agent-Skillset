---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.7 Cash", "6.1.7.1 CashDeposit1", "6.1.7.1.2 NumberOfNotes <NbOfNotes>"]
file_pages: [824]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.7.1.2 NumberOfNotes <NbOfNotes>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 824 to 824.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 824

```text
Note: The decimal separator is a dot.
6.1.7.1.2  NumberOfNotes <NbOfNotes>
Presence: [1..1]
Definition: Specifies the number of notes of the same denomination in the deposit.
Datatype: "Max15NumericText" on page 915
6.1.7.1.3  Amount <Amt>
Presence: [1..1]
Definition: Specifies the total amount of money in the cash deposit, that is the note denomination times
the number of notes.
Impacted by: C1 "ActiveCurrency", C7 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 885
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
6.1.8 Cash Entry
6.1.8.1  CashAvailability1
Definition: Indicates when the amount of money will become available, that is can be accessed and
start generating interest.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [1..1]  824
{Or     NumberOfDays <NbOfDays> [1..1] Text 825
Or}     ActualDate <ActlDt> [1..1] Date 825
   Amount <Amt> [1..1] Amount C1, C5 825
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 825
6.1.8.1.1  Date <Dt>
Presence: [1..1]
Definition: Indicates when the amount of money will become available.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
824 March 2026
```

