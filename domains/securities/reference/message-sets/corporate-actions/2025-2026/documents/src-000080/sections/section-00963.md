---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.48 CountryCode"]
file_pages: [1205]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.48 CountryCode

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1205 to 1205.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1205

```text
CodeName Name Definition
UKWN Unknown Unknown whether the fund is calculating
the taxable income per dividend/taxable
income per share.
16.2.2.48  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
16.2.2.49  CreditDebitCode
Definition: Specifies if an operation is an increase or a decrease.
Type: CodeSet
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
16.2.2.50  DateType1Code
Definition: Specifies when date is unknown.
Type: CodeSet
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
16.2.2.51  DateType7Code
Definition: Type of date.
Type: CodeSet
CodeName Name Definition
ONGO Ongoing Ongoing basis, which indicates that the
date is determined by "ongoing basis"
process, for example "au fil de l'eau".
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1205 February 2026
```

