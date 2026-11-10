---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.5 IdentifierSet", "7.2.5.8 RatingValueIdentifier"]
file_pages: [665]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.5.8 RatingValueIdentifier

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 665 to 665.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 665

```text
Identification scheme: SWIFT; MICIdentifier
Format
pattern [A-Z0-9]{4,4}
7.2.5.8  RatingValueIdentifier
Definition: Identifies the rating values that may be assigned to a security by a rating agency.
Type: IdentifierSet
Identification scheme: FPL; FIX
7.2.5.9  UPICIdentifier
Definition: Universal Payment Identification Code (UPIC). Identifier used by the New York Clearing
House to mask confidential data, such as bank accounts and bank routing numbers. UPIC numbers
remain with business customers, regardless of banking relationship changes.
Type: IdentifierSet
Identification scheme: The Clearing House (formerly The New York Clearing House); Universal
Payment Identification Code
Format
pattern [0-9]{8,17}
7.2.5.10  UTIIdentifier
Definition: Unique Transaction Identifier (UTI). Unique number allocated to a financial transaction as
agreed among the parties and/or within the regulatory system under which it is formed. The UTI is
described in the latest edition of the international standard ISO 23897:2020.
Type: IdentifierSet
Identification scheme: Parties to a trade; UTIIdentier
Format
pattern [A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}
7.2.6 Indicator
7.2.6.1  PlusOrMinusIndicator
Definition: Indicates a positive or negative value.
Type: Indicator
Meaning When True: Plus
Meaning When False: Minus
7.2.6.2  YesNoIndicator
Definition: Indicates a "Yes" or "No" type of answer for an element.
Type: Indicator
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 665 February 2025
```

