---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.5 IdentifierSet", "66.2.5.7 BloombergIdentifier"]
file_pages: [5391]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.5.7 BloombergIdentifier

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5391 to 5391.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5391

```text
66.2.5.7  BloombergIdentifier
Definition: An identifier of a security assigned by the Bloomberg organisation.
Type: IdentifierSet
Identification scheme: Bloomberg; BloombergIdentifier
Format
minLength 1
maxLength 35
66.2.5.8  CanadianPaymentsARNIdentifier
Definition: Canadian Payments Association Routing Number. Identifies Canadian financial institutions
on the Canadian national clearing system.
Type: IdentifierSet
Identification scheme: Candian Payment Association; Payment Routing Number
Format
pattern CA[0-9]{9,9}
66.2.5.9  CFIOct2015Identifier
Definition: Classification type of the financial instrument, as per the ISO 10962 Classification of
Financial Instrument (CFI) codification, for example, common share with voting rights, fully paid, or
registered.
Note: this identifier also supports the updated versions of the standard, which were published in 2019
and 2021 (ISO 10962 :2019 and ISO 10962:2021) as there is no update in the pattern.
Type: IdentifierSet
Identification scheme: ANNA; CFIIdentifier
Format
pattern [A-Z]{6,6}
66.2.5.10  CHIPSParticipantIdentifier
Definition: (United States) Clearing House Interbank Payment System (CHIPS) Participant Identifier
(ID). Identifies financial institutions participating on CHIPS. The CHIPS Participant ID is assigned by the
New York Clearing House.
Type: IdentifierSet
Identification scheme: American Banker's Association (ABA); CHIPS Participant Number
Format
pattern CP[0-9]{4,4}
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5391 May 2026
```

