---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.5 IdentifierSet", "66.2.5.11 CHIPSUniversalIdentifier"]
file_pages: [5392]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.5.11 CHIPSUniversalIdentifier

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5392 to 5392.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5392

```text
66.2.5.11  CHIPSUniversalIdentifier
Definition: (United States) Clearing House Interbank Payments System (CHIPS) Universal Identification
(UID). Identifies entities that own accounts at CHIPS participating financial institutions, through which
CHIPS payments are effected. The CHIPS UID is assigned by the New York Clearing House.
Type: IdentifierSet
Identification scheme: American Banker's Association (ABA); CHIPS UID
Format
pattern CH[0-9]{6,6}
66.2.5.12  ConsolidatedTapeAssociationIdentifier
Definition: Identifier of a security assigned by the Consolidated Tape Association.
Type: IdentifierSet
Identification scheme: CTAIdentifier; CTAIdentifier
Format
minLength 1
maxLength 35
66.2.5.13  CUSIPIdentifier
Definition: Committee on Uniform Securities and Identification Procedures (CUSIP). The standards
body that created and maintains the securities classification system in the US. Non-US securities have
a similar number called the CINS number.
Type: IdentifierSet
Identification scheme: Standards and Poor's CUSIP Service Bureau; CUSIPIdentifier
66.2.5.14  DTI2024Identifier
Definition: The Digital Token Identifier (DTI) is an 8 character code assigned to fungible digital assets
which uses distributed ledger technology for its issuance, storage, exchange, record of ownership or
transaction validation and is not a currency (ISO 4217) as described in ISO 24165 - DTI. A check
character, using the same character set as the base number, shall be calculated and added.
Type: IdentifierSet
Identification scheme: Digital Token Identifier Foundation (DTIF)
Format
pattern [1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}
66.2.5.15  DutchIdentifier
Definition: Identifier for Dutch securities.
Type: IdentifierSet
Identification scheme: Dutch agency; DutchIdentifier
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5392 May 2026
```

