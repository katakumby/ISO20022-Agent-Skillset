---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.6 Bank Transaction Code", "6.1.6.3 BankTransactionCodeStructure5", "6.1.6.3.1 Code <Cd>"]
file_pages: [823]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.6.3.1 Code <Cd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 823 to 823.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 823

```text
6.1.6.3.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the business area of the underlying transaction.
Datatype: "ExternalBankTransactionDomain1Code" on page 893
6.1.6.3.2  Family <Fmly>
Presence: [1..1]
Definition: Specifies the family and the sub-family of the bank transaction code, within a specific
domain, in a structured and hierarchical format.
Family <Fmly> contains the following elements (see "BankTransactionCodeStructure6" on page 822
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet 822
   SubFamilyCode <SubFmlyCd> [1..1] CodeSet 822
6.1.7 Cash
6.1.7.1  CashDeposit1
Definition: Deposit of an amount of money defined in cash notes and/or coins.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoteDenomination <NoteDnmtn> [1..1] Amount C1, C7 823
   NumberOfNotes <NbOfNotes> [1..1] Text 824
   Amount <Amt> [1..1] Amount C1, C7 824
6.1.7.1.1  NoteDenomination <NoteDnmtn>
Presence: [1..1]
Definition: Specifies the note or coin denomination, including the currency, such as a 50 euro note.
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
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
823 March 2026
```

