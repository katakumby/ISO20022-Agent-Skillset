---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.5 IdentifierSet", "7.2.5.2 BBANIdentifier"]
file_pages: [663]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.5.2 BBANIdentifier

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 663 to 663.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 663

```text
Type: IdentifierSet
Identification scheme: SWIFT; AnyBICIdentifier
Format
pattern [A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
7.2.5.2  BBANIdentifier
Definition: Basic Bank Account Number (BBAN). Identifier used nationally by financial institutions, ie, in
individual countries, generally as part of a National Account Numbering Scheme(s), which uniquely
identifies the account of a customer.
Type: IdentifierSet
Identification scheme: National Banking Association; Basic Bank Account Number
Format
pattern [a-zA-Z0-9]{1,30}
7.2.5.3  BICNonFIDec2014Identifier
Definition: Code allocated to a non-financial institution by the ISO 9362 Registration Authority as
described in ISO 9362: 2014 - "Banking - Banking telecommunication messages - Business identifier
code (BIC)".
Type: IdentifierSet
Identification scheme: SWIFT; BEIIdentifier
Format
pattern [A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}
Constraints
• BICNonFI
Valid BICs for non-financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
7.2.5.4  CFIOct2015Identifier
Definition: Classification type of the financial instrument, as per the ISO 10962 Classification of
Financial Instrument (CFI) codification, for example, common share with voting rights, fully paid, or
registered.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 663 February 2025
```

