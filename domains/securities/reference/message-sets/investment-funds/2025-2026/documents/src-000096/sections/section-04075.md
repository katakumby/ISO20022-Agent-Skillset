---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.5 IdentifierSet", "66.2.5.29 MICIdentifier"]
file_pages: [5396]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.5.29 MICIdentifier

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5396 to 5396.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5396

```text
Type: IdentifierSet
Identification scheme: Global LEI System; LEIIdentifier
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
66.2.5.29  MICIdentifier
Definition: Market Identifier Code. The identification of a financial market, as stipulated in the norm ISO
10383 'Codes for exchanges and market identifications'.
Type: IdentifierSet
Identification scheme: SWIFT; MICIdentifier
Format
pattern [A-Z0-9]{4,4}
66.2.5.30  NewZealandNCCIdentifier
Definition: New Zealand Bank/Branch Code. Identifies New Zealand institutions on the New Zealand
national clearing system. The code is assigned by the New Zealand Bankers' Association (NZBA).
Type: IdentifierSet
Identification scheme: New Zealand Bankers Association; NewZealandNCC
Format
pattern NZ[0-9]{6,6}
66.2.5.31  PolishNationalClearingCodeIdentifier
Definition: Polish National Clearing Code Identifier. Identifies Polish financial institutions on the Polish
national clearing system.
Type: IdentifierSet
Identification scheme: Polish Central Bank; Payment Routing Number
Format
pattern PL[0-9]{8,8}
66.2.5.32  PortugueseNCCIdentifier
Definition: Portuguese National Clearing Code. Identifies Portuguese financial institutions on the
Portuguese national clearing system.
Type: IdentifierSet
Identification scheme: Banco de Portugal; PortugueseNCC
Format
pattern PT[0-9]{8,8}
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5396 May 2026
```

