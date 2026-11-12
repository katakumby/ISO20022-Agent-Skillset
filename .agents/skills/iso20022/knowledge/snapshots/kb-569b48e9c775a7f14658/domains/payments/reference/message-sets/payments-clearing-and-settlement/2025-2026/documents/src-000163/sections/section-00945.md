---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.2 Message Datatypes", "10.2.6 IdentifierSet"]
file_pages: [1240]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.2.6 IdentifierSet

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1240 to 1240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1240

```text
Decimal fractions of seconds may be included. In this case, the involved parties shall agree on the
maximum number of digits that are allowed.
Type: DateTime
10.2.6 IdentifierSet
10.2.6.1  AnyBICDec2014Identifier
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
10.2.6.2  BICFIDec2014Identifier
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
10.2.6.3  IBAN2007Identifier
Definition: The International Bank Account Number is a code used internationally by financial
institutions to uniquely identify the account of a customer at a financial institution as described in the
2007 edition of the ISO 13616 standard "Banking and related financial services - International Bank
Account Number (IBAN)" and replaced by the more recent edition of the standard.
Type: IdentifierSet
Identification scheme: National Banking Association; International Bank Account Number (ISO 13616)
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1240 March 2026
```

