---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.5 IdentifierSet", "66.2.5.3 AustrianBankleitzahlIdentifier"]
file_pages: [5390]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.5.3 AustrianBankleitzahlIdentifier

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5390 to 5390.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5390

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory, and
consists of eight (8) or eleven (11) contiguous characters.
66.2.5.3  AustrianBankleitzahlIdentifier
Definition: Austrian Bankleitzahl. Identifies Austrian financial institutions on the Austrian national
clearing system.
Type: IdentifierSet
Identification scheme: Oesterreichische NationalBank; Austrian Bankleitzahl
Format
pattern AT[0-9]{5,5}
66.2.5.4  BelgianIdentifier
Definition: Identifier for Belgian securities.
Type: IdentifierSet
Identification scheme: The Belgian identifier for securities.
66.2.5.5  BICFIDec2014Identifier
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
66.2.5.6  Bloomberg2Identifier
Definition: An identifier of a security assigned by the Bloomberg organisation.
Type: IdentifierSet
Identification scheme: Bloomberg; BloombergIdentifier
Format
pattern (BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5390 May 2026
```

