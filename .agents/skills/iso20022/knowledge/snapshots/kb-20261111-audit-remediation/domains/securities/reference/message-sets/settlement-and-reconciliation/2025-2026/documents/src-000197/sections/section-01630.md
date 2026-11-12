---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.5 IdentifierSet", "35.2.5.2 BICFIDec2014Identifier"]
file_pages: [2186]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.5.2 BICFIDec2014Identifier

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2186 to 2186.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2186

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
35.2.5.2  BICFIDec2014Identifier
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
35.2.5.3  CFIOct2015Identifier
Definition: Classification type of the financial instrument, as per the ISO 10962 Classification of
Financial Instrument (CFI) codification, for example, common share with voting rights, fully paid, or
registered.
Note: this identifier also supports the updated versions of the standard, which were published in 2019
and 2021 (ISO 10962 :2019 and ISO 10962:2021) as there is no update in the pattern.
Type: IdentifierSet
Identification scheme: ANNA; CFIIdentifier
Format
pattern [A-Z]{6,6}
35.2.5.4  DTI2024Identifier
Definition: The Digital Token Identifier (DTI) is an 8 character code assigned to fungible digital assets
which uses distributed ledger technology for its issuance, storage, exchange, record of ownership or
transaction validation and is not a currency (ISO 4217) as described in ISO 24165 - DTI. A check
character, using the same character set as the base number, shall be calculated and added.
Type: IdentifierSet
Identification scheme: Digital Token Identifier Foundation (DTIF)
Format
pattern [1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2186 March 2026
```

