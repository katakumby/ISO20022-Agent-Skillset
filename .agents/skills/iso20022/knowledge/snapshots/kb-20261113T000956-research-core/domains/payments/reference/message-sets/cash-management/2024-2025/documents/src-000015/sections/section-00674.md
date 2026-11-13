---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.8 CountryCode"]
file_pages: [851]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.8 CountryCode

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 851 to 851.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 851

```text
CodeName Name Definition
PDNG Pending The payment is awaiting settlement.
FINL Final The payment has been settled or
stopped.
37.2.2.8  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
37.2.2.9  CreditDebitCode
Definition: Specifies if an operation is an increase or a decrease.
Type: CodeSet
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
37.2.2.10  EntryStatus1Code
Definition: Specifies the status of an entry.
Type: CodeSet
CodeName Name Definition
BOOK Booked Booked means that the transfer of
money has been completed between
account servicer and account owner
Usage:
Status Booked does not necessarily
imply finality of money as this depends
on other factors such as the payment
system used, the completion of the end-
to-end transaction and the terms agreed
between account servicer and owner.
Status Booked is the only status that can
be reversed.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 851 February 2025
```

