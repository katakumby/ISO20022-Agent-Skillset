---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.5 IdentifierSet"]
file_pages: [884]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.5 IdentifierSet

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 884 to 884.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 884

```text
37.2.5 IdentifierSet
37.2.5.1  AnyBICDec2014Identifier
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
37.2.5.2  BICFIDec2014Identifier
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
37.2.5.3  EntryTypeIdentifier
Definition: Identifier providing additional system specific information about the entry.
Type: IdentifierSet
Identification scheme: EntryType; EntryTypeValue
Format
pattern [BEOVW]{1,1}[0-9]{2,2}|DUM
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 884 February 2025
```

