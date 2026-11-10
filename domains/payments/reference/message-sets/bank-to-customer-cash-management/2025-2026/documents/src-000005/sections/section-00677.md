---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.5 IdentifierSet", "6.2.5.6 UTIIdentifier"]
file_pages: [911]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.5.6 UTIIdentifier

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 911 to 911.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 911

```text
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
6.2.5.6  UTIIdentifier
Definition: Unique Transaction Identifier (UTI). Unique number allocated to a financial transaction as
agreed among the parties and/or within the regulatory system under which it is formed. The UTI is
described in the latest edition of the international standard ISO 23897:2020.
Type: IdentifierSet
Identification scheme: Parties to a trade; UTIIdentier
Format
pattern [A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}
6.2.5.7  UUIDv4Identifier
Definition: Universally Unique IDentifier (UUID) version 4, as described in IETC RFC 4122 "Universally
Unique IDentifier (UUID) URN Namespace".
Type: IdentifierSet
Identification scheme: RFC4122; UUIDv4
Format
pattern [a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}
6.2.6 Indicator
6.2.6.1  ChargeIncludedIndicator
Definition: Indicates whether charges have already been included.
Type: Indicator
Meaning When True: Included
Meaning When False: Pre-advised
6.2.6.2  TrueFalseIndicator
Definition: A flag indicating a True or False value.
Type: Indicator
Meaning When True: True
Meaning When False: False
6.2.6.3  YesNoIndicator
Definition: Indicates a "Yes" or "No" type of answer for an element.
Type: Indicator
Meaning When True: Yes
Meaning When False: No
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
911 March 2026
```

