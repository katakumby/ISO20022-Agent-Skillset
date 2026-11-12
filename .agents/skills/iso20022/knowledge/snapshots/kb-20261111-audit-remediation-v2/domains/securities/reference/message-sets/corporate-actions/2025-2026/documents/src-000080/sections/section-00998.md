---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.5 IdentifierSet"]
file_pages: [1244]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.5 IdentifierSet

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1244 to 1244.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1244

```text
Decimal fractions of seconds may be included. In this case, the involved parties shall agree on the
maximum number of digits that are allowed.
Type: DateTime
16.2.5 IdentifierSet
16.2.5.1  AnyBICDec2014Identifier
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362: 2014 - "Banking - Banking telecommunication messages -
Business identifier code (BIC)".
Type: IdentifierSet
Identification scheme: SWIFT; AnyBICIdentifier
Format
pattern [A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
16.2.5.2  BICFIDec2014Identifier
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority as described
in ISO 9362: 2014 - "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Type: IdentifierSet
Identification scheme: SWIFT; BICIdentifier
Format
pattern [A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
16.2.5.3  CFIOct2015Identifier
Definition: Classification type of the financial instrument, as per the ISO 10962 Classification of
Financial Instrument (CFI) codification, for example, common share with voting rights, fully paid, or
registered.
Note: this identifier also supports the updated versions of the standard, which were published in 2019
and 2021 (ISO 10962 :2019 and ISO 10962:2021) as there is no update in the pattern.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1244 February 2026
```

