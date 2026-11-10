---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.2 CodeSet", "6.2.2.13 CountryCode"]
file_pages: [892]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.2.13 CountryCode

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 892 to 892.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 892

```text
6.2.2.13  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
6.2.2.14  CreditDebitCode
Definition: Specifies if an operation is an increase or a decrease.
Type: CodeSet
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
6.2.2.15  CSCManagement1Code
Definition: CSC (Card Security Code) management associated with the transaction.
Type: CodeSet
CodeName Name Definition
PRST CSCPresent Card security code present.
BYPS CSCByPass Card security code by-passed or not
provided by the merchant.
UNRD CSCUnread Card security code unreadable.
NCSC NoCSC No card security code imprint.
6.2.2.16  ExternalAccountIdentification1Code
Definition: Specifies the external account identification scheme name code in the format of character
string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
Type: CodeSet
Format
minLength 1
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
892 March 2026
```

