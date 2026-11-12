---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.2 Message Datatypes", "10.2.6 IdentifierSet", "10.2.6.4 LEIIdentifier"]
file_pages: [1241]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.2.6.4 LEIIdentifier

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1241 to 1241.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1241

```text
Format
pattern [A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
10.2.6.4  LEIIdentifier
Definition: Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial
Services - Legal Entity Identifier (LEI)".
Type: IdentifierSet
Identification scheme: Global LEI System; LEIIdentifier
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
10.2.6.5  UTIIdentifier
Definition: Unique Transaction Identifier (UTI). Unique number allocated to a financial transaction as
agreed among the parties and/or within the regulatory system under which it is formed. The UTI is
described in the latest edition of the international standard ISO 23897:2020.
Type: IdentifierSet
Identification scheme: Parties to a trade; UTIIdentier
Format
pattern [A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}
10.2.6.6  UUIDv4Identifier
Definition: Universally Unique IDentifier (UUID) version 4, as described in IETC RFC 4122 "Universally
Unique IDentifier (UUID) URN Namespace".
Type: IdentifierSet
Identification scheme: RFC4122; UUIDv4
Format
pattern [a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}
10.2.7 Indicator
10.2.7.1  BatchBookingIndicator
Definition: Identifies whether the sending party requests a single debit or credit entry per individual
transaction or a batch entry for the sum of the amounts of all transactions.
Type: Indicator
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1241 March 2026
```

